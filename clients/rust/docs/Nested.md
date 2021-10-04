# Nested

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**password** | **String** |  | 
**is_superuser** | Option<**bool**> |  | [optional]
**is_staff** | Option<**bool**> |  | [optional]
**is_active** | Option<**bool**> |  | [optional]
**date_joined** | Option<**String**> |  | [optional]
**last_login** | Option<**String**> |  | [optional]
**first_name** | Option<**String**> |  | [optional]
**last_name** | Option<**String**> |  | [optional]
**email** | **String** |  | 
**groups** | Option<**Vec<i32>**> | The groups this user belongs to. A user will get all permissions granted to each of their groups. | [optional]
**user_permissions** | Option<**Vec<i32>**> | Specific permissions for this user. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


