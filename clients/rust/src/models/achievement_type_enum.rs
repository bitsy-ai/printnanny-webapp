/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.110.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum AchievementTypeEnum {
    #[serde(rename = "Free Beta")]
    FreeBeta,
    #[serde(rename = "Founding Member")]
    FoundingMember,

}

impl ToString for AchievementTypeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::FreeBeta => String::from("Free Beta"),
            Self::FoundingMember => String::from("Founding Member"),
        }
    }
}

impl Default for AchievementTypeEnum {
    fn default() -> AchievementTypeEnum {
        Self::FreeBeta
    }
}



