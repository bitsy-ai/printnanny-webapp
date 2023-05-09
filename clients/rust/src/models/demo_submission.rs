/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.134.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct DemoSubmission {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "email")]
    pub email: String,
    #[serde(rename = "submission")]
    pub submission: String,
    #[serde(rename = "result")]
    pub result: String,
    #[serde(rename = "feedback_nozzle")]
    pub feedback_nozzle: Option<Box<crate::models::DemoFeedbackEnum>>,
    #[serde(rename = "feedback_adhesion")]
    pub feedback_adhesion: Option<Box<crate::models::DemoFeedbackEnum>>,
    #[serde(rename = "feedback_spaghetti")]
    pub feedback_spaghetti: Option<Box<crate::models::DemoFeedbackEnum>>,
    #[serde(rename = "feedback_print")]
    pub feedback_print: Option<Box<crate::models::DemoFeedbackEnum>>,
    #[serde(rename = "feedback_raft")]
    pub feedback_raft: Option<Box<crate::models::DemoFeedbackEnum>>,
}

impl DemoSubmission {
    pub fn new(id: String, created_dt: String, email: String, submission: String, result: String, feedback_nozzle: Option<crate::models::DemoFeedbackEnum>, feedback_adhesion: Option<crate::models::DemoFeedbackEnum>, feedback_spaghetti: Option<crate::models::DemoFeedbackEnum>, feedback_print: Option<crate::models::DemoFeedbackEnum>, feedback_raft: Option<crate::models::DemoFeedbackEnum>) -> DemoSubmission {
        DemoSubmission {
            id,
            created_dt,
            email,
            submission,
            result,
            feedback_nozzle: feedback_nozzle.map(Box::new),
            feedback_adhesion: feedback_adhesion.map(Box::new),
            feedback_spaghetti: feedback_spaghetti.map(Box::new),
            feedback_print: feedback_print.map(Box::new),
            feedback_raft: feedback_raft.map(Box::new),
        }
    }
}


