/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "resourcetype")]
pub enum PatchedPrinterProfilePolymorphicRequest {
    #[serde(rename="OctoprintPrinterProfile")]
    PatchedOctoprintPrinterProfileRequest {
        #[serde(rename = "name", skip_serializing_if = "Option::is_none")]
        name: Option<String>,
        #[serde(rename = "axes_e_inverted", skip_serializing_if = "Option::is_none")]
        axes_e_inverted: Option<bool>,
        #[serde(rename = "axes_e_speed", skip_serializing_if = "Option::is_none")]
        axes_e_speed: Option<i32>,
        #[serde(rename = "axes_x_speed", skip_serializing_if = "Option::is_none")]
        axes_x_speed: Option<i32>,
        #[serde(rename = "axes_x_inverted", skip_serializing_if = "Option::is_none")]
        axes_x_inverted: Option<bool>,
        #[serde(rename = "axes_y_inverted", skip_serializing_if = "Option::is_none")]
        axes_y_inverted: Option<bool>,
        #[serde(rename = "axes_y_speed", skip_serializing_if = "Option::is_none")]
        axes_y_speed: Option<i32>,
        #[serde(rename = "axes_z_inverted", skip_serializing_if = "Option::is_none")]
        axes_z_inverted: Option<bool>,
        #[serde(rename = "axes_z_speed", skip_serializing_if = "Option::is_none")]
        axes_z_speed: Option<i32>,
        #[serde(rename = "extruder_count", skip_serializing_if = "Option::is_none")]
        extruder_count: Option<i32>,
        #[serde(rename = "extruder_nozzle_diameter", skip_serializing_if = "Option::is_none")]
        extruder_nozzle_diameter: Option<f32>,
        #[serde(rename = "extruder_shared_nozzle", skip_serializing_if = "Option::is_none")]
        extruder_shared_nozzle: Option<bool>,
        #[serde(rename = "heated_bed", skip_serializing_if = "Option::is_none")]
        heated_bed: Option<bool>,
        #[serde(rename = "heated_chamber", skip_serializing_if = "Option::is_none")]
        heated_chamber: Option<bool>,
        #[serde(rename = "model", skip_serializing_if = "Option::is_none")]
        model: Option<String>,
        #[serde(rename = "volume_custom_box", skip_serializing_if = "Option::is_none")]
        volume_custom_box: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "volume_depth", skip_serializing_if = "Option::is_none")]
        volume_depth: Option<f32>,
        #[serde(rename = "volume_formfactor", skip_serializing_if = "Option::is_none")]
        volume_formfactor: Option<String>,
        #[serde(rename = "volume_height", skip_serializing_if = "Option::is_none")]
        volume_height: Option<f32>,
        #[serde(rename = "volume_origin", skip_serializing_if = "Option::is_none")]
        volume_origin: Option<String>,
        #[serde(rename = "volume_width", skip_serializing_if = "Option::is_none")]
        volume_width: Option<f32>,
        #[serde(rename = "controller", skip_serializing_if = "Option::is_none")]
        controller: Option<i32>,
        #[serde(rename = "device", skip_serializing_if = "Option::is_none")]
        device: Option<i32>,
        #[serde(rename = "octoprint_controller", skip_serializing_if = "Option::is_none")]
        octoprint_controller: Option<i32>,
    },
    #[serde(rename="PrinterProfile")]
    PatchedPrinterProfileRequest {
        #[serde(rename = "name", skip_serializing_if = "Option::is_none")]
        name: Option<String>,
        #[serde(rename = "controller", skip_serializing_if = "Option::is_none")]
        controller: Option<i32>,
        #[serde(rename = "device", skip_serializing_if = "Option::is_none")]
        device: Option<i32>,
    },
}




