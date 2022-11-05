# PiNatsApp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**app_name** | Option<**String**> |  | [optional]
**json** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Output of `nsc describe account` | [optional]
**pi** | **i32** |  | 
**organization** | [**crate::models::NatsOrganization**](NatsOrganization.md) |  | 
**organization_user** | **i32** |  | 
**nats_server_uri** | **String** |  | [readonly]
**nats_ws_uri** | **String** |  | [readonly]
**nats_subject_pattern** | **String** |  | [readonly]
**nats_subject_pattern_template** | **String** |  | [readonly]
**mqtt_subject_template_moonraker_request** | **String** |  | [readonly]
**mqtt_subject_moonraker_request** | **String** |  | [readonly]
**mqtt_subject_template_moonraker_response** | **String** |  | [readonly]
**mqtt_subject_moonraker_response** | **String** |  | [readonly]
**mqtt_subject_template_klipper_status** | **String** |  | [readonly]
**mqtt_subject_klipper_status** | **String** |  | [readonly]
**mqtt_broker_host** | **String** |  | [readonly]
**mqtt_broker_port** | **i32** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


