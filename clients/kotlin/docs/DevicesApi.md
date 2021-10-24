# DevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicesAnsibleFactsCreate**](DevicesApi.md#devicesAnsibleFactsCreate) | **POST** /api/devices/{device_id}/ansible-facts/ | 
[**devicesAnsibleFactsList**](DevicesApi.md#devicesAnsibleFactsList) | **GET** /api/devices/{device_id}/ansible-facts/ | 
[**devicesAnsibleFactsPartialUpdate**](DevicesApi.md#devicesAnsibleFactsPartialUpdate) | **PATCH** /api/devices/{device_id}/ansible-facts/{id}/ | 
[**devicesAnsibleFactsRetrieve**](DevicesApi.md#devicesAnsibleFactsRetrieve) | **GET** /api/devices/{device_id}/ansible-facts/{id}/ | 
[**devicesAnsibleFactsUpdate**](DevicesApi.md#devicesAnsibleFactsUpdate) | **PUT** /api/devices/{device_id}/ansible-facts/{id}/ | 
[**devicesCamerasCreate**](DevicesApi.md#devicesCamerasCreate) | **POST** /api/devices/{device_id}/cameras/ | 
[**devicesCamerasList**](DevicesApi.md#devicesCamerasList) | **GET** /api/devices/{device_id}/cameras/ | 
[**devicesCamerasPartialUpdate**](DevicesApi.md#devicesCamerasPartialUpdate) | **PATCH** /api/devices/{device_id}/cameras/{id}/ | 
[**devicesCamerasRetrieve**](DevicesApi.md#devicesCamerasRetrieve) | **GET** /api/devices/{device_id}/cameras/{id}/ | 
[**devicesCamerasUpdate**](DevicesApi.md#devicesCamerasUpdate) | **PUT** /api/devices/{device_id}/cameras/{id}/ | 
[**devicesCloudIotDevicesCreate**](DevicesApi.md#devicesCloudIotDevicesCreate) | **POST** /api/devices/{device_id}/cloud-iot-devices/ | 
[**devicesCloudIotDevicesList**](DevicesApi.md#devicesCloudIotDevicesList) | **GET** /api/devices/{device_id}/cloud-iot-devices/ | 
[**devicesCloudIotDevicesPartialUpdate**](DevicesApi.md#devicesCloudIotDevicesPartialUpdate) | **PATCH** /api/devices/{device_id}/cloud-iot-devices/{id}/ | 
[**devicesCloudIotDevicesRetrieve**](DevicesApi.md#devicesCloudIotDevicesRetrieve) | **GET** /api/devices/{device_id}/cloud-iot-devices/{id}/ | 
[**devicesCloudIotDevicesUpdate**](DevicesApi.md#devicesCloudIotDevicesUpdate) | **PUT** /api/devices/{device_id}/cloud-iot-devices/{id}/ | 
[**devicesCreate**](DevicesApi.md#devicesCreate) | **POST** /api/devices/ | 
[**devicesKeypairsCreate**](DevicesApi.md#devicesKeypairsCreate) | **POST** /api/devices/{device_id}/keypairs/ | 
[**devicesKeypairsList**](DevicesApi.md#devicesKeypairsList) | **GET** /api/devices/{device_id}/keypairs/ | 
[**devicesKeypairsRetrieve**](DevicesApi.md#devicesKeypairsRetrieve) | **GET** /api/devices/{device_id}/keypairs/{id}/ | 
[**devicesList**](DevicesApi.md#devicesList) | **GET** /api/devices/ | 
[**devicesPartialUpdate**](DevicesApi.md#devicesPartialUpdate) | **PATCH** /api/devices/{id}/ | 
[**devicesPrinterControllersCreate**](DevicesApi.md#devicesPrinterControllersCreate) | **POST** /api/devices/{device_id}/printer-controllers/ | 
[**devicesPrinterControllersList**](DevicesApi.md#devicesPrinterControllersList) | **GET** /api/devices/{device_id}/printer-controllers/ | 
[**devicesPrinterControllersPartialUpdate**](DevicesApi.md#devicesPrinterControllersPartialUpdate) | **PATCH** /api/devices/{device_id}/printer-controllers/{id}/ | 
[**devicesPrinterControllersRetrieve**](DevicesApi.md#devicesPrinterControllersRetrieve) | **GET** /api/devices/{device_id}/printer-controllers/{id}/ | 
[**devicesPrinterControllersUpdate**](DevicesApi.md#devicesPrinterControllersUpdate) | **PUT** /api/devices/{device_id}/printer-controllers/{id}/ | 
[**devicesRetrieve**](DevicesApi.md#devicesRetrieve) | **GET** /api/devices/{id}/ | 
[**devicesRetrieveHostname**](DevicesApi.md#devicesRetrieveHostname) | **GET** /api/devices/{hostname} | 
[**devicesUpdate**](DevicesApi.md#devicesUpdate) | **PUT** /api/devices/{id}/ | 


<a name="devicesAnsibleFactsCreate"></a>
# **devicesAnsibleFactsCreate**
> AnsibleFacts devicesAnsibleFactsCreate(deviceId, ansibleFactsRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val ansibleFactsRequest : AnsibleFactsRequest =  // AnsibleFactsRequest | 
try {
    val result : AnsibleFacts = apiInstance.devicesAnsibleFactsCreate(deviceId, ansibleFactsRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesAnsibleFactsCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesAnsibleFactsCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesAnsibleFactsList"></a>
# **devicesAnsibleFactsList**
> PaginatedAnsibleFactsList devicesAnsibleFactsList(deviceId, page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedAnsibleFactsList = apiInstance.devicesAnsibleFactsList(deviceId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesAnsibleFactsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesAnsibleFactsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesAnsibleFactsPartialUpdate"></a>
# **devicesAnsibleFactsPartialUpdate**
> AnsibleFacts devicesAnsibleFactsPartialUpdate(deviceId, id, patchedAnsibleFactsRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this ansible facts.
val patchedAnsibleFactsRequest : PatchedAnsibleFactsRequest =  // PatchedAnsibleFactsRequest | 
try {
    val result : AnsibleFacts = apiInstance.devicesAnsibleFactsPartialUpdate(deviceId, id, patchedAnsibleFactsRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesAnsibleFactsPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesAnsibleFactsPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesAnsibleFactsRetrieve"></a>
# **devicesAnsibleFactsRetrieve**
> AnsibleFacts devicesAnsibleFactsRetrieve(deviceId, id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this ansible facts.
try {
    val result : AnsibleFacts = apiInstance.devicesAnsibleFactsRetrieve(deviceId, id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesAnsibleFactsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesAnsibleFactsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesAnsibleFactsUpdate"></a>
# **devicesAnsibleFactsUpdate**
> AnsibleFacts devicesAnsibleFactsUpdate(deviceId, id, ansibleFactsRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this ansible facts.
val ansibleFactsRequest : AnsibleFactsRequest =  // AnsibleFactsRequest | 
try {
    val result : AnsibleFacts = apiInstance.devicesAnsibleFactsUpdate(deviceId, id, ansibleFactsRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesAnsibleFactsUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesAnsibleFactsUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCamerasCreate"></a>
# **devicesCamerasCreate**
> Camera devicesCamerasCreate(deviceId, cameraRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val cameraRequest : CameraRequest =  // CameraRequest | 
try {
    val result : Camera = apiInstance.devicesCamerasCreate(deviceId, cameraRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCamerasCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCamerasCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCamerasList"></a>
# **devicesCamerasList**
> PaginatedCameraList devicesCamerasList(deviceId, page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedCameraList = apiInstance.devicesCamerasList(deviceId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCamerasList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCamerasList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCamerasPartialUpdate"></a>
# **devicesCamerasPartialUpdate**
> Camera devicesCamerasPartialUpdate(deviceId, id, patchedCameraRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this camera.
val patchedCameraRequest : PatchedCameraRequest =  // PatchedCameraRequest | 
try {
    val result : Camera = apiInstance.devicesCamerasPartialUpdate(deviceId, id, patchedCameraRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCamerasPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCamerasPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCamerasRetrieve"></a>
# **devicesCamerasRetrieve**
> Camera devicesCamerasRetrieve(deviceId, id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this camera.
try {
    val result : Camera = apiInstance.devicesCamerasRetrieve(deviceId, id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCamerasRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCamerasRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCamerasUpdate"></a>
# **devicesCamerasUpdate**
> Camera devicesCamerasUpdate(deviceId, id, cameraRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this camera.
val cameraRequest : CameraRequest =  // CameraRequest | 
try {
    val result : Camera = apiInstance.devicesCamerasUpdate(deviceId, id, cameraRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCamerasUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCamerasUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCloudIotDevicesCreate"></a>
# **devicesCloudIotDevicesCreate**
> CloudIoTDevice devicesCloudIotDevicesCreate(deviceId, cloudIoTDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val cloudIoTDeviceRequest : CloudIoTDeviceRequest =  // CloudIoTDeviceRequest | 
try {
    val result : CloudIoTDevice = apiInstance.devicesCloudIotDevicesCreate(deviceId, cloudIoTDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCloudIotDevicesCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCloudIotDevicesCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCloudIotDevicesList"></a>
# **devicesCloudIotDevicesList**
> PaginatedCloudIoTDeviceList devicesCloudIotDevicesList(deviceId, page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedCloudIoTDeviceList = apiInstance.devicesCloudIotDevicesList(deviceId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCloudIotDevicesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCloudIotDevicesList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCloudIotDevicesPartialUpdate"></a>
# **devicesCloudIotDevicesPartialUpdate**
> CloudIoTDevice devicesCloudIotDevicesPartialUpdate(deviceId, id, patchedCloudIoTDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.String = id_example // kotlin.String | 
val patchedCloudIoTDeviceRequest : PatchedCloudIoTDeviceRequest =  // PatchedCloudIoTDeviceRequest | 
try {
    val result : CloudIoTDevice = apiInstance.devicesCloudIotDevicesPartialUpdate(deviceId, id, patchedCloudIoTDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCloudIotDevicesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCloudIotDevicesPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCloudIotDevicesRetrieve"></a>
# **devicesCloudIotDevicesRetrieve**
> CloudIoTDevice devicesCloudIotDevicesRetrieve(deviceId, id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.String = id_example // kotlin.String | 
try {
    val result : CloudIoTDevice = apiInstance.devicesCloudIotDevicesRetrieve(deviceId, id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCloudIotDevicesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCloudIotDevicesRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCloudIotDevicesUpdate"></a>
# **devicesCloudIotDevicesUpdate**
> CloudIoTDevice devicesCloudIotDevicesUpdate(deviceId, id, cloudIoTDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.String = id_example // kotlin.String | 
val cloudIoTDeviceRequest : CloudIoTDeviceRequest =  // CloudIoTDeviceRequest | 
try {
    val result : CloudIoTDevice = apiInstance.devicesCloudIotDevicesUpdate(deviceId, id, cloudIoTDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCloudIotDevicesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCloudIotDevicesUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesCreate"></a>
# **devicesCreate**
> Device devicesCreate(deviceRequest)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceRequest : DeviceRequest =  // DeviceRequest | 
try {
    val result : Device = apiInstance.devicesCreate(deviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceRequest** | [**DeviceRequest**](DeviceRequest.md)|  |

### Return type

[**Device**](Device.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="devicesKeypairsCreate"></a>
# **devicesKeypairsCreate**
> DeviceKeyPair devicesKeypairsCreate(deviceId)



Public key for Print Nanny Device Only one public key may be active at a time DELETE &lt;:endpoint&gt; will soft-delete a key

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : DeviceKeyPair = apiInstance.devicesKeypairsCreate(deviceId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesKeypairsCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesKeypairsCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |

### Return type

[**DeviceKeyPair**](DeviceKeyPair.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="devicesKeypairsList"></a>
# **devicesKeypairsList**
> PaginatedDevicePublicKeyList devicesKeypairsList(deviceId, page)



Public key for Print Nanny Device Only one public key may be active at a time DELETE &lt;:endpoint&gt; will soft-delete a key

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedDevicePublicKeyList = apiInstance.devicesKeypairsList(deviceId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesKeypairsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesKeypairsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedDevicePublicKeyList**](PaginatedDevicePublicKeyList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="devicesKeypairsRetrieve"></a>
# **devicesKeypairsRetrieve**
> DevicePublicKey devicesKeypairsRetrieve(deviceId, id)



Public key for Print Nanny Device Only one public key may be active at a time DELETE &lt;:endpoint&gt; will soft-delete a key

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device public key.
try {
    val result : DevicePublicKey = apiInstance.devicesKeypairsRetrieve(deviceId, id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesKeypairsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesKeypairsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this device public key. |

### Return type

[**DevicePublicKey**](DevicePublicKey.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="devicesList"></a>
# **devicesList**
> PaginatedDeviceList devicesList(page)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedDeviceList = apiInstance.devicesList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedDeviceList**](PaginatedDeviceList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="devicesPartialUpdate"></a>
# **devicesPartialUpdate**
> Device devicesPartialUpdate(id, patchedDeviceRequest)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device.
val patchedDeviceRequest : PatchedDeviceRequest =  // PatchedDeviceRequest | 
try {
    val result : Device = apiInstance.devicesPartialUpdate(id, patchedDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this device. |
 **patchedDeviceRequest** | [**PatchedDeviceRequest**](PatchedDeviceRequest.md)|  | [optional]

### Return type

[**Device**](Device.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="devicesPrinterControllersCreate"></a>
# **devicesPrinterControllersCreate**
> PrinterController devicesPrinterControllersCreate(deviceId, deviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val deviceRequest : DeviceRequest =  // DeviceRequest | 
try {
    val result : PrinterController = apiInstance.devicesPrinterControllersCreate(deviceId, deviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesPrinterControllersCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesPrinterControllersCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
 **deviceRequest** | [**DeviceRequest**](DeviceRequest.md)|  |

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

<a name="devicesPrinterControllersList"></a>
# **devicesPrinterControllersList**
> PaginatedPrinterControllerList devicesPrinterControllersList(deviceId, page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrinterControllerList = apiInstance.devicesPrinterControllersList(deviceId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesPrinterControllersList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesPrinterControllersList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesPrinterControllersPartialUpdate"></a>
# **devicesPrinterControllersPartialUpdate**
> PrinterController devicesPrinterControllersPartialUpdate(deviceId, id, patchedPrinterControllerRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer controller.
val patchedPrinterControllerRequest : PatchedPrinterControllerRequest =  // PatchedPrinterControllerRequest | 
try {
    val result : PrinterController = apiInstance.devicesPrinterControllersPartialUpdate(deviceId, id, patchedPrinterControllerRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesPrinterControllersPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesPrinterControllersPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesPrinterControllersRetrieve"></a>
# **devicesPrinterControllersRetrieve**
> PrinterController devicesPrinterControllersRetrieve(deviceId, id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer controller.
try {
    val result : PrinterController = apiInstance.devicesPrinterControllersRetrieve(deviceId, id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesPrinterControllersRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesPrinterControllersRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
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

<a name="devicesPrinterControllersUpdate"></a>
# **devicesPrinterControllersUpdate**
> PrinterController devicesPrinterControllersUpdate(deviceId, id, deviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceId : kotlin.Int = 56 // kotlin.Int | 
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer controller.
val deviceRequest : DeviceRequest =  // DeviceRequest | 
try {
    val result : PrinterController = apiInstance.devicesPrinterControllersUpdate(deviceId, id, deviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesPrinterControllersUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesPrinterControllersUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **kotlin.Int**|  |
 **id** | **kotlin.Int**| A unique integer value identifying this printer controller. |
 **deviceRequest** | [**DeviceRequest**](DeviceRequest.md)|  |

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

<a name="devicesRetrieve"></a>
# **devicesRetrieve**
> Device devicesRetrieve(id)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device.
try {
    val result : Device = apiInstance.devicesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this device. |

### Return type

[**Device**](Device.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="devicesRetrieveHostname"></a>
# **devicesRetrieveHostname**
> Device devicesRetrieveHostname(hostname)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val hostname : kotlin.String = hostname_example // kotlin.String | 
try {
    val result : Device = apiInstance.devicesRetrieveHostname(hostname)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesRetrieveHostname")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesRetrieveHostname")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **kotlin.String**|  |

### Return type

[**Device**](Device.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="devicesUpdate"></a>
# **devicesUpdate**
> Device devicesUpdate(id, deviceRequest)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device.
val deviceRequest : DeviceRequest =  // DeviceRequest | 
try {
    val result : Device = apiInstance.devicesUpdate(id, deviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this device. |
 **deviceRequest** | [**DeviceRequest**](DeviceRequest.md)|  |

### Return type

[**Device**](Device.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

