# AlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertsList**](AlertsApi.md#alertsList) | **GET** /api/alerts/ | 
[**alertsPartialUpdate**](AlertsApi.md#alertsPartialUpdate) | **PATCH** /api/alerts/{id}/ | 
[**alertsRecent**](AlertsApi.md#alertsRecent) | **GET** /api/alerts/recent/ | 
[**alertsRetrieve**](AlertsApi.md#alertsRetrieve) | **GET** /api/alerts/{id}/ | 
[**alertsSeen**](AlertsApi.md#alertsSeen) | **PATCH** /api/alerts/seen/ | 
[**alertsUnread**](AlertsApi.md#alertsUnread) | **GET** /api/alerts/unread/ | 
[**alertsUpdate**](AlertsApi.md#alertsUpdate) | **PUT** /api/alerts/{id}/ | 
[**printSessionAlertCreate**](AlertsApi.md#printSessionAlertCreate) | **POST** /api/print-session-alerts/ | 


<a name="alertsList"></a>
# **alertsList**
> PaginatedAlertPolymorphicList alertsList(page)



### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = AlertsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedAlertPolymorphicList = apiInstance.alertsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertsApi#alertsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertsApi#alertsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedAlertPolymorphicList**](PaginatedAlertPolymorphicList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="alertsPartialUpdate"></a>
# **alertsPartialUpdate**
> AlertPolymorphic alertsPartialUpdate(id, patchedAlertPolymorphicRequest)



### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = AlertsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert.
val patchedAlertPolymorphicRequest : PatchedAlertPolymorphicRequest =  // PatchedAlertPolymorphicRequest | 
try {
    val result : AlertPolymorphic = apiInstance.alertsPartialUpdate(id, patchedAlertPolymorphicRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertsApi#alertsPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertsApi#alertsPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this alert. |
 **patchedAlertPolymorphicRequest** | [**PatchedAlertPolymorphicRequest**](PatchedAlertPolymorphicRequest.md)|  | [optional]

### Return type

[**AlertPolymorphic**](AlertPolymorphic.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="alertsRecent"></a>
# **alertsRecent**
> AlertBulkResponse alertsRecent()



### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = AlertsApi()
try {
    val result : AlertBulkResponse = apiInstance.alertsRecent()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertsApi#alertsRecent")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertsApi#alertsRecent")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertBulkResponse**](AlertBulkResponse.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="alertsRetrieve"></a>
# **alertsRetrieve**
> AlertPolymorphic alertsRetrieve(id)



### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = AlertsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert.
try {
    val result : AlertPolymorphic = apiInstance.alertsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertsApi#alertsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertsApi#alertsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this alert. |

### Return type

[**AlertPolymorphic**](AlertPolymorphic.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="alertsSeen"></a>
# **alertsSeen**
> AlertBulkResponse alertsSeen(patchedAlertBulkRequestRequest)



### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = AlertsApi()
val patchedAlertBulkRequestRequest : PatchedAlertBulkRequestRequest =  // PatchedAlertBulkRequestRequest | 
try {
    val result : AlertBulkResponse = apiInstance.alertsSeen(patchedAlertBulkRequestRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertsApi#alertsSeen")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertsApi#alertsSeen")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patchedAlertBulkRequestRequest** | [**PatchedAlertBulkRequestRequest**](PatchedAlertBulkRequestRequest.md)|  | [optional]

### Return type

[**AlertBulkResponse**](AlertBulkResponse.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="alertsUnread"></a>
# **alertsUnread**
> AlertBulkResponse alertsUnread()



### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = AlertsApi()
try {
    val result : AlertBulkResponse = apiInstance.alertsUnread()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertsApi#alertsUnread")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertsApi#alertsUnread")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertBulkResponse**](AlertBulkResponse.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="alertsUpdate"></a>
# **alertsUpdate**
> AlertPolymorphic alertsUpdate(id, alertPolymorphicRequest)



### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = AlertsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert.
val alertPolymorphicRequest : AlertPolymorphicRequest =  // AlertPolymorphicRequest | 
try {
    val result : AlertPolymorphic = apiInstance.alertsUpdate(id, alertPolymorphicRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertsApi#alertsUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertsApi#alertsUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this alert. |
 **alertPolymorphicRequest** | [**AlertPolymorphicRequest**](AlertPolymorphicRequest.md)|  | [optional]

### Return type

[**AlertPolymorphic**](AlertPolymorphic.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="printSessionAlertCreate"></a>
# **printSessionAlertCreate**
> PrintSessionAlert printSessionAlertCreate(createPrintSessionAlertRequest)



### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = AlertsApi()
val createPrintSessionAlertRequest : CreatePrintSessionAlertRequest =  // CreatePrintSessionAlertRequest | 
try {
    val result : PrintSessionAlert = apiInstance.printSessionAlertCreate(createPrintSessionAlertRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertsApi#printSessionAlertCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertsApi#printSessionAlertCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createPrintSessionAlertRequest** | [**CreatePrintSessionAlertRequest**](CreatePrintSessionAlertRequest.md)|  |

### Return type

[**PrintSessionAlert**](PrintSessionAlert.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

