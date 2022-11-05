# NatsOrganization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**name** | **String** | The name of the organization | 
**is_active** | Option<**bool**> |  | [optional]
**created** | **String** |  | [readonly]
**modified** | **String** |  | [readonly]
**slug** | **String** | The name in all lowercase, suitable for URL identification | 
**json** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Output of `nsc describe account` | [optional]
**jetstream_enabled** | Option<**bool**> | Enable JetStream for all users/apps belonging to NatsOrganization account | [optional]
**jetstream_max_mem** | Option<**String**> | JetStream memory resource limits (shared across all users/apps beloning to NatsOrganization account) | [optional]
**jetstream_max_file** | Option<**String**> | JetStream file resource limits (shared across all users/apps beloning to NatsOrganization account) | [optional]
**jetstream_max_streams** | Option<**i32**> | JetStream max number of streams (shared across all users/apps beloning to NatsOrganization account) | [optional]
**jetstream_max_consumers** | Option<**i32**> | JetStream max number of consumers (shared across all users/apps beloning to NatsOrganization account) | [optional]
**imports** | **Vec<i32>** |  | 
**exports** | **Vec<i32>** |  | 
**users** | **Vec<i32>** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


