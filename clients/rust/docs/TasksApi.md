# \TasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_tasks_create**](TasksApi.md#devices_tasks_create) | **POST** /api/devices/{device_id}/tasks/ | 
[**devices_tasks_list**](TasksApi.md#devices_tasks_list) | **GET** /api/devices/{device_id}/tasks/ | 
[**devices_tasks_retrieve**](TasksApi.md#devices_tasks_retrieve) | **GET** /api/devices/{device_id}/tasks/{id}/ | 
[**devices_tasks_status_create**](TasksApi.md#devices_tasks_status_create) | **POST** /api/devices/{device_id}/tasks/{task_id}/status/ | 
[**devices_tasks_status_list**](TasksApi.md#devices_tasks_status_list) | **GET** /api/devices/{device_id}/tasks/{task_id}/status/ | 
[**devices_tasks_status_retrieve**](TasksApi.md#devices_tasks_status_retrieve) | **GET** /api/devices/{device_id}/tasks/{task_id}/status/{id}/ | 



## devices_tasks_create

> crate::models::PolymorphicTask devices_tasks_create(device_id, polymorphic_task_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**polymorphic_task_request** | Option<[**PolymorphicTaskRequest**](PolymorphicTaskRequest.md)> |  |  |

### Return type

[**crate::models::PolymorphicTask**](PolymorphicTask.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_tasks_list

> crate::models::PaginatedPolymorphicTaskList devices_tasks_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicTaskList**](PaginatedPolymorphicTaskList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_tasks_retrieve

> crate::models::PolymorphicTask devices_tasks_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this task. | [required] |

### Return type

[**crate::models::PolymorphicTask**](PolymorphicTask.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_tasks_status_create

> crate::models::TaskStatus devices_tasks_status_create(device_id, task_id, task_status_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **String** |  | [required] |
**task_id** | **i32** |  | [required] |
**task_status_request** | [**TaskStatusRequest**](TaskStatusRequest.md) |  | [required] |

### Return type

[**crate::models::TaskStatus**](TaskStatus.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_tasks_status_list

> crate::models::PaginatedTaskStatusList devices_tasks_status_list(device_id, task_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **String** |  | [required] |
**task_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedTaskStatusList**](PaginatedTaskStatusList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_tasks_status_retrieve

> crate::models::TaskStatus devices_tasks_status_retrieve(device_id, id, task_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **String** |  | [required] |
**id** | **i32** | A unique integer value identifying this task status. | [required] |
**task_id** | **i32** |  | [required] |

### Return type

[**crate::models::TaskStatus**](TaskStatus.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

