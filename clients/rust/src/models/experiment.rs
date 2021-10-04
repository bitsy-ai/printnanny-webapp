/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Experiment {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "hypothesis")]
    pub hypothesis: String,
    #[serde(rename = "control")]
    pub control: Option<Box<crate::models::Nested>>,
    #[serde(rename = "treatments")]
    pub treatments: Vec<crate::models::Nested>,
    #[serde(rename = "notion_url", skip_serializing_if = "Option::is_none")]
    pub notion_url: Option<String>,
}

impl Experiment {
    pub fn new(id: i32, created_dt: String, name: String, hypothesis: String, control: Option<crate::models::Nested>, treatments: Vec<crate::models::Nested>) -> Experiment {
        Experiment {
            id,
            created_dt,
            active: None,
            name,
            hypothesis,
            control: Box::new(control),
            treatments,
            notion_url: None,
        }
    }
}


