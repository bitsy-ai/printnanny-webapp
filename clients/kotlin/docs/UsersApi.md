# UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiUsersList**](UsersApi.md#apiUsersList) | **GET** /api/users/ | 
[**apiUsersMeRetrieve**](UsersApi.md#apiUsersMeRetrieve) | **GET** /api/users/me/ | 
[**apiUsersPartialUpdate**](UsersApi.md#apiUsersPartialUpdate) | **PATCH** /api/users/{id}/ | 
[**apiUsersRetrieve**](UsersApi.md#apiUsersRetrieve) | **GET** /api/users/{id}/ | 
[**apiUsersUpdate**](UsersApi.md#apiUsersUpdate) | **PUT** /api/users/{id}/ | 


<a name="apiUsersList"></a>
# **apiUsersList**
> PaginatedUserList apiUsersList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = UsersApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedUserList = apiInstance.apiUsersList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UsersApi#apiUsersList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UsersApi#apiUsersList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedUserList**](PaginatedUserList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiUsersMeRetrieve"></a>
# **apiUsersMeRetrieve**
> User apiUsersMeRetrieve()



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = UsersApi()
try {
    val result : User = apiInstance.apiUsersMeRetrieve()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UsersApi#apiUsersMeRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UsersApi#apiUsersMeRetrieve")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiUsersPartialUpdate"></a>
# **apiUsersPartialUpdate**
> User apiUsersPartialUpdate(id, patchedUserRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = UsersApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this user.
val patchedUserRequest : PatchedUserRequest =  // PatchedUserRequest | 
try {
    val result : User = apiInstance.apiUsersPartialUpdate(id, patchedUserRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UsersApi#apiUsersPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UsersApi#apiUsersPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this user. |
 **patchedUserRequest** | [**PatchedUserRequest**](PatchedUserRequest.md)|  | [optional]

### Return type

[**User**](User.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="apiUsersRetrieve"></a>
# **apiUsersRetrieve**
> User apiUsersRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = UsersApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this user.
try {
    val result : User = apiInstance.apiUsersRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UsersApi#apiUsersRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UsersApi#apiUsersRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this user. |

### Return type

[**User**](User.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiUsersUpdate"></a>
# **apiUsersUpdate**
> User apiUsersUpdate(id, userRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = UsersApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this user.
val userRequest : UserRequest =  // UserRequest | 
try {
    val result : User = apiInstance.apiUsersUpdate(id, userRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UsersApi#apiUsersUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UsersApi#apiUsersUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this user. |
 **userRequest** | [**UserRequest**](UserRequest.md)|  |

### Return type

[**User**](User.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

