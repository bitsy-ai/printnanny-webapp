/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.8
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum UsageTypeEnum {
    #[serde(rename = "licensed")]
    Licensed,
    #[serde(rename = "metered")]
    Metered,

}

impl ToString for UsageTypeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Licensed => String::from("licensed"),
            Self::Metered => String::from("metered"),
        }
    }
}

impl Default for UsageTypeEnum {
    fn default() -> UsageTypeEnum {
        Self::Licensed
    }
}




