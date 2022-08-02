/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintBackup {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "deleted")]
    pub deleted: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "hostname")]
    pub hostname: String,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "octoprint_version")]
    pub octoprint_version: String,
    #[serde(rename = "file")]
    pub file: String,
    #[serde(rename = "user")]
    pub user: i32,
}

impl OctoPrintBackup {
    pub fn new(id: i32, deleted: String, created_dt: String, hostname: String, name: String, octoprint_version: String, file: String, user: i32) -> OctoPrintBackup {
        OctoPrintBackup {
            id,
            deleted,
            created_dt,
            hostname,
            name,
            octoprint_version,
            file,
            user,
        }
    }
}


