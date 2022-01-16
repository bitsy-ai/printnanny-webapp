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
pub struct PatchedPublicKeyRequest {
    #[serde(rename = "pem", skip_serializing_if = "Option::is_none")]
    pub pem: Option<String>,
    #[serde(rename = "cipher", skip_serializing_if = "Option::is_none")]
    pub cipher: Option<crate::models::CipherEnum>,
    #[serde(rename = "length", skip_serializing_if = "Option::is_none")]
    pub length: Option<i32>,
    #[serde(rename = "fingerprint", skip_serializing_if = "Option::is_none")]
    pub fingerprint: Option<String>,
    #[serde(rename = "device", skip_serializing_if = "Option::is_none")]
    pub device: Option<i32>,
}

impl PatchedPublicKeyRequest {
    pub fn new() -> PatchedPublicKeyRequest {
        PatchedPublicKeyRequest {
            pem: None,
            cipher: None,
            length: None,
            fingerprint: None,
            device: None,
        }
    }
}


