/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.103.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct NatsOrganization {
    #[serde(rename = "id")]
    pub id: i32,
    /// The name of the organization
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "is_active", skip_serializing_if = "Option::is_none")]
    pub is_active: Option<bool>,
    #[serde(rename = "created")]
    pub created: String,
    #[serde(rename = "modified")]
    pub modified: String,
    /// The name in all lowercase, suitable for URL identification
    #[serde(rename = "slug")]
    pub slug: String,
    /// Output of `nsc describe account`
    #[serde(rename = "json", skip_serializing_if = "Option::is_none")]
    pub json: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "imports")]
    pub imports: Vec<i32>,
    #[serde(rename = "exports")]
    pub exports: Vec<i32>,
    #[serde(rename = "users")]
    pub users: Vec<i32>,
}

impl NatsOrganization {
    pub fn new(id: i32, name: String, created: String, modified: String, slug: String, imports: Vec<i32>, exports: Vec<i32>, users: Vec<i32>) -> NatsOrganization {
        NatsOrganization {
            id,
            name,
            is_active: None,
            created,
            modified,
            slug,
            json: None,
            imports,
            exports,
            users,
        }
    }
}


