# TelemetryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiOctoprintEventsCreate**](TelemetryApi.md#apiOctoprintEventsCreate) | **POST** /api/octoprint-events/ | 
[**apiOctoprintEventsList**](TelemetryApi.md#apiOctoprintEventsList) | **GET** /api/octoprint-events/ | 
[**apiOctoprintEventsRetrieve**](TelemetryApi.md#apiOctoprintEventsRetrieve) | **GET** /api/octoprint-events/{id}/ | 
[**apiPrintJobEventsList**](TelemetryApi.md#apiPrintJobEventsList) | **GET** /api/print-job-events/ | 
[**apiPrintJobEventsRetrieve**](TelemetryApi.md#apiPrintJobEventsRetrieve) | **GET** /api/print-job-events/{id}/ | 
[**apiPrintNannyPluginEventsList**](TelemetryApi.md#apiPrintNannyPluginEventsList) | **GET** /api/print-nanny-plugin-events/ | 
[**apiPrintNannyPluginEventsRetrieve**](TelemetryApi.md#apiPrintNannyPluginEventsRetrieve) | **GET** /api/print-nanny-plugin-events/{id}/ | 
[**apiRemoteCommandEventsList**](TelemetryApi.md#apiRemoteCommandEventsList) | **GET** /api/remote-command-events/ | 
[**apiRemoteCommandEventsRetrieve**](TelemetryApi.md#apiRemoteCommandEventsRetrieve) | **GET** /api/remote-command-events/{id}/ | 
[**apiTelemetryEventsList**](TelemetryApi.md#apiTelemetryEventsList) | **GET** /api/telemetry-events/ | 
[**apiTelemetryEventsRetrieve**](TelemetryApi.md#apiTelemetryEventsRetrieve) | **GET** /api/telemetry-events/{id}/ | 


<a name="apiOctoprintEventsCreate"></a>
# **apiOctoprintEventsCreate**
> OctoPrintEvent apiOctoprintEventsCreate(octoPrintEventRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val octoPrintEventRequest : OctoPrintEventRequest =  // OctoPrintEventRequest | 
try {
    val result : OctoPrintEvent = apiInstance.apiOctoprintEventsCreate(octoPrintEventRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiOctoprintEventsCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiOctoprintEventsCreate")
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

<a name="apiOctoprintEventsList"></a>
# **apiOctoprintEventsList**
> PaginatedOctoPrintEventList apiOctoprintEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedOctoPrintEventList = apiInstance.apiOctoprintEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiOctoprintEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiOctoprintEventsList")
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

<a name="apiOctoprintEventsRetrieve"></a>
# **apiOctoprintEventsRetrieve**
> OctoPrintEvent apiOctoprintEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print event.
try {
    val result : OctoPrintEvent = apiInstance.apiOctoprintEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiOctoprintEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiOctoprintEventsRetrieve")
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

<a name="apiPrintJobEventsList"></a>
# **apiPrintJobEventsList**
> PaginatedPrintJobEventList apiPrintJobEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrintJobEventList = apiInstance.apiPrintJobEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiPrintJobEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiPrintJobEventsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedPrintJobEventList**](PaginatedPrintJobEventList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiPrintJobEventsRetrieve"></a>
# **apiPrintJobEventsRetrieve**
> PrintJobEvent apiPrintJobEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this print job event.
try {
    val result : PrintJobEvent = apiInstance.apiPrintJobEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiPrintJobEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiPrintJobEventsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this print job event. |

### Return type

[**PrintJobEvent**](PrintJobEvent.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiPrintNannyPluginEventsList"></a>
# **apiPrintNannyPluginEventsList**
> PaginatedPrintNannyPluginEventList apiPrintNannyPluginEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrintNannyPluginEventList = apiInstance.apiPrintNannyPluginEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiPrintNannyPluginEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiPrintNannyPluginEventsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedPrintNannyPluginEventList**](PaginatedPrintNannyPluginEventList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiPrintNannyPluginEventsRetrieve"></a>
# **apiPrintNannyPluginEventsRetrieve**
> PrintNannyPluginEvent apiPrintNannyPluginEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this print nanny plugin event.
try {
    val result : PrintNannyPluginEvent = apiInstance.apiPrintNannyPluginEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiPrintNannyPluginEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiPrintNannyPluginEventsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this print nanny plugin event. |

### Return type

[**PrintNannyPluginEvent**](PrintNannyPluginEvent.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiRemoteCommandEventsList"></a>
# **apiRemoteCommandEventsList**
> PaginatedRemoteCommandEventList apiRemoteCommandEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedRemoteCommandEventList = apiInstance.apiRemoteCommandEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiRemoteCommandEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiRemoteCommandEventsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedRemoteCommandEventList**](PaginatedRemoteCommandEventList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiRemoteCommandEventsRetrieve"></a>
# **apiRemoteCommandEventsRetrieve**
> RemoteCommandEvent apiRemoteCommandEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this remote command event.
try {
    val result : RemoteCommandEvent = apiInstance.apiRemoteCommandEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiRemoteCommandEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiRemoteCommandEventsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this remote command event. |

### Return type

[**RemoteCommandEvent**](RemoteCommandEvent.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiTelemetryEventsList"></a>
# **apiTelemetryEventsList**
> PaginatedTelemetryEventPolymorphicList apiTelemetryEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedTelemetryEventPolymorphicList = apiInstance.apiTelemetryEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiTelemetryEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiTelemetryEventsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedTelemetryEventPolymorphicList**](PaginatedTelemetryEventPolymorphicList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiTelemetryEventsRetrieve"></a>
# **apiTelemetryEventsRetrieve**
> TelemetryEventPolymorphic apiTelemetryEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this telemetry event.
try {
    val result : TelemetryEventPolymorphic = apiInstance.apiTelemetryEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#apiTelemetryEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#apiTelemetryEventsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this telemetry event. |

### Return type

[**TelemetryEventPolymorphic**](TelemetryEventPolymorphic.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

