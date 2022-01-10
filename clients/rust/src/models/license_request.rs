/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */

/// LicenseRequest : Deserialize data/license info into /opt/printnanny during License Activation



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct LicenseRequest {
    #[serde(rename = "activated", skip_serializing_if = "Option::is_none")]
    pub activated: Option<bool>,
    #[serde(rename = "janus_admin_secret", skip_serializing_if = "Option::is_none")]
    pub janus_admin_secret: Option<String>,
    #[serde(rename = "janus_token", skip_serializing_if = "Option::is_none")]
    pub janus_token: Option<String>,
}

impl LicenseRequest {
    /// Deserialize data/license info into /opt/printnanny during License Activation
    pub fn new() -> LicenseRequest {
        LicenseRequest {
            activated: None,
            janus_admin_secret: None,
            janus_token: None,
        }
    }
}


