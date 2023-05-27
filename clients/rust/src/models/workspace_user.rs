/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.135.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct WorkspaceUser {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "user")]
    pub user: Box<crate::models::User>,
    #[serde(rename = "created")]
    pub created: String,
    #[serde(rename = "modified")]
    pub modified: String,
    #[serde(rename = "is_admin", skip_serializing_if = "Option::is_none")]
    pub is_admin: Option<bool>,
    #[serde(rename = "organization")]
    pub organization: i32,
}

impl WorkspaceUser {
    pub fn new(id: i32, user: crate::models::User, created: String, modified: String, organization: i32) -> WorkspaceUser {
        WorkspaceUser {
            id,
            user: Box::new(user),
            created,
            modified,
            is_admin: None,
            organization,
        }
    }
}


