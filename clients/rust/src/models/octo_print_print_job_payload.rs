/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.6
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// OctoPrintPrintJobPayload : Serialize OctoPrint print job status events: https://docs.octoprint.org/en/master/events/index.html?highlight=events#printing



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintPrintJobPayload {
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "path")]
    pub path: String,
    #[serde(rename = "origin")]
    pub origin: String,
    #[serde(rename = "size", skip_serializing_if = "Option::is_none")]
    pub size: Option<i32>,
    #[serde(rename = "time", skip_serializing_if = "Option::is_none")]
    pub time: Option<f64>,
    #[serde(rename = "position")]
    pub position: ::std::collections::HashMap<String, serde_json::Value>,
}

impl OctoPrintPrintJobPayload {
    /// Serialize OctoPrint print job status events: https://docs.octoprint.org/en/master/events/index.html?highlight=events#printing
    pub fn new(name: String, path: String, origin: String, position: ::std::collections::HashMap<String, serde_json::Value>) -> OctoPrintPrintJobPayload {
        OctoPrintPrintJobPayload {
            name,
            path,
            origin,
            size: None,
            time: None,
            position,
        }
    }
}


