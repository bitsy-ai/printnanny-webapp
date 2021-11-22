/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct AnsibleExtraVarsRequest {
    #[serde(rename = "janus_version")]
    pub janus_version: String,
    #[serde(rename = "janus_libwebsockets_version")]
    pub janus_libwebsockets_version: String,
    #[serde(rename = "janus_libnice_version")]
    pub janus_libnice_version: String,
    #[serde(rename = "janus_usrsctp_version")]
    pub janus_usrsctp_version: String,
    #[serde(rename = "janus_libsrtp_version")]
    pub janus_libsrtp_version: String,
    #[serde(rename = "tflite_version")]
    pub tflite_version: String,
    #[serde(rename = "printnanny_cli_version")]
    pub printnanny_cli_version: String,
    #[serde(rename = "libcamera_version")]
    pub libcamera_version: String,
}

impl AnsibleExtraVarsRequest {
    pub fn new(janus_version: String, janus_libwebsockets_version: String, janus_libnice_version: String, janus_usrsctp_version: String, janus_libsrtp_version: String, tflite_version: String, printnanny_cli_version: String, libcamera_version: String) -> AnsibleExtraVarsRequest {
        AnsibleExtraVarsRequest {
            janus_version,
            janus_libwebsockets_version,
            janus_libnice_version,
            janus_usrsctp_version,
            janus_libsrtp_version,
            tflite_version,
            printnanny_cli_version,
            libcamera_version,
        }
    }
}


