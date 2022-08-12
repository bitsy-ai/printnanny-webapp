/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.9
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PrintNannyLicense {
    #[serde(rename = "nats_app")]
    pub nats_app: Option<Box<crate::models::NatsApp>>,
    #[serde(rename = "api")]
    pub api: Option<Box<crate::models::PrintNannyApiConfig>>,
    #[serde(rename = "pi")]
    pub pi: Option<Box<crate::models::Pi>>,
}

impl PrintNannyLicense {
    pub fn new(nats_app: Option<crate::models::NatsApp>, api: Option<crate::models::PrintNannyApiConfig>, pi: Option<crate::models::Pi>) -> PrintNannyLicense {
        PrintNannyLicense {
            nats_app: nats_app.map(Box::new),
            api: api.map(Box::new),
            pi: pi.map(Box::new),
        }
    }
}


