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
pub struct OctoprintPrinterDataRequest {
    #[serde(rename = "job")]
    pub job: Box<crate::models::OctoprintJobRequest>,
    #[serde(rename = "state")]
    pub state: Box<crate::models::OctoprintPrinterStateRequest>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<String>,
    #[serde(rename = "currentZ", skip_serializing_if = "Option::is_none")]
    pub current_z: Option<f32>,
    #[serde(rename = "progress")]
    pub progress: Box<crate::models::OctoprintProgressRequest>,
    #[serde(rename = "resends")]
    pub resends: ::std::collections::HashMap<String, serde_json::Value>,
    #[serde(rename = "offsets")]
    pub offsets: ::std::collections::HashMap<String, serde_json::Value>,
}

impl OctoprintPrinterDataRequest {
    pub fn new(job: crate::models::OctoprintJobRequest, state: crate::models::OctoprintPrinterStateRequest, progress: crate::models::OctoprintProgressRequest, resends: ::std::collections::HashMap<String, serde_json::Value>, offsets: ::std::collections::HashMap<String, serde_json::Value>) -> OctoprintPrinterDataRequest {
        OctoprintPrinterDataRequest {
            job: Box::new(job),
            state: Box::new(state),
            user: None,
            current_z: None,
            progress: Box::new(progress),
            resends,
            offsets,
        }
    }
}


