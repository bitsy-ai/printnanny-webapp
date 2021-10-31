# ReleasesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**releasesLatestRetrieve**](ReleasesApi.md#releasesLatestRetrieve) | **GET** /api/releases/{release_channel}/latest/ | 
[**releasesList**](ReleasesApi.md#releasesList) | **GET** /api/releases/ | 
[**releasesRetrieve**](ReleasesApi.md#releasesRetrieve) | **GET** /api/releases/{id}/ | 


<a name="releasesLatestRetrieve"></a>
# **releasesLatestRetrieve**
> Release releasesLatestRetrieve(releaseChannel)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = ReleasesApi()
val releaseChannel : kotlin.String = releaseChannel_example // kotlin.String | 
try {
    val result : Release = apiInstance.releasesLatestRetrieve(releaseChannel)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ReleasesApi#releasesLatestRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ReleasesApi#releasesLatestRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **releaseChannel** | **kotlin.String**|  |

### Return type

[**Release**](Release.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="releasesList"></a>
# **releasesList**
> PaginatedReleaseList releasesList(page)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = ReleasesApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedReleaseList = apiInstance.releasesList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ReleasesApi#releasesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ReleasesApi#releasesList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedReleaseList**](PaginatedReleaseList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="releasesRetrieve"></a>
# **releasesRetrieve**
> Release releasesRetrieve(id)



All-in-one Print Nanny installation via print-nanny-main-&lt;platform&gt;-&lt;cpu&gt;.img

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = ReleasesApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this release.
try {
    val result : Release = apiInstance.releasesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ReleasesApi#releasesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ReleasesApi#releasesRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this release. |

### Return type

[**Release**](Release.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

