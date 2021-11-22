/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum ReleaseChannelEnum {
    #[serde(rename = "stable")]
    Stable,
    #[serde(rename = "nightly")]
    Nightly,

}

impl ToString for ReleaseChannelEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Stable => String::from("stable"),
            Self::Nightly => String::from("nightly"),
        }
    }
}

impl Default for ReleaseChannelEnum {
    fn default() -> ReleaseChannelEnum {
        Self::Stable
    }
}




