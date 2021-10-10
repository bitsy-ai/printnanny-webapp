# \AppliancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appliances_cameras_create**](AppliancesApi.md#appliances_cameras_create) | **POST** /api/appliances/{appliance_id}/cameras/ | 
[**appliances_cameras_list**](AppliancesApi.md#appliances_cameras_list) | **GET** /api/appliances/{appliance_id}/cameras/ | 
[**appliances_cameras_partial_update**](AppliancesApi.md#appliances_cameras_partial_update) | **PATCH** /api/appliances/{appliance_id}/cameras/{id}/ | 
[**appliances_cameras_retrieve**](AppliancesApi.md#appliances_cameras_retrieve) | **GET** /api/appliances/{appliance_id}/cameras/{id}/ | 
[**appliances_cameras_update**](AppliancesApi.md#appliances_cameras_update) | **PUT** /api/appliances/{appliance_id}/cameras/{id}/ | 
[**appliances_create**](AppliancesApi.md#appliances_create) | **POST** /api/appliances/ | 
[**appliances_list**](AppliancesApi.md#appliances_list) | **GET** /api/appliances/ | 
[**appliances_partial_update**](AppliancesApi.md#appliances_partial_update) | **PATCH** /api/appliances/{id}/ | 
[**appliances_printer_controllers_create**](AppliancesApi.md#appliances_printer_controllers_create) | **POST** /api/appliances/{appliance_id}/printer-controllers/ | 
[**appliances_printer_controllers_list**](AppliancesApi.md#appliances_printer_controllers_list) | **GET** /api/appliances/{appliance_id}/printer-controllers/ | 
[**appliances_printer_controllers_partial_update**](AppliancesApi.md#appliances_printer_controllers_partial_update) | **PATCH** /api/appliances/{appliance_id}/printer-controllers/{id}/ | 
[**appliances_printer_controllers_retrieve**](AppliancesApi.md#appliances_printer_controllers_retrieve) | **GET** /api/appliances/{appliance_id}/printer-controllers/{id}/ | 
[**appliances_printer_controllers_update**](AppliancesApi.md#appliances_printer_controllers_update) | **PUT** /api/appliances/{appliance_id}/printer-controllers/{id}/ | 
[**appliances_retrieve**](AppliancesApi.md#appliances_retrieve) | **GET** /api/appliances/{id}/ | 
[**appliances_update**](AppliancesApi.md#appliances_update) | **PUT** /api/appliances/{id}/ | 



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


## appliances_create

> crate::models::Appliance appliances_create(create_appliance_request)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**create_appliance_request** | [**CreateApplianceRequest**](CreateApplianceRequest.md) |  | [required] |

### Return type

[**crate::models::Appliance**](Appliance.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

> crate::models::PrinterController appliances_printer_controllers_create(appliance_id, printer_controller_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**printer_controller_request** | [**PrinterControllerRequest**](PrinterControllerRequest.md) |  | [required] |

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

> crate::models::PrinterController appliances_printer_controllers_update(appliance_id, id, printer_controller_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appliance_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this printer controller. | [required] |
**printer_controller_request** | [**PrinterControllerRequest**](PrinterControllerRequest.md) |  | [required] |

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

