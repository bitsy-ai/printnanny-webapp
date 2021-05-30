# TelemetryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**telemetryList**](TelemetryApi.md#telemetryList) | **GET** /api/telemetry/ | 
[**telemetryOctoprintEventsCreate**](TelemetryApi.md#telemetryOctoprintEventsCreate) | **POST** /api/telemetry/octoprint-events/ | 
[**telemetryOctoprintEventsList**](TelemetryApi.md#telemetryOctoprintEventsList) | **GET** /api/telemetry/octoprint-events/ | 
[**telemetryOctoprintEventsRetrieve**](TelemetryApi.md#telemetryOctoprintEventsRetrieve) | **GET** /api/telemetry/octoprint-events/{id}/ | 
[**telemetryPrintNannyPluginEventsList**](TelemetryApi.md#telemetryPrintNannyPluginEventsList) | **GET** /api/telemetry/print-nanny-plugin-events/ | 
[**telemetryPrintNannyPluginEventsRetrieve**](TelemetryApi.md#telemetryPrintNannyPluginEventsRetrieve) | **GET** /api/telemetry/print-nanny-plugin-events/{id}/ | 
[**telemetryPrintStatusEventsList**](TelemetryApi.md#telemetryPrintStatusEventsList) | **GET** /api/telemetry/print-status-events/ | 
[**telemetryPrintStatusEventsRetrieve**](TelemetryApi.md#telemetryPrintStatusEventsRetrieve) | **GET** /api/telemetry/print-status-events/{id}/ | 
[**telemetryRemoteCommandEventsList**](TelemetryApi.md#telemetryRemoteCommandEventsList) | **GET** /api/telemetry/remote-command-events/ | 
[**telemetryRemoteCommandEventsRetrieve**](TelemetryApi.md#telemetryRemoteCommandEventsRetrieve) | **GET** /api/telemetry/remote-command-events/{id}/ | 
[**telemetryRetrieve**](TelemetryApi.md#telemetryRetrieve) | **GET** /api/telemetry/{id}/ | 


<a name="telemetryList"></a>
# **telemetryList**
> PaginatedTelemetryEventPolymorphicList telemetryList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedTelemetryEventPolymorphicList = apiInstance.telemetryList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryList")
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

<a name="telemetryPrintNannyPluginEventsList"></a>
# **telemetryPrintNannyPluginEventsList**
> PaginatedPrintNannyPluginEventList telemetryPrintNannyPluginEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrintNannyPluginEventList = apiInstance.telemetryPrintNannyPluginEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryPrintNannyPluginEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryPrintNannyPluginEventsList")
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

<a name="telemetryPrintNannyPluginEventsRetrieve"></a>
# **telemetryPrintNannyPluginEventsRetrieve**
> PrintNannyPluginEvent telemetryPrintNannyPluginEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this print nanny plugin event.
try {
    val result : PrintNannyPluginEvent = apiInstance.telemetryPrintNannyPluginEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryPrintNannyPluginEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryPrintNannyPluginEventsRetrieve")
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

<a name="telemetryRemoteCommandEventsList"></a>
# **telemetryRemoteCommandEventsList**
> PaginatedRemoteCommandEventList telemetryRemoteCommandEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedRemoteCommandEventList = apiInstance.telemetryRemoteCommandEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryRemoteCommandEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryRemoteCommandEventsList")
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

<a name="telemetryRemoteCommandEventsRetrieve"></a>
# **telemetryRemoteCommandEventsRetrieve**
> RemoteCommandEvent telemetryRemoteCommandEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this remote command event.
try {
    val result : RemoteCommandEvent = apiInstance.telemetryRemoteCommandEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryRemoteCommandEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryRemoteCommandEventsRetrieve")
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

<a name="telemetryRetrieve"></a>
# **telemetryRetrieve**
> TelemetryEventPolymorphic telemetryRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this telemetry event.
try {
    val result : TelemetryEventPolymorphic = apiInstance.telemetryRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryRetrieve")
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

