/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.135.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedOctoPrinterProfileRequest {
    #[serde(rename = "axes_e_inverted", skip_serializing_if = "Option::is_none")]
    pub axes_e_inverted: Option<bool>,
    #[serde(rename = "axes_e_speed", skip_serializing_if = "Option::is_none")]
    pub axes_e_speed: Option<i32>,
    #[serde(rename = "axes_x_speed", skip_serializing_if = "Option::is_none")]
    pub axes_x_speed: Option<i32>,
    #[serde(rename = "axes_x_inverted", skip_serializing_if = "Option::is_none")]
    pub axes_x_inverted: Option<bool>,
    #[serde(rename = "axes_y_inverted", skip_serializing_if = "Option::is_none")]
    pub axes_y_inverted: Option<bool>,
    #[serde(rename = "axes_y_speed", skip_serializing_if = "Option::is_none")]
    pub axes_y_speed: Option<i32>,
    #[serde(rename = "axes_z_inverted", skip_serializing_if = "Option::is_none")]
    pub axes_z_inverted: Option<bool>,
    #[serde(rename = "axes_z_speed", skip_serializing_if = "Option::is_none")]
    pub axes_z_speed: Option<i32>,
    #[serde(rename = "extruder_count", skip_serializing_if = "Option::is_none")]
    pub extruder_count: Option<i32>,
    #[serde(rename = "extruder_nozzle_diameter", skip_serializing_if = "Option::is_none")]
    pub extruder_nozzle_diameter: Option<f64>,
    #[serde(rename = "extruder_shared_nozzle", skip_serializing_if = "Option::is_none")]
    pub extruder_shared_nozzle: Option<bool>,
    #[serde(rename = "heated_bed", skip_serializing_if = "Option::is_none")]
    pub heated_bed: Option<bool>,
    #[serde(rename = "heated_chamber", skip_serializing_if = "Option::is_none")]
    pub heated_chamber: Option<bool>,
    #[serde(rename = "model", skip_serializing_if = "Option::is_none")]
    pub model: Option<String>,
    #[serde(rename = "name", skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    #[serde(rename = "octoprint_key", skip_serializing_if = "Option::is_none")]
    pub octoprint_key: Option<String>,
    #[serde(rename = "volume_custom_box", skip_serializing_if = "Option::is_none")]
    pub volume_custom_box: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "volume_depth", skip_serializing_if = "Option::is_none")]
    pub volume_depth: Option<f64>,
    #[serde(rename = "volume_formfactor", skip_serializing_if = "Option::is_none")]
    pub volume_formfactor: Option<String>,
    #[serde(rename = "volume_height", skip_serializing_if = "Option::is_none")]
    pub volume_height: Option<f64>,
    #[serde(rename = "volume_origin", skip_serializing_if = "Option::is_none")]
    pub volume_origin: Option<String>,
    #[serde(rename = "volume_width", skip_serializing_if = "Option::is_none")]
    pub volume_width: Option<f64>,
}

impl PatchedOctoPrinterProfileRequest {
    pub fn new() -> PatchedOctoPrinterProfileRequest {
        PatchedOctoPrinterProfileRequest {
            axes_e_inverted: None,
            axes_e_speed: None,
            axes_x_speed: None,
            axes_x_inverted: None,
            axes_y_inverted: None,
            axes_y_speed: None,
            axes_z_inverted: None,
            axes_z_speed: None,
            extruder_count: None,
            extruder_nozzle_diameter: None,
            extruder_shared_nozzle: None,
            heated_bed: None,
            heated_chamber: None,
            model: None,
            name: None,
            octoprint_key: None,
            volume_custom_box: None,
            volume_depth: None,
            volume_formfactor: None,
            volume_height: None,
            volume_origin: None,
            volume_width: None,
        }
    }
}


