/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.96.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct DeviceRequest {
    /// Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)
    #[serde(rename = "hostname", skip_serializing_if = "Option::is_none")]
    pub hostname: Option<String>,
    #[serde(rename = "fqdn", skip_serializing_if = "Option::is_none")]
    pub fqdn: Option<String>,
    #[serde(rename = "favorite", skip_serializing_if = "Option::is_none")]
    pub favorite: Option<bool>,
    #[serde(rename = "ws_connected", skip_serializing_if = "Option::is_none")]
    pub ws_connected: Option<bool>,
}

impl DeviceRequest {
    pub fn new() -> DeviceRequest {
        DeviceRequest {
            hostname: None,
            fqdn: None,
            favorite: None,
            ws_connected: None,
        }
    }
}


