/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.114.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct RestAuthDetail {
    #[serde(rename = "detail")]
    pub detail: String,
}

impl RestAuthDetail {
    pub fn new(detail: String) -> RestAuthDetail {
        RestAuthDetail {
            detail,
        }
    }
}


