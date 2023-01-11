/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.121.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct GcodeFile {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "file")]
    pub file: String,
    #[serde(rename = "hash")]
    pub hash: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "user")]
    pub user: i32,
}

impl GcodeFile {
    pub fn new(id: i32, name: String, file: String, hash: String, created_dt: String, user: i32) -> GcodeFile {
        GcodeFile {
            id,
            name,
            file,
            hash,
            created_dt,
            user,
        }
    }
}


