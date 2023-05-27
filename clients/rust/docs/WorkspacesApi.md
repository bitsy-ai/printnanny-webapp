# \WorkspacesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_pi_to_workspace**](WorkspacesApi.md#assign_pi_to_workspace) | **POST** /api/devices/{pi_id}/assign-workspace/{workspace_id}/ | 
[**workspaces_create**](WorkspacesApi.md#workspaces_create) | **POST** /api/workspaces/ | 
[**workspaces_create_invite**](WorkspacesApi.md#workspaces_create_invite) | **POST** /api/workspaces/invite/ | 
[**workspaces_list**](WorkspacesApi.md#workspaces_list) | **GET** /api/workspaces/ | 
[**workspaces_partial_update**](WorkspacesApi.md#workspaces_partial_update) | **PATCH** /api/workspaces/{id}/ | 
[**workspaces_remind_invite**](WorkspacesApi.md#workspaces_remind_invite) | **POST** /api/workspaces/remind/ | 
[**workspaces_retrieve**](WorkspacesApi.md#workspaces_retrieve) | **GET** /api/workspaces/{id}/ | 
[**workspaces_update**](WorkspacesApi.md#workspaces_update) | **PUT** /api/workspaces/{id}/ | 
[**workspaces_verify_invite**](WorkspacesApi.md#workspaces_verify_invite) | **POST** /api/workspace-invites/verify/ | 



## assign_pi_to_workspace

> crate::models::Pi assign_pi_to_workspace(pi_id, workspace_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**workspace_id** | **i32** |  | [required] |

### Return type

[**crate::models::Pi**](Pi.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## workspaces_create

> crate::models::Workspace workspaces_create(workspace_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**workspace_request** | [**WorkspaceRequest**](WorkspaceRequest.md) |  | [required] |

### Return type

[**crate::models::Workspace**](Workspace.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## workspaces_create_invite

> crate::models::WorkspaceInvite workspaces_create_invite(workspace_invite_create_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**workspace_invite_create_request** | [**WorkspaceInviteCreateRequest**](WorkspaceInviteCreateRequest.md) |  | [required] |

### Return type

[**crate::models::WorkspaceInvite**](WorkspaceInvite.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## workspaces_list

> crate::models::PaginatedWorkspaceList workspaces_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedWorkspaceList**](PaginatedWorkspaceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## workspaces_partial_update

> crate::models::PaginatedWorkspaceList workspaces_partial_update(id, page, patched_workspace_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this organization. | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |
**patched_workspace_request** | Option<[**PatchedWorkspaceRequest**](PatchedWorkspaceRequest.md)> |  |  |

### Return type

[**crate::models::PaginatedWorkspaceList**](PaginatedWorkspaceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## workspaces_remind_invite

> crate::models::WorkspaceInvite workspaces_remind_invite(workspace_invite_remind_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**workspace_invite_remind_request** | [**WorkspaceInviteRemindRequest**](WorkspaceInviteRemindRequest.md) |  | [required] |

### Return type

[**crate::models::WorkspaceInvite**](WorkspaceInvite.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## workspaces_retrieve

> crate::models::Workspace workspaces_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this organization. | [required] |

### Return type

[**crate::models::Workspace**](Workspace.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## workspaces_update

> crate::models::Workspace workspaces_update(id, workspace_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this organization. | [required] |
**workspace_request** | [**WorkspaceRequest**](WorkspaceRequest.md) |  | [required] |

### Return type

[**crate::models::Workspace**](Workspace.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## workspaces_verify_invite

> crate::models::WorkspaceInvite workspaces_verify_invite(workspace_invite_verify_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**workspace_invite_verify_request** | [**WorkspaceInviteVerifyRequest**](WorkspaceInviteVerifyRequest.md) |  | [required] |

### Return type

[**crate::models::WorkspaceInvite**](WorkspaceInvite.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

