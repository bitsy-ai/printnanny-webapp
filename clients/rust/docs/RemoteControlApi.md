# \RemoteControlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commands_list**](RemoteControlApi.md#commands_list) | **GET** /api/commands/ | 
[**commands_partial_update**](RemoteControlApi.md#commands_partial_update) | **PATCH** /api/commands/{id}/ | 
[**commands_retrieve**](RemoteControlApi.md#commands_retrieve) | **GET** /api/commands/{id}/ | 
[**commands_update**](RemoteControlApi.md#commands_update) | **PUT** /api/commands/{id}/ | 
[**gcode_files_create**](RemoteControlApi.md#gcode_files_create) | **POST** /api/gcode-files/ | 
[**gcode_files_list**](RemoteControlApi.md#gcode_files_list) | **GET** /api/gcode-files/ | 
[**gcode_files_partial_update**](RemoteControlApi.md#gcode_files_partial_update) | **PATCH** /api/gcode-files/{id}/ | 
[**gcode_files_retrieve**](RemoteControlApi.md#gcode_files_retrieve) | **GET** /api/gcode-files/{id}/ | 
[**gcode_files_update**](RemoteControlApi.md#gcode_files_update) | **PUT** /api/gcode-files/{id}/ | 
[**gcode_files_update_or_create**](RemoteControlApi.md#gcode_files_update_or_create) | **POST** /api/gcode-files/update-or-create/ | 
[**octoprint_devices_create**](RemoteControlApi.md#octoprint_devices_create) | **POST** /api/octoprint-devices/ | 
[**octoprint_devices_list**](RemoteControlApi.md#octoprint_devices_list) | **GET** /api/octoprint-devices/ | 
[**octoprint_devices_partial_update**](RemoteControlApi.md#octoprint_devices_partial_update) | **PATCH** /api/octoprint-devices/{id}/ | 
[**octoprint_devices_retrieve**](RemoteControlApi.md#octoprint_devices_retrieve) | **GET** /api/octoprint-devices/{id}/ | 
[**octoprint_devices_update**](RemoteControlApi.md#octoprint_devices_update) | **PUT** /api/octoprint-devices/{id}/ | 
[**octoprint_devices_update_or_create**](RemoteControlApi.md#octoprint_devices_update_or_create) | **POST** /api/octoprint-devices/update-or-create/ | 
[**print_session_partial_update**](RemoteControlApi.md#print_session_partial_update) | **PATCH** /api/print-sessions/{session}/ | 
[**print_session_update**](RemoteControlApi.md#print_session_update) | **PUT** /api/print-sessions/{session}/ | 
[**print_sessions_create**](RemoteControlApi.md#print_sessions_create) | **POST** /api/print-sessions/ | 
[**print_sessions_list**](RemoteControlApi.md#print_sessions_list) | **GET** /api/print-sessions/ | 
[**print_sessions_retrieve**](RemoteControlApi.md#print_sessions_retrieve) | **GET** /api/print-sessions/{session}/ | 
[**printer_profiles_create**](RemoteControlApi.md#printer_profiles_create) | **POST** /api/printer-profiles/ | 
[**printer_profiles_list**](RemoteControlApi.md#printer_profiles_list) | **GET** /api/printer-profiles/ | 
[**printer_profiles_partial_update**](RemoteControlApi.md#printer_profiles_partial_update) | **PATCH** /api/printer-profiles/{id}/ | 
[**printer_profiles_retrieve**](RemoteControlApi.md#printer_profiles_retrieve) | **GET** /api/printer-profiles/{id}/ | 
[**printer_profiles_update**](RemoteControlApi.md#printer_profiles_update) | **PUT** /api/printer-profiles/{id}/ | 
[**printer_profiles_update_or_create**](RemoteControlApi.md#printer_profiles_update_or_create) | **POST** /api/printer-profiles/update-or-create/ | 



## commands_list

> crate::models::PaginatedRemoteControlCommandList commands_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedRemoteControlCommandList**](PaginatedRemoteControlCommandList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## commands_partial_update

> crate::models::RemoteControlCommand commands_partial_update(id, patched_remote_control_command_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this remote control command. | [required] |
**patched_remote_control_command_request** | Option<[**PatchedRemoteControlCommandRequest**](PatchedRemoteControlCommandRequest.md)> |  |  |

### Return type

[**crate::models::RemoteControlCommand**](RemoteControlCommand.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## commands_retrieve

> crate::models::RemoteControlCommand commands_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this remote control command. | [required] |

### Return type

[**crate::models::RemoteControlCommand**](RemoteControlCommand.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## commands_update

> crate::models::RemoteControlCommand commands_update(id, remote_control_command_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this remote control command. | [required] |
**remote_control_command_request** | [**RemoteControlCommandRequest**](RemoteControlCommandRequest.md) |  | [required] |

### Return type

[**crate::models::RemoteControlCommand**](RemoteControlCommand.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## gcode_files_create

> crate::models::GcodeFile gcode_files_create(name, file, file_hash, octoprint_device)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** |  | [required] |
**file** | **std::path::PathBuf** |  | [required] |
**file_hash** | **String** |  | [required] |
**octoprint_device** | **String** |  | [required] |

### Return type

[**crate::models::GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## gcode_files_list

> crate::models::PaginatedGcodeFileList gcode_files_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedGcodeFileList**](PaginatedGcodeFileList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## gcode_files_partial_update

> crate::models::GcodeFile gcode_files_partial_update(id, name, file, file_hash, octoprint_device)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** |  | [required] |
**name** | Option<**String**> |  |  |
**file** | Option<**std::path::PathBuf**> |  |  |
**file_hash** | Option<**String**> |  |  |
**octoprint_device** | Option<**String**> |  |  |

### Return type

[**crate::models::GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## gcode_files_retrieve

> crate::models::GcodeFile gcode_files_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** |  | [required] |

### Return type

[**crate::models::GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## gcode_files_update

> crate::models::GcodeFile gcode_files_update(id, name, file, file_hash, octoprint_device)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** |  | [required] |
**name** | **String** |  | [required] |
**file** | **std::path::PathBuf** |  | [required] |
**file_hash** | **String** |  | [required] |
**octoprint_device** | **String** |  | [required] |

### Return type

[**crate::models::GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## gcode_files_update_or_create

> crate::models::GcodeFile gcode_files_update_or_create(name, file, file_hash, octoprint_device)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** |  | [required] |
**file** | **std::path::PathBuf** |  | [required] |
**file_hash** | **String** |  | [required] |
**octoprint_device** | **String** |  | [required] |

### Return type

[**crate::models::GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_devices_create

> crate::models::OctoPrintDevice octoprint_devices_create(octo_print_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_print_device_request** | [**OctoPrintDeviceRequest**](OctoPrintDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintDevice**](OctoPrintDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_devices_list

> crate::models::PaginatedOctoPrintDeviceList octoprint_devices_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedOctoPrintDeviceList**](PaginatedOctoPrintDeviceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_devices_partial_update

> crate::models::OctoPrintDevice octoprint_devices_partial_update(id, patched_octo_print_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print device. | [required] |
**patched_octo_print_device_request** | Option<[**PatchedOctoPrintDeviceRequest**](PatchedOctoPrintDeviceRequest.md)> |  |  |

### Return type

[**crate::models::OctoPrintDevice**](OctoPrintDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_devices_retrieve

> crate::models::OctoPrintDevice octoprint_devices_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print device. | [required] |

### Return type

[**crate::models::OctoPrintDevice**](OctoPrintDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_devices_update

> crate::models::OctoPrintDevice octoprint_devices_update(id, octo_print_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print device. | [required] |
**octo_print_device_request** | [**OctoPrintDeviceRequest**](OctoPrintDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintDevice**](OctoPrintDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_devices_update_or_create

> crate::models::OctoPrintDevice octoprint_devices_update_or_create(octo_print_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_print_device_request** | [**OctoPrintDeviceRequest**](OctoPrintDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintDevice**](OctoPrintDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## print_session_partial_update

> crate::models::PrintSession print_session_partial_update(session, patched_print_session_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**session** | **String** |  | [required] |
**patched_print_session_request** | Option<[**PatchedPrintSessionRequest**](PatchedPrintSessionRequest.md)> |  |  |

### Return type

[**crate::models::PrintSession**](PrintSession.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## print_session_update

> crate::models::PrintSession print_session_update(session, print_session_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**session** | **String** |  | [required] |
**print_session_request** | [**PrintSessionRequest**](PrintSessionRequest.md) |  | [required] |

### Return type

[**crate::models::PrintSession**](PrintSession.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## print_sessions_create

> crate::models::PrintSession print_sessions_create(print_session_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**print_session_request** | [**PrintSessionRequest**](PrintSessionRequest.md) |  | [required] |

### Return type

[**crate::models::PrintSession**](PrintSession.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## print_sessions_list

> crate::models::PaginatedPrintSessionList print_sessions_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPrintSessionList**](PaginatedPrintSessionList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## print_sessions_retrieve

> crate::models::PrintSession print_sessions_retrieve(session)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**session** | **String** |  | [required] |

### Return type

[**crate::models::PrintSession**](PrintSession.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## printer_profiles_create

> crate::models::PrintSession printer_profiles_create(printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**printer_profile_request** | [**PrinterProfileRequest**](PrinterProfileRequest.md) |  | [required] |

### Return type

[**crate::models::PrintSession**](PrintSession.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## printer_profiles_list

> crate::models::PaginatedPrinterProfileList printer_profiles_list(name, page, user)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | Option<**String**> |  |  |
**page** | Option<**i32**> | A page number within the paginated result set. |  |
**user** | Option<**i32**> |  |  |

### Return type

[**crate::models::PaginatedPrinterProfileList**](PaginatedPrinterProfileList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## printer_profiles_partial_update

> crate::models::PrinterProfile printer_profiles_partial_update(id, patched_printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this printer profile. | [required] |
**patched_printer_profile_request** | Option<[**PatchedPrinterProfileRequest**](PatchedPrinterProfileRequest.md)> |  |  |

### Return type

[**crate::models::PrinterProfile**](PrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## printer_profiles_retrieve

> crate::models::PrinterProfile printer_profiles_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this printer profile. | [required] |

### Return type

[**crate::models::PrinterProfile**](PrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## printer_profiles_update

> crate::models::PrinterProfile printer_profiles_update(id, printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this printer profile. | [required] |
**printer_profile_request** | [**PrinterProfileRequest**](PrinterProfileRequest.md) |  | [required] |

### Return type

[**crate::models::PrinterProfile**](PrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## printer_profiles_update_or_create

> crate::models::PrinterProfile printer_profiles_update_or_create(printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**printer_profile_request** | [**PrinterProfileRequest**](PrinterProfileRequest.md) |  | [required] |

### Return type

[**crate::models::PrinterProfile**](PrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

