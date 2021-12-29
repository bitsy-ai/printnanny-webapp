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
pub struct Release {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "deleted")]
    pub deleted: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "variant")]
    pub variant: crate::models::VariantEnum,
    #[serde(rename = "image_url")]
    pub image_url: String,
    #[serde(rename = "manifest_url")]
    pub manifest_url: String,
    #[serde(rename = "sig_url")]
    pub sig_url: String,
    #[serde(rename = "checksum")]
    pub checksum: String,
    #[serde(rename = "checksum_url")]
    pub checksum_url: String,
    #[serde(rename = "release_channel", skip_serializing_if = "Option::is_none")]
    pub release_channel: Option<crate::models::ReleaseChannelEnum>,
}

impl Release {
    pub fn new(id: i32, deleted: String, created_dt: String, name: String, variant: crate::models::VariantEnum, image_url: String, manifest_url: String, sig_url: String, checksum: String, checksum_url: String) -> Release {
        Release {
            id,
            deleted,
            created_dt,
            name,
            variant,
            image_url,
            manifest_url,
            sig_url,
            checksum,
            checksum_url,
            release_channel: None,
        }
    }
}


