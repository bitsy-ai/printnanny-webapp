# Class3dgeeksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geeks3dMetadataRetrieve**](Class3dgeeksApi.md#geeks3dMetadataRetrieve) | **GET** /api/partners/3d-geeks/{id}/ | 


<a name="geeks3dMetadataRetrieve"></a>
# **geeks3dMetadataRetrieve**
> GeeksMetadata geeks3dMetadataRetrieve(id)



3D Geeks calls this endpoint to validate token &amp; fetch printer metadata

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = Class3dgeeksApi()
val id : kotlin.String = id_example // kotlin.String | 
try {
    val result : GeeksMetadata = apiInstance.geeks3dMetadataRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling Class3dgeeksApi#geeks3dMetadataRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling Class3dgeeksApi#geeks3dMetadataRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.String**|  |

### Return type

[**GeeksMetadata**](GeeksMetadata.md)

### Authorization


Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

