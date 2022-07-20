/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.96.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum AlertMethodsEnum {
    #[serde(rename = "UI")]
    UI,
    #[serde(rename = "EMAIL")]
    EMAIL,
    #[serde(rename = "DISCORD")]
    DISCORD,
    #[serde(rename = "PARTNER_3DGEEKS")]
    PARTNER3DGEEKS,

}

impl ToString for AlertMethodsEnum {
    fn to_string(&self) -> String {
        match self {
            Self::UI => String::from("UI"),
            Self::EMAIL => String::from("EMAIL"),
            Self::DISCORD => String::from("DISCORD"),
            Self::PARTNER3DGEEKS => String::from("PARTNER_3DGEEKS"),
        }
    }
}

impl Default for AlertMethodsEnum {
    fn default() -> AlertMethodsEnum {
        Self::UI
    }
}




