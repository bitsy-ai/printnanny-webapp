/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.107.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiSoftwareUpdatePayload {
    #[serde(rename = "wic_tarball_url")]
    pub wic_tarball_url: String,
    #[serde(rename = "wic_bmap_url")]
    pub wic_bmap_url: String,
    #[serde(rename = "manifest_url")]
    pub manifest_url: String,
    #[serde(rename = "swu_url")]
    pub swu_url: String,
    #[serde(rename = "version_id")]
    pub version_id: String,
    #[serde(rename = "version")]
    pub version: String,
    #[serde(rename = "version_codename")]
    pub version_codename: String,
}

impl PiSoftwareUpdatePayload {
    pub fn new(wic_tarball_url: String, wic_bmap_url: String, manifest_url: String, swu_url: String, version_id: String, version: String, version_codename: String) -> PiSoftwareUpdatePayload {
        PiSoftwareUpdatePayload {
            wic_tarball_url,
            wic_bmap_url,
            manifest_url,
            swu_url,
            version_id,
            version,
            version_codename,
        }
    }
}


