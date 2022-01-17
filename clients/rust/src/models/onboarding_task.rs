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
pub struct OnboardingTask {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "task")]
    pub task: crate::models::TaskEnum,
    #[serde(rename = "status")]
    pub status: crate::models::TaskStatusType,
    #[serde(rename = "device")]
    pub device: i32,
}

impl OnboardingTask {
    pub fn new(id: i32, created_dt: String, task: crate::models::TaskEnum, status: crate::models::TaskStatusType, device: i32) -> OnboardingTask {
        OnboardingTask {
            id,
            created_dt,
            task,
            status,
            device,
        }
    }
}


