# AppliancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appliancesCreate**](AppliancesApi.md#appliancesCreate) | **POST** /api/appliances/ | 
[**appliancesList**](AppliancesApi.md#appliancesList) | **GET** /api/appliances/ | 
[**appliancesPartialUpdate**](AppliancesApi.md#appliancesPartialUpdate) | **PATCH** /api/appliances/{id}/ | 
[**appliancesRetrieve**](AppliancesApi.md#appliancesRetrieve) | **GET** /api/appliances/{id}/ | 
[**appliancesUpdate**](AppliancesApi.md#appliancesUpdate) | **PUT** /api/appliances/{id}/ | 


<a name="appliancesCreate"></a>
# **appliancesCreate**
> Appliance appliancesCreate(createApplianceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val createApplianceRequest : CreateApplianceRequest =  // CreateApplianceRequest | 
try {
    val result : Appliance = apiInstance.appliancesCreate(createApplianceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createApplianceRequest** | [**CreateApplianceRequest**](CreateApplianceRequest.md)|  |

### Return type

[**Appliance**](Appliance.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesList"></a>
# **appliancesList**
> PaginatedApplianceList appliancesList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedApplianceList = apiInstance.appliancesList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedApplianceList**](PaginatedApplianceList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesPartialUpdate"></a>
# **appliancesPartialUpdate**
> Appliance appliancesPartialUpdate(id, patchedApplianceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this appliance.
val patchedApplianceRequest : PatchedApplianceRequest =  // PatchedApplianceRequest | 
try {
    val result : Appliance = apiInstance.appliancesPartialUpdate(id, patchedApplianceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this appliance. |
 **patchedApplianceRequest** | [**PatchedApplianceRequest**](PatchedApplianceRequest.md)|  | [optional]

### Return type

[**Appliance**](Appliance.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="appliancesRetrieve"></a>
# **appliancesRetrieve**
> Appliance appliancesRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this appliance.
try {
    val result : Appliance = apiInstance.appliancesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this appliance. |

### Return type

[**Appliance**](Appliance.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="appliancesUpdate"></a>
# **appliancesUpdate**
> Appliance appliancesUpdate(id, applianceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = AppliancesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this appliance.
val applianceRequest : ApplianceRequest =  // ApplianceRequest | 
try {
    val result : Appliance = apiInstance.appliancesUpdate(id, applianceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AppliancesApi#appliancesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AppliancesApi#appliancesUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this appliance. |
 **applianceRequest** | [**ApplianceRequest**](ApplianceRequest.md)|  |

### Return type

[**Appliance**](Appliance.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

