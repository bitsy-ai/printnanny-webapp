# AppliancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicesRetrieveHostname**](AppliancesApi.md#devicesRetrieveHostname) | **GET** /api/appliances/{hostname} | 


<a name="devicesRetrieveHostname"></a>
# **devicesRetrieveHostname**
> Device devicesRetrieveHostname(hostname)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val hostname : kotlin.String = hostname_example // kotlin.String | 
try {
    val result : Device = apiInstance.devicesRetrieveHostname(hostname)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#devicesRetrieveHostname")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#devicesRetrieveHostname")
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

