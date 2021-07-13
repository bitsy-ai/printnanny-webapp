# ApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiAlertsList**](ApiApi.md#apiAlertsList) | **GET** /api/alerts/ | 
[**apiAlertsPartialUpdate**](ApiApi.md#apiAlertsPartialUpdate) | **PATCH** /api/alerts/{id}/ | 
[**apiAlertsRetrieve**](ApiApi.md#apiAlertsRetrieve) | **GET** /api/alerts/{id}/ | 
[**apiAlertsUpdate**](ApiApi.md#apiAlertsUpdate) | **PUT** /api/alerts/{id}/ | 
[**apiAuthTokenCreate**](ApiApi.md#apiAuthTokenCreate) | **POST** /api/auth-token/ | 
[**apiSchemaRetrieve**](ApiApi.md#apiSchemaRetrieve) | **GET** /api/schema/ | 


<a name="apiAlertsList"></a>
# **apiAlertsList**
> PaginatedAlertList apiAlertsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = ApiApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedAlertList = apiInstance.apiAlertsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ApiApi#apiAlertsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ApiApi#apiAlertsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedAlertList**](PaginatedAlertList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiAlertsPartialUpdate"></a>
# **apiAlertsPartialUpdate**
> Alert apiAlertsPartialUpdate(id, patchedAlertRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = ApiApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert message.
val patchedAlertRequest : PatchedAlertRequest =  // PatchedAlertRequest | 
try {
    val result : Alert = apiInstance.apiAlertsPartialUpdate(id, patchedAlertRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ApiApi#apiAlertsPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ApiApi#apiAlertsPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this alert message. |
 **patchedAlertRequest** | [**PatchedAlertRequest**](PatchedAlertRequest.md)|  | [optional]

### Return type

[**Alert**](Alert.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="apiAlertsRetrieve"></a>
# **apiAlertsRetrieve**
> Alert apiAlertsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = ApiApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert message.
try {
    val result : Alert = apiInstance.apiAlertsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ApiApi#apiAlertsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ApiApi#apiAlertsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this alert message. |

### Return type

[**Alert**](Alert.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiAlertsUpdate"></a>
# **apiAlertsUpdate**
> Alert apiAlertsUpdate(id, alertRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = ApiApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert message.
val alertRequest : AlertRequest =  // AlertRequest | 
try {
    val result : Alert = apiInstance.apiAlertsUpdate(id, alertRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ApiApi#apiAlertsUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ApiApi#apiAlertsUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this alert message. |
 **alertRequest** | [**AlertRequest**](AlertRequest.md)|  |

### Return type

[**Alert**](Alert.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="apiAuthTokenCreate"></a>
# **apiAuthTokenCreate**
> AuthToken apiAuthTokenCreate(username, password)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = ApiApi()
val username : kotlin.String = username_example // kotlin.String | 
val password : kotlin.String = password_example // kotlin.String | 
try {
    val result : AuthToken = apiInstance.apiAuthTokenCreate(username, password)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ApiApi#apiAuthTokenCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ApiApi#apiAuthTokenCreate")
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

<a name="apiSchemaRetrieve"></a>
# **apiSchemaRetrieve**
> kotlin.collections.Map&lt;kotlin.String, AnyType&gt; apiSchemaRetrieve(lang)



OpenApi3 schema for this API. Format can be selected via content negotiation.  - YAML: application/vnd.oai.openapi - JSON: application/vnd.oai.openapi+json

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = ApiApi()
val lang : kotlin.String = lang_example // kotlin.String | 
try {
    val result : kotlin.collections.Map<kotlin.String, AnyType> = apiInstance.apiSchemaRetrieve(lang)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ApiApi#apiSchemaRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ApiApi#apiSchemaRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **kotlin.String**|  | [optional] [enum: af, ar, ar-dz, ast, az, be, bg, bn, br, bs, ca, cs, cy, da, de, dsb, el, en, en-au, en-gb, eo, es, es-ar, es-co, es-mx, es-ni, es-ve, et, eu, fa, fi, fr, fy, ga, gd, gl, he, hi, hr, hsb, hu, hy, ia, id, ig, io, is, it, ja, ka, kab, kk, km, kn, ko, ky, lb, lt, lv, mk, ml, mn, mr, my, nb, ne, nl, nn, os, pa, pl, pt, pt-br, ro, ru, sk, sl, sq, sr, sr-latn, sv, sw, ta, te, tg, th, tk, tr, tt, udm, uk, ur, uz, vi, zh-hans, zh-hant]

### Return type

[**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.oai.openapi+json, application/json

