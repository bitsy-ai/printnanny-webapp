/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.126.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PreferredDnsType {
    #[serde(rename = "multicast")]
    Multicast,
    #[serde(rename = "tailscale")]
    Tailscale,

}

impl ToString for PreferredDnsType {
    fn to_string(&self) -> String {
        match self {
            Self::Multicast => String::from("multicast"),
            Self::Tailscale => String::from("tailscale"),
        }
    }
}

impl Default for PreferredDnsType {
    fn default() -> PreferredDnsType {
        Self::Multicast
    }
}




