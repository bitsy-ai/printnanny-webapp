/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.134.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct CameraSnapshot {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "image")]
    pub image: String,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl CameraSnapshot {
    pub fn new(id: String, created_dt: String, image: String, pi: i32) -> CameraSnapshot {
        CameraSnapshot {
            id,
            created_dt,
            image,
            pi,
        }
    }
}


