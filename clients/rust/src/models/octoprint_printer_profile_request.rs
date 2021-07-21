/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoprintPrinterProfileRequest {
    #[serde(rename = "name")]
    pub name: String,
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
    pub extruder_nozzle_diameter: Option<f32>,
    #[serde(rename = "extruder_shared_nozzle", skip_serializing_if = "Option::is_none")]
    pub extruder_shared_nozzle: Option<bool>,
    #[serde(rename = "heated_bed", skip_serializing_if = "Option::is_none")]
    pub heated_bed: Option<bool>,
    #[serde(rename = "heated_chamber", skip_serializing_if = "Option::is_none")]
    pub heated_chamber: Option<bool>,
    #[serde(rename = "model", skip_serializing_if = "Option::is_none")]
    pub model: Option<String>,
    #[serde(rename = "volume_custom_box", skip_serializing_if = "Option::is_none")]
    pub volume_custom_box: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "volume_depth", skip_serializing_if = "Option::is_none")]
    pub volume_depth: Option<f32>,
    #[serde(rename = "volume_formfactor", skip_serializing_if = "Option::is_none")]
    pub volume_formfactor: Option<String>,
    #[serde(rename = "volume_height", skip_serializing_if = "Option::is_none")]
    pub volume_height: Option<f32>,
    #[serde(rename = "volume_origin", skip_serializing_if = "Option::is_none")]
    pub volume_origin: Option<String>,
    #[serde(rename = "volume_width", skip_serializing_if = "Option::is_none")]
    pub volume_width: Option<f32>,
    #[serde(rename = "controller")]
    pub controller: i32,
    #[serde(rename = "device")]
    pub device: i32,
    #[serde(rename = "octoprint_controller")]
    pub octoprint_controller: i32,
}

impl OctoprintPrinterProfileRequest {
    pub fn new(name: String, controller: i32, device: i32, octoprint_controller: i32) -> OctoprintPrinterProfileRequest {
        OctoprintPrinterProfileRequest {
            name,
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
            volume_custom_box: None,
            volume_depth: None,
            volume_formfactor: None,
            volume_height: None,
            volume_origin: None,
            volume_width: None,
            controller,
            device,
            octoprint_controller,
        }
    }
}


