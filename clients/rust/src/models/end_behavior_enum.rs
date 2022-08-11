/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.6
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum EndBehaviorEnum {
    #[serde(rename = "cancel")]
    Cancel,
    #[serde(rename = "release")]
    Release,

}

impl ToString for EndBehaviorEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Cancel => String::from("cancel"),
            Self::Release => String::from("release"),
        }
    }
}

impl Default for EndBehaviorEnum {
    fn default() -> EndBehaviorEnum {
        Self::Cancel
    }
}




