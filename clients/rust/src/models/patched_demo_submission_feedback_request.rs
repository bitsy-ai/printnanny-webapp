/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.134.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedDemoSubmissionFeedbackRequest {
    #[serde(rename = "feedback_nozzle", skip_serializing_if = "Option::is_none")]
    pub feedback_nozzle: Option<Box<crate::models::OneOfDemoFeedbackEnumNullEnum>>,
    #[serde(rename = "feedback_adhesion", skip_serializing_if = "Option::is_none")]
    pub feedback_adhesion: Option<Box<crate::models::OneOfDemoFeedbackEnumNullEnum>>,
    #[serde(rename = "feedback_spaghetti", skip_serializing_if = "Option::is_none")]
    pub feedback_spaghetti: Option<Box<crate::models::OneOfDemoFeedbackEnumNullEnum>>,
    #[serde(rename = "feedback_print", skip_serializing_if = "Option::is_none")]
    pub feedback_print: Option<Box<crate::models::OneOfDemoFeedbackEnumNullEnum>>,
    #[serde(rename = "feedback_raft", skip_serializing_if = "Option::is_none")]
    pub feedback_raft: Option<Box<crate::models::OneOfDemoFeedbackEnumNullEnum>>,
}

impl PatchedDemoSubmissionFeedbackRequest {
    pub fn new() -> PatchedDemoSubmissionFeedbackRequest {
        PatchedDemoSubmissionFeedbackRequest {
            feedback_nozzle: None,
            feedback_adhesion: None,
            feedback_spaghetti: None,
            feedback_print: None,
            feedback_raft: None,
        }
    }
}


