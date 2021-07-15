# DevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiDevicesCreate**](DevicesApi.md#apiDevicesCreate) | **POST** /api/devices/ | 
[**apiDevicesList**](DevicesApi.md#apiDevicesList) | **GET** /api/devices/ | 
[**apiDevicesRetrieve**](DevicesApi.md#apiDevicesRetrieve) | **GET** /api/devices/{id}/ | 
[**devicesUpdateOrCreate**](DevicesApi.md#devicesUpdateOrCreate) | **POST** /api/devices/update-or-create/ | 
[**octoprintDevicesPartialUpdate**](DevicesApi.md#octoprintDevicesPartialUpdate) | **PATCH** /api/devices/{id}/ | 
[**octoprintDevicesUpdate**](DevicesApi.md#octoprintDevicesUpdate) | **PUT** /api/devices/{id}/ | 


<a name="apiDevicesCreate"></a>
# **apiDevicesCreate**
> Device apiDevicesCreate(deviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceRequest : DeviceRequest =  // DeviceRequest | 
try {
    val result : Device = apiInstance.apiDevicesCreate(deviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#apiDevicesCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#apiDevicesCreate")
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

<a name="apiDevicesList"></a>
# **apiDevicesList**
> PaginatedDeviceList apiDevicesList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedDeviceList = apiInstance.apiDevicesList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#apiDevicesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#apiDevicesList")
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

<a name="apiDevicesRetrieve"></a>
# **apiDevicesRetrieve**
> Device apiDevicesRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device.
try {
    val result : Device = apiInstance.apiDevicesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#apiDevicesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#apiDevicesRetrieve")
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

<a name="devicesUpdateOrCreate"></a>
# **devicesUpdateOrCreate**
> Device devicesUpdateOrCreate(deviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val deviceRequest : DeviceRequest =  // DeviceRequest | 
try {
    val result : Device = apiInstance.devicesUpdateOrCreate(deviceRequest)
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

<a name="octoprintDevicesPartialUpdate"></a>
# **octoprintDevicesPartialUpdate**
> Device octoprintDevicesPartialUpdate(id, patchedDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device.
val patchedDeviceRequest : PatchedDeviceRequest =  // PatchedDeviceRequest | 
try {
    val result : Device = apiInstance.octoprintDevicesPartialUpdate(id, patchedDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#octoprintDevicesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#octoprintDevicesPartialUpdate")
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

<a name="octoprintDevicesUpdate"></a>
# **octoprintDevicesUpdate**
> Device octoprintDevicesUpdate(id, deviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = DevicesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this device.
val deviceRequest : DeviceRequest =  // DeviceRequest | 
try {
    val result : Device = apiInstance.octoprintDevicesUpdate(id, deviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DevicesApi#octoprintDevicesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DevicesApi#octoprintDevicesUpdate")
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

