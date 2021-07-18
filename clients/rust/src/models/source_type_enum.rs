/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum SourceTypeEnum {
    #[serde(rename = "MJPG Streamer")]
    MJPGStreamer,
    #[serde(rename = "Gstreamer")]
    Gstreamer,

}

impl ToString for SourceTypeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::MJPGStreamer => String::from("MJPG Streamer"),
            Self::Gstreamer => String::from("Gstreamer"),
        }
    }
}




