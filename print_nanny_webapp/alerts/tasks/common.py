import logging
import os
import shutil
import sys

from celery import shared_task, group
from django.apps import apps
from django.core.files.images import File, ImageFile
from django.core.files.base import ContentFile
import imageio
from skimage.io import imread_collection

import plotly
import plotly.express as px
import plotly.graph_objects as go
from scipy import signal
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

# minimum confidence score for detection to be accepted for post-processing
CONFIDENCE_THRESHOLD = 0.5
# minimum ratio of failed:neutral detections required to send email
FAILURE_NOTIFY_THRESHOLD = 0.5
# small number added to ratio denominator
FAILURE_EPSILON = 1e-7

LABELS = {
    1: "nozzle",
    2: "adhesion",
    3: "spaghetti",
    4: "print",
    5: "raft",
}

FAILURES = {
    2: "adhesion",
    3: "spaghetti",
}


@shared_task
def trigger_alerts_task(alert_id, serialized_obj):
    logger.info(
        f"trigger_alerts_task called with alert_id={alert_id} serialized_obj={serialized_obj}"
    )
    Alert = apps.get_model("alerts", "Alert")
    alert = Alert.objects.get(id=alert_id)
    return alert.trigger_alerts(serialized_obj)


def dict_to_series(data):
    return pd.Series(data.values(), index=data.keys())


def savgol_filter(x, fps):
    logger.info(type(x))
    # assert x > window
    if len(x) <= fps:
        window = len(x) // 8
    else:
        window = int(fps)

    # window must be an odd number
    if window % 2 == 0:
        window += 1

    # assert polyorder < window
    if window <= 3:
        return x

    return signal.savgol_filter(x, window, 1)


def create_alert_plot(filename, tmp_dir, function, title, description, alert_id):

    ManualVideoUploadAlert = apps.get_model("alerts", "ManualVideoUploadAlert")
    AlertPlot = apps.get_model("alerts", "AlertPlot")

    with open(os.path.join(tmp_dir, filename + ".png"), "rb") as png_f:
        wrapped_png = ImageFile(png_f)
        with open(os.path.join(tmp_dir, filename + ".html"), "rb") as html_f:
            wrapped_html = File(html_f)
            alert_plot = AlertPlot(
                function=function,
                title=title,
                description=description,
                alert=ManualVideoUploadAlert.objects.filter(id=alert_id).first(),
            )
            alert_plot.image.save(filename + ".png", wrapped_png)
            alert_plot.html.save(filename + ".html", wrapped_html)
            alert_plot.save()
            return alert_plot


@shared_task
def rm_tmp_dir(temp_dir):
    return shutil.rmtree(temp_dir)


@shared_task
def create_box_plot(confident_df, alert_id, temp_dir):

    filename = f"{alert_id}_boxplot"
    fig = confident_df.reset_index().plot(
        x="label",
        y="detection_scores",
        kind="box",
        title="Confidence Distribution by Label",
        color="label",
    )

    html = os.path.join(temp_dir, f"{filename}.html")
    with open(html, "w+") as f:
        plotly.io.write_html(fig, f, include_plotlyjs="cdn", full_html=True)

    png = os.path.join(temp_dir, f"{filename}.png")
    fig.write_image(png)

    alert_plot = create_alert_plot(
        filename,
        temp_dir,
        sys._getframe().f_code.co_name,
        "Confidence Distribution",
        "boxplot",
        alert_id,
    )

    return alert_plot


@shared_task
def create_line_subplots(confident_df, alert_id, temp_dir, fps):
    g = confident_df.reset_index()

    y = savgol_filter(g["detection_scores"], fps)

    fig = px.line(
        g,
        x="frame_id",
        y=y,
        color="label",
        facet_col="label",
        line_group="label",
        facet_col_wrap=1,
        facet_col_spacing=0.05,
    )

    fig.update_yaxes(title_text="Confidence")
    fig.update_layout(
        overwrite=True,
        title_text="Confidence over Time, Breakout by Detection Type",
        xaxis_title="Time (frame id)",
        legend_title="Detection",
        height=800,
    )

    filename = f"{alert_id}_lines_subplot"
    html = os.path.join(temp_dir, f"{filename}.html")
    with open(html, "w+") as f:
        fig.write_html(f, include_plotlyjs="cdn", full_html=True)

    png = os.path.join(temp_dir, f"{filename}.png")
    fig.write_image(png)

    alert_plot = create_alert_plot(
        filename,
        temp_dir,
        sys._getframe().f_code.co_name,
        "Confidence over Time",
        "Breakout by Detection Type",
        alert_id,
    )

    return alert_plot


