/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiUrls {
    #[serde(rename = "swupdate")]
    pub swupdate: String,
    #[serde(rename = "octoprint")]
    pub octoprint: String,
}

impl PiUrls {
    pub fn new(swupdate: String, octoprint: String) -> PiUrls {
        PiUrls {
            swupdate,
            octoprint,
        }
    }
}


