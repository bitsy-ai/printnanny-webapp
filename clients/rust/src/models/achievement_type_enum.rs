/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.9
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// AchievementTypeEnum : * `FreeBeta` - Participated in free beta program * `FoundingMember` - Supported PrintNanny by pre-ordering an annual subscription * `Cloud Starter` - Subscribed to PrintNanny Cloud Starter plan * `Cloud Scaler` - Subscribed to PrintNanny Cloud Scaler plan

/// * `FreeBeta` - Participated in free beta program * `FoundingMember` - Supported PrintNanny by pre-ordering an annual subscription * `Cloud Starter` - Subscribed to PrintNanny Cloud Starter plan * `Cloud Scaler` - Subscribed to PrintNanny Cloud Scaler plan
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum AchievementTypeEnum {
    #[serde(rename = "FreeBeta")]
    FreeBeta,
    #[serde(rename = "FoundingMember")]
    FoundingMember,
    #[serde(rename = "Cloud Starter")]
    CloudStarter,
    #[serde(rename = "Cloud Scaler")]
    CloudScaler,

}

impl ToString for AchievementTypeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::FreeBeta => String::from("FreeBeta"),
            Self::FoundingMember => String::from("FoundingMember"),
            Self::CloudStarter => String::from("Cloud Starter"),
            Self::CloudScaler => String::from("Cloud Scaler"),
        }
    }
}

impl Default for AchievementTypeEnum {
    fn default() -> AchievementTypeEnum {
        Self::FreeBeta
    }
}




