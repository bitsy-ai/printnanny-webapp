/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OsEdition {
    #[serde(rename = "octoprint_lite")]
    OctoprintLite,

}

impl ToString for OsEdition {
    fn to_string(&self) -> String {
        match self {
            Self::OctoprintLite => String::from("octoprint_lite"),
        }
    }
}

impl Default for OsEdition {
    fn default() -> OsEdition {
        Self::OctoprintLite
    }
}




