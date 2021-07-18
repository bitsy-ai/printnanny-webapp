# DevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicesCreate**](DevicesApi.md#devicesCreate) | **POST** /api/devices/ | 
[**devicesList**](DevicesApi.md#devicesList) | **GET** /api/devices/ | 
[**devicesPartialUpdate**](DevicesApi.md#devicesPartialUpdate) | **PATCH** /api/devices/{id}/ | 
[**devicesRetrieve**](DevicesApi.md#devicesRetrieve) | **GET** /api/devices/{id}/ | 
[**devicesUpdate**](DevicesApi.md#devicesUpdate) | **PUT** /api/devices/{id}/ | 
[**devicesUpdateOrCreate**](DevicesApi.md#devicesUpdateOrCreate) | **POST** /api/devices/update-or-create/ | 


<a name="devicesCreate"></a>
# **devicesCreate**
> Device devicesCreate(deviceRequest)



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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="devicesList"></a>
# **devicesList**
> PaginatedDeviceList devicesList(page)



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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="devicesPartialUpdate"></a>
# **devicesPartialUpdate**
> Device devicesPartialUpdate(id, patchedDeviceRequest)



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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="devicesRetrieve"></a>
# **devicesRetrieve**
> Device devicesRetrieve(id)



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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="devicesUpdate"></a>
# **devicesUpdate**
> Device devicesUpdate(id, deviceRequest)



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
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="devicesUpdateOrCreate"></a>
# **devicesUpdateOrCreate**
> DeviceIdentity devicesUpdateOrCreate(deviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceRequest : DeviceRequest =  // DeviceRequest | 
try {
    val result : DeviceIdentity = apiInstance.devicesUpdateOrCreate(deviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#devicesUpdateOrCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#devicesUpdateOrCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceRequest** | [**DeviceRequest**](DeviceRequest.md)|  |

### Return type

[**DeviceIdentity**](DeviceIdentity.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

