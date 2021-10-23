# AppliancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appliancesAnsibleFactsCreate**](AppliancesApi.md#appliancesAnsibleFactsCreate) | **POST** /api/appliances/{appliance_id}/ansible-facts/ | 
[**appliancesAnsibleFactsList**](AppliancesApi.md#appliancesAnsibleFactsList) | **GET** /api/appliances/{appliance_id}/ansible-facts/ | 
[**appliancesAnsibleFactsPartialUpdate**](AppliancesApi.md#appliancesAnsibleFactsPartialUpdate) | **PATCH** /api/appliances/{appliance_id}/ansible-facts/{id}/ | 
[**appliancesAnsibleFactsRetrieve**](AppliancesApi.md#appliancesAnsibleFactsRetrieve) | **GET** /api/appliances/{appliance_id}/ansible-facts/{id}/ | 
[**appliancesAnsibleFactsUpdate**](AppliancesApi.md#appliancesAnsibleFactsUpdate) | **PUT** /api/appliances/{appliance_id}/ansible-facts/{id}/ | 
[**appliancesCamerasCreate**](AppliancesApi.md#appliancesCamerasCreate) | **POST** /api/appliances/{appliance_id}/cameras/ | 
[**appliancesCamerasList**](AppliancesApi.md#appliancesCamerasList) | **GET** /api/appliances/{appliance_id}/cameras/ | 
[**appliancesCamerasPartialUpdate**](AppliancesApi.md#appliancesCamerasPartialUpdate) | **PATCH** /api/appliances/{appliance_id}/cameras/{id}/ | 
[**appliancesCamerasRetrieve**](AppliancesApi.md#appliancesCamerasRetrieve) | **GET** /api/appliances/{appliance_id}/cameras/{id}/ | 
[**appliancesCamerasUpdate**](AppliancesApi.md#appliancesCamerasUpdate) | **PUT** /api/appliances/{appliance_id}/cameras/{id}/ | 
[**appliancesCloudIotDevicesCreate**](AppliancesApi.md#appliancesCloudIotDevicesCreate) | **POST** /api/appliances/{appliance_id}/cloud-iot-devices/ | 
[**appliancesCloudIotDevicesList**](AppliancesApi.md#appliancesCloudIotDevicesList) | **GET** /api/appliances/{appliance_id}/cloud-iot-devices/ | 
[**appliancesCloudIotDevicesPartialUpdate**](AppliancesApi.md#appliancesCloudIotDevicesPartialUpdate) | **PATCH** /api/appliances/{appliance_id}/cloud-iot-devices/{id}/ | 
[**appliancesCloudIotDevicesRetrieve**](AppliancesApi.md#appliancesCloudIotDevicesRetrieve) | **GET** /api/appliances/{appliance_id}/cloud-iot-devices/{id}/ | 
[**appliancesCloudIotDevicesUpdate**](AppliancesApi.md#appliancesCloudIotDevicesUpdate) | **PUT** /api/appliances/{appliance_id}/cloud-iot-devices/{id}/ | 
[**appliancesCreate**](AppliancesApi.md#appliancesCreate) | **POST** /api/appliances/ | 
[**appliancesKeypairsCreate**](AppliancesApi.md#appliancesKeypairsCreate) | **POST** /api/appliances/{appliance_id}/keypairs/ | 
[**appliancesKeypairsList**](AppliancesApi.md#appliancesKeypairsList) | **GET** /api/appliances/{appliance_id}/keypairs/ | 
[**appliancesKeypairsRetrieve**](AppliancesApi.md#appliancesKeypairsRetrieve) | **GET** /api/appliances/{appliance_id}/keypairs/{id}/ | 
[**appliancesList**](AppliancesApi.md#appliancesList) | **GET** /api/appliances/ | 
[**appliancesPartialUpdate**](AppliancesApi.md#appliancesPartialUpdate) | **PATCH** /api/appliances/{id}/ | 
[**appliancesPrinterControllersCreate**](AppliancesApi.md#appliancesPrinterControllersCreate) | **POST** /api/appliances/{appliance_id}/printer-controllers/ | 
[**appliancesPrinterControllersList**](AppliancesApi.md#appliancesPrinterControllersList) | **GET** /api/appliances/{appliance_id}/printer-controllers/ | 
[**appliancesPrinterControllersPartialUpdate**](AppliancesApi.md#appliancesPrinterControllersPartialUpdate) | **PATCH** /api/appliances/{appliance_id}/printer-controllers/{id}/ | 
[**appliancesPrinterControllersRetrieve**](AppliancesApi.md#appliancesPrinterControllersRetrieve) | **GET** /api/appliances/{appliance_id}/printer-controllers/{id}/ | 
[**appliancesPrinterControllersUpdate**](AppliancesApi.md#appliancesPrinterControllersUpdate) | **PUT** /api/appliances/{appliance_id}/printer-controllers/{id}/ | 
[**appliancesRetrieve**](AppliancesApi.md#appliancesRetrieve) | **GET** /api/appliances/{id}/ | 
[**appliancesRetrieveHostname**](AppliancesApi.md#appliancesRetrieveHostname) | **GET** /api/appliances/{hostname} | 
[**appliancesUpdate**](AppliancesApi.md#appliancesUpdate) | **PUT** /api/appliances/{id}/ | 


<a name="appliancesAnsibleFactsCreate"></a>
# **appliancesAnsibleFactsCreate**
> AnsibleFacts appliancesAnsibleFactsCreate(applianceId, ansibleFactsRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val ansibleFactsRequest : AnsibleFactsRequest =  // AnsibleFactsRequest | 
try {
    val result : AnsibleFacts = apiInstance.appliancesAnsibleFactsCreate(applianceId, ansibleFactsRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesAnsibleFactsCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesAnsibleFactsCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **ansibleFactsRequest** | [**AnsibleFactsRequest**](AnsibleFactsRequest.md)|  |

### Return type

[**AnsibleFacts**](AnsibleFacts.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesAnsibleFactsList"></a>
# **appliancesAnsibleFactsList**
> PaginatedAnsibleFactsList appliancesAnsibleFactsList(applianceId, page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedAnsibleFactsList = apiInstance.appliancesAnsibleFactsList(applianceId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesAnsibleFactsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesAnsibleFactsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedAnsibleFactsList**](PaginatedAnsibleFactsList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesAnsibleFactsPartialUpdate"></a>
# **appliancesAnsibleFactsPartialUpdate**
> AnsibleFacts appliancesAnsibleFactsPartialUpdate(applianceId, id, patchedAnsibleFactsRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this ansible facts.
val patchedAnsibleFactsRequest : PatchedAnsibleFactsRequest =  // PatchedAnsibleFactsRequest | 
try {
    val result : AnsibleFacts = apiInstance.appliancesAnsibleFactsPartialUpdate(applianceId, id, patchedAnsibleFactsRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesAnsibleFactsPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesAnsibleFactsPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this ansible facts. |
 **patchedAnsibleFactsRequest** | [**PatchedAnsibleFactsRequest**](PatchedAnsibleFactsRequest.md)|  | [optional]

### Return type

[**AnsibleFacts**](AnsibleFacts.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesAnsibleFactsRetrieve"></a>
# **appliancesAnsibleFactsRetrieve**
> AnsibleFacts appliancesAnsibleFactsRetrieve(applianceId, id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this ansible facts.
try {
    val result : AnsibleFacts = apiInstance.appliancesAnsibleFactsRetrieve(applianceId, id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesAnsibleFactsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesAnsibleFactsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this ansible facts. |

### Return type

[**AnsibleFacts**](AnsibleFacts.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesAnsibleFactsUpdate"></a>
# **appliancesAnsibleFactsUpdate**
> AnsibleFacts appliancesAnsibleFactsUpdate(applianceId, id, ansibleFactsRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this ansible facts.
val ansibleFactsRequest : AnsibleFactsRequest =  // AnsibleFactsRequest | 
try {
    val result : AnsibleFacts = apiInstance.appliancesAnsibleFactsUpdate(applianceId, id, ansibleFactsRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesAnsibleFactsUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesAnsibleFactsUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this ansible facts. |
 **ansibleFactsRequest** | [**AnsibleFactsRequest**](AnsibleFactsRequest.md)|  |

### Return type

[**AnsibleFacts**](AnsibleFacts.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesCamerasCreate"></a>
# **appliancesCamerasCreate**
> Camera appliancesCamerasCreate(applianceId, cameraRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val cameraRequest : CameraRequest =  // CameraRequest | 
try {
    val result : Camera = apiInstance.appliancesCamerasCreate(applianceId, cameraRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCamerasCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCamerasCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **cameraRequest** | [**CameraRequest**](CameraRequest.md)|  |

### Return type

[**Camera**](Camera.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesCamerasList"></a>
# **appliancesCamerasList**
> PaginatedCameraList appliancesCamerasList(applianceId, page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedCameraList = apiInstance.appliancesCamerasList(applianceId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCamerasList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCamerasList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedCameraList**](PaginatedCameraList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesCamerasPartialUpdate"></a>
# **appliancesCamerasPartialUpdate**
> Camera appliancesCamerasPartialUpdate(applianceId, id, patchedCameraRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this camera.
val patchedCameraRequest : PatchedCameraRequest =  // PatchedCameraRequest | 
try {
    val result : Camera = apiInstance.appliancesCamerasPartialUpdate(applianceId, id, patchedCameraRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCamerasPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCamerasPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this camera. |
 **patchedCameraRequest** | [**PatchedCameraRequest**](PatchedCameraRequest.md)|  | [optional]

### Return type

[**Camera**](Camera.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesCamerasRetrieve"></a>
# **appliancesCamerasRetrieve**
> Camera appliancesCamerasRetrieve(applianceId, id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this camera.
try {
    val result : Camera = apiInstance.appliancesCamerasRetrieve(applianceId, id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCamerasRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCamerasRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this camera. |

### Return type

[**Camera**](Camera.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesCamerasUpdate"></a>
# **appliancesCamerasUpdate**
> Camera appliancesCamerasUpdate(applianceId, id, cameraRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this camera.
val cameraRequest : CameraRequest =  // CameraRequest | 
try {
    val result : Camera = apiInstance.appliancesCamerasUpdate(applianceId, id, cameraRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCamerasUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCamerasUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this camera. |
 **cameraRequest** | [**CameraRequest**](CameraRequest.md)|  |

### Return type

[**Camera**](Camera.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesCloudIotDevicesCreate"></a>
# **appliancesCloudIotDevicesCreate**
> CloudIoTDevice appliancesCloudIotDevicesCreate(applianceId, cloudIoTDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val cloudIoTDeviceRequest : CloudIoTDeviceRequest =  // CloudIoTDeviceRequest | 
try {
    val result : CloudIoTDevice = apiInstance.appliancesCloudIotDevicesCreate(applianceId, cloudIoTDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCloudIotDevicesCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCloudIotDevicesCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **cloudIoTDeviceRequest** | [**CloudIoTDeviceRequest**](CloudIoTDeviceRequest.md)|  |

### Return type

[**CloudIoTDevice**](CloudIoTDevice.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesCloudIotDevicesList"></a>
# **appliancesCloudIotDevicesList**
> PaginatedCloudIoTDeviceList appliancesCloudIotDevicesList(applianceId, page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedCloudIoTDeviceList = apiInstance.appliancesCloudIotDevicesList(applianceId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCloudIotDevicesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCloudIotDevicesList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedCloudIoTDeviceList**](PaginatedCloudIoTDeviceList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesCloudIotDevicesPartialUpdate"></a>
# **appliancesCloudIotDevicesPartialUpdate**
> CloudIoTDevice appliancesCloudIotDevicesPartialUpdate(applianceId, id, patchedCloudIoTDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.String = id_example // kotlin.String | 
val patchedCloudIoTDeviceRequest : PatchedCloudIoTDeviceRequest =  // PatchedCloudIoTDeviceRequest | 
try {
    val result : CloudIoTDevice = apiInstance.appliancesCloudIotDevicesPartialUpdate(applianceId, id, patchedCloudIoTDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCloudIotDevicesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCloudIotDevicesPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.String**|  |
 **patchedCloudIoTDeviceRequest** | [**PatchedCloudIoTDeviceRequest**](PatchedCloudIoTDeviceRequest.md)|  | [optional]

### Return type

[**CloudIoTDevice**](CloudIoTDevice.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesCloudIotDevicesRetrieve"></a>
# **appliancesCloudIotDevicesRetrieve**
> CloudIoTDevice appliancesCloudIotDevicesRetrieve(applianceId, id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.String = id_example // kotlin.String | 
try {
    val result : CloudIoTDevice = apiInstance.appliancesCloudIotDevicesRetrieve(applianceId, id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCloudIotDevicesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCloudIotDevicesRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.String**|  |

### Return type

[**CloudIoTDevice**](CloudIoTDevice.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesCloudIotDevicesUpdate"></a>
# **appliancesCloudIotDevicesUpdate**
> CloudIoTDevice appliancesCloudIotDevicesUpdate(applianceId, id, cloudIoTDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.String = id_example // kotlin.String | 
val cloudIoTDeviceRequest : CloudIoTDeviceRequest =  // CloudIoTDeviceRequest | 
try {
    val result : CloudIoTDevice = apiInstance.appliancesCloudIotDevicesUpdate(applianceId, id, cloudIoTDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCloudIotDevicesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCloudIotDevicesUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.String**|  |
 **cloudIoTDeviceRequest** | [**CloudIoTDeviceRequest**](CloudIoTDeviceRequest.md)|  |

### Return type

[**CloudIoTDevice**](CloudIoTDevice.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesCreate"></a>
# **appliancesCreate**
> Appliance appliancesCreate(applianceRequest)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceRequest : ApplianceRequest =  // ApplianceRequest | 
try {
    val result : Appliance = apiInstance.appliancesCreate(applianceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceRequest** | [**ApplianceRequest**](ApplianceRequest.md)|  |

### Return type

[**Appliance**](Appliance.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesKeypairsCreate"></a>
# **appliancesKeypairsCreate**
> ApplianceKeyPair appliancesKeypairsCreate(applianceId)



Public key for Print Nanny Appliance Only one public key may be active at a time DELETE &lt;:endpoint&gt; will soft-delete a key

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : ApplianceKeyPair = apiInstance.appliancesKeypairsCreate(applianceId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesKeypairsCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesKeypairsCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |

### Return type

[**ApplianceKeyPair**](ApplianceKeyPair.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesKeypairsList"></a>
# **appliancesKeypairsList**
> PaginatedAppliancePublicKeyList appliancesKeypairsList(applianceId, page)



Public key for Print Nanny Appliance Only one public key may be active at a time DELETE &lt;:endpoint&gt; will soft-delete a key

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedAppliancePublicKeyList = apiInstance.appliancesKeypairsList(applianceId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesKeypairsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesKeypairsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedAppliancePublicKeyList**](PaginatedAppliancePublicKeyList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesKeypairsRetrieve"></a>
# **appliancesKeypairsRetrieve**
> AppliancePublicKey appliancesKeypairsRetrieve(applianceId, id)



Public key for Print Nanny Appliance Only one public key may be active at a time DELETE &lt;:endpoint&gt; will soft-delete a key

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this appliance public key.
try {
    val result : AppliancePublicKey = apiInstance.appliancesKeypairsRetrieve(applianceId, id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesKeypairsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesKeypairsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this appliance public key. |

### Return type

[**AppliancePublicKey**](AppliancePublicKey.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesList"></a>
# **appliancesList**
> PaginatedApplianceList appliancesList(page)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedApplianceList = apiInstance.appliancesList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedApplianceList**](PaginatedApplianceList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesPartialUpdate"></a>
# **appliancesPartialUpdate**
> Appliance appliancesPartialUpdate(id, patchedApplianceRequest)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this appliance.
val patchedApplianceRequest : PatchedApplianceRequest =  // PatchedApplianceRequest | 
try {
    val result : Appliance = apiInstance.appliancesPartialUpdate(id, patchedApplianceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this appliance. |
 **patchedApplianceRequest** | [**PatchedApplianceRequest**](PatchedApplianceRequest.md)|  | [optional]

### Return type

[**Appliance**](Appliance.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesPrinterControllersCreate"></a>
# **appliancesPrinterControllersCreate**
> PrinterController appliancesPrinterControllersCreate(applianceId, applianceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val applianceRequest : ApplianceRequest =  // ApplianceRequest | 
try {
    val result : PrinterController = apiInstance.appliancesPrinterControllersCreate(applianceId, applianceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesPrinterControllersCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesPrinterControllersCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **applianceRequest** | [**ApplianceRequest**](ApplianceRequest.md)|  |

### Return type

[**PrinterController**](PrinterController.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesPrinterControllersList"></a>
# **appliancesPrinterControllersList**
> PaginatedPrinterControllerList appliancesPrinterControllersList(applianceId, page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrinterControllerList = apiInstance.appliancesPrinterControllersList(applianceId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesPrinterControllersList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesPrinterControllersList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedPrinterControllerList**](PaginatedPrinterControllerList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesPrinterControllersPartialUpdate"></a>
# **appliancesPrinterControllersPartialUpdate**
> PrinterController appliancesPrinterControllersPartialUpdate(applianceId, id, patchedPrinterControllerRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer controller.
val patchedPrinterControllerRequest : PatchedPrinterControllerRequest =  // PatchedPrinterControllerRequest | 
try {
    val result : PrinterController = apiInstance.appliancesPrinterControllersPartialUpdate(applianceId, id, patchedPrinterControllerRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesPrinterControllersPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesPrinterControllersPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this printer controller. |
 **patchedPrinterControllerRequest** | [**PatchedPrinterControllerRequest**](PatchedPrinterControllerRequest.md)|  | [optional]

### Return type

[**PrinterController**](PrinterController.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesPrinterControllersRetrieve"></a>
# **appliancesPrinterControllersRetrieve**
> PrinterController appliancesPrinterControllersRetrieve(applianceId, id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer controller.
try {
    val result : PrinterController = apiInstance.appliancesPrinterControllersRetrieve(applianceId, id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesPrinterControllersRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesPrinterControllersRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this printer controller. |

### Return type

[**PrinterController**](PrinterController.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesPrinterControllersUpdate"></a>
# **appliancesPrinterControllersUpdate**
> PrinterController appliancesPrinterControllersUpdate(applianceId, id, applianceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val applianceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer controller.
val applianceRequest : ApplianceRequest =  // ApplianceRequest | 
try {
    val result : PrinterController = apiInstance.appliancesPrinterControllersUpdate(applianceId, id, applianceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesPrinterControllersUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesPrinterControllersUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applianceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this printer controller. |
 **applianceRequest** | [**ApplianceRequest**](ApplianceRequest.md)|  |

### Return type

[**PrinterController**](PrinterController.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesRetrieve"></a>
# **appliancesRetrieve**
> Appliance appliancesRetrieve(id)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this appliance.
try {
    val result : Appliance = apiInstance.appliancesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this appliance. |

### Return type

[**Appliance**](Appliance.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesRetrieveHostname"></a>
# **appliancesRetrieveHostname**
> Appliance appliancesRetrieveHostname(hostname)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val hostname : kotlin.String = hostname_example // kotlin.String | 
try {
    val result : Appliance = apiInstance.appliancesRetrieveHostname(hostname)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesRetrieveHostname")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesRetrieveHostname")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **kotlin.String**|  |

### Return type

[**Appliance**](Appliance.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesUpdate"></a>
# **appliancesUpdate**
> Appliance appliancesUpdate(id, applianceRequest)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this appliance.
val applianceRequest : ApplianceRequest =  // ApplianceRequest | 
try {
    val result : Appliance = apiInstance.appliancesUpdate(id, applianceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this appliance. |
 **applianceRequest** | [**ApplianceRequest**](ApplianceRequest.md)|  |

### Return type

[**Appliance**](Appliance.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

