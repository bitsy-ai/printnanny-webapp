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
**imports** | **Vec<i32>** |  | 
**exports** | **Vec<i32>** |  | 
**users** | **Vec<i32>** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


