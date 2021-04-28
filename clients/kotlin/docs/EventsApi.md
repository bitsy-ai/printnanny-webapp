# EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**octoprintCoreEventsEnumRetrieve**](EventsApi.md#octoprintCoreEventsEnumRetrieve) | **GET** /api/octoprint-events/enum/ | 
[**octoprintEventsCreate**](EventsApi.md#octoprintEventsCreate) | **POST** /api/octoprint-events/ | 
[**octoprintEventsList**](EventsApi.md#octoprintEventsList) | **GET** /api/octoprint-events/ | 
[**octoprintEventsRetrieve**](EventsApi.md#octoprintEventsRetrieve) | **GET** /api/octoprint-events/{id}/ | 
[**pluginEventsEnumRetrieve**](EventsApi.md#pluginEventsEnumRetrieve) | **GET** /api/plugin-events/enum/ | 
[**pluginEventsList**](EventsApi.md#pluginEventsList) | **GET** /api/plugin-events/ | 
[**pluginEventsRetrieve**](EventsApi.md#pluginEventsRetrieve) | **GET** /api/plugin-events/{id}/ | 
[**printJobStatesList**](EventsApi.md#printJobStatesList) | **GET** /api/print-job-states/ | 
[**printJobStatesRetrieve**](EventsApi.md#printJobStatesRetrieve) | **GET** /api/print-job-states/{id}/ | 
[**printSessionEventEnumRetrieve**](EventsApi.md#printSessionEventEnumRetrieve) | **GET** /api/print-job-states/enum/ | 


<a name="octoprintCoreEventsEnumRetrieve"></a>
# **octoprintCoreEventsEnumRetrieve**
> kotlin.String octoprintCoreEventsEnumRetrieve()



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = EventsApi()
try {
    val result : kotlin.String = apiInstance.octoprintCoreEventsEnumRetrieve()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EventsApi#octoprintCoreEventsEnumRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EventsApi#octoprintCoreEventsEnumRetrieve")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.String**

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="octoprintEventsCreate"></a>
# **octoprintEventsCreate**
> OctoPrintEvent octoprintEventsCreate(octoPrintEventRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = EventsApi()
val octoPrintEventRequest : OctoPrintEventRequest =  // OctoPrintEventRequest | 
try {
    val result : OctoPrintEvent = apiInstance.octoprintEventsCreate(octoPrintEventRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EventsApi#octoprintEventsCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EventsApi#octoprintEventsCreate")
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

val apiInstance = EventsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedOctoPrintEventList = apiInstance.octoprintEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EventsApi#octoprintEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EventsApi#octoprintEventsList")
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

val apiInstance = EventsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print event.
try {
    val result : OctoPrintEvent = apiInstance.octoprintEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EventsApi#octoprintEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EventsApi#octoprintEventsRetrieve")
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

<a name="pluginEventsEnumRetrieve"></a>
# **pluginEventsEnumRetrieve**
> kotlin.String pluginEventsEnumRetrieve()



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = EventsApi()
try {
    val result : kotlin.String = apiInstance.pluginEventsEnumRetrieve()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EventsApi#pluginEventsEnumRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EventsApi#pluginEventsEnumRetrieve")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.String**

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="pluginEventsList"></a>
# **pluginEventsList**
> PaginatedPluginEventList pluginEventsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = EventsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPluginEventList = apiInstance.pluginEventsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EventsApi#pluginEventsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EventsApi#pluginEventsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedPluginEventList**](PaginatedPluginEventList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="pluginEventsRetrieve"></a>
# **pluginEventsRetrieve**
> PluginEvent pluginEventsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = EventsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this plugin event.
try {
    val result : PluginEvent = apiInstance.pluginEventsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EventsApi#pluginEventsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EventsApi#pluginEventsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this plugin event. |

### Return type

[**PluginEvent**](PluginEvent.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="printJobStatesList"></a>
# **printJobStatesList**
> PaginatedPrintSessionStateList printJobStatesList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = EventsApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrintSessionStateList = apiInstance.printJobStatesList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EventsApi#printJobStatesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EventsApi#printJobStatesList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedPrintSessionStateList**](PaginatedPrintSessionStateList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="printJobStatesRetrieve"></a>
# **printJobStatesRetrieve**
> PrintSessionState printJobStatesRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = EventsApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this print session state.
try {
    val result : PrintSessionState = apiInstance.printJobStatesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EventsApi#printJobStatesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EventsApi#printJobStatesRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this print session state. |

### Return type

[**PrintSessionState**](PrintSessionState.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="printSessionEventEnumRetrieve"></a>
# **printSessionEventEnumRetrieve**
> kotlin.String printSessionEventEnumRetrieve()



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = EventsApi()
try {
    val result : kotlin.String = apiInstance.printSessionEventEnumRetrieve()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EventsApi#printSessionEventEnumRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EventsApi#printSessionEventEnumRetrieve")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.String**

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

