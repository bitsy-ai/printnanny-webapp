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
pub struct License {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<i32>,
    #[serde(rename = "deleted", skip_serializing_if = "Option::is_none")]
    pub deleted: Option<String>,
    #[serde(rename = "public_key", skip_serializing_if = "Option::is_none")]
    pub public_key: Option<String>,
    #[serde(rename = "public_key_checksum", skip_serializing_if = "Option::is_none")]
    pub public_key_checksum: Option<String>,
    #[serde(rename = "fingerprint", skip_serializing_if = "Option::is_none")]
    pub fingerprint: Option<String>,
    #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
    pub created_dt: Option<String>,
    #[serde(rename = "device")]
    pub device: i32,
}

impl License {
    pub fn new(device: i32) -> License {
        License {
            id: None,
            deleted: None,
            public_key: None,
            public_key_checksum: None,
            fingerprint: None,
            created_dt: None,
            device,
        }
    }
}


