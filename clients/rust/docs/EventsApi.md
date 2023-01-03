# \EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**octoprint_events_create**](EventsApi.md#octoprint_events_create) | **POST** /api/octoprint/events/ | 
[**octoprint_events_list**](EventsApi.md#octoprint_events_list) | **GET** /api/octoprint/events/ | 
[**octoprint_events_retrieve**](EventsApi.md#octoprint_events_retrieve) | **GET** /api/octoprint/events/{id}/ | 
[**pis_all_events_list**](EventsApi.md#pis_all_events_list) | **GET** /api/pis/events | 
[**pis_commands_create**](EventsApi.md#pis_commands_create) | **POST** /api/pis/commands | 
[**pis_commands_list**](EventsApi.md#pis_commands_list) | **GET** /api/pis/commands | 
[**pis_events_commands_list**](EventsApi.md#pis_events_commands_list) | **GET** /api/pis/{pi_id}/events/commands/ | 
[**pis_events_create**](EventsApi.md#pis_events_create) | **POST** /api/pis/events | 
[**pis_events_list**](EventsApi.md#pis_events_list) | **GET** /api/pis/{pi_id}/events/ | 
[**pis_events_retrieve**](EventsApi.md#pis_events_retrieve) | **GET** /api/pis/events/{id} | 
[**pis_events_status_list**](EventsApi.md#pis_events_status_list) | **GET** /api/pis/{pi_id}/events/status/ | 
[**pis_status_create**](EventsApi.md#pis_status_create) | **POST** /api/pis/status | 
[**pis_status_list**](EventsApi.md#pis_status_list) | **GET** /api/pis/status | 



## octoprint_events_create

> crate::models::PolymorphicOctoPrintEvent octoprint_events_create(polymorphic_octo_print_event_request)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**polymorphic_octo_print_event_request** | Option<[**PolymorphicOctoPrintEventRequest**](PolymorphicOctoPrintEventRequest.md)> |  |  |

### Return type

[**crate::models::PolymorphicOctoPrintEvent**](PolymorphicOctoPrintEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_events_list

> crate::models::PaginatedPolymorphicOctoPrintEventList octoprint_events_list(page)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicOctoPrintEventList**](PaginatedPolymorphicOctoPrintEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_events_retrieve

> crate::models::PolymorphicOctoPrintEvent octoprint_events_retrieve(id)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this base octo print event. | [required] |

### Return type

[**crate::models::PolymorphicOctoPrintEvent**](PolymorphicOctoPrintEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_all_events_list

> crate::models::PaginatedPolymorphicPiEventList pis_all_events_list(page)


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


## pis_commands_create

> crate::models::PolymorphicPiCommand pis_commands_create(polymorphic_pi_command_request)


Interact with all Raspberry Pi remote commands

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**polymorphic_pi_command_request** | Option<[**PolymorphicPiCommandRequest**](PolymorphicPiCommandRequest.md)> |  |  |

### Return type

[**crate::models::PolymorphicPiCommand**](PolymorphicPiCommand.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_commands_list

> crate::models::PaginatedPolymorphicPiCommandList pis_commands_list(page)


Interact with all Raspberry Pi remote commands

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicPiCommandList**](PaginatedPolymorphicPiCommandList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_events_commands_list

> crate::models::PaginatedPolymorphicPiCommandList pis_events_commands_list(pi_id, page)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicPiCommandList**](PaginatedPolymorphicPiCommandList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


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

> crate::models::PaginatedPolymorphicPiEventList pis_events_list(pi_id, page)


Interact with all events inheriting from BasePiEvent, filtered by a single Pi

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
**id** | **i32** |  | [required] |

### Return type

[**crate::models::PolymorphicPiEvent**](PolymorphicPiEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_events_status_list

> crate::models::PaginatedPolymorphicPiStatusList pis_events_status_list(pi_id, page)


Interact with all status events for Raspberry Pi, filtered by a single Pi

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicPiStatusList**](PaginatedPolymorphicPiStatusList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_status_create

> crate::models::PolymorphicPiStatus pis_status_create(polymorphic_pi_status_request)


Interact with all status events for Raspberry Pi

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**polymorphic_pi_status_request** | Option<[**PolymorphicPiStatusRequest**](PolymorphicPiStatusRequest.md)> |  |  |

### Return type

[**crate::models::PolymorphicPiStatus**](PolymorphicPiStatus.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_status_list

> crate::models::PaginatedPolymorphicPiStatusList pis_status_list(page)


Interact with all status events for Raspberry Pi

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicPiStatusList**](PaginatedPolymorphicPiStatusList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

