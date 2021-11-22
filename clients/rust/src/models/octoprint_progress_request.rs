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
pub struct OctoprintProgressRequest {
    #[serde(rename = "completion")]
    pub completion: Option<f32>,
    #[serde(rename = "filepos")]
    pub filepos: Option<i32>,
    #[serde(rename = "printTime")]
    pub print_time: Option<i32>,
    #[serde(rename = "printTimeLeft")]
    pub print_time_left: Option<i32>,
    #[serde(rename = "printTimeOrigin", skip_serializing_if = "Option::is_none")]
    pub print_time_origin: Option<String>,
}

impl OctoprintProgressRequest {
    pub fn new(completion: Option<f32>, filepos: Option<i32>, print_time: Option<i32>, print_time_left: Option<i32>) -> OctoprintProgressRequest {
        OctoprintProgressRequest {
            completion,
            filepos,
            print_time,
            print_time_left,
            print_time_origin: None,
        }
    }
}


