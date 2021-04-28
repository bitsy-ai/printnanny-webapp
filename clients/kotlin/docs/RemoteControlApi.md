# RemoteControlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commandsList**](RemoteControlApi.md#commandsList) | **GET** /api/commands/ | 
[**commandsPartialUpdate**](RemoteControlApi.md#commandsPartialUpdate) | **PATCH** /api/commands/{id}/ | 
[**commandsRetrieve**](RemoteControlApi.md#commandsRetrieve) | **GET** /api/commands/{id}/ | 
[**commandsUpdate**](RemoteControlApi.md#commandsUpdate) | **PUT** /api/commands/{id}/ | 
[**gcodeFilesCreate**](RemoteControlApi.md#gcodeFilesCreate) | **POST** /api/gcode-files/ | 
[**gcodeFilesList**](RemoteControlApi.md#gcodeFilesList) | **GET** /api/gcode-files/ | 
[**gcodeFilesPartialUpdate**](RemoteControlApi.md#gcodeFilesPartialUpdate) | **PATCH** /api/gcode-files/{id}/ | 
[**gcodeFilesRetrieve**](RemoteControlApi.md#gcodeFilesRetrieve) | **GET** /api/gcode-files/{id}/ | 
[**gcodeFilesUpdate**](RemoteControlApi.md#gcodeFilesUpdate) | **PUT** /api/gcode-files/{id}/ | 
[**gcodeFilesUpdateOrCreate**](RemoteControlApi.md#gcodeFilesUpdateOrCreate) | **POST** /api/gcode-files/update-or-create/ | 
[**octoprintDevicesCreate**](RemoteControlApi.md#octoprintDevicesCreate) | **POST** /api/octoprint-devices/ | 
[**octoprintDevicesList**](RemoteControlApi.md#octoprintDevicesList) | **GET** /api/octoprint-devices/ | 
[**octoprintDevicesPartialUpdate**](RemoteControlApi.md#octoprintDevicesPartialUpdate) | **PATCH** /api/octoprint-devices/{id}/ | 
[**octoprintDevicesRetrieve**](RemoteControlApi.md#octoprintDevicesRetrieve) | **GET** /api/octoprint-devices/{id}/ | 
[**octoprintDevicesUpdate**](RemoteControlApi.md#octoprintDevicesUpdate) | **PUT** /api/octoprint-devices/{id}/ | 
[**octoprintDevicesUpdateOrCreate**](RemoteControlApi.md#octoprintDevicesUpdateOrCreate) | **POST** /api/octoprint-devices/update-or-create/ | 
[**printSessionPartialUpdate**](RemoteControlApi.md#printSessionPartialUpdate) | **PATCH** /api/print-sessions/{session}/ | 
[**printSessionUpdate**](RemoteControlApi.md#printSessionUpdate) | **PUT** /api/print-sessions/{session}/ | 
[**printSessionsCreate**](RemoteControlApi.md#printSessionsCreate) | **POST** /api/print-sessions/ | 
[**printSessionsList**](RemoteControlApi.md#printSessionsList) | **GET** /api/print-sessions/ | 
[**printSessionsRetrieve**](RemoteControlApi.md#printSessionsRetrieve) | **GET** /api/print-sessions/{session}/ | 
[**printerProfilesCreate**](RemoteControlApi.md#printerProfilesCreate) | **POST** /api/printer-profiles/ | 
[**printerProfilesList**](RemoteControlApi.md#printerProfilesList) | **GET** /api/printer-profiles/ | 
[**printerProfilesPartialUpdate**](RemoteControlApi.md#printerProfilesPartialUpdate) | **PATCH** /api/printer-profiles/{id}/ | 
[**printerProfilesRetrieve**](RemoteControlApi.md#printerProfilesRetrieve) | **GET** /api/printer-profiles/{id}/ | 
[**printerProfilesUpdate**](RemoteControlApi.md#printerProfilesUpdate) | **PUT** /api/printer-profiles/{id}/ | 
[**printerProfilesUpdateOrCreate**](RemoteControlApi.md#printerProfilesUpdateOrCreate) | **POST** /api/printer-profiles/update-or-create/ | 
[**validCommandsRetrieve**](RemoteControlApi.md#validCommandsRetrieve) | **GET** /api/commands/valid/ | 


<a name="commandsList"></a>
# **commandsList**
> PaginatedRemoteControlCommandList commandsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedRemoteControlCommandList = apiInstance.commandsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#commandsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#commandsList")
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

<a name="commandsPartialUpdate"></a>
# **commandsPartialUpdate**
> RemoteControlCommand commandsPartialUpdate(id, patchedRemoteControlCommandRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this remote control command.
val patchedRemoteControlCommandRequest : PatchedRemoteControlCommandRequest =  // PatchedRemoteControlCommandRequest | 
try {
    val result : RemoteControlCommand = apiInstance.commandsPartialUpdate(id, patchedRemoteControlCommandRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#commandsPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#commandsPartialUpdate")
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

<a name="commandsRetrieve"></a>
# **commandsRetrieve**
> RemoteControlCommand commandsRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this remote control command.
try {
    val result : RemoteControlCommand = apiInstance.commandsRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#commandsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#commandsRetrieve")
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

<a name="commandsUpdate"></a>
# **commandsUpdate**
> RemoteControlCommand commandsUpdate(id, remoteControlCommandRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this remote control command.
val remoteControlCommandRequest : RemoteControlCommandRequest =  // RemoteControlCommandRequest | 
try {
    val result : RemoteControlCommand = apiInstance.commandsUpdate(id, remoteControlCommandRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#commandsUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#commandsUpdate")
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

<a name="gcodeFilesList"></a>
# **gcodeFilesList**
> PaginatedGcodeFileList gcodeFilesList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedGcodeFileList = apiInstance.gcodeFilesList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#gcodeFilesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#gcodeFilesList")
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

<a name="gcodeFilesPartialUpdate"></a>
# **gcodeFilesPartialUpdate**
> GcodeFile gcodeFilesPartialUpdate(id, name, file, fileHash, octoprintDevice)



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
    val result : GcodeFile = apiInstance.gcodeFilesPartialUpdate(id, name, file, fileHash, octoprintDevice)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#gcodeFilesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#gcodeFilesPartialUpdate")
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

<a name="gcodeFilesRetrieve"></a>
# **gcodeFilesRetrieve**
> GcodeFile gcodeFilesRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.String = id_example // kotlin.String | 
try {
    val result : GcodeFile = apiInstance.gcodeFilesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#gcodeFilesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#gcodeFilesRetrieve")
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

<a name="gcodeFilesUpdate"></a>
# **gcodeFilesUpdate**
> GcodeFile gcodeFilesUpdate(id, name, file, fileHash, octoprintDevice)



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
    val result : GcodeFile = apiInstance.gcodeFilesUpdate(id, name, file, fileHash, octoprintDevice)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#gcodeFilesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#gcodeFilesUpdate")
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

<a name="octoprintDevicesCreate"></a>
# **octoprintDevicesCreate**
> OctoPrintDevice octoprintDevicesCreate(octoPrintDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val octoPrintDeviceRequest : OctoPrintDeviceRequest =  // OctoPrintDeviceRequest | 
try {
    val result : OctoPrintDevice = apiInstance.octoprintDevicesCreate(octoPrintDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#octoprintDevicesCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#octoprintDevicesCreate")
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

<a name="octoprintDevicesList"></a>
# **octoprintDevicesList**
> PaginatedOctoPrintDeviceList octoprintDevicesList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedOctoPrintDeviceList = apiInstance.octoprintDevicesList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#octoprintDevicesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#octoprintDevicesList")
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

<a name="octoprintDevicesPartialUpdate"></a>
# **octoprintDevicesPartialUpdate**
> OctoPrintDevice octoprintDevicesPartialUpdate(id, patchedOctoPrintDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print device.
val patchedOctoPrintDeviceRequest : PatchedOctoPrintDeviceRequest =  // PatchedOctoPrintDeviceRequest | 
try {
    val result : OctoPrintDevice = apiInstance.octoprintDevicesPartialUpdate(id, patchedOctoPrintDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#octoprintDevicesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#octoprintDevicesPartialUpdate")
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

<a name="octoprintDevicesRetrieve"></a>
# **octoprintDevicesRetrieve**
> OctoPrintDevice octoprintDevicesRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print device.
try {
    val result : OctoPrintDevice = apiInstance.octoprintDevicesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#octoprintDevicesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#octoprintDevicesRetrieve")
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

<a name="octoprintDevicesUpdate"></a>
# **octoprintDevicesUpdate**
> OctoPrintDevice octoprintDevicesUpdate(id, octoPrintDeviceRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this octo print device.
val octoPrintDeviceRequest : OctoPrintDeviceRequest =  // OctoPrintDeviceRequest | 
try {
    val result : OctoPrintDevice = apiInstance.octoprintDevicesUpdate(id, octoPrintDeviceRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#octoprintDevicesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#octoprintDevicesUpdate")
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

<a name="printSessionsCreate"></a>
# **printSessionsCreate**
> PrintSession printSessionsCreate(printSessionRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val printSessionRequest : PrintSessionRequest =  // PrintSessionRequest | 
try {
    val result : PrintSession = apiInstance.printSessionsCreate(printSessionRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printSessionsCreate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printSessionsCreate")
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

<a name="printSessionsList"></a>
# **printSessionsList**
> PaginatedPrintSessionList printSessionsList(page)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val page : kotlin.Int = 56 // kotlin.Int | A page number within the paginated result set.
try {
    val result : PaginatedPrintSessionList = apiInstance.printSessionsList(page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printSessionsList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printSessionsList")
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

<a name="printSessionsRetrieve"></a>
# **printSessionsRetrieve**
> PrintSession printSessionsRetrieve(session)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val session : kotlin.String = session_example // kotlin.String | 
try {
    val result : PrintSession = apiInstance.printSessionsRetrieve(session)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printSessionsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printSessionsRetrieve")
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

<a name="printerProfilesList"></a>
# **printerProfilesList**
> PaginatedPrinterProfileList printerProfilesList(name, page, user)



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
    val result : PaginatedPrinterProfileList = apiInstance.printerProfilesList(name, page, user)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printerProfilesList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printerProfilesList")
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

<a name="printerProfilesPartialUpdate"></a>
# **printerProfilesPartialUpdate**
> PrinterProfile printerProfilesPartialUpdate(id, patchedPrinterProfileRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer profile.
val patchedPrinterProfileRequest : PatchedPrinterProfileRequest =  // PatchedPrinterProfileRequest | 
try {
    val result : PrinterProfile = apiInstance.printerProfilesPartialUpdate(id, patchedPrinterProfileRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printerProfilesPartialUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printerProfilesPartialUpdate")
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

<a name="printerProfilesRetrieve"></a>
# **printerProfilesRetrieve**
> PrinterProfile printerProfilesRetrieve(id)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer profile.
try {
    val result : PrinterProfile = apiInstance.printerProfilesRetrieve(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printerProfilesRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printerProfilesRetrieve")
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

<a name="printerProfilesUpdate"></a>
# **printerProfilesUpdate**
> PrinterProfile printerProfilesUpdate(id, printerProfileRequest)



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
val id : kotlin.Int = 56 // kotlin.Int | A unique integer value identifying this printer profile.
val printerProfileRequest : PrinterProfileRequest =  // PrinterProfileRequest | 
try {
    val result : PrinterProfile = apiInstance.printerProfilesUpdate(id, printerProfileRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#printerProfilesUpdate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#printerProfilesUpdate")
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

<a name="validCommandsRetrieve"></a>
# **validCommandsRetrieve**
> kotlin.String validCommandsRetrieve()



### Example
```kotlin
// Import classes:
//import com.print-nanny.client.infrastructure.*
//import com.print-nanny.client.models.*

val apiInstance = RemoteControlApi()
try {
    val result : kotlin.String = apiInstance.validCommandsRetrieve()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RemoteControlApi#validCommandsRetrieve")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RemoteControlApi#validCommandsRetrieve")
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

