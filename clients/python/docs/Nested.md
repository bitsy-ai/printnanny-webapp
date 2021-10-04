# Nested


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**password** | **str** |  | 
**is_superuser** | **bool** |  | [optional] 
**is_staff** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**date_joined** | **datetime** |  | [optional] 
**last_login** | **datetime** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | 
**groups** | **list[int]** | The groups this user belongs to. A user will get all permissions granted to each of their groups. | [optional] 
**user_permissions** | **list[int]** | Specific permissions for this user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


