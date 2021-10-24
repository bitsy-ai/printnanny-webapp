# \DevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_ansible_facts_create**](DevicesApi.md#devices_ansible_facts_create) | **POST** /api/devices/{device_id}/ansible-facts/ | 
[**devices_ansible_facts_list**](DevicesApi.md#devices_ansible_facts_list) | **GET** /api/devices/{device_id}/ansible-facts/ | 
[**devices_ansible_facts_partial_update**](DevicesApi.md#devices_ansible_facts_partial_update) | **PATCH** /api/devices/{device_id}/ansible-facts/{id}/ | 
[**devices_ansible_facts_retrieve**](DevicesApi.md#devices_ansible_facts_retrieve) | **GET** /api/devices/{device_id}/ansible-facts/{id}/ | 
[**devices_ansible_facts_update**](DevicesApi.md#devices_ansible_facts_update) | **PUT** /api/devices/{device_id}/ansible-facts/{id}/ | 
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
[**devices_create**](DevicesApi.md#devices_create) | **POST** /api/devices/ | 
[**devices_keypairs_create**](DevicesApi.md#devices_keypairs_create) | **POST** /api/devices/{device_id}/keypairs/ | 
[**devices_keypairs_list**](DevicesApi.md#devices_keypairs_list) | **GET** /api/devices/{device_id}/keypairs/ | 
[**devices_keypairs_retrieve**](DevicesApi.md#devices_keypairs_retrieve) | **GET** /api/devices/{device_id}/keypairs/{id}/ | 
[**devices_list**](DevicesApi.md#devices_list) | **GET** /api/devices/ | 
[**devices_partial_update**](DevicesApi.md#devices_partial_update) | **PATCH** /api/devices/{id}/ | 
[**devices_printer_controllers_create**](DevicesApi.md#devices_printer_controllers_create) | **POST** /api/devices/{device_id}/printer-controllers/ | 
[**devices_printer_controllers_list**](DevicesApi.md#devices_printer_controllers_list) | **GET** /api/devices/{device_id}/printer-controllers/ | 
[**devices_printer_controllers_partial_update**](DevicesApi.md#devices_printer_controllers_partial_update) | **PATCH** /api/devices/{device_id}/printer-controllers/{id}/ | 
[**devices_printer_controllers_retrieve**](DevicesApi.md#devices_printer_controllers_retrieve) | **GET** /api/devices/{device_id}/printer-controllers/{id}/ | 
[**devices_printer_controllers_update**](DevicesApi.md#devices_printer_controllers_update) | **PUT** /api/devices/{device_id}/printer-controllers/{id}/ | 
[**devices_retrieve**](DevicesApi.md#devices_retrieve) | **GET** /api/devices/{id}/ | 
[**devices_update**](DevicesApi.md#devices_update) | **PUT** /api/devices/{id}/ | 



## devices_ansible_facts_create

> crate::models::AnsibleFacts devices_ansible_facts_create(device_id, ansible_facts_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**ansible_facts_request** | [**AnsibleFactsRequest**](AnsibleFactsRequest.md) |  | [required] |

### Return type

[**crate::models::AnsibleFacts**](AnsibleFacts.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_ansible_facts_list

> crate::models::PaginatedAnsibleFactsList devices_ansible_facts_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedAnsibleFactsList**](PaginatedAnsibleFactsList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_ansible_facts_partial_update

> crate::models::AnsibleFacts devices_ansible_facts_partial_update(device_id, id, patched_ansible_facts_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this ansible facts. | [required] |
**patched_ansible_facts_request** | Option<[**PatchedAnsibleFactsRequest**](PatchedAnsibleFactsRequest.md)> |  |  |

### Return type

[**crate::models::AnsibleFacts**](AnsibleFacts.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_ansible_facts_retrieve

> crate::models::AnsibleFacts devices_ansible_facts_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this ansible facts. | [required] |

### Return type

[**crate::models::AnsibleFacts**](AnsibleFacts.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_ansible_facts_update

> crate::models::AnsibleFacts devices_ansible_facts_update(device_id, id, ansible_facts_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this ansible facts. | [required] |
**ansible_facts_request** | [**AnsibleFactsRequest**](AnsibleFactsRequest.md) |  | [required] |

### Return type

[**crate::models::AnsibleFacts**](AnsibleFacts.md)

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

> crate::models::CloudIoTDevice devices_cloud_iot_devices_create(device_id, cloud_io_t_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**cloud_io_t_device_request** | [**CloudIoTDeviceRequest**](CloudIoTDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::CloudIoTDevice**](CloudIoTDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloud_iot_devices_list

> crate::models::PaginatedCloudIoTDeviceList devices_cloud_iot_devices_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedCloudIoTDeviceList**](PaginatedCloudIoTDeviceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloud_iot_devices_partial_update

> crate::models::CloudIoTDevice devices_cloud_iot_devices_partial_update(device_id, id, patched_cloud_io_t_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **String** |  | [required] |
**patched_cloud_io_t_device_request** | Option<[**PatchedCloudIoTDeviceRequest**](PatchedCloudIoTDeviceRequest.md)> |  |  |

### Return type

[**crate::models::CloudIoTDevice**](CloudIoTDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloud_iot_devices_retrieve

> crate::models::CloudIoTDevice devices_cloud_iot_devices_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **String** |  | [required] |

### Return type

[**crate::models::CloudIoTDevice**](CloudIoTDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloud_iot_devices_update

> crate::models::CloudIoTDevice devices_cloud_iot_devices_update(device_id, id, cloud_io_t_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **String** |  | [required] |
**cloud_io_t_device_request** | [**CloudIoTDeviceRequest**](CloudIoTDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::CloudIoTDevice**](CloudIoTDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_create

> crate::models::Device devices_create(device_request)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

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


## devices_keypairs_create

> crate::models::DeviceKeyPair devices_keypairs_create(device_id)


Public key for Print Nanny Device Only one public key may be active at a time DELETE <:endpoint> will soft-delete a key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |

### Return type

[**crate::models::DeviceKeyPair**](DeviceKeyPair.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_keypairs_list

> crate::models::PaginatedDevicePublicKeyList devices_keypairs_list(device_id, page)


Public key for Print Nanny Device Only one public key may be active at a time DELETE <:endpoint> will soft-delete a key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedDevicePublicKeyList**](PaginatedDevicePublicKeyList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_keypairs_retrieve

> crate::models::DevicePublicKey devices_keypairs_retrieve(device_id, id)


Public key for Print Nanny Device Only one public key may be active at a time DELETE <:endpoint> will soft-delete a key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this device public key. | [required] |

### Return type

[**crate::models::DevicePublicKey**](DevicePublicKey.md)

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
**device_request** | [**DeviceRequest**](DeviceRequest.md) |  | [required] |

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
**device_request** | [**DeviceRequest**](DeviceRequest.md) |  | [required] |

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


## devices_update

> crate::models::Device devices_update(id, device_request)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

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

