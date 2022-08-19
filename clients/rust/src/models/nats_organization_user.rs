/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.103.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct NatsOrganizationUser {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "app_name", skip_serializing_if = "Option::is_none")]
    pub app_name: Option<String>,
    #[serde(rename = "organization")]
    pub organization: i32,
    #[serde(rename = "creds")]
    pub creds: String,
    /// Output of `nsc describe account`
    #[serde(rename = "json", skip_serializing_if = "Option::is_none")]
    pub json: Option<::std::collections::HashMap<String, serde_json::Value>>,
}

impl NatsOrganizationUser {
    pub fn new(id: i32, organization: i32, creds: String) -> NatsOrganizationUser {
        NatsOrganizationUser {
            id,
            app_name: None,
            organization,
            creds,
            json: None,
        }
    }
}


