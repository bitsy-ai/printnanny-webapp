# \MlOpsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_calibration_update_or_create**](MlOpsApi.md#device_calibration_update_or_create) | **post** /api/device-calibrations/update-or-create/ | 
[**device_calibrations_list**](MlOpsApi.md#device_calibrations_list) | **get** /api/device-calibrations/ | 
[**device_calibrations_partial_update**](MlOpsApi.md#device_calibrations_partial_update) | **patch** /api/device-calibrations/{id}/ | 
[**device_calibrations_retrieve**](MlOpsApi.md#device_calibrations_retrieve) | **get** /api/device-calibrations/{id}/ | 
[**device_calibrations_update**](MlOpsApi.md#device_calibrations_update) | **put** /api/device-calibrations/{id}/ | 
[**experiment_device_configs_list**](MlOpsApi.md#experiment_device_configs_list) | **get** /api/experiment-device-configs/ | 
[**experiment_device_configs_retrieve**](MlOpsApi.md#experiment_device_configs_retrieve) | **get** /api/experiment-device-configs/{id}/ | 
[**experiments_list**](MlOpsApi.md#experiments_list) | **get** /api/experiments/ | 
[**experiments_retrieve**](MlOpsApi.md#experiments_retrieve) | **get** /api/experiments/{id}/ | 
[**model_artifacts_list**](MlOpsApi.md#model_artifacts_list) | **get** /api/model-artifacts/ | 
[**model_artifacts_retrieve**](MlOpsApi.md#model_artifacts_retrieve) | **get** /api/model-artifacts/{id}/ | 



## device_calibration_update_or_create

> crate::models::DeviceCalibration device_calibration_update_or_create(device_calibration_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_calibration_request** | [**DeviceCalibrationRequest**](DeviceCalibrationRequest.md) |  | [required] |

### Return type

[**crate::models::DeviceCalibration**](DeviceCalibration.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## device_calibrations_list

> crate::models::PaginatedDeviceCalibrationList device_calibrations_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedDeviceCalibrationList**](PaginatedDeviceCalibrationList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## device_calibrations_partial_update

> crate::models::DeviceCalibration device_calibrations_partial_update(id, patched_device_calibration_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this device calibration. | [required] |
**patched_device_calibration_request** | Option<[**PatchedDeviceCalibrationRequest**](PatchedDeviceCalibrationRequest.md)> |  |  |

### Return type

[**crate::models::DeviceCalibration**](DeviceCalibration.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## device_calibrations_retrieve

> crate::models::DeviceCalibration device_calibrations_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this device calibration. | [required] |

### Return type

[**crate::models::DeviceCalibration**](DeviceCalibration.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## device_calibrations_update

> crate::models::DeviceCalibration device_calibrations_update(id, device_calibration_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this device calibration. | [required] |
**device_calibration_request** | [**DeviceCalibrationRequest**](DeviceCalibrationRequest.md) |  | [required] |

### Return type

[**crate::models::DeviceCalibration**](DeviceCalibration.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## experiment_device_configs_list

> crate::models::PaginatedExperimentDeviceConfigList experiment_device_configs_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedExperimentDeviceConfigList**](PaginatedExperimentDeviceConfigList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## experiment_device_configs_retrieve

> crate::models::ExperimentDeviceConfig experiment_device_configs_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this experiment device config. | [required] |

### Return type

[**crate::models::ExperimentDeviceConfig**](ExperimentDeviceConfig.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## experiments_list

> crate::models::PaginatedExperimentList experiments_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedExperimentList**](PaginatedExperimentList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## experiments_retrieve

> crate::models::Experiment experiments_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this experiment. | [required] |

### Return type

[**crate::models::Experiment**](Experiment.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## model_artifacts_list

> crate::models::PaginatedModelArtifactList model_artifacts_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedModelArtifactList**](PaginatedModelArtifactList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## model_artifacts_retrieve

> crate::models::ModelArtifact model_artifacts_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this model artifact. | [required] |

### Return type

[**crate::models::ModelArtifact**](ModelArtifact.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

