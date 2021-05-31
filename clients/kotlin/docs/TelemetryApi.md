# TelemetryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**octoprintEventsCreate**](TelemetryApi.md#octoprintEventsCreate) | **POST** /api/octoprint-events/ | 
[**octoprintEventsList**](TelemetryApi.md#octoprintEventsList) | **GET** /api/octoprint-events/ | 
[**octoprintEventsRetrieve**](TelemetryApi.md#octoprintEventsRetrieve) | **GET** /api/octoprint-events/{id}/ | 
[**printNannyPluginEventsList**](TelemetryApi.md#printNannyPluginEventsList) | **GET** /api/print-nanny-plugin-events/ | 
[**printNannyPluginEventsRetrieve**](TelemetryApi.md#printNannyPluginEventsRetrieve) | **GET** /api/print-nanny-plugin-events/{id}/ | 
[**printStatusEventsList**](TelemetryApi.md#printStatusEventsList) | **GET** /api/print-status-events/ | 
[**printStatusEventsRetrieve**](TelemetryApi.md#printStatusEventsRetrieve) | **GET** /api/print-status-events/{id}/ | 
[**remoteCommandEventsList**](TelemetryApi.md#remoteCommandEventsList) | **GET** /api/remote-command-events/ | 
[**remoteCommandEventsRetrieve**](TelemetryApi.md#remoteCommandEventsRetrieve) | **GET** /api/remote-command-events/{id}/ | 
[**telemetryEventsList**](TelemetryApi.md#telemetryEventsList) | **GET** /api/telemetry-events/ | 
[**telemetryEventsRetrieve**](TelemetryApi.md#telemetryEventsRetrieve) | **GET** /api/telemetry-events/{id}/ | 


<a name="octoprintEventsCreate"></a>
# **octoprintEventsCreate**
> OctoPrintEvent octoprintEventsCreate(octoPrintEventRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val octoPrintEventRequest : OctoPrintEventRequest =  // OctoPrintEventRequest | 
try {
    val result : OctoPrintEvent = apiInstance.octoprintEventsCreate(octoPrintEventRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#octoprintEventsCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#octoprintEventsCreate")
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

<a name="octoprintEventsList"></a>
# **octoprintEventsList**
> PaginatedOctoPrintEventList octoprintEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedOctoPrintEventList = apiInstance.octoprintEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#octoprintEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#octoprintEventsList")
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

<a name="octoprintEventsRetrieve"></a>
# **octoprintEventsRetrieve**
> OctoPrintEvent octoprintEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print event.
try {
    val result : OctoPrintEvent = apiInstance.octoprintEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#octoprintEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#octoprintEventsRetrieve")
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

<a name="printNannyPluginEventsList"></a>
# **printNannyPluginEventsList**
> PaginatedPrintNannyPluginEventList printNannyPluginEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrintNannyPluginEventList = apiInstance.printNannyPluginEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#printNannyPluginEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#printNannyPluginEventsList")
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

<a name="printNannyPluginEventsRetrieve"></a>
# **printNannyPluginEventsRetrieve**
> PrintNannyPluginEvent printNannyPluginEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this print nanny plugin event.
try {
    val result : PrintNannyPluginEvent = apiInstance.printNannyPluginEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#printNannyPluginEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#printNannyPluginEventsRetrieve")
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

<a name="printStatusEventsList"></a>
# **printStatusEventsList**
> PaginatedPrintStatusEventList printStatusEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrintStatusEventList = apiInstance.printStatusEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#printStatusEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#printStatusEventsList")
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

<a name="printStatusEventsRetrieve"></a>
# **printStatusEventsRetrieve**
> PrintStatusEvent printStatusEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this print status event.
try {
    val result : PrintStatusEvent = apiInstance.printStatusEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#printStatusEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#printStatusEventsRetrieve")
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

<a name="remoteCommandEventsList"></a>
# **remoteCommandEventsList**
> PaginatedRemoteCommandEventList remoteCommandEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedRemoteCommandEventList = apiInstance.remoteCommandEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#remoteCommandEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#remoteCommandEventsList")
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

<a name="remoteCommandEventsRetrieve"></a>
# **remoteCommandEventsRetrieve**
> RemoteCommandEvent remoteCommandEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this remote command event.
try {
    val result : RemoteCommandEvent = apiInstance.remoteCommandEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#remoteCommandEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#remoteCommandEventsRetrieve")
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

<a name="telemetryEventsList"></a>
# **telemetryEventsList**
> PaginatedTelemetryEventPolymorphicList telemetryEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedTelemetryEventPolymorphicList = apiInstance.telemetryEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryEventsList")
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

<a name="telemetryEventsRetrieve"></a>
# **telemetryEventsRetrieve**
> TelemetryEventPolymorphic telemetryEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = TelemetryApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this telemetry event.
try {
    val result : TelemetryEventPolymorphic = apiInstance.telemetryEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TelemetryApi#telemetryEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TelemetryApi#telemetryEventsRetrieve")
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

