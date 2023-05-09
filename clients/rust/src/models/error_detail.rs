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
pub struct ErrorDetail {
    #[serde(rename = "detail")]
    pub detail: String,
    #[serde(rename = "code")]
    pub code: String,
}

impl ErrorDetail {
    pub fn new(detail: String, code: String) -> ErrorDetail {
        ErrorDetail {
            detail,
            code,
        }
    }
}


