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
pub enum OctoPrintEventModelEnum {
    #[serde(rename = "OctoPrintEvent")]
    OctoPrintEvent,

}

impl ToString for OctoPrintEventModelEnum {
    fn to_string(&self) -> String {
        match self {
            Self::OctoPrintEvent => String::from("OctoPrintEvent"),
        }
    }
}

impl Default for OctoPrintEventModelEnum {
    fn default() -> OctoPrintEventModelEnum {
        Self::OctoPrintEvent
    }
}




