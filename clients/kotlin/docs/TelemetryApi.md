# TelemetryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**telemetryOctoprintEventsCreate**](TelemetryApi.md#telemetryOctoprintEventsCreate) | **POST** /api/telemetry/octoprint-events/ | 
[**telemetryOctoprintEventsList**](TelemetryApi.md#telemetryOctoprintEventsList) | **GET** /api/telemetry/octoprint-events/ | 
[**telemetryOctoprintEventsRetrieve**](TelemetryApi.md#telemetryOctoprintEventsRetrieve) | **GET** /api/telemetry/octoprint-events/{id}/ | 
[**telemetryOctoprintPluginEventsList**](TelemetryApi.md#telemetryOctoprintPluginEventsList) | **GET** /api/telemetry/octoprint-plugin-events/ | 
[**telemetryOctoprintPluginEventsRetrieve**](TelemetryApi.md#telemetryOctoprintPluginEventsRetrieve) | **GET** /api/telemetry/octoprint-plugin-events/{id}/ | 
[**telemetryPrintStatusEventsList**](TelemetryApi.md#telemetryPrintStatusEventsList) | **GET** /api/telemetry/print-status-events/ | 
[**telemetryPrintStatusEventsRetrieve**](TelemetryApi.md#telemetryPrintStatusEventsRetrieve) | **GET** /api/telemetry/print-status-events/{id}/ | 


<a name="telemetryOctoprintEventsCreate"></a>
# **telemetryOctoprintEventsCreate**
> OctoPrintEvent telemetryOctoprintEventsCreate(octoPrintEventRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val octoPrintEventRequest : OctoPrintEventRequest =  // OctoPrintEventRequest | 
try {
    val result : OctoPrintEvent = apiInstance.telemetryOctoprintEventsCreate(octoPrintEventRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryOctoprintEventsCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryOctoprintEventsCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **octoPrintEventRequest** | [**OctoPrintEventRequest**](OctoPrintEventRequest.md)|  |

### Return type

[**OctoPrintEvent**](OctoPrintEvent.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="telemetryOctoprintEventsList"></a>
# **telemetryOctoprintEventsList**
> PaginatedOctoPrintEventList telemetryOctoprintEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedOctoPrintEventList = apiInstance.telemetryOctoprintEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryOctoprintEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryOctoprintEventsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedOctoPrintEventList**](PaginatedOctoPrintEventList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="telemetryOctoprintEventsRetrieve"></a>
# **telemetryOctoprintEventsRetrieve**
> OctoPrintEvent telemetryOctoprintEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print event.
try {
    val result : OctoPrintEvent = apiInstance.telemetryOctoprintEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryOctoprintEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryOctoprintEventsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this octo print event. |

### Return type

[**OctoPrintEvent**](OctoPrintEvent.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="telemetryOctoprintPluginEventsList"></a>
# **telemetryOctoprintPluginEventsList**
> PaginatedOctoPrintPluginEventList telemetryOctoprintPluginEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedOctoPrintPluginEventList = apiInstance.telemetryOctoprintPluginEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryOctoprintPluginEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryOctoprintPluginEventsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedOctoPrintPluginEventList**](PaginatedOctoPrintPluginEventList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="telemetryOctoprintPluginEventsRetrieve"></a>
# **telemetryOctoprintPluginEventsRetrieve**
> OctoPrintPluginEvent telemetryOctoprintPluginEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print plugin event.
try {
    val result : OctoPrintPluginEvent = apiInstance.telemetryOctoprintPluginEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryOctoprintPluginEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryOctoprintPluginEventsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this octo print plugin event. |

### Return type

[**OctoPrintPluginEvent**](OctoPrintPluginEvent.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="telemetryPrintStatusEventsList"></a>
# **telemetryPrintStatusEventsList**
> PaginatedPrintStatusEventList telemetryPrintStatusEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrintStatusEventList = apiInstance.telemetryPrintStatusEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryPrintStatusEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryPrintStatusEventsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedPrintStatusEventList**](PaginatedPrintStatusEventList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="telemetryPrintStatusEventsRetrieve"></a>
# **telemetryPrintStatusEventsRetrieve**
> PrintStatusEvent telemetryPrintStatusEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this print status event.
try {
    val result : PrintStatusEvent = apiInstance.telemetryPrintStatusEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryPrintStatusEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryPrintStatusEventsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this print status event. |

### Return type

[**PrintStatusEvent**](PrintStatusEvent.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

