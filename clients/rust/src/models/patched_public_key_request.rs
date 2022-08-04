/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.6
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedPublicKeyRequest {
    #[serde(rename = "pem", skip_serializing_if = "Option::is_none")]
    pub pem: Option<String>,
    #[serde(rename = "cipher", skip_serializing_if = "Option::is_none")]
    pub cipher: Option<String>,
    #[serde(rename = "length", skip_serializing_if = "Option::is_none")]
    pub length: Option<i32>,
    #[serde(rename = "fingerprint", skip_serializing_if = "Option::is_none")]
    pub fingerprint: Option<String>,
    #[serde(rename = "pi", skip_serializing_if = "Option::is_none")]
    pub pi: Option<i32>,
}

impl PatchedPublicKeyRequest {
    pub fn new() -> PatchedPublicKeyRequest {
        PatchedPublicKeyRequest {
            pem: None,
            cipher: None,
            length: None,
            fingerprint: None,
            pi: None,
        }
    }
}


