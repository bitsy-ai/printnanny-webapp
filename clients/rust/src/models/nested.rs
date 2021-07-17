/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct Nested {
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
    #[serde(rename = "notion_url", skip_serializing_if = "Option::is_none")]
    pub notion_url: Option<String>,
    #[serde(rename = "control")]
    pub control: i32,
    #[serde(rename = "treatments", skip_serializing_if = "Option::is_none")]
    pub treatments: Option<Vec<i32>>,
}

impl Nested {
    pub fn new(id: i32, created_dt: String, name: String, hypothesis: String, control: i32) -> Nested {
        Nested {
            id,
            created_dt,
            active: None,
            name,
            hypothesis,
            notion_url: None,
            control,
            treatments: None,
        }
    }
}


