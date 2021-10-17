/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct AppliancePkiRequest {
    #[serde(rename = "public_key_path")]
    pub public_key_path: String,
    #[serde(rename = "private_key_path")]
    pub private_key_path: String,
    #[serde(rename = "public_key")]
    pub public_key: String,
    #[serde(rename = "public_key_checksum")]
    pub public_key_checksum: String,
    #[serde(rename = "fingerprint")]
    pub fingerprint: String,
}

impl AppliancePkiRequest {
    pub fn new(public_key_path: String, private_key_path: String, public_key: String, public_key_checksum: String, fingerprint: String) -> AppliancePkiRequest {
        AppliancePkiRequest {
            public_key_path,
            private_key_path,
            public_key,
            public_key_checksum,
            fingerprint,
        }
    }
}


