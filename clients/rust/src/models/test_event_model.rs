/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.97.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum TestEventModel {
    #[serde(rename = "TestEvent")]
    TestEvent,

}

impl ToString for TestEventModel {
    fn to_string(&self) -> String {
        match self {
            Self::TestEvent => String::from("TestEvent"),
        }
    }
}

impl Default for TestEventModel {
    fn default() -> TestEventModel {
        Self::TestEvent
    }
}




