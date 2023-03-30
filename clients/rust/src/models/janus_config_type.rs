/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.132.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// JanusConfigType : * `cloud` - Cloud WebRTC Gateway * `edge` - Edge WebRTC Gateway

/// * `cloud` - Cloud WebRTC Gateway * `edge` - Edge WebRTC Gateway
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum JanusConfigType {
    #[serde(rename = "cloud")]
    Cloud,
    #[serde(rename = "edge")]
    Edge,

}

impl ToString for JanusConfigType {
    fn to_string(&self) -> String {
        match self {
            Self::Cloud => String::from("cloud"),
            Self::Edge => String::from("edge"),
        }
    }
}

impl Default for JanusConfigType {
    fn default() -> JanusConfigType {
        Self::Cloud
    }
}




