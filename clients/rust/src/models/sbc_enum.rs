/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.127.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum SbcEnum {
    #[serde(rename = "rpi_4")]
    Rpi4,

}

impl ToString for SbcEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Rpi4 => String::from("rpi_4"),
        }
    }
}

impl Default for SbcEnum {
    fn default() -> SbcEnum {
        Self::Rpi4
    }
}




