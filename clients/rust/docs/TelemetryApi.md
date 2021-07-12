# \TelemetryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_octoprint_events_create**](TelemetryApi.md#api_octoprint_events_create) | **post** /api/octoprint-events/ | 
[**api_octoprint_events_list**](TelemetryApi.md#api_octoprint_events_list) | **get** /api/octoprint-events/ | 
[**api_octoprint_events_retrieve**](TelemetryApi.md#api_octoprint_events_retrieve) | **get** /api/octoprint-events/{id}/ | 
[**api_print_job_events_list**](TelemetryApi.md#api_print_job_events_list) | **get** /api/print-job-events/ | 
[**api_print_job_events_retrieve**](TelemetryApi.md#api_print_job_events_retrieve) | **get** /api/print-job-events/{id}/ | 
[**api_print_nanny_plugin_events_list**](TelemetryApi.md#api_print_nanny_plugin_events_list) | **get** /api/print-nanny-plugin-events/ | 
[**api_print_nanny_plugin_events_retrieve**](TelemetryApi.md#api_print_nanny_plugin_events_retrieve) | **get** /api/print-nanny-plugin-events/{id}/ | 
[**api_remote_command_events_list**](TelemetryApi.md#api_remote_command_events_list) | **get** /api/remote-command-events/ | 
[**api_remote_command_events_retrieve**](TelemetryApi.md#api_remote_command_events_retrieve) | **get** /api/remote-command-events/{id}/ | 
[**api_telemetry_events_list**](TelemetryApi.md#api_telemetry_events_list) | **get** /api/telemetry-events/ | 
[**api_telemetry_events_retrieve**](TelemetryApi.md#api_telemetry_events_retrieve) | **get** /api/telemetry-events/{id}/ | 



## api_octoprint_events_create

> crate::models::OctoPrintEvent api_octoprint_events_create(octo_print_event_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_print_event_request** | [**OctoPrintEventRequest**](OctoPrintEventRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintEvent**](OctoPrintEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_octoprint_events_list

> crate::models::PaginatedOctoPrintEventList api_octoprint_events_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedOctoPrintEventList**](PaginatedOctoPrintEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_octoprint_events_retrieve

> crate::models::OctoPrintEvent api_octoprint_events_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print event. | [required] |

### Return type

[**crate::models::OctoPrintEvent**](OctoPrintEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_print_job_events_list

> crate::models::PaginatedPrintJobEventList api_print_job_events_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPrintJobEventList**](PaginatedPrintJobEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_print_job_events_retrieve

> crate::models::PrintJobEvent api_print_job_events_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this print job event. | [required] |

### Return type

[**crate::models::PrintJobEvent**](PrintJobEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_print_nanny_plugin_events_list

> crate::models::PaginatedPrintNannyPluginEventList api_print_nanny_plugin_events_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPrintNannyPluginEventList**](PaginatedPrintNannyPluginEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_print_nanny_plugin_events_retrieve

> crate::models::PrintNannyPluginEvent api_print_nanny_plugin_events_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this print nanny plugin event. | [required] |

### Return type

[**crate::models::PrintNannyPluginEvent**](PrintNannyPluginEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_remote_command_events_list

> crate::models::PaginatedRemoteCommandEventList api_remote_command_events_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedRemoteCommandEventList**](PaginatedRemoteCommandEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_remote_command_events_retrieve

> crate::models::RemoteCommandEvent api_remote_command_events_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this remote command event. | [required] |

### Return type

[**crate::models::RemoteCommandEvent**](RemoteCommandEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_telemetry_events_list

> crate::models::PaginatedTelemetryEventPolymorphicList api_telemetry_events_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedTelemetryEventPolymorphicList**](PaginatedTelemetryEventPolymorphicList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_telemetry_events_retrieve

> crate::models::TelemetryEventPolymorphic api_telemetry_events_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this telemetry event. | [required] |

### Return type

[**crate::models::TelemetryEventPolymorphic**](TelemetryEventPolymorphic.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

