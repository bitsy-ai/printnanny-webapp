/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct JanusAuth {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "janus_admin_secret")]
    pub janus_admin_secret: String,
    #[serde(rename = "janus_token")]
    pub janus_token: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "device")]
    pub device: i32,
}

impl JanusAuth {
    pub fn new(id: i32, janus_admin_secret: String, janus_token: String, created_dt: String, device: i32) -> JanusAuth {
        JanusAuth {
            id,
            janus_admin_secret,
            janus_token,
            created_dt,
            device,
        }
    }
}