@shared_task()
def create_health_abs_plot(confident_df, fail_df, alert_id, temp_dir, fps):
    g = confident_df.reset_index()

    fig = go.Figure()

    print_trace = g[g["label"] == "print"]
    fail_trace = fail_df.reset_index()

    window = int(fps)

    fig.add_trace(
        go.Scatter(
            x=print_trace["frame_id"],
            y=savgol_filter(print_trace["detection_scores"], fps),
            fill=None,
            mode="lines",
            name="print",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=fail_trace["frame_id"],
            y=savgol_filter(fail_trace["detection_scores"], fps),
            fill=None,
            mode="lines",
            name="defects",
        )
    )

    fig.update_layout(
        overwrite=True,
        title_text="Print Health Scores over Time (Absolute)",
        xaxis_title="Time (frame id)",
        yaxis_title="Health Score",
    )

    filename = f"{alert_id}_health_abs_plot"
    html = os.path.join(temp_dir, f"{filename}.html")
    with open(html, "w+") as f:
        fig.write_html(f, include_plotlyjs="cdn", full_html=True)

    png = os.path.join(temp_dir, f"{filename}.png")
    fig.write_image(png)

    alert_plot = create_alert_plot(
        filename,
        temp_dir,
        sys._getframe().f_code.co_name,
        "Change in Print Health Over Time (Relative)",
        "Health score over time, breakout by print vs all defects",
        alert_id,
    )

    return alert_plot


@shared_task()
def create_health_rel_plot(confident_df, fail_df, alert_id, temp_dir, fps):
    g = confident_df.reset_index()
    print_trace = g[g["label"] == "print"]
    fail_trace = fail_df.reset_index()
    split_df = pd.concat({"fail": fail_trace, "print": print_trace}).reset_index()

    mask = split_df.level_0 == "fail"

    y = (
        split_df[~mask]
        .groupby("timecode")["detection_scores"]
        .sum()
        .subtract(
            np.log10(
                split_df[mask].groupby("timecode")["detection_scores"].sum().cumsum()
            ),
            fill_value=0,
        )
    )
    fig = go.Figure(
        go.Waterfall(
            orientation="v",
            x=y.index,
            y=y,
        )
    )

    fig.update_layout(
        overwrite=True,
        title_text="Change in Print Health Over Time",
        xaxis_title="Time (relative)",
        yaxis_title="Health Score",
    )

    fig.update_xaxes(nticks=20)

    if len(y[y < 0]) >= (fps / 2):
        alert_offset = int(fps / 2)
        x0 = np.polynomial.Polynomial.fit(
            y.reset_index().index, y.reset_index()["detection_scores"], 2
        )
        intercept = list(x0)[-1]

        notify_timecode = y[y <= intercept].index[alert_offset]
        notify_seconds = int(_seconds(notify_timecode, fps))
        ManualVideoUploadAlert = apps.get_model("alerts", "ManualVideoUploadAlert")

        ManualVideoUploadAlert.objects.filter(id=alert_id).update(
            notify_seconds=notify_seconds, notify_timecode=notify_timecode
        )
        fig.add_annotation(
            x=y[y <= intercept].index[alert_offset],
            y=y.reset_index()["detection_scores"].cumsum().min(),
            text="Print Nanny alerts you at this time",
            showarrow=True,
            arrowhead=1,
        )

        fig.add_vrect(
            x0=y[y <= intercept].index[alert_offset],
            x1=y[y < 0].index[-1],
            fillcolor="LightSalmon",
            opacity=0.5,
            layer="below",
            line_width=0,
        )

    filename = f"{alert_id}_health_rel_plot"

    png = os.path.join(temp_dir, f"{filename}.png")
    fig.write_image(png)

    html = os.path.join(temp_dir, f"{filename}.html")
    with open(html, "w+") as f:
        fig.write_html(f, include_plotlyjs="cdn", full_html=True)

    alert_plot = create_alert_plot(
        filename,
        temp_dir,
        sys._getframe().f_code.co_name,
        "Change in Print Health Over Time",
        "Relative change (waterfall) health scores over time",
        alert_id,
    )

    return alert_plot


