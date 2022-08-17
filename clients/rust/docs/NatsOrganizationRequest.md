# NatsOrganizationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the organization | 
**is_active** | Option<**bool**> |  | [optional]
**slug** | **String** | The name in all lowercase, suitable for URL identification | 
**json** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Output of `nsc describe account` | [optional]
**imports** | **Vec<i32>** |  | 
**exports** | **Vec<i32>** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


