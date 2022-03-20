# \OctoprintApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**octoprint_backups_create**](OctoprintApi.md#octoprint_backups_create) | **POST** /api/octoprint/backups/ | 
[**octoprint_backups_list**](OctoprintApi.md#octoprint_backups_list) | **GET** /api/octoprint/backups/ | 
[**octoprint_backups_retrieve**](OctoprintApi.md#octoprint_backups_retrieve) | **GET** /api/octoprint/backups/{id}/ | 
[**octoprint_gcode_files_create**](OctoprintApi.md#octoprint_gcode_files_create) | **POST** /api/octoprint/gcode-files/ | 
[**octoprint_gcode_files_list**](OctoprintApi.md#octoprint_gcode_files_list) | **GET** /api/octoprint/gcode-files/ | 
[**octoprint_gcode_files_retrieve**](OctoprintApi.md#octoprint_gcode_files_retrieve) | **GET** /api/octoprint/gcode-files/{id}/ | 
[**octoprint_printer_profiles_create**](OctoprintApi.md#octoprint_printer_profiles_create) | **POST** /api/octoprint/printer-profiles/ | 
[**octoprint_printer_profiles_list**](OctoprintApi.md#octoprint_printer_profiles_list) | **GET** /api/octoprint/printer-profiles/ | 
[**octoprint_printer_profiles_partial_update**](OctoprintApi.md#octoprint_printer_profiles_partial_update) | **PATCH** /api/octoprint/printer-profiles/{id}/ | 
[**octoprint_printer_profiles_update**](OctoprintApi.md#octoprint_printer_profiles_update) | **PUT** /api/octoprint/printer-profiles/{id}/ | 
[**octoprint_settings_create**](OctoprintApi.md#octoprint_settings_create) | **POST** /api/octoprint/settings/ | 
[**octoprint_settings_device_update_or_create**](OctoprintApi.md#octoprint_settings_device_update_or_create) | **POST** /api/octoprint/printer-profiles/update-or-create/ | 
[**octoprint_settings_device_update_or_create2**](OctoprintApi.md#octoprint_settings_device_update_or_create2) | **POST** /api/octoprint/settings/update-or-create/ | 
[**octoprint_settings_list**](OctoprintApi.md#octoprint_settings_list) | **GET** /api/octoprint/settings/ | 
[**octoprint_settings_partial_update**](OctoprintApi.md#octoprint_settings_partial_update) | **PATCH** /api/octoprint/settings/{id}/ | 
[**octoprint_settings_update**](OctoprintApi.md#octoprint_settings_update) | **PUT** /api/octoprint/settings/{id}/ | 



## octoprint_backups_create

> crate::models::OctoPrintBackup octoprint_backups_create(hostname, name, octoprint_version, file)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hostname** | **String** |  | [required] |
**name** | **String** |  | [required] |
**octoprint_version** | **String** |  | [required] |
**file** | **std::path::PathBuf** |  | [required] |

### Return type

[**crate::models::OctoPrintBackup**](OctoPrintBackup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_backups_list

> crate::models::PaginatedOctoPrintBackupList octoprint_backups_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedOctoPrintBackupList**](PaginatedOctoPrintBackupList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_backups_retrieve

> crate::models::OctoPrintBackup octoprint_backups_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print backup. | [required] |

### Return type

[**crate::models::OctoPrintBackup**](OctoPrintBackup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_gcode_files_create

> crate::models::GcodeFile octoprint_gcode_files_create(gcode_file_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**gcode_file_request** | [**GcodeFileRequest**](GcodeFileRequest.md) |  | [required] |

### Return type

[**crate::models::GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_gcode_files_list

> crate::models::PaginatedGcodeFileList octoprint_gcode_files_list(page)


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


## octoprint_gcode_files_retrieve

> crate::models::GcodeFile octoprint_gcode_files_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this gcode file. | [required] |

### Return type

[**crate::models::GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_printer_profiles_create

> crate::models::OctoPrinterProfile octoprint_printer_profiles_create(octo_printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_printer_profile_request** | [**OctoPrinterProfileRequest**](OctoPrinterProfileRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrinterProfile**](OctoPrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_printer_profiles_list

> crate::models::PaginatedOctoPrinterProfileList octoprint_printer_profiles_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedOctoPrinterProfileList**](PaginatedOctoPrinterProfileList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_printer_profiles_partial_update

> crate::models::OctoPrinterProfile octoprint_printer_profiles_partial_update(id, patched_octo_printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo printer profile. | [required] |
**patched_octo_printer_profile_request** | Option<[**PatchedOctoPrinterProfileRequest**](PatchedOctoPrinterProfileRequest.md)> |  |  |

### Return type

[**crate::models::OctoPrinterProfile**](OctoPrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_printer_profiles_update

> octoprint_printer_profiles_update(id, octo_printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo printer profile. | [required] |
**octo_printer_profile_request** | [**OctoPrinterProfileRequest**](OctoPrinterProfileRequest.md) |  | [required] |

### Return type

 (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_create

> crate::models::OctoPrinterProfile octoprint_settings_create(octo_printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_printer_profile_request** | [**OctoPrinterProfileRequest**](OctoPrinterProfileRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrinterProfile**](OctoPrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_device_update_or_create

> crate::models::OctoPrinterProfile octoprint_settings_device_update_or_create(octo_printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_printer_profile_request** | [**OctoPrinterProfileRequest**](OctoPrinterProfileRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrinterProfile**](OctoPrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_device_update_or_create2

> crate::models::OctoPrinterProfile octoprint_settings_device_update_or_create2(octo_printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_printer_profile_request** | [**OctoPrinterProfileRequest**](OctoPrinterProfileRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrinterProfile**](OctoPrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_list

> crate::models::PaginatedOctoPrinterProfileList octoprint_settings_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedOctoPrinterProfileList**](PaginatedOctoPrinterProfileList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_partial_update

> crate::models::OctoPrinterProfile octoprint_settings_partial_update(id, patched_octo_printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print settings. | [required] |
**patched_octo_printer_profile_request** | Option<[**PatchedOctoPrinterProfileRequest**](PatchedOctoPrinterProfileRequest.md)> |  |  |

### Return type

[**crate::models::OctoPrinterProfile**](OctoPrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_update

> octoprint_settings_update(id, octo_printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print settings. | [required] |
**octo_printer_profile_request** | [**OctoPrinterProfileRequest**](OctoPrinterProfileRequest.md) |  | [required] |

### Return type

 (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
