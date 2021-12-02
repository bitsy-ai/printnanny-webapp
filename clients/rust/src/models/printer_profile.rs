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
pub struct PrinterProfile {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "octoprint_device")]
    pub octoprint_device: i32,
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
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "octoprint_key")]
    pub octoprint_key: String,
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
    #[serde(rename = "url")]
    pub url: String,
}

impl PrinterProfile {
    pub fn new(id: i32, user: i32, octoprint_device: i32, name: String, octoprint_key: String, url: String) -> PrinterProfile {
        PrinterProfile {
            id,
            user,
            octoprint_device,
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
            name,
            octoprint_key,
            volume_custom_box: None,
            volume_depth: None,
            volume_formfactor: None,
            volume_height: None,
            volume_origin: None,
            volume_width: None,
            url,
        }
    }
}


