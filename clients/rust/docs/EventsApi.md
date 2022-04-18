# \EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commands_create**](EventsApi.md#commands_create) | **POST** /api/commands/ | 
[**commands_list**](EventsApi.md#commands_list) | **GET** /api/commands/ | 
[**commands_retrieve**](EventsApi.md#commands_retrieve) | **GET** /api/commands/{id}/ | 
[**events_create**](EventsApi.md#events_create) | **POST** /api/events/ | 
[**events_list**](EventsApi.md#events_list) | **GET** /api/events/ | 
[**events_retrieve**](EventsApi.md#events_retrieve) | **GET** /api/events/{id}/ | 



## commands_create

> crate::models::PolymorphicCommand commands_create(polymorphic_command_request_request)


Generic events viewset

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**polymorphic_command_request_request** | Option<[**PolymorphicCommandRequestRequest**](PolymorphicCommandRequestRequest.md)> |  |  |

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


## events_create

> crate::models::PolymorphicEvent events_create(polymorphic_event_request_request)


Generic events viewset

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**polymorphic_event_request_request** | Option<[**PolymorphicEventRequestRequest**](PolymorphicEventRequestRequest.md)> |  |  |

### Return type

[**crate::models::PolymorphicEvent**](PolymorphicEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## events_list

> crate::models::PaginatedPolymorphicEventList events_list(page)


Generic events viewset

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicEventList**](PaginatedPolymorphicEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## events_retrieve

> crate::models::PolymorphicEvent events_retrieve(id)


Generic events viewset

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this event. | [required] |

### Return type

[**crate::models::PolymorphicEvent**](PolymorphicEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

