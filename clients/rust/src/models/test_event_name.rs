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
pub enum TestEventName {
    #[serde(rename = "mqtt_ping")]
    Ping,
    #[serde(rename = "mqtt_pong")]
    Pong,

}

impl ToString for TestEventName {
    fn to_string(&self) -> String {
        match self {
            Self::Ping => String::from("mqtt_ping"),
            Self::Pong => String::from("mqtt_pong"),
        }
    }
}

impl Default for TestEventName {
    fn default() -> TestEventName {
        Self::Ping
    }
}




