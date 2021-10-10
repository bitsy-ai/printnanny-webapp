/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct CreateAppliancePkiRequest {
    #[serde(rename = "public_key")]
    pub public_key: String,
    #[serde(rename = "public_key_checksum")]
    pub public_key_checksum: String,
    #[serde(rename = "fingerprint")]
    pub fingerprint: String,
}

impl CreateAppliancePkiRequest {
    pub fn new(public_key: String, public_key_checksum: String, fingerprint: String) -> CreateAppliancePkiRequest {
        CreateAppliancePkiRequest {
            public_key,
            public_key_checksum,
            fingerprint,
        }
    }
}


