# AlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertsRecent**](AlertsApi.md#alertsRecent) | **GET** /api/alerts/recent/ | 
[**alertsSeen**](AlertsApi.md#alertsSeen) | **PATCH** /api/alerts/seen/ | 
[**alertsUnread**](AlertsApi.md#alertsUnread) | **GET** /api/alerts/unread/ | 


<a name="alertsRecent"></a>
# **alertsRecent**
> AlertBulkResponse alertsRecent()



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

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

<a name="alertsSeen"></a>
# **alertsSeen**
> AlertBulkResponse alertsSeen(patchedAlertBulkRequestRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

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
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

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

