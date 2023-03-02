/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.127.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OctoPrintServerStatusType {
    #[serde(rename = "Test")]
    Test,
    #[serde(rename = "Startup")]
    Startup,
    #[serde(rename = "Shutdown")]
    Shutdown,

}

impl ToString for OctoPrintServerStatusType {
    fn to_string(&self) -> String {
        match self {
            Self::Test => String::from("Test"),
            Self::Startup => String::from("Startup"),
            Self::Shutdown => String::from("Shutdown"),
        }
    }
}

impl Default for OctoPrintServerStatusType {
    fn default() -> OctoPrintServerStatusType {
        Self::Test
    }
}




