# \EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pis_events_create**](EventsApi.md#pis_events_create) | **POST** /api/pis/events/ | 
[**pis_events_list**](EventsApi.md#pis_events_list) | **GET** /api/pis/events/ | 
[**pis_events_list2**](EventsApi.md#pis_events_list2) | **GET** /api/pis/{pi_id}/events/ | 
[**pis_events_retrieve**](EventsApi.md#pis_events_retrieve) | **GET** /api/pis/events/{id}/ | 



## pis_events_create

> crate::models::PolymorphicPiEvent pis_events_create(polymorphic_pi_event_request)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**polymorphic_pi_event_request** | Option<[**PolymorphicPiEventRequest**](PolymorphicPiEventRequest.md)> |  |  |

### Return type

[**crate::models::PolymorphicPiEvent**](PolymorphicPiEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_events_list

> crate::models::PaginatedPolymorphicPiEventList pis_events_list(page)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicPiEventList**](PaginatedPolymorphicPiEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_events_list2

> crate::models::PaginatedPolymorphicPiEventList pis_events_list2(pi_id, page)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicPiEventList**](PaginatedPolymorphicPiEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_events_retrieve

> crate::models::PolymorphicPiEvent pis_events_retrieve(id)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this base pi event. | [required] |

### Return type

[**crate::models::PolymorphicPiEvent**](PolymorphicPiEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

