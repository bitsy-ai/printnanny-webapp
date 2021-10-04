# UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersList**](UsersApi.md#usersList) | **GET** /api/users/ | 
[**usersMeRetrieve**](UsersApi.md#usersMeRetrieve) | **GET** /api/users/me/ | 
[**usersPartialUpdate**](UsersApi.md#usersPartialUpdate) | **PATCH** /api/users/{id}/ | 
[**usersRetrieve**](UsersApi.md#usersRetrieve) | **GET** /api/users/{id}/ | 
[**usersUpdate**](UsersApi.md#usersUpdate) | **PUT** /api/users/{id}/ | 


<a name="usersList"></a>
# **usersList**
> PaginatedUserList usersList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = UsersApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedUserList = apiInstance.usersList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UsersApi#usersList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UsersApi#usersList")
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
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="usersMeRetrieve"></a>
# **usersMeRetrieve**
> User usersMeRetrieve()



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = UsersApi()
try {
    val result : User = apiInstance.usersMeRetrieve()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UsersApi#usersMeRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UsersApi#usersMeRetrieve")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="usersPartialUpdate"></a>
# **usersPartialUpdate**
> User usersPartialUpdate(id, patchedUserRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = UsersApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this user.
val patchedUserRequest : PatchedUserRequest =  // PatchedUserRequest | 
try {
    val result : User = apiInstance.usersPartialUpdate(id, patchedUserRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UsersApi#usersPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UsersApi#usersPartialUpdate")
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
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="usersRetrieve"></a>
# **usersRetrieve**
> User usersRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = UsersApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this user.
try {
    val result : User = apiInstance.usersRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UsersApi#usersRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UsersApi#usersRetrieve")
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
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="usersUpdate"></a>
# **usersUpdate**
> User usersUpdate(id, userRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = UsersApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this user.
val userRequest : UserRequest =  // UserRequest | 
try {
    val result : User = apiInstance.usersUpdate(id, userRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UsersApi#usersUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UsersApi#usersUpdate")
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
    ApiClient.apiKey["sessionid"] = ""
    ApiClient.apiKeyPrefix["sessionid"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

