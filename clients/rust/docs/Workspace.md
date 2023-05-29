# Workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**users** | [**Vec<crate::models::User>**](User.md) |  | [readonly]
**owner** | Option<[**crate::models::WorkspaceOwner**](WorkspaceOwner.md)> |  | [readonly]
**pending_invites** | [**Vec<crate::models::WorkspaceInvite>**](WorkspaceInvite.md) |  | [readonly]
**name** | **String** | The name of the organization | 
**is_active** | Option<**bool**> |  | [optional]
**created** | **String** |  | [readonly]
**modified** | **String** |  | [readonly]
**slug** | **String** | The name in all lowercase, suitable for URL identification | 
**description** | **String** |  | 
**icon** | Option<**String**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


