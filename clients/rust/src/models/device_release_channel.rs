/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum DeviceReleaseChannel {
    #[serde(rename = "stable")]
    Stable,
    #[serde(rename = "nightly")]
    Nightly,

}

impl ToString for DeviceReleaseChannel {
    fn to_string(&self) -> String {
        match self {
            Self::Stable => String::from("stable"),
            Self::Nightly => String::from("nightly"),
        }
    }
}

impl Default for DeviceReleaseChannel {
    fn default() -> DeviceReleaseChannel {
        Self::Stable
    }
}




