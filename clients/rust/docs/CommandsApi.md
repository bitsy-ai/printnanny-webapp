# \CommandsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commands_create**](CommandsApi.md#commands_create) | **POST** /api/commands/ | 
[**commands_list**](CommandsApi.md#commands_list) | **GET** /api/commands/ | 
[**commands_retrieve**](CommandsApi.md#commands_retrieve) | **GET** /api/commands/{id}/ | 



## commands_create

> crate::models::PolymorphicCommand commands_create(polymorphic_command_create_request)


Generic events viewset

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**polymorphic_command_create_request** | Option<[**PolymorphicCommandCreateRequest**](PolymorphicCommandCreateRequest.md)> |  |  |

### Return type

[**crate::models::PolymorphicCommand**](PolymorphicCommand.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## commands_list

> crate::models::PaginatedPolymorphicCommandList commands_list(page)


Generic events viewset

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicCommandList**](PaginatedPolymorphicCommandList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## commands_retrieve

> crate::models::PolymorphicCommand commands_retrieve(id)


Generic events viewset

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this event. | [required] |

### Return type

[**crate::models::PolymorphicCommand**](PolymorphicCommand.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

