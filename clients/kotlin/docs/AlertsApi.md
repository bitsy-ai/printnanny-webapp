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


<a name="alertsList"></a>
# **alertsList**
> PaginatedAlertList alertsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AlertsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedAlertList = apiInstance.alertsList(page)
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

<a name="alertsPartialUpdate"></a>
# **alertsPartialUpdate**
> Alert alertsPartialUpdate(id, patchedAlertRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AlertsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert.
val patchedAlertRequest : PatchedAlertRequest =  // PatchedAlertRequest | 
try {
    val result : Alert = apiInstance.alertsPartialUpdate(id, patchedAlertRequest)
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

<a name="alertsRetrieve"></a>
# **alertsRetrieve**
> Alert alertsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AlertsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert.
try {
    val result : Alert = apiInstance.alertsRetrieve(id)
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

<a name="alertsUpdate"></a>
# **alertsUpdate**
> Alert alertsUpdate(id, alertRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AlertsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert.
val alertRequest : AlertRequest =  // AlertRequest | 
try {
    val result : Alert = apiInstance.alertsUpdate(id, alertRequest)
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

