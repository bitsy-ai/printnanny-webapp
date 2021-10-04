# MlOpsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deviceCalibrationUpdateOrCreate**](MlOpsApi.md#deviceCalibrationUpdateOrCreate) | **POST** /api/device-calibrations/update-or-create/ | 
[**deviceCalibrationsList**](MlOpsApi.md#deviceCalibrationsList) | **GET** /api/device-calibrations/ | 
[**deviceCalibrationsPartialUpdate**](MlOpsApi.md#deviceCalibrationsPartialUpdate) | **PATCH** /api/device-calibrations/{id}/ | 
[**deviceCalibrationsRetrieve**](MlOpsApi.md#deviceCalibrationsRetrieve) | **GET** /api/device-calibrations/{id}/ | 
[**deviceCalibrationsUpdate**](MlOpsApi.md#deviceCalibrationsUpdate) | **PUT** /api/device-calibrations/{id}/ | 
[**experimentDeviceConfigsList**](MlOpsApi.md#experimentDeviceConfigsList) | **GET** /api/experiment-device-configs/ | 
[**experimentDeviceConfigsRetrieve**](MlOpsApi.md#experimentDeviceConfigsRetrieve) | **GET** /api/experiment-device-configs/{id}/ | 
[**experimentsList**](MlOpsApi.md#experimentsList) | **GET** /api/experiments/ | 
[**experimentsRetrieve**](MlOpsApi.md#experimentsRetrieve) | **GET** /api/experiments/{id}/ | 
[**modelArtifactsList**](MlOpsApi.md#modelArtifactsList) | **GET** /api/model-artifacts/ | 
[**modelArtifactsRetrieve**](MlOpsApi.md#modelArtifactsRetrieve) | **GET** /api/model-artifacts/{id}/ | 


<a name="deviceCalibrationUpdateOrCreate"></a>
# **deviceCalibrationUpdateOrCreate**
> DeviceCalibration deviceCalibrationUpdateOrCreate(deviceCalibrationRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val deviceCalibrationRequest : DeviceCalibrationRequest =  // DeviceCalibrationRequest | 
try {
    val result : DeviceCalibration = apiInstance.deviceCalibrationUpdateOrCreate(deviceCalibrationRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#deviceCalibrationUpdateOrCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#deviceCalibrationUpdateOrCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceCalibrationRequest** | [**DeviceCalibrationRequest**](DeviceCalibrationRequest.md)|  |

### Return type

[**DeviceCalibration**](DeviceCalibration.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="deviceCalibrationsList"></a>
# **deviceCalibrationsList**
> PaginatedDeviceCalibrationList deviceCalibrationsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedDeviceCalibrationList = apiInstance.deviceCalibrationsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#deviceCalibrationsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#deviceCalibrationsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedDeviceCalibrationList**](PaginatedDeviceCalibrationList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deviceCalibrationsPartialUpdate"></a>
# **deviceCalibrationsPartialUpdate**
> DeviceCalibration deviceCalibrationsPartialUpdate(id, patchedDeviceCalibrationRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device calibration.
val patchedDeviceCalibrationRequest : PatchedDeviceCalibrationRequest =  // PatchedDeviceCalibrationRequest | 
try {
    val result : DeviceCalibration = apiInstance.deviceCalibrationsPartialUpdate(id, patchedDeviceCalibrationRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#deviceCalibrationsPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#deviceCalibrationsPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this device calibration. |
 **patchedDeviceCalibrationRequest** | [**PatchedDeviceCalibrationRequest**](PatchedDeviceCalibrationRequest.md)|  | [optional]

### Return type

[**DeviceCalibration**](DeviceCalibration.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="deviceCalibrationsRetrieve"></a>
# **deviceCalibrationsRetrieve**
> DeviceCalibration deviceCalibrationsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device calibration.
try {
    val result : DeviceCalibration = apiInstance.deviceCalibrationsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#deviceCalibrationsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#deviceCalibrationsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this device calibration. |

### Return type

[**DeviceCalibration**](DeviceCalibration.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deviceCalibrationsUpdate"></a>
# **deviceCalibrationsUpdate**
> DeviceCalibration deviceCalibrationsUpdate(id, deviceCalibrationRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device calibration.
val deviceCalibrationRequest : DeviceCalibrationRequest =  // DeviceCalibrationRequest | 
try {
    val result : DeviceCalibration = apiInstance.deviceCalibrationsUpdate(id, deviceCalibrationRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#deviceCalibrationsUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#deviceCalibrationsUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this device calibration. |
 **deviceCalibrationRequest** | [**DeviceCalibrationRequest**](DeviceCalibrationRequest.md)|  |

### Return type

[**DeviceCalibration**](DeviceCalibration.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="experimentDeviceConfigsList"></a>
# **experimentDeviceConfigsList**
> PaginatedExperimentDeviceConfigList experimentDeviceConfigsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedExperimentDeviceConfigList = apiInstance.experimentDeviceConfigsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#experimentDeviceConfigsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#experimentDeviceConfigsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedExperimentDeviceConfigList**](PaginatedExperimentDeviceConfigList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="experimentDeviceConfigsRetrieve"></a>
# **experimentDeviceConfigsRetrieve**
> ExperimentDeviceConfig experimentDeviceConfigsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this experiment device config.
try {
    val result : ExperimentDeviceConfig = apiInstance.experimentDeviceConfigsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#experimentDeviceConfigsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#experimentDeviceConfigsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this experiment device config. |

### Return type

[**ExperimentDeviceConfig**](ExperimentDeviceConfig.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="experimentsList"></a>
# **experimentsList**
> PaginatedExperimentList experimentsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedExperimentList = apiInstance.experimentsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#experimentsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#experimentsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedExperimentList**](PaginatedExperimentList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="experimentsRetrieve"></a>
# **experimentsRetrieve**
> Experiment experimentsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this experiment.
try {
    val result : Experiment = apiInstance.experimentsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#experimentsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#experimentsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this experiment. |

### Return type

[**Experiment**](Experiment.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="modelArtifactsList"></a>
# **modelArtifactsList**
> PaginatedModelArtifactList modelArtifactsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedModelArtifactList = apiInstance.modelArtifactsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#modelArtifactsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#modelArtifactsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedModelArtifactList**](PaginatedModelArtifactList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="modelArtifactsRetrieve"></a>
# **modelArtifactsRetrieve**
> ModelArtifact modelArtifactsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this model artifact.
try {
    val result : ModelArtifact = apiInstance.modelArtifactsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#modelArtifactsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#modelArtifactsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this model artifact. |

### Return type

[**ModelArtifact**](ModelArtifact.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

