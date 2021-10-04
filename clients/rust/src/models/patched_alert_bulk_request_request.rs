/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */

/// PatchedAlertBulkRequestRequest : Serializer used in POST /api/alerts/seen and POST /api/alerts/dismiss requests



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PatchedAlertBulkRequestRequest {
    #[serde(rename = "ids", skip_serializing_if = "Option::is_none")]
    pub ids: Option<Vec<i32>>,
}

impl PatchedAlertBulkRequestRequest {
    /// Serializer used in POST /api/alerts/seen and POST /api/alerts/dismiss requests
    pub fn new() -> PatchedAlertBulkRequestRequest {
        PatchedAlertBulkRequestRequest {
            ids: None,
        }
    }
}


