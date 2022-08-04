/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PublicKey {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "pem")]
    pub pem: String,
    #[serde(rename = "cipher")]
    pub cipher: String,
    #[serde(rename = "length")]
    pub length: i32,
    #[serde(rename = "fingerprint")]
    pub fingerprint: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl PublicKey {
    pub fn new(id: i32, pem: String, cipher: String, length: i32, fingerprint: String, created_dt: String, updated_dt: String, pi: i32) -> PublicKey {
        PublicKey {
            id,
            pem,
            cipher,
            length,
            fingerprint,
            created_dt,
            updated_dt,
            pi,
        }
    }
}


