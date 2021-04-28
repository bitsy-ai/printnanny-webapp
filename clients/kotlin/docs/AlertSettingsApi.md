# AlertSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertSettingsList**](AlertSettingsApi.md#alertSettingsList) | **GET** /api/alert_settings/ | 
[**alertSettingsMethodsRetrieve**](AlertSettingsApi.md#alertSettingsMethodsRetrieve) | **GET** /api/alert_settings/methods/ | 
[**alertSettingsPartialUpdate**](AlertSettingsApi.md#alertSettingsPartialUpdate) | **PATCH** /api/alert_settings/{id}/ | 
[**alertSettingsRetrieve**](AlertSettingsApi.md#alertSettingsRetrieve) | **GET** /api/alert_settings/{id}/ | 
[**alertSettingsUpdate**](AlertSettingsApi.md#alertSettingsUpdate) | **PUT** /api/alert_settings/{id}/ | 


<a name="alertSettingsList"></a>
# **alertSettingsList**
> PaginatedAlertSettingsPolymorphicList alertSettingsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AlertSettingsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedAlertSettingsPolymorphicList = apiInstance.alertSettingsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertSettingsApi#alertSettingsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertSettingsApi#alertSettingsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedAlertSettingsPolymorphicList**](PaginatedAlertSettingsPolymorphicList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="alertSettingsMethodsRetrieve"></a>
# **alertSettingsMethodsRetrieve**
> AlertMethod alertSettingsMethodsRetrieve()



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AlertSettingsApi()
try {
    val result : AlertMethod = apiInstance.alertSettingsMethodsRetrieve()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertSettingsApi#alertSettingsMethodsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertSettingsApi#alertSettingsMethodsRetrieve")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertMethod**](AlertMethod.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="alertSettingsPartialUpdate"></a>
# **alertSettingsPartialUpdate**
> AlertSettingsPolymorphic alertSettingsPartialUpdate(id, patchedAlertSettingsPolymorphicRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AlertSettingsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert settings.
val patchedAlertSettingsPolymorphicRequest : PatchedAlertSettingsPolymorphicRequest =  // PatchedAlertSettingsPolymorphicRequest | 
try {
    val result : AlertSettingsPolymorphic = apiInstance.alertSettingsPartialUpdate(id, patchedAlertSettingsPolymorphicRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertSettingsApi#alertSettingsPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertSettingsApi#alertSettingsPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this alert settings. |
 **patchedAlertSettingsPolymorphicRequest** | [**PatchedAlertSettingsPolymorphicRequest**](PatchedAlertSettingsPolymorphicRequest.md)|  | [optional]

### Return type

[**AlertSettingsPolymorphic**](AlertSettingsPolymorphic.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="alertSettingsRetrieve"></a>
# **alertSettingsRetrieve**
> AlertSettingsPolymorphic alertSettingsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AlertSettingsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert settings.
try {
    val result : AlertSettingsPolymorphic = apiInstance.alertSettingsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertSettingsApi#alertSettingsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertSettingsApi#alertSettingsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this alert settings. |

### Return type

[**AlertSettingsPolymorphic**](AlertSettingsPolymorphic.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="alertSettingsUpdate"></a>
# **alertSettingsUpdate**
> AlertSettingsPolymorphic alertSettingsUpdate(id, alertSettingsPolymorphicRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AlertSettingsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this alert settings.
val alertSettingsPolymorphicRequest : AlertSettingsPolymorphicRequest =  // AlertSettingsPolymorphicRequest | 
try {
    val result : AlertSettingsPolymorphic = apiInstance.alertSettingsUpdate(id, alertSettingsPolymorphicRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AlertSettingsApi#alertSettingsUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AlertSettingsApi#alertSettingsUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this alert settings. |
 **alertSettingsPolymorphicRequest** | [**AlertSettingsPolymorphicRequest**](AlertSettingsPolymorphicRequest.md)|  | [optional]

### Return type

[**AlertSettingsPolymorphic**](AlertSettingsPolymorphic.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

