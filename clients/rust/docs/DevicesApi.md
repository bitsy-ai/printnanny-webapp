# \DevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_devices_create**](DevicesApi.md#api_devices_create) | **post** /api/devices/ | 
[**api_devices_list**](DevicesApi.md#api_devices_list) | **get** /api/devices/ | 
[**api_devices_retrieve**](DevicesApi.md#api_devices_retrieve) | **get** /api/devices/{id}/ | 
[**devices_update_or_create**](DevicesApi.md#devices_update_or_create) | **post** /api/devices/update-or-create/ | 
[**octoprint_devices_partial_update**](DevicesApi.md#octoprint_devices_partial_update) | **patch** /api/devices/{id}/ | 
[**octoprint_devices_update**](DevicesApi.md#octoprint_devices_update) | **put** /api/devices/{id}/ | 



## api_devices_create

> crate::models::Device api_devices_create(device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_request** | [**DeviceRequest**](DeviceRequest.md) |  | [required] |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_devices_list

> crate::models::PaginatedDeviceList api_devices_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedDeviceList**](PaginatedDeviceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## api_devices_retrieve

> crate::models::Device api_devices_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this device. | [required] |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_update_or_create

> crate::models::DeviceIdentity devices_update_or_create(device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_request** | [**DeviceRequest**](DeviceRequest.md) |  | [required] |

### Return type

[**crate::models::DeviceIdentity**](DeviceIdentity.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_devices_partial_update

> crate::models::Device octoprint_devices_partial_update(id, patched_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this device. | [required] |
**patched_device_request** | Option<[**PatchedDeviceRequest**](PatchedDeviceRequest.md)> |  |  |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_devices_update

> crate::models::Device octoprint_devices_update(id, device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this device. | [required] |
**device_request** | [**DeviceRequest**](DeviceRequest.md) |  | [required] |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

