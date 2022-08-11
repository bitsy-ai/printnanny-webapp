/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.8
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PublicKeyRequest {
    #[serde(rename = "pem")]
    pub pem: String,
    #[serde(rename = "cipher")]
    pub cipher: String,
    #[serde(rename = "length")]
    pub length: i32,
    #[serde(rename = "fingerprint")]
    pub fingerprint: String,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PublicKeyRequest {
    pub fn new(pem: String, cipher: String, length: i32, fingerprint: String, pi: i32) -> PublicKeyRequest {
        PublicKeyRequest {
            pem,
            cipher,
            length,
            fingerprint,
            pi,
        }
    }
}


