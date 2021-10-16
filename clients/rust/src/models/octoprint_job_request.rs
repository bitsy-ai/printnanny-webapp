/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoprintJobRequest {
    #[serde(rename = "file", skip_serializing_if = "Option::is_none")]
    pub file: Option<Box<crate::models::OctoprintFileRequest>>,
    #[serde(rename = "estimatedPrintTime", skip_serializing_if = "Option::is_none")]
    pub estimated_print_time: Option<f32>,
    #[serde(rename = "averagePrintTime", skip_serializing_if = "Option::is_none")]
    pub average_print_time: Option<f32>,
    #[serde(rename = "lastPrintTime", skip_serializing_if = "Option::is_none")]
    pub last_print_time: Option<f32>,
    #[serde(rename = "filament")]
    pub filament: Option<::std::collections::HashMap<String, serde_json::Value>>,
}

impl OctoprintJobRequest {
    pub fn new(filament: Option<::std::collections::HashMap<String, serde_json::Value>>) -> OctoprintJobRequest {
        OctoprintJobRequest {
            file: NoneSome(,
            estimated_print_time: NoneSome(,
            average_print_time: NoneSome(,
            last_print_time: NoneSome(,
            filamentSome(Some(,
        }
    }
}


