# PartnersGeeks3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertsList**](PartnersGeeks3Api.md#alertsList) | **GET** /api/partners/3d-geeks/{id}/alerts/ | 


<a name="alertsList"></a>
# **alertsList**
> Partner3DGeeksAlert alertsList(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = PartnersGeeks3Api()
val id : kotlin.String = id_example // kotlin.String | 
try {
    val result : Partner3DGeeksAlert = apiInstance.alertsList(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PartnersGeeks3Api#alertsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PartnersGeeks3Api#alertsList")
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

