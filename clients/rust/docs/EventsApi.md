# \EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_events_create**](EventsApi.md#devices_events_create) | **POST** /api/devices/{device_id}/events/ | 
[**devices_events_list**](EventsApi.md#devices_events_list) | **GET** /api/devices/{device_id}/events/ | 
[**devices_events_retrieve**](EventsApi.md#devices_events_retrieve) | **GET** /api/devices/{device_id}/events/{id}/ | 
[**devices_test_events_create**](EventsApi.md#devices_test_events_create) | **POST** /api/devices/{device_id}/test-events/ | 
[**devices_test_events_list**](EventsApi.md#devices_test_events_list) | **GET** /api/devices/{device_id}/test-events/ | 
[**devices_test_events_retrieve**](EventsApi.md#devices_test_events_retrieve) | **GET** /api/devices/{device_id}/test-events/{id}/ | 



## devices_events_create

> crate::models::PolymorphicEvent devices_events_create(device_id, polymorphic_event_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **String** |  | [required] |
**polymorphic_event_request** | Option<[**PolymorphicEventRequest**](PolymorphicEventRequest.md)> |  |  |

### Return type

[**crate::models::PolymorphicEvent**](PolymorphicEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_events_list

> crate::models::PaginatedPolymorphicEventList devices_events_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **String** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicEventList**](PaginatedPolymorphicEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_events_retrieve

> crate::models::PolymorphicEvent devices_events_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **String** |  | [required] |
**id** | **i32** | A unique integer value identifying this event. | [required] |

### Return type

[**crate::models::PolymorphicEvent**](PolymorphicEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_test_events_create

> crate::models::TestEvent devices_test_events_create(device_id, test_event_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**test_event_request** | [**TestEventRequest**](TestEventRequest.md) |  | [required] |

### Return type

[**crate::models::TestEvent**](TestEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_test_events_list

> crate::models::PaginatedTestEventList devices_test_events_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedTestEventList**](PaginatedTestEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_test_events_retrieve

> crate::models::TestEvent devices_test_events_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this test event. | [required] |

### Return type

[**crate::models::TestEvent**](TestEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

