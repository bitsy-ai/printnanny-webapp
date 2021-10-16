/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct RemoteControlCommandRequest {
    #[serde(rename = "command", skip_serializing_if = "Option::is_none")]
    pub command: Option<crate::models::CommandEnum>,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "device")]
    pub device: i32,
    #[serde(rename = "received", skip_serializing_if = "Option::is_none")]
    pub received: Option<bool>,
    #[serde(rename = "success", skip_serializing_if = "Option::is_none")]
    pub success: Option<bool>,
    #[serde(rename = "iotcore_response", skip_serializing_if = "Option::is_none")]
    pub iotcore_response: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "metadata", skip_serializing_if = "Option::is_none")]
    pub metadata: Option<::std::collections::HashMap<String, serde_json::Value>>,
}

impl RemoteControlCommandRequest {
    pub fn new(user: i32, device: i32) -> RemoteControlCommandRequest {
        RemoteControlCommandRequest {
            command: None,
            user,
            device,
            received: None,
            success: None,
            iotcore_response: None,
            metadata: None,
        }
    }
}


