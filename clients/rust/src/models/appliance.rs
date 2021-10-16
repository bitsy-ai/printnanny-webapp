/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct Appliance {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "pki")]
    pub pki: Option<Box<crate::models::AppliancePki>>,
    #[serde(rename = "ansible_facts")]
    pub ansible_facts: Option<Box<crate::models::AnsibleFacts>>,
    #[serde(rename = "cameras")]
    pub cameras: Vec<crate::models::Camera>,
    #[serde(rename = "printer_controllers")]
    pub printer_controllers: Vec<crate::models::PrinterController>,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "deleted")]
    pub deleted: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "hostname")]
    pub hostname: String,
}

impl Appliance {
    pub fn new(id: i32, pki: Option<crate::models::AppliancePki>, ansible_facts: Option<crate::models::AnsibleFacts>, cameras: Vec<crate::models::Camera>, printer_controllers: Vec<crate::models::PrinterController>, user: i32, deleted: String, created_dt: String, updated_dt: String, hostname: String) -> Appliance {
        Appliance {
            id,
            pki: None,
            ansible_facts: None,
            cameras,
            printer_controllers,
            user,
            deleted,
            created_dt,
            updated_dt,
            hostname,
        }
    }
}


