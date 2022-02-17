# \UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_janus_auth_create**](UsersApi.md#users_janus_auth_create) | **POST** /api/users/{user_id}/janus-auth/ | 
[**users_janus_auth_list**](UsersApi.md#users_janus_auth_list) | **GET** /api/users/{user_id}/janus-auth/ | 
[**users_janus_auth_retrieve**](UsersApi.md#users_janus_auth_retrieve) | **GET** /api/users/{user_id}/janus-auth/{id}/ | 
[**users_janus_auth_update_or_create**](UsersApi.md#users_janus_auth_update_or_create) | **POST** /api/users/{user_id}/janus-auth/update-or-create/ | 
[**users_me_retrieve**](UsersApi.md#users_me_retrieve) | **GET** /api/users/me/ | 
[**users_partial_update**](UsersApi.md#users_partial_update) | **PATCH** /api/users/{id}/ | 
[**users_retrieve**](UsersApi.md#users_retrieve) | **GET** /api/users/{id}/ | 
[**users_update**](UsersApi.md#users_update) | **PUT** /api/users/{id}/ | 



## users_janus_auth_create

> crate::models::JanusAuth users_janus_auth_create(user_id, janus_auth_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**user_id** | **i32** |  | [required] |
**janus_auth_request** | [**JanusAuthRequest**](JanusAuthRequest.md) |  | [required] |

### Return type

[**crate::models::JanusAuth**](JanusAuth.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_janus_auth_list

> crate::models::PaginatedJanusAuthList users_janus_auth_list(user_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**user_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedJanusAuthList**](PaginatedJanusAuthList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_janus_auth_retrieve

> crate::models::JanusAuth users_janus_auth_retrieve(id, user_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this janus auth. | [required] |
**user_id** | **i32** |  | [required] |

### Return type

[**crate::models::JanusAuth**](JanusAuth.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_janus_auth_update_or_create

> crate::models::JanusAuth users_janus_auth_update_or_create(user_id, janus_auth_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**user_id** | **i32** |  | [required] |
**janus_auth_request** | [**JanusAuthRequest**](JanusAuthRequest.md) |  | [required] |

### Return type

[**crate::models::JanusAuth**](JanusAuth.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_me_retrieve

> crate::models::User users_me_retrieve()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::User**](User.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_partial_update

> crate::models::User users_partial_update(id, patched_user_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this user. | [required] |
**patched_user_request** | Option<[**PatchedUserRequest**](PatchedUserRequest.md)> |  |  |

### Return type

[**crate::models::User**](User.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_retrieve

> crate::models::User users_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this user. | [required] |

### Return type

[**crate::models::User**](User.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_update

> crate::models::User users_update(id, user_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this user. | [required] |
**user_request** | [**UserRequest**](UserRequest.md) |  | [required] |

### Return type

[**crate::models::User**](User.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