def _timecode(seconds, framerate):
    return "{h:02d}:{m:02d}:{s:02d}:{f:02d}".format(
        h=int(seconds / 3600),
        m=int(seconds / 60 % 60),
        s=int(seconds % 60),
        f=round((seconds - int(seconds)) * framerate),
    )


def _seconds(value, framerate):
    if isinstance(value, str):  # value seems to be a timestamp
        _zip_ft = zip((3600, 60, 1, 1 / framerate), value.split(":"))
        return sum(f * float(t) for f, t in _zip_ft)
    elif isinstance(value, (int, float)):  # frames
        return value / framerate
    else:
        return 0


def _frames(seconds, framerate):
    return seconds * framerate


def timecode_to_frames(timecode, framerate):
    return _frames(_seconds(timecode) - _seconds(start, framerate), framerate)


def frames_to_timecode(frames, framerate, start=None):
    return _timecode(
        _seconds(frames, framerate) + _seconds(start, framerate), framerate
    )


def calc_metrics(df, framerate):

    NUM_DETECTIONS_PER_FRAME = len(df["detection_scores"].iloc[0])
    df = df[["detection_classes", "detection_scores"]]
    df = df.reset_index()
    df = df.rename(columns={"id": "frame_id"})
    NUM_FRAMES = len(df)
    df["timecode"] = df["frame_id"].apply(lambda x: frames_to_timecode(x, framerate))
    # explode detection_classes and detection_scores together
    df = df.set_index(["frame_id"]).apply(pd.Series.explode).reset_index()
    assert len(df) == NUM_FRAMES * NUM_DETECTIONS_PER_FRAME

    # add string labels
    df["label"] = df["detection_classes"].map(LABELS)

    # create a hierarchal index
    df = df.set_index(["frame_id", "label"])

    confident_df = df[df["detection_scores"] > CONFIDENCE_THRESHOLD]
    mask = (df["detection_scores"] > CONFIDENCE_THRESHOLD) & (
        df["detection_classes"].isin(FAILURES)
    )
    fail_df = df[mask]

    return df, fail_df, confident_df


@shared_task
def create_report_card(df, alert_id, temp_dir, fps, callback):
    ManualVideoUploadAlert = apps.get_model("alerts", "ManualVideoUploadAlert")

    alert = ManualVideoUploadAlert.objects.filter(id=alert_id).first()

    multi_df, fail_df, confident_df = calc_metrics(df, fps)

    filename = f"alert_{alert_id}_dataframe.json"
    outcontent = multi_df.reset_index().to_json().encode("utf-8")
    alert.dataframe.save(filename, ContentFile(outcontent))
    alert.save()

    workflow = group(
        [
            create_box_plot.si(confident_df, alert_id, temp_dir),
            create_line_subplots.si(confident_df, alert_id, temp_dir, fps),
            create_health_abs_plot.si(confident_df, fail_df, alert_id, temp_dir, fps),
            create_health_rel_plot.si(confident_df, fail_df, alert_id, temp_dir, fps),
        ]
    )

    workflow = workflow | callback.si(alert_id)

    return workflow()


@shared_task
def render_alert_annotated_video(alert_id, temp_dir, fps):
    ManualVideoUploadAlert = apps.get_model("alerts", "ManualVideoUploadAlert")

    annotated_images = imread_collection(temp_dir + "/*.jpg")
    filename = f"alert_{alert_id}_annotated_video.mp4"
    file_path = os.path.join(temp_dir, filename)
    imageio.mimwrite(file_path, annotated_images, fps=fps, format="FFMPEG")

    with open(file_path, "rb") as f:
        wrapped_file = File(f)
        alert = ManualVideoUploadAlert.objects.filter(id=alert_id).first()
        alert.annotated_video.save(filename, wrapped_file)

    logger.info(f"Updated alert {alert_id} with {file_path}")
    return alert


@shared_task
def prediction_dicts_to_dataframe(predict_dicts):
    predict_dicts = np.array(predict_dicts, dtype=np.object)
    predict_dicts = np.hstack(predict_dicts)
    df = pd.DataFrame.from_records(predict_dicts, index="id")
    df = df.dropna()
    df = df["predict_data"].apply(dict_to_series)

    return df
