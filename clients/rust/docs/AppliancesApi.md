# \AppliancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appliances_ansible_facts_create**](AppliancesApi.md#appliances_ansible_facts_create) | **POST** /api/appliances/{appliance_id}/ansible-facts/ | 
[**appliances_ansible_facts_list**](AppliancesApi.md#appliances_ansible_facts_list) | **GET** /api/appliances/{appliance_id}/ansible-facts/ | 
[**appliances_ansible_facts_partial_update**](AppliancesApi.md#appliances_ansible_facts_partial_update) | **PATCH** /api/appliances/{appliance_id}/ansible-facts/{id}/ | 
[**appliances_ansible_facts_retrieve**](AppliancesApi.md#appliances_ansible_facts_retrieve) | **GET** /api/appliances/{appliance_id}/ansible-facts/{id}/ | 
[**appliances_ansible_facts_update**](AppliancesApi.md#appliances_ansible_facts_update) | **PUT** /api/appliances/{appliance_id}/ansible-facts/{id}/ | 
[**appliances_cameras_create**](AppliancesApi.md#appliances_cameras_create) | **POST** /api/appliances/{appliance_id}/cameras/ | 
[**appliances_cameras_list**](AppliancesApi.md#appliances_cameras_list) | **GET** /api/appliances/{appliance_id}/cameras/ | 
[**appliances_cameras_partial_update**](AppliancesApi.md#appliances_cameras_partial_update) | **PATCH** /api/appliances/{appliance_id}/cameras/{id}/ | 
[**appliances_cameras_retrieve**](AppliancesApi.md#appliances_cameras_retrieve) | **GET** /api/appliances/{appliance_id}/cameras/{id}/ | 
[**appliances_cameras_update**](AppliancesApi.md#appliances_cameras_update) | **PUT** /api/appliances/{appliance_id}/cameras/{id}/ | 
[**appliances_cloud_iot_devices_create**](AppliancesApi.md#appliances_cloud_iot_devices_create) | **POST** /api/appliances/{appliance_id}/cloud-iot-devices/ | 
[**appliances_cloud_iot_devices_list**](AppliancesApi.md#appliances_cloud_iot_devices_list) | **GET** /api/appliances/{appliance_id}/cloud-iot-devices/ | 
[**appliances_cloud_iot_devices_partial_update**](AppliancesApi.md#appliances_cloud_iot_devices_partial_update) | **PATCH** /api/appliances/{appliance_id}/cloud-iot-devices/{id}/ | 
[**appliances_cloud_iot_devices_retrieve**](AppliancesApi.md#appliances_cloud_iot_devices_retrieve) | **GET** /api/appliances/{appliance_id}/cloud-iot-devices/{id}/ | 
[**appliances_cloud_iot_devices_update**](AppliancesApi.md#appliances_cloud_iot_devices_update) | **PUT** /api/appliances/{appliance_id}/cloud-iot-devices/{id}/ | 
[**appliances_create**](AppliancesApi.md#appliances_create) | **POST** /api/appliances/ | 
[**appliances_keypairs_create**](AppliancesApi.md#appliances_keypairs_create) | **POST** /api/appliances/{appliance_id}/keypairs/ | 
[**appliances_keypairs_list**](AppliancesApi.md#appliances_keypairs_list) | **GET** /api/appliances/{appliance_id}/keypairs/ | 
[**appliances_keypairs_retrieve**](AppliancesApi.md#appliances_keypairs_retrieve) | **GET** /api/appliances/{appliance_id}/keypairs/{id}/ | 
[**appliances_list**](AppliancesApi.md#appliances_list) | **GET** /api/appliances/ | 
[**appliances_partial_update**](AppliancesApi.md#appliances_partial_update) | **PATCH** /api/appliances/{id}/ | 
[**appliances_printer_controllers_create**](AppliancesApi.md#appliances_printer_controllers_create) | **POST** /api/appliances/{appliance_id}/printer-controllers/ | 
[**appliances_printer_controllers_list**](AppliancesApi.md#appliances_printer_controllers_list) | **GET** /api/appliances/{appliance_id}/printer-controllers/ | 
[**appliances_printer_controllers_partial_update**](AppliancesApi.md#appliances_printer_controllers_partial_update) | **PATCH** /api/appliances/{appliance_id}/printer-controllers/{id}/ | 
[**appliances_printer_controllers_retrieve**](AppliancesApi.md#appliances_printer_controllers_retrieve) | **GET** /api/appliances/{appliance_id}/printer-controllers/{id}/ | 
[**appliances_printer_controllers_update**](AppliancesApi.md#appliances_printer_controllers_update) | **PUT** /api/appliances/{appliance_id}/printer-controllers/{id}/ | 
[**appliances_retrieve**](AppliancesApi.md#appliances_retrieve) | **GET** /api/appliances/{id}/ | 
[**appliances_retrieve_hostname**](AppliancesApi.md#appliances_retrieve_hostname) | **GET** /api/appliances/{hostname} | 
[**appliances_update**](AppliancesApi.md#appliances_update) | **PUT** /api/appliances/{id}/ | 



## appliances_ansible_facts_create

> crate::models::AnsibleFacts appliances_ansible_facts_create(appliance_id, ansible_facts_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**ansible_facts_request** | [**AnsibleFactsRequest**](AnsibleFactsRequest.md) |  | [required] |

### Return type

[**crate::models::AnsibleFacts**](AnsibleFacts.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_ansible_facts_list

> crate::models::PaginatedAnsibleFactsList appliances_ansible_facts_list(appliance_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedAnsibleFactsList**](PaginatedAnsibleFactsList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_ansible_facts_partial_update

> crate::models::AnsibleFacts appliances_ansible_facts_partial_update(appliance_id, id, patched_ansible_facts_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
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


## appliances_ansible_facts_retrieve

> crate::models::AnsibleFacts appliances_ansible_facts_retrieve(appliance_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this ansible facts. | [required] |

### Return type

[**crate::models::AnsibleFacts**](AnsibleFacts.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_ansible_facts_update

> crate::models::AnsibleFacts appliances_ansible_facts_update(appliance_id, id, ansible_facts_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
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


## appliances_cameras_create

> crate::models::Camera appliances_cameras_create(appliance_id, camera_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**camera_request** | [**CameraRequest**](CameraRequest.md) |  | [required] |

### Return type

[**crate::models::Camera**](Camera.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_cameras_list

> crate::models::PaginatedCameraList appliances_cameras_list(appliance_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedCameraList**](PaginatedCameraList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_cameras_partial_update

> crate::models::Camera appliances_cameras_partial_update(appliance_id, id, patched_camera_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
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


## appliances_cameras_retrieve

> crate::models::Camera appliances_cameras_retrieve(appliance_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this camera. | [required] |

### Return type

[**crate::models::Camera**](Camera.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_cameras_update

> crate::models::Camera appliances_cameras_update(appliance_id, id, camera_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
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


## appliances_cloud_iot_devices_create

> crate::models::CloudIoTDevice appliances_cloud_iot_devices_create(appliance_id, cloud_io_t_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**cloud_io_t_device_request** | [**CloudIoTDeviceRequest**](CloudIoTDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::CloudIoTDevice**](CloudIoTDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_cloud_iot_devices_list

> crate::models::PaginatedCloudIoTDeviceList appliances_cloud_iot_devices_list(appliance_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedCloudIoTDeviceList**](PaginatedCloudIoTDeviceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_cloud_iot_devices_partial_update

> crate::models::CloudIoTDevice appliances_cloud_iot_devices_partial_update(appliance_id, id, patched_cloud_io_t_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
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


## appliances_cloud_iot_devices_retrieve

> crate::models::CloudIoTDevice appliances_cloud_iot_devices_retrieve(appliance_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**id** | **String** |  | [required] |

### Return type

[**crate::models::CloudIoTDevice**](CloudIoTDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_cloud_iot_devices_update

> crate::models::CloudIoTDevice appliances_cloud_iot_devices_update(appliance_id, id, cloud_io_t_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
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


## appliances_create

> crate::models::Appliance appliances_create(appliance_request)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_request** | [**ApplianceRequest**](ApplianceRequest.md) |  | [required] |

### Return type

[**crate::models::Appliance**](Appliance.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_keypairs_create

> crate::models::ApplianceKeyPair appliances_keypairs_create(appliance_id)


Public key for Print Nanny Appliance Only one public key may be active at a time DELETE <:endpoint> will soft-delete a key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |

### Return type

[**crate::models::ApplianceKeyPair**](ApplianceKeyPair.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_keypairs_list

> crate::models::PaginatedAppliancePublicKeyList appliances_keypairs_list(appliance_id, page)


Public key for Print Nanny Appliance Only one public key may be active at a time DELETE <:endpoint> will soft-delete a key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedAppliancePublicKeyList**](PaginatedAppliancePublicKeyList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_keypairs_retrieve

> crate::models::AppliancePublicKey appliances_keypairs_retrieve(appliance_id, id)


Public key for Print Nanny Appliance Only one public key may be active at a time DELETE <:endpoint> will soft-delete a key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this appliance public key. | [required] |

### Return type

[**crate::models::AppliancePublicKey**](AppliancePublicKey.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_list

> crate::models::PaginatedApplianceList appliances_list(page)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedApplianceList**](PaginatedApplianceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_partial_update

> crate::models::Appliance appliances_partial_update(id, patched_appliance_request)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this appliance. | [required] |
**patched_appliance_request** | Option<[**PatchedApplianceRequest**](PatchedApplianceRequest.md)> |  |  |

### Return type

[**crate::models::Appliance**](Appliance.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_printer_controllers_create

> crate::models::PrinterController appliances_printer_controllers_create(appliance_id, appliance_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**appliance_request** | [**ApplianceRequest**](ApplianceRequest.md) |  | [required] |

### Return type

[**crate::models::PrinterController**](PrinterController.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_printer_controllers_list

> crate::models::PaginatedPrinterControllerList appliances_printer_controllers_list(appliance_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPrinterControllerList**](PaginatedPrinterControllerList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_printer_controllers_partial_update

> crate::models::PrinterController appliances_printer_controllers_partial_update(appliance_id, id, patched_printer_controller_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
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


## appliances_printer_controllers_retrieve

> crate::models::PrinterController appliances_printer_controllers_retrieve(appliance_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this printer controller. | [required] |

### Return type

[**crate::models::PrinterController**](PrinterController.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_printer_controllers_update

> crate::models::PrinterController appliances_printer_controllers_update(appliance_id, id, appliance_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this printer controller. | [required] |
**appliance_request** | [**ApplianceRequest**](ApplianceRequest.md) |  | [required] |

### Return type

[**crate::models::PrinterController**](PrinterController.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_retrieve

> crate::models::Appliance appliances_retrieve(id)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this appliance. | [required] |

### Return type

[**crate::models::Appliance**](Appliance.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_retrieve_hostname

> crate::models::Appliance appliances_retrieve_hostname(hostname)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hostname** | **String** |  | [required] |

### Return type

[**crate::models::Appliance**](Appliance.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_update

> crate::models::Appliance appliances_update(id, appliance_request)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this appliance. | [required] |
**appliance_request** | [**ApplianceRequest**](ApplianceRequest.md) |  | [required] |

### Return type

[**crate::models::Appliance**](Appliance.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

