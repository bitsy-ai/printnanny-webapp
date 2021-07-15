# RemoteControlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCommandsList**](RemoteControlApi.md#apiCommandsList) | **GET** /api/commands/ | 
[**apiCommandsPartialUpdate**](RemoteControlApi.md#apiCommandsPartialUpdate) | **PATCH** /api/commands/{id}/ | 
[**apiCommandsRetrieve**](RemoteControlApi.md#apiCommandsRetrieve) | **GET** /api/commands/{id}/ | 
[**apiCommandsUpdate**](RemoteControlApi.md#apiCommandsUpdate) | **PUT** /api/commands/{id}/ | 
[**apiGcodeFilesList**](RemoteControlApi.md#apiGcodeFilesList) | **GET** /api/gcode-files/ | 
[**apiGcodeFilesPartialUpdate**](RemoteControlApi.md#apiGcodeFilesPartialUpdate) | **PATCH** /api/gcode-files/{id}/ | 
[**apiGcodeFilesRetrieve**](RemoteControlApi.md#apiGcodeFilesRetrieve) | **GET** /api/gcode-files/{id}/ | 
[**apiGcodeFilesUpdate**](RemoteControlApi.md#apiGcodeFilesUpdate) | **PUT** /api/gcode-files/{id}/ | 
[**apiOctoprintDevicesCreate**](RemoteControlApi.md#apiOctoprintDevicesCreate) | **POST** /api/octoprint-devices/ | 
[**apiOctoprintDevicesList**](RemoteControlApi.md#apiOctoprintDevicesList) | **GET** /api/octoprint-devices/ | 
[**apiOctoprintDevicesRetrieve**](RemoteControlApi.md#apiOctoprintDevicesRetrieve) | **GET** /api/octoprint-devices/{id}/ | 
[**apiPrintSessionsCreate**](RemoteControlApi.md#apiPrintSessionsCreate) | **POST** /api/print-sessions/ | 
[**apiPrintSessionsList**](RemoteControlApi.md#apiPrintSessionsList) | **GET** /api/print-sessions/ | 
[**apiPrintSessionsRetrieve**](RemoteControlApi.md#apiPrintSessionsRetrieve) | **GET** /api/print-sessions/{session}/ | 
[**apiPrinterProfilesList**](RemoteControlApi.md#apiPrinterProfilesList) | **GET** /api/printer-profiles/ | 
[**apiPrinterProfilesPartialUpdate**](RemoteControlApi.md#apiPrinterProfilesPartialUpdate) | **PATCH** /api/printer-profiles/{id}/ | 
[**apiPrinterProfilesRetrieve**](RemoteControlApi.md#apiPrinterProfilesRetrieve) | **GET** /api/printer-profiles/{id}/ | 
[**apiPrinterProfilesUpdate**](RemoteControlApi.md#apiPrinterProfilesUpdate) | **PUT** /api/printer-profiles/{id}/ | 
[**gcodeFilesCreate**](RemoteControlApi.md#gcodeFilesCreate) | **POST** /api/gcode-files/ | 
[**gcodeFilesUpdateOrCreate**](RemoteControlApi.md#gcodeFilesUpdateOrCreate) | **POST** /api/gcode-files/update-or-create/ | 
[**octoprintDevicesPartialUpdate2**](RemoteControlApi.md#octoprintDevicesPartialUpdate2) | **PATCH** /api/octoprint-devices/{id}/ | 
[**octoprintDevicesUpdate2**](RemoteControlApi.md#octoprintDevicesUpdate2) | **PUT** /api/octoprint-devices/{id}/ | 
[**octoprintDevicesUpdateOrCreate**](RemoteControlApi.md#octoprintDevicesUpdateOrCreate) | **POST** /api/octoprint-devices/update-or-create/ | 
[**printSessionPartialUpdate**](RemoteControlApi.md#printSessionPartialUpdate) | **PATCH** /api/print-sessions/{session}/ | 
[**printSessionUpdate**](RemoteControlApi.md#printSessionUpdate) | **PUT** /api/print-sessions/{session}/ | 
[**printerProfilesCreate**](RemoteControlApi.md#printerProfilesCreate) | **POST** /api/printer-profiles/ | 
[**printerProfilesUpdateOrCreate**](RemoteControlApi.md#printerProfilesUpdateOrCreate) | **POST** /api/printer-profiles/update-or-create/ | 


<a name="apiCommandsList"></a>
# **apiCommandsList**
> PaginatedRemoteControlCommandList apiCommandsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedRemoteControlCommandList = apiInstance.apiCommandsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiCommandsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiCommandsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedRemoteControlCommandList**](PaginatedRemoteControlCommandList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiCommandsPartialUpdate"></a>
# **apiCommandsPartialUpdate**
> RemoteControlCommand apiCommandsPartialUpdate(id, patchedRemoteControlCommandRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this remote control command.
val patchedRemoteControlCommandRequest : PatchedRemoteControlCommandRequest =  // PatchedRemoteControlCommandRequest | 
try {
    val result : RemoteControlCommand = apiInstance.apiCommandsPartialUpdate(id, patchedRemoteControlCommandRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiCommandsPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiCommandsPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this remote control command. |
 **patchedRemoteControlCommandRequest** | [**PatchedRemoteControlCommandRequest**](PatchedRemoteControlCommandRequest.md)|  | [optional]

### Return type

[**RemoteControlCommand**](RemoteControlCommand.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="apiCommandsRetrieve"></a>
# **apiCommandsRetrieve**
> RemoteControlCommand apiCommandsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this remote control command.
try {
    val result : RemoteControlCommand = apiInstance.apiCommandsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiCommandsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiCommandsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this remote control command. |

### Return type

[**RemoteControlCommand**](RemoteControlCommand.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiCommandsUpdate"></a>
# **apiCommandsUpdate**
> RemoteControlCommand apiCommandsUpdate(id, remoteControlCommandRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this remote control command.
val remoteControlCommandRequest : RemoteControlCommandRequest =  // RemoteControlCommandRequest | 
try {
    val result : RemoteControlCommand = apiInstance.apiCommandsUpdate(id, remoteControlCommandRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiCommandsUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiCommandsUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this remote control command. |
 **remoteControlCommandRequest** | [**RemoteControlCommandRequest**](RemoteControlCommandRequest.md)|  |

### Return type

[**RemoteControlCommand**](RemoteControlCommand.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="apiGcodeFilesList"></a>
# **apiGcodeFilesList**
> PaginatedGcodeFileList apiGcodeFilesList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedGcodeFileList = apiInstance.apiGcodeFilesList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiGcodeFilesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiGcodeFilesList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedGcodeFileList**](PaginatedGcodeFileList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiGcodeFilesPartialUpdate"></a>
# **apiGcodeFilesPartialUpdate**
> GcodeFile apiGcodeFilesPartialUpdate(id, name, file, fileHash, octoprintDevice)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.String = id_example // kotlin.String | 
val name : kotlin.String = name_example // kotlin.String | 
val file : java.io.File = BINARY_DATA_HERE // java.io.File | 
val fileHash : kotlin.String = fileHash_example // kotlin.String | 
val octoprintDevice : kotlin.String = octoprintDevice_example // kotlin.String | 
try {
    val result : GcodeFile = apiInstance.apiGcodeFilesPartialUpdate(id, name, file, fileHash, octoprintDevice)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiGcodeFilesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiGcodeFilesPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.String**|  |
 **name** | **kotlin.String**|  | [optional]
 **file** | **java.io.File**|  | [optional]
 **fileHash** | **kotlin.String**|  | [optional]
 **octoprintDevice** | **kotlin.String**|  | [optional]

### Return type

[**GcodeFile**](GcodeFile.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

<a name="apiGcodeFilesRetrieve"></a>
# **apiGcodeFilesRetrieve**
> GcodeFile apiGcodeFilesRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.String = id_example // kotlin.String | 
try {
    val result : GcodeFile = apiInstance.apiGcodeFilesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiGcodeFilesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiGcodeFilesRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.String**|  |

### Return type

[**GcodeFile**](GcodeFile.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiGcodeFilesUpdate"></a>
# **apiGcodeFilesUpdate**
> GcodeFile apiGcodeFilesUpdate(id, name, file, fileHash, octoprintDevice)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.String = id_example // kotlin.String | 
val name : kotlin.String = name_example // kotlin.String | 
val file : java.io.File = BINARY_DATA_HERE // java.io.File | 
val fileHash : kotlin.String = fileHash_example // kotlin.String | 
val octoprintDevice : kotlin.String = octoprintDevice_example // kotlin.String | 
try {
    val result : GcodeFile = apiInstance.apiGcodeFilesUpdate(id, name, file, fileHash, octoprintDevice)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiGcodeFilesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiGcodeFilesUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.String**|  |
 **name** | **kotlin.String**|  |
 **file** | **java.io.File**|  |
 **fileHash** | **kotlin.String**|  |
 **octoprintDevice** | **kotlin.String**|  |

### Return type

[**GcodeFile**](GcodeFile.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

<a name="apiOctoprintDevicesCreate"></a>
# **apiOctoprintDevicesCreate**
> OctoPrintDevice apiOctoprintDevicesCreate(octoPrintDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val octoPrintDeviceRequest : OctoPrintDeviceRequest =  // OctoPrintDeviceRequest | 
try {
    val result : OctoPrintDevice = apiInstance.apiOctoprintDevicesCreate(octoPrintDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiOctoprintDevicesCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiOctoprintDevicesCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **octoPrintDeviceRequest** | [**OctoPrintDeviceRequest**](OctoPrintDeviceRequest.md)|  |

### Return type

[**OctoPrintDevice**](OctoPrintDevice.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="apiOctoprintDevicesList"></a>
# **apiOctoprintDevicesList**
> PaginatedOctoPrintDeviceList apiOctoprintDevicesList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedOctoPrintDeviceList = apiInstance.apiOctoprintDevicesList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiOctoprintDevicesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiOctoprintDevicesList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedOctoPrintDeviceList**](PaginatedOctoPrintDeviceList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiOctoprintDevicesRetrieve"></a>
# **apiOctoprintDevicesRetrieve**
> OctoPrintDevice apiOctoprintDevicesRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print device.
try {
    val result : OctoPrintDevice = apiInstance.apiOctoprintDevicesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiOctoprintDevicesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiOctoprintDevicesRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this octo print device. |

### Return type

[**OctoPrintDevice**](OctoPrintDevice.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiPrintSessionsCreate"></a>
# **apiPrintSessionsCreate**
> PrintSession apiPrintSessionsCreate(printSessionRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val printSessionRequest : PrintSessionRequest =  // PrintSessionRequest | 
try {
    val result : PrintSession = apiInstance.apiPrintSessionsCreate(printSessionRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiPrintSessionsCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiPrintSessionsCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **printSessionRequest** | [**PrintSessionRequest**](PrintSessionRequest.md)|  |

### Return type

[**PrintSession**](PrintSession.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="apiPrintSessionsList"></a>
# **apiPrintSessionsList**
> PaginatedPrintSessionList apiPrintSessionsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrintSessionList = apiInstance.apiPrintSessionsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiPrintSessionsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiPrintSessionsList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]

### Return type

[**PaginatedPrintSessionList**](PaginatedPrintSessionList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiPrintSessionsRetrieve"></a>
# **apiPrintSessionsRetrieve**
> PrintSession apiPrintSessionsRetrieve(session)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val session : kotlin.String = session_example // kotlin.String | 
try {
    val result : PrintSession = apiInstance.apiPrintSessionsRetrieve(session)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiPrintSessionsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiPrintSessionsRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **kotlin.String**|  |

### Return type

[**PrintSession**](PrintSession.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiPrinterProfilesList"></a>
# **apiPrinterProfilesList**
> PaginatedPrinterProfileList apiPrinterProfilesList(name, page, user)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val name : kotlin.String = name_example // kotlin.String | 
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
val user : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : PaginatedPrinterProfileList = apiInstance.apiPrinterProfilesList(name, page, user)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiPrinterProfilesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiPrinterProfilesList")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **kotlin.String**|  | [optional]
 **page** | **kotlin.Int**| A page number within the paginated result set. | [optional]
 **user** | **kotlin.Int**|  | [optional]

### Return type

[**PaginatedPrinterProfileList**](PaginatedPrinterProfileList.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiPrinterProfilesPartialUpdate"></a>
# **apiPrinterProfilesPartialUpdate**
> PrinterProfile apiPrinterProfilesPartialUpdate(id, patchedPrinterProfileRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer profile.
val patchedPrinterProfileRequest : PatchedPrinterProfileRequest =  // PatchedPrinterProfileRequest | 
try {
    val result : PrinterProfile = apiInstance.apiPrinterProfilesPartialUpdate(id, patchedPrinterProfileRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiPrinterProfilesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiPrinterProfilesPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this printer profile. |
 **patchedPrinterProfileRequest** | [**PatchedPrinterProfileRequest**](PatchedPrinterProfileRequest.md)|  | [optional]

### Return type

[**PrinterProfile**](PrinterProfile.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="apiPrinterProfilesRetrieve"></a>
# **apiPrinterProfilesRetrieve**
> PrinterProfile apiPrinterProfilesRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer profile.
try {
    val result : PrinterProfile = apiInstance.apiPrinterProfilesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiPrinterProfilesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiPrinterProfilesRetrieve")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this printer profile. |

### Return type

[**PrinterProfile**](PrinterProfile.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiPrinterProfilesUpdate"></a>
# **apiPrinterProfilesUpdate**
> PrinterProfile apiPrinterProfilesUpdate(id, printerProfileRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer profile.
val printerProfileRequest : PrinterProfileRequest =  // PrinterProfileRequest | 
try {
    val result : PrinterProfile = apiInstance.apiPrinterProfilesUpdate(id, printerProfileRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#apiPrinterProfilesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#apiPrinterProfilesUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this printer profile. |
 **printerProfileRequest** | [**PrinterProfileRequest**](PrinterProfileRequest.md)|  |

### Return type

[**PrinterProfile**](PrinterProfile.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="gcodeFilesCreate"></a>
# **gcodeFilesCreate**
> GcodeFile gcodeFilesCreate(name, file, fileHash, octoprintDevice)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val name : kotlin.String = name_example // kotlin.String | 
val file : java.io.File = BINARY_DATA_HERE // java.io.File | 
val fileHash : kotlin.String = fileHash_example // kotlin.String | 
val octoprintDevice : kotlin.String = octoprintDevice_example // kotlin.String | 
try {
    val result : GcodeFile = apiInstance.gcodeFilesCreate(name, file, fileHash, octoprintDevice)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#gcodeFilesCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#gcodeFilesCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **kotlin.String**|  |
 **file** | **java.io.File**|  |
 **fileHash** | **kotlin.String**|  |
 **octoprintDevice** | **kotlin.String**|  |

### Return type

[**GcodeFile**](GcodeFile.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

<a name="gcodeFilesUpdateOrCreate"></a>
# **gcodeFilesUpdateOrCreate**
> GcodeFile gcodeFilesUpdateOrCreate(name, file, fileHash, octoprintDevice)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val name : kotlin.String = name_example // kotlin.String | 
val file : java.io.File = BINARY_DATA_HERE // java.io.File | 
val fileHash : kotlin.String = fileHash_example // kotlin.String | 
val octoprintDevice : kotlin.String = octoprintDevice_example // kotlin.String | 
try {
    val result : GcodeFile = apiInstance.gcodeFilesUpdateOrCreate(name, file, fileHash, octoprintDevice)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#gcodeFilesUpdateOrCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#gcodeFilesUpdateOrCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **kotlin.String**|  |
 **file** | **java.io.File**|  |
 **fileHash** | **kotlin.String**|  |
 **octoprintDevice** | **kotlin.String**|  |

### Return type

[**GcodeFile**](GcodeFile.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

<a name="octoprintDevicesPartialUpdate2"></a>
# **octoprintDevicesPartialUpdate2**
> OctoPrintDevice octoprintDevicesPartialUpdate2(id, patchedOctoPrintDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print device.
val patchedOctoPrintDeviceRequest : PatchedOctoPrintDeviceRequest =  // PatchedOctoPrintDeviceRequest | 
try {
    val result : OctoPrintDevice = apiInstance.octoprintDevicesPartialUpdate2(id, patchedOctoPrintDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#octoprintDevicesPartialUpdate2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#octoprintDevicesPartialUpdate2")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this octo print device. |
 **patchedOctoPrintDeviceRequest** | [**PatchedOctoPrintDeviceRequest**](PatchedOctoPrintDeviceRequest.md)|  | [optional]

### Return type

[**OctoPrintDevice**](OctoPrintDevice.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="octoprintDevicesUpdate2"></a>
# **octoprintDevicesUpdate2**
> OctoPrintDevice octoprintDevicesUpdate2(id, octoPrintDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print device.
val octoPrintDeviceRequest : OctoPrintDeviceRequest =  // OctoPrintDeviceRequest | 
try {
    val result : OctoPrintDevice = apiInstance.octoprintDevicesUpdate2(id, octoPrintDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#octoprintDevicesUpdate2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#octoprintDevicesUpdate2")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| A unique integer value identifying this octo print device. |
 **octoPrintDeviceRequest** | [**OctoPrintDeviceRequest**](OctoPrintDeviceRequest.md)|  |

### Return type

[**OctoPrintDevice**](OctoPrintDevice.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="octoprintDevicesUpdateOrCreate"></a>
# **octoprintDevicesUpdateOrCreate**
> OctoPrintDevice octoprintDevicesUpdateOrCreate(octoPrintDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val octoPrintDeviceRequest : OctoPrintDeviceRequest =  // OctoPrintDeviceRequest | 
try {
    val result : OctoPrintDevice = apiInstance.octoprintDevicesUpdateOrCreate(octoPrintDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#octoprintDevicesUpdateOrCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#octoprintDevicesUpdateOrCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **octoPrintDeviceRequest** | [**OctoPrintDeviceRequest**](OctoPrintDeviceRequest.md)|  |

### Return type

[**OctoPrintDevice**](OctoPrintDevice.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="printSessionPartialUpdate"></a>
# **printSessionPartialUpdate**
> PrintSession printSessionPartialUpdate(session, patchedPrintSessionRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val session : kotlin.String = session_example // kotlin.String | 
val patchedPrintSessionRequest : PatchedPrintSessionRequest =  // PatchedPrintSessionRequest | 
try {
    val result : PrintSession = apiInstance.printSessionPartialUpdate(session, patchedPrintSessionRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printSessionPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printSessionPartialUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **kotlin.String**|  |
 **patchedPrintSessionRequest** | [**PatchedPrintSessionRequest**](PatchedPrintSessionRequest.md)|  | [optional]

### Return type

[**PrintSession**](PrintSession.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="printSessionUpdate"></a>
# **printSessionUpdate**
> PrintSession printSessionUpdate(session, printSessionRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val session : kotlin.String = session_example // kotlin.String | 
val printSessionRequest : PrintSessionRequest =  // PrintSessionRequest | 
try {
    val result : PrintSession = apiInstance.printSessionUpdate(session, printSessionRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printSessionUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printSessionUpdate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **kotlin.String**|  |
 **printSessionRequest** | [**PrintSessionRequest**](PrintSessionRequest.md)|  |

### Return type

[**PrintSession**](PrintSession.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="printerProfilesCreate"></a>
# **printerProfilesCreate**
> PrintSession printerProfilesCreate(printerProfileRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val printerProfileRequest : PrinterProfileRequest =  // PrinterProfileRequest | 
try {
    val result : PrintSession = apiInstance.printerProfilesCreate(printerProfileRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printerProfilesCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printerProfilesCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **printerProfileRequest** | [**PrinterProfileRequest**](PrinterProfileRequest.md)|  |

### Return type

[**PrintSession**](PrintSession.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="printerProfilesUpdateOrCreate"></a>
# **printerProfilesUpdateOrCreate**
> PrinterProfile printerProfilesUpdateOrCreate(printerProfileRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val printerProfileRequest : PrinterProfileRequest =  // PrinterProfileRequest | 
try {
    val result : PrinterProfile = apiInstance.printerProfilesUpdateOrCreate(printerProfileRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printerProfilesUpdateOrCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printerProfilesUpdateOrCreate")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **printerProfileRequest** | [**PrinterProfileRequest**](PrinterProfileRequest.md)|  |

### Return type

[**PrinterProfile**](PrinterProfile.md)

### Authorization


Configure cookieAuth:
    ApiClient.apiKey["Session"] = ""
    ApiClient.apiKeyPrefix["Session"] = ""
Configure tokenAuth:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

