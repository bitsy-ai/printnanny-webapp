/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.133.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// InterestEnum : * `printnanny` - Subscribe to PrintNanny news and development updates * `sdwire` - Get notified when SDWire is back in stock * `rpi4_kit` - Get notified when Raspberry Pi 4 kits are available

/// * `printnanny` - Subscribe to PrintNanny news and development updates * `sdwire` - Get notified when SDWire is back in stock * `rpi4_kit` - Get notified when Raspberry Pi 4 kits are available
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum InterestEnum {
    #[serde(rename = "printnanny")]
    Printnanny,
    #[serde(rename = "sdwire")]
    Sdwire,
    #[serde(rename = "rpi4_kit")]
    Rpi4Kit,

}

impl ToString for InterestEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Printnanny => String::from("printnanny"),
            Self::Sdwire => String::from("sdwire"),
            Self::Rpi4Kit => String::from("rpi4_kit"),
        }
    }
}

impl Default for InterestEnum {
    fn default() -> InterestEnum {
        Self::Printnanny
    }
}




