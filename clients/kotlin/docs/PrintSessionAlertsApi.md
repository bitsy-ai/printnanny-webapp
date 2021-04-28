# PrintSessionAlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**printSessionAlertsList**](PrintSessionAlertsApi.md#printSessionAlertsList) | **GET** /api/print-session-alerts/ | 
[**printSessionAlertsRetrieve**](PrintSessionAlertsApi.md#printSessionAlertsRetrieve) | **GET** /api/print-session-alerts/{id}/ | 


<a name="printSessionAlertsList"></a>
# **printSessionAlertsList**
> PaginatedPrintSessionAlertList printSessionAlertsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = PrintSessionAlertsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrintSessionAlertList = apiInstance.printSessionAlertsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PrintSessionAlertsApi#printSessionAlertsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PrintSessionAlertsApi#printSessionAlertsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedPrintSessionAlertList**](PaginatedPrintSessionAlertList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="printSessionAlertsRetrieve"></a>
# **printSessionAlertsRetrieve**
> PrintSessionAlert printSessionAlertsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = PrintSessionAlertsApi()
val id : kotlin.String = id_example // kotlin.String | 
try {
    val result : PrintSessionAlert = apiInstance.printSessionAlertsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PrintSessionAlertsApi#printSessionAlertsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PrintSessionAlertsApi#printSessionAlertsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.String**|  |

### Return type

[**PrintSessionAlert**](PrintSessionAlert.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

