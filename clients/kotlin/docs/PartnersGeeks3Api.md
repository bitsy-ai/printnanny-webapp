# PartnersGeeks3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertsList2**](PartnersGeeks3Api.md#alertsList2) | **GET** /api/partners/3d-geeks/{id}/alerts/ | 


<a name="alertsList2"></a>
# **alertsList2**
> Partner3DGeeksAlert alertsList2(id)



3D Geeks calls this endpoint to validate token &amp; fetch printer metadata

### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = PartnersGeeks3Api()
val id : kotlin.String = id_example // kotlin.String | 
try {
    val result : Partner3DGeeksAlert = apiInstance.alertsList2(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PartnersGeeks3Api#alertsList2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PartnersGeeks3Api#alertsList2")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.String**|  |

### Return type

[**Partner3DGeeksAlert**](Partner3DGeeksAlert.md)

### Authorization


Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

