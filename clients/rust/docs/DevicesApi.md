# \DevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_info_update_or_create**](DevicesApi.md#device_info_update_or_create) | **POST** /api/devices/{device_id}/info/update-or-create/ | 
[**devices_cameras_create**](DevicesApi.md#devices_cameras_create) | **POST** /api/devices/{device_id}/cameras/ | 
[**devices_cameras_list**](DevicesApi.md#devices_cameras_list) | **GET** /api/devices/{device_id}/cameras/ | 
[**devices_cameras_partial_update**](DevicesApi.md#devices_cameras_partial_update) | **PATCH** /api/devices/{device_id}/cameras/{id}/ | 
[**devices_cameras_retrieve**](DevicesApi.md#devices_cameras_retrieve) | **GET** /api/devices/{device_id}/cameras/{id}/ | 
[**devices_cameras_update**](DevicesApi.md#devices_cameras_update) | **PUT** /api/devices/{device_id}/cameras/{id}/ | 
[**devices_cloud_iot_devices_create**](DevicesApi.md#devices_cloud_iot_devices_create) | **POST** /api/devices/{device_id}/cloud-iot-devices/ | 
[**devices_cloud_iot_devices_list**](DevicesApi.md#devices_cloud_iot_devices_list) | **GET** /api/devices/{device_id}/cloud-iot-devices/ | 
[**devices_cloud_iot_devices_partial_update**](DevicesApi.md#devices_cloud_iot_devices_partial_update) | **PATCH** /api/devices/{device_id}/cloud-iot-devices/{id}/ | 
[**devices_cloud_iot_devices_retrieve**](DevicesApi.md#devices_cloud_iot_devices_retrieve) | **GET** /api/devices/{device_id}/cloud-iot-devices/{id}/ | 
[**devices_cloud_iot_devices_update**](DevicesApi.md#devices_cloud_iot_devices_update) | **PUT** /api/devices/{device_id}/cloud-iot-devices/{id}/ | 
[**devices_config_list**](DevicesApi.md#devices_config_list) | **GET** /api/devices/{device_id}/config/ | 
[**devices_config_retrieve**](DevicesApi.md#devices_config_retrieve) | **GET** /api/devices/{device_id}/config/{id}/ | 
[**devices_create**](DevicesApi.md#devices_create) | **POST** /api/devices/ | 
[**devices_info_create**](DevicesApi.md#devices_info_create) | **POST** /api/devices/{device_id}/info/ | 
[**devices_info_list**](DevicesApi.md#devices_info_list) | **GET** /api/devices/{device_id}/info/ | 
[**devices_info_partial_update**](DevicesApi.md#devices_info_partial_update) | **PATCH** /api/devices/{device_id}/info/{id}/ | 
[**devices_info_retrieve**](DevicesApi.md#devices_info_retrieve) | **GET** /api/devices/{device_id}/info/{id}/ | 
[**devices_info_update**](DevicesApi.md#devices_info_update) | **PUT** /api/devices/{device_id}/info/{id}/ | 
[**devices_license_retrieve**](DevicesApi.md#devices_license_retrieve) | **GET** /api/devices/{id}/license/ | 
[**devices_list**](DevicesApi.md#devices_list) | **GET** /api/devices/ | 
[**devices_partial_update**](DevicesApi.md#devices_partial_update) | **PATCH** /api/devices/{id}/ | 
[**devices_printer_controllers_create**](DevicesApi.md#devices_printer_controllers_create) | **POST** /api/devices/{device_id}/printer-controllers/ | 
[**devices_printer_controllers_list**](DevicesApi.md#devices_printer_controllers_list) | **GET** /api/devices/{device_id}/printer-controllers/ | 
[**devices_printer_controllers_partial_update**](DevicesApi.md#devices_printer_controllers_partial_update) | **PATCH** /api/devices/{device_id}/printer-controllers/{id}/ | 
[**devices_printer_controllers_retrieve**](DevicesApi.md#devices_printer_controllers_retrieve) | **GET** /api/devices/{device_id}/printer-controllers/{id}/ | 
[**devices_printer_controllers_update**](DevicesApi.md#devices_printer_controllers_update) | **PUT** /api/devices/{device_id}/printer-controllers/{id}/ | 
[**devices_retrieve**](DevicesApi.md#devices_retrieve) | **GET** /api/devices/{id}/ | 
[**devices_retrieve_hostname**](DevicesApi.md#devices_retrieve_hostname) | **GET** /api/devices/{hostname} | 
[**devices_system_tasks_create**](DevicesApi.md#devices_system_tasks_create) | **POST** /api/devices/{device_id}/system-tasks/ | 
[**devices_system_tasks_list**](DevicesApi.md#devices_system_tasks_list) | **GET** /api/devices/{device_id}/system-tasks/ | 
[**devices_system_tasks_retrieve**](DevicesApi.md#devices_system_tasks_retrieve) | **GET** /api/devices/{device_id}/system-tasks/{id}/ | 
[**devices_update**](DevicesApi.md#devices_update) | **PUT** /api/devices/{id}/ | 



## device_info_update_or_create

> crate::models::DeviceInfo device_info_update_or_create(device_id, device_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**device_info_request** | [**DeviceInfoRequest**](DeviceInfoRequest.md) |  | [required] |

### Return type

[**crate::models::DeviceInfo**](DeviceInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cameras_create

> crate::models::Camera devices_cameras_create(device_id, camera_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**camera_request** | [**CameraRequest**](CameraRequest.md) |  | [required] |

### Return type

[**crate::models::Camera**](Camera.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cameras_list

> crate::models::PaginatedCameraList devices_cameras_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedCameraList**](PaginatedCameraList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cameras_partial_update

> crate::models::Camera devices_cameras_partial_update(device_id, id, patched_camera_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this camera. | [required] |
**patched_camera_request** | Option<[**PatchedCameraRequest**](PatchedCameraRequest.md)> |  |  |

### Return type

[**crate::models::Camera**](Camera.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cameras_retrieve

> crate::models::Camera devices_cameras_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this camera. | [required] |

### Return type

[**crate::models::Camera**](Camera.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cameras_update

> crate::models::Camera devices_cameras_update(device_id, id, camera_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this camera. | [required] |
**camera_request** | [**CameraRequest**](CameraRequest.md) |  | [required] |

### Return type

[**crate::models::Camera**](Camera.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloud_iot_devices_create

> crate::models::CloudiotDevice devices_cloud_iot_devices_create(device_id, cloudiot_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**cloudiot_device_request** | [**CloudiotDeviceRequest**](CloudiotDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::CloudiotDevice**](CloudiotDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloud_iot_devices_list

> crate::models::PaginatedCloudiotDeviceList devices_cloud_iot_devices_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedCloudiotDeviceList**](PaginatedCloudiotDeviceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloud_iot_devices_partial_update

> crate::models::CloudiotDevice devices_cloud_iot_devices_partial_update(device_id, id, patched_cloudiot_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **String** |  | [required] |
**patched_cloudiot_device_request** | Option<[**PatchedCloudiotDeviceRequest**](PatchedCloudiotDeviceRequest.md)> |  |  |

### Return type

[**crate::models::CloudiotDevice**](CloudiotDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloud_iot_devices_retrieve

> crate::models::CloudiotDevice devices_cloud_iot_devices_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **String** |  | [required] |

### Return type

[**crate::models::CloudiotDevice**](CloudiotDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloud_iot_devices_update

> crate::models::CloudiotDevice devices_cloud_iot_devices_update(device_id, id, cloudiot_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **String** |  | [required] |
**cloudiot_device_request** | [**CloudiotDeviceRequest**](CloudiotDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::CloudiotDevice**](CloudiotDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_config_list

> crate::models::PaginatedDeviceConfigList devices_config_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedDeviceConfigList**](PaginatedDeviceConfigList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_config_retrieve

> crate::models::DeviceConfig devices_config_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this device config. | [required] |

### Return type

[**crate::models::DeviceConfig**](DeviceConfig.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_create

> crate::models::Device devices_create(device_request)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_request** | Option<[**DeviceRequest**](DeviceRequest.md)> |  |  |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_info_create

> crate::models::DeviceInfo devices_info_create(device_id, device_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**device_info_request** | [**DeviceInfoRequest**](DeviceInfoRequest.md) |  | [required] |

### Return type

[**crate::models::DeviceInfo**](DeviceInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_info_list

> crate::models::PaginatedDeviceInfoList devices_info_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedDeviceInfoList**](PaginatedDeviceInfoList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_info_partial_update

> crate::models::DeviceInfo devices_info_partial_update(device_id, id, patched_device_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this device info. | [required] |
**patched_device_info_request** | Option<[**PatchedDeviceInfoRequest**](PatchedDeviceInfoRequest.md)> |  |  |

### Return type

[**crate::models::DeviceInfo**](DeviceInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_info_retrieve

> crate::models::DeviceInfo devices_info_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this device info. | [required] |

### Return type

[**crate::models::DeviceInfo**](DeviceInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_info_update

> crate::models::DeviceInfo devices_info_update(device_id, id, device_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this device info. | [required] |
**device_info_request** | [**DeviceInfoRequest**](DeviceInfoRequest.md) |  | [required] |

### Return type

[**crate::models::DeviceInfo**](DeviceInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_license_retrieve

> crate::models::Device devices_license_retrieve(id)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

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


## devices_list

> crate::models::PaginatedDeviceList devices_list(page)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

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


## devices_partial_update

> crate::models::Device devices_partial_update(id, patched_device_request)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

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


## devices_printer_controllers_create

> crate::models::PrinterController devices_printer_controllers_create(device_id, device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**device_request** | Option<[**DeviceRequest**](DeviceRequest.md)> |  |  |

### Return type

[**crate::models::PrinterController**](PrinterController.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_printer_controllers_list

> crate::models::PaginatedPrinterControllerList devices_printer_controllers_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPrinterControllerList**](PaginatedPrinterControllerList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_printer_controllers_partial_update

> crate::models::PrinterController devices_printer_controllers_partial_update(device_id, id, patched_printer_controller_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this printer controller. | [required] |
**patched_printer_controller_request** | Option<[**PatchedPrinterControllerRequest**](PatchedPrinterControllerRequest.md)> |  |  |

### Return type

[**crate::models::PrinterController**](PrinterController.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_printer_controllers_retrieve

> crate::models::PrinterController devices_printer_controllers_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this printer controller. | [required] |

### Return type

[**crate::models::PrinterController**](PrinterController.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_printer_controllers_update

> crate::models::PrinterController devices_printer_controllers_update(device_id, id, device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this printer controller. | [required] |
**device_request** | Option<[**DeviceRequest**](DeviceRequest.md)> |  |  |

### Return type

[**crate::models::PrinterController**](PrinterController.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_retrieve

> crate::models::Device devices_retrieve(id)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

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


## devices_retrieve_hostname

> crate::models::Device devices_retrieve_hostname(hostname)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hostname** | **String** |  | [required] |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_system_tasks_create

> crate::models::Device devices_system_tasks_create(device_id, device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**device_request** | Option<[**DeviceRequest**](DeviceRequest.md)> |  |  |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_system_tasks_list

> crate::models::PaginatedSystemTaskList devices_system_tasks_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedSystemTaskList**](PaginatedSystemTaskList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_system_tasks_retrieve

> crate::models::SystemTask devices_system_tasks_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this system task. | [required] |

### Return type

[**crate::models::SystemTask**](SystemTask.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_update

> crate::models::Device devices_update(id, device_request)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this device. | [required] |
**device_request** | Option<[**DeviceRequest**](DeviceRequest.md)> |  |  |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

