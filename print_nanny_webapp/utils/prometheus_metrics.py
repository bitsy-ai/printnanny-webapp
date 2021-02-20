from django.apps import apps
import prometheus_client

# from print_nanny_webapp.client_events.models import PrintJobState

# print_job_status = prometheus_client.Enum(
#     "print_job_status",
#     "Last seen status of a print job",
#     states=PrintJobState.EventType.values,
# )

predict_frames_per_minute = prometheus_client.Summary(
    "predict_events_per_minute",
    "Raw number of events seen. Calculated via schedule_active_jobs_analysis() periodic runs",
)

detections_per_minute = prometheus_client.Summary(
    "detections_per_minute",
    "Number of detections above confidence threshold. Calculated via schedule_active_jobs_analysis() periodic run",
    ["alert_type", "detection_class"],
)

detections_per_frame = prometheus_client.Summary(
    "detections_per_frame",
    "Number of detections above confidence threshold. Calculated via schedule_active_jobs_analysis() periodic run",
    ["alert_type", "detection_class"],
)

detections_confidence_per_label = prometheus_client.Summary(
    "confidence_per_label",
    "Raw confidence score per detection per label",
    ["alert_type", "detection_class"],
)

detections_failure_ratio = prometheus_client.Summary(
    "detections_failure_ratio",
    "Num detected failure / num detected neutral frames",
)

build_version = prometheus_client.Info(
    "build_version", "key:value of deployment and build configuration"
)

annotated_ws_publisher_connected_metric = prometheus_client.Gauge(
    "annotated_ws_publisher_connected",
    "Number of clients publishing a stream of annotated images",
)
annotated_ws_consumer_connected_metric = prometheus_client.Gauge(
    "annotated_ws_consumer_connected",
    "Number of clients subscribed to a stream of annotated images",
)

##
# the following metrics are only relevate if running in gateway mode
##
# mqtt_client_connected_metric = prometheus_client.Gauge(
#     "mqtt_client_connected",
#     "Number of client devices connected to gateway device/server"
# )

# mqtt_gateway_connected_metric = prometheus_client.Gauge(
#     "mqtt_gateway_connected",
#     "Number of gateway devices connected to MQTT bridge"
# )

# mqtt_gateway_retrying_metric = prometheus_client.Gauge(
#     "mqtt_gateway_retrying",
#     "Number of gateway devices attempting to reconnect to MQTT bridge (includes JWT refresh)"
# )
