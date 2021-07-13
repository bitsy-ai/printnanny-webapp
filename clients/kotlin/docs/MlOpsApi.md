# MlOpsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiDeviceCalibrationsList**](MlOpsApi.md#apiDeviceCalibrationsList) | **GET** /api/device-calibrations/ | 
[**apiDeviceCalibrationsPartialUpdate**](MlOpsApi.md#apiDeviceCalibrationsPartialUpdate) | **PATCH** /api/device-calibrations/{id}/ | 
[**apiDeviceCalibrationsRetrieve**](MlOpsApi.md#apiDeviceCalibrationsRetrieve) | **GET** /api/device-calibrations/{id}/ | 
[**apiDeviceCalibrationsUpdate**](MlOpsApi.md#apiDeviceCalibrationsUpdate) | **PUT** /api/device-calibrations/{id}/ | 
[**apiExperimentDeviceConfigsList**](MlOpsApi.md#apiExperimentDeviceConfigsList) | **GET** /api/experiment-device-configs/ | 
[**apiExperimentDeviceConfigsRetrieve**](MlOpsApi.md#apiExperimentDeviceConfigsRetrieve) | **GET** /api/experiment-device-configs/{id}/ | 
[**apiExperimentsList**](MlOpsApi.md#apiExperimentsList) | **GET** /api/experiments/ | 
[**apiExperimentsRetrieve**](MlOpsApi.md#apiExperimentsRetrieve) | **GET** /api/experiments/{id}/ | 
[**apiModelArtifactsList**](MlOpsApi.md#apiModelArtifactsList) | **GET** /api/model-artifacts/ | 
[**apiModelArtifactsRetrieve**](MlOpsApi.md#apiModelArtifactsRetrieve) | **GET** /api/model-artifacts/{id}/ | 
[**deviceCalibrationUpdateOrCreate**](MlOpsApi.md#deviceCalibrationUpdateOrCreate) | **POST** /api/device-calibrations/update-or-create/ | 


<a name="apiDeviceCalibrationsList"></a>
# **apiDeviceCalibrationsList**
> PaginatedDeviceCalibrationList apiDeviceCalibrationsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedDeviceCalibrationList = apiInstance.apiDeviceCalibrationsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#apiDeviceCalibrationsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#apiDeviceCalibrationsList")
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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiDeviceCalibrationsPartialUpdate"></a>
# **apiDeviceCalibrationsPartialUpdate**
> DeviceCalibration apiDeviceCalibrationsPartialUpdate(id, patchedDeviceCalibrationRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device calibration.
val patchedDeviceCalibrationRequest : PatchedDeviceCalibrationRequest =  // PatchedDeviceCalibrationRequest | 
try {
    val result : DeviceCalibration = apiInstance.apiDeviceCalibrationsPartialUpdate(id, patchedDeviceCalibrationRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#apiDeviceCalibrationsPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#apiDeviceCalibrationsPartialUpdate")
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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="apiDeviceCalibrationsRetrieve"></a>
# **apiDeviceCalibrationsRetrieve**
> DeviceCalibration apiDeviceCalibrationsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device calibration.
try {
    val result : DeviceCalibration = apiInstance.apiDeviceCalibrationsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#apiDeviceCalibrationsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#apiDeviceCalibrationsRetrieve")
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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiDeviceCalibrationsUpdate"></a>
# **apiDeviceCalibrationsUpdate**
> DeviceCalibration apiDeviceCalibrationsUpdate(id, deviceCalibrationRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device calibration.
val deviceCalibrationRequest : DeviceCalibrationRequest =  // DeviceCalibrationRequest | 
try {
    val result : DeviceCalibration = apiInstance.apiDeviceCalibrationsUpdate(id, deviceCalibrationRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#apiDeviceCalibrationsUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#apiDeviceCalibrationsUpdate")
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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="apiExperimentDeviceConfigsList"></a>
# **apiExperimentDeviceConfigsList**
> PaginatedExperimentDeviceConfigList apiExperimentDeviceConfigsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedExperimentDeviceConfigList = apiInstance.apiExperimentDeviceConfigsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#apiExperimentDeviceConfigsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#apiExperimentDeviceConfigsList")
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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiExperimentDeviceConfigsRetrieve"></a>
# **apiExperimentDeviceConfigsRetrieve**
> ExperimentDeviceConfig apiExperimentDeviceConfigsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this experiment device config.
try {
    val result : ExperimentDeviceConfig = apiInstance.apiExperimentDeviceConfigsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#apiExperimentDeviceConfigsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#apiExperimentDeviceConfigsRetrieve")
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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiExperimentsList"></a>
# **apiExperimentsList**
> PaginatedExperimentList apiExperimentsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedExperimentList = apiInstance.apiExperimentsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#apiExperimentsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#apiExperimentsList")
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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiExperimentsRetrieve"></a>
# **apiExperimentsRetrieve**
> Experiment apiExperimentsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this experiment.
try {
    val result : Experiment = apiInstance.apiExperimentsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#apiExperimentsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#apiExperimentsRetrieve")
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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiModelArtifactsList"></a>
# **apiModelArtifactsList**
> PaginatedModelArtifactList apiModelArtifactsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedModelArtifactList = apiInstance.apiModelArtifactsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#apiModelArtifactsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#apiModelArtifactsList")
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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiModelArtifactsRetrieve"></a>
# **apiModelArtifactsRetrieve**
> ModelArtifact apiModelArtifactsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = MlOpsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this model artifact.
try {
    val result : ModelArtifact = apiInstance.apiModelArtifactsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MlOpsApi#apiModelArtifactsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MlOpsApi#apiModelArtifactsRetrieve")
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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

