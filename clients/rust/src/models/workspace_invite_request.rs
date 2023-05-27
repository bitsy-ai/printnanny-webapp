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
pub struct WorkspaceInviteRequest {
    /// The contact identifier for the invitee, email, phone number, social media handle, etc.
    #[serde(rename = "invitee_identifier")]
    pub invitee_identifier: String,
    #[serde(rename = "invited_by")]
    pub invited_by: i32,
    #[serde(rename = "invitee", skip_serializing_if = "Option::is_none")]
    pub invitee: Option<i32>,
    #[serde(rename = "organization")]
    pub organization: i32,
}

impl WorkspaceInviteRequest {
    pub fn new(invitee_identifier: String, invited_by: i32, organization: i32) -> WorkspaceInviteRequest {
        WorkspaceInviteRequest {
            invitee_identifier,
            invited_by,
            invitee: None,
            organization,
        }
    }
}


