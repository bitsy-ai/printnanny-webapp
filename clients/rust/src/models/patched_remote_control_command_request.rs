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
pub struct PatchedRemoteControlCommandRequest {
    #[serde(rename = "command", skip_serializing_if = "Option::is_none")]
    pub command: Option<crate::models::RemoteControlCommandCommandEnum>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<i32>,
    #[serde(rename = "device", skip_serializing_if = "Option::is_none")]
    pub device: Option<i32>,
    #[serde(rename = "received", skip_serializing_if = "Option::is_none")]
    pub received: Option<bool>,
    #[serde(rename = "success", skip_serializing_if = "Option::is_none")]
    pub success: Option<bool>,
    #[serde(rename = "iotcore_response", skip_serializing_if = "Option::is_none")]
    pub iotcore_response: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "metadata", skip_serializing_if = "Option::is_none")]
    pub metadata: Option<::std::collections::HashMap<String, serde_json::Value>>,
}

impl PatchedRemoteControlCommandRequest {
    pub fn new() -> PatchedRemoteControlCommandRequest {
        PatchedRemoteControlCommandRequest {
            command: None,
            user: None,
            device: None,
            received: None,
            success: None,
            iotcore_response: None,
            metadata: None,
        }
    }
}


