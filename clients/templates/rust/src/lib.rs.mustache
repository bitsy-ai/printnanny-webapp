
use pyo3::prelude::*;
extern crate flatbuffers;
#[allow(dead_code, unused_imports)]
#[path = "./telemetry.rs"]
pub mod telemetry;
pub use telemetry::{
    Image,
    ImageArgs,
    MonitoringFrame,
    MonitoringFrameArgs
    PluginEvent,
    ENUM_NAMES_PLUGIN_EVENT,
    TelemetryMessage, 
    BoundingBoxes, 
    Box
}
use bytes::Bytes;

#[pymodule]
fn print_nanny_message_rust(py: Python, m: &PyModule) -> PyResult<()> {

    #[pyfn(m, "build_monitoring_frame_post_message")]
    fn build_monitoring_frame_post_message(_py: Python, ts: i32, height: i32, width: i32, image_bytes: Bytes) -> PyResult<String> {
        let mut builder = flatbuffers::FlatBufferBuilder::new_with_capacity(1024);

        let data = builder.create_vector(&image_bytes);
        let image = Image::create(&mut builder, &ImageArgs(
            width: width,
            height: height,
            data: data
        ));

        let message = MonitoringFrame::create(&mut, &MonitoringFrameArgs(
            ts: ts,
            image: image,
            event_type: PluginEvent::monitoring
        ))
        Ok()
    }

    Ok(())
}