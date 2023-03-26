/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiUrls {
    #[serde(rename = "moonraker_api")]
    pub moonraker_api: String,
    #[serde(rename = "mission_control")]
    pub mission_control: String,
    #[serde(rename = "octoprint")]
    pub octoprint: String,
    #[serde(rename = "swupdate")]
    pub swupdate: String,
    #[serde(rename = "syncthing")]
    pub syncthing: String,
}

impl PiUrls {
    pub fn new(moonraker_api: String, mission_control: String, octoprint: String, swupdate: String, syncthing: String) -> PiUrls {
        PiUrls {
            moonraker_api,
            mission_control,
            octoprint,
            swupdate,
            syncthing,
        }
    }
}


