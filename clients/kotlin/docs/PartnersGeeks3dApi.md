# PartnersGeeks3dApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadataRetrieve**](PartnersGeeks3dApi.md#metadataRetrieve) | **GET** /api/partners/3d-geeks/{id}/ | 


<a name="metadataRetrieve"></a>
# **metadataRetrieve**
> PartnerOctoPrintDevice metadataRetrieve(id)



3D Geeks calls this endpoint to validate token &amp; fetch printer metadata

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = PartnersGeeks3dApi()
val id : kotlin.String = id_example // kotlin.String | 
try {
    val result : PartnerOctoPrintDevice = apiInstance.metadataRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PartnersGeeks3dApi#metadataRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PartnersGeeks3dApi#metadataRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.String**|  |

### Return type

[**PartnerOctoPrintDevice**](PartnerOctoPrintDevice.md)

### Authorization


Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

