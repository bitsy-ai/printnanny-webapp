# NatsOrganization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | The name of the organization | 
**is_active** | **bool** |  | [optional] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**slug** | **str** | The name in all lowercase, suitable for URL identification | 
**json** | **dict(str, object)** | Output of &#x60;nsc describe account&#x60; | [optional] 
**imports** | **list[int]** |  | 
**exports** | **list[int]** |  | 
**users** | **list[int]** |  | [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


