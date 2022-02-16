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
pub struct JanusCloudAuthRequest {
    #[serde(rename = "api_token")]
    pub api_token: String,
    #[serde(rename = "user")]
    pub user: i32,
}

impl JanusCloudAuthRequest {
    pub fn new(api_token: String, user: i32) -> JanusCloudAuthRequest {
        JanusCloudAuthRequest {
            api_token,
            user,
        }
    }
}


