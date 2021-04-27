# AuthTokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authTokenCreate**](AuthTokenApi.md#authTokenCreate) | **POST** /api/auth-token/ | 


<a name="authTokenCreate"></a>
# **authTokenCreate**
> AuthToken authTokenCreate(username, password)



### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = AuthTokenApi()
val username : kotlin.String = username_example // kotlin.String | 
val password : kotlin.String = password_example // kotlin.String | 
try {
    val result : AuthToken = apiInstance.authTokenCreate(username, password)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthTokenApi#authTokenCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthTokenApi#authTokenCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **kotlin.String**|  |
 **password** | **kotlin.String**|  |

### Return type

[**AuthToken**](AuthToken.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data, application/json
 - **Accept**: application/json

