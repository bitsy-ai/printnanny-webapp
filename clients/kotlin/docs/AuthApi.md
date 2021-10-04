# AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authEmailCreate**](AuthApi.md#authEmailCreate) | **POST** /auth/email/ | 
[**authMobileCreate**](AuthApi.md#authMobileCreate) | **POST** /auth/mobile/ | 
[**authTokenCreate**](AuthApi.md#authTokenCreate) | **POST** /auth/token/ | 
[**authVerifyCreate**](AuthApi.md#authVerifyCreate) | **POST** /auth/verify/ | 
[**authVerifyEmailCreate**](AuthApi.md#authVerifyEmailCreate) | **POST** /auth/verify/email/ | 
[**authVerifyMobileCreate**](AuthApi.md#authVerifyMobileCreate) | **POST** /auth/verify/mobile/ | 


<a name="authEmailCreate"></a>
# **authEmailCreate**
> DetailResponse authEmailCreate(emailAuthRequest)



This returns a 6-digit callback token we can trade for a user&#39;s Auth Token.

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AuthApi()
val emailAuthRequest : EmailAuthRequest =  // EmailAuthRequest | 
try {
    val result : DetailResponse = apiInstance.authEmailCreate(emailAuthRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#authEmailCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#authEmailCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailAuthRequest** | [**EmailAuthRequest**](EmailAuthRequest.md)|  |

### Return type

[**DetailResponse**](DetailResponse.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="authMobileCreate"></a>
# **authMobileCreate**
> DetailResponse authMobileCreate(mobileAuthRequest)



This returns a 6-digit callback token we can trade for a user&#39;s Auth Token.

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AuthApi()
val mobileAuthRequest : MobileAuthRequest =  // MobileAuthRequest | 
try {
    val result : DetailResponse = apiInstance.authMobileCreate(mobileAuthRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#authMobileCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#authMobileCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobileAuthRequest** | [**MobileAuthRequest**](MobileAuthRequest.md)|  |

### Return type

[**DetailResponse**](DetailResponse.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="authTokenCreate"></a>
# **authTokenCreate**
> TokenResponse authTokenCreate(callbackTokenAuthRequest)



This is a duplicate of rest_framework&#39;s own ObtainAuthToken method. Instead, this returns an Auth Token based on our callback token and source.

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AuthApi()
val callbackTokenAuthRequest : CallbackTokenAuthRequest =  // CallbackTokenAuthRequest | 
try {
    val result : TokenResponse = apiInstance.authTokenCreate(callbackTokenAuthRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#authTokenCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#authTokenCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callbackTokenAuthRequest** | [**CallbackTokenAuthRequest**](CallbackTokenAuthRequest.md)|  |

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="authVerifyCreate"></a>
# **authVerifyCreate**
> CallbackTokenVerification authVerifyCreate(callbackTokenVerificationRequest)



This verifies an alias on correct callback token entry using the same logic as auth. Should be refactored at some point.

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AuthApi()
val callbackTokenVerificationRequest : CallbackTokenVerificationRequest =  // CallbackTokenVerificationRequest | 
try {
    val result : CallbackTokenVerification = apiInstance.authVerifyCreate(callbackTokenVerificationRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#authVerifyCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#authVerifyCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callbackTokenVerificationRequest** | [**CallbackTokenVerificationRequest**](CallbackTokenVerificationRequest.md)|  |

### Return type

[**CallbackTokenVerification**](CallbackTokenVerification.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="authVerifyEmailCreate"></a>
# **authVerifyEmailCreate**
> DetailResponse authVerifyEmailCreate()



This returns a 6-digit callback token we can trade for a user&#39;s Auth Token.

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AuthApi()
try {
    val result : DetailResponse = apiInstance.authVerifyEmailCreate()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#authVerifyEmailCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#authVerifyEmailCreate")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DetailResponse**](DetailResponse.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="authVerifyMobileCreate"></a>
# **authVerifyMobileCreate**
> DetailResponse authVerifyMobileCreate()



This returns a 6-digit callback token we can trade for a user&#39;s Auth Token.

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AuthApi()
try {
    val result : DetailResponse = apiInstance.authVerifyMobileCreate()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#authVerifyMobileCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#authVerifyMobileCreate")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DetailResponse**](DetailResponse.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

