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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

