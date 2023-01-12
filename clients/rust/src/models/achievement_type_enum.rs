/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.122.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum AchievementTypeEnum {
    #[serde(rename = "FreeBeta")]
    FreeBeta,
    #[serde(rename = "FoundingMember")]
    FoundingMember,

}

impl ToString for AchievementTypeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::FreeBeta => String::from("FreeBeta"),
            Self::FoundingMember => String::from("FoundingMember"),
        }
    }
}

impl Default for AchievementTypeEnum {
    fn default() -> AchievementTypeEnum {
        Self::FreeBeta
    }
}




