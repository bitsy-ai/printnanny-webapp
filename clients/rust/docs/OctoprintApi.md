# \OctoprintApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**octoprint_backups_create**](OctoprintApi.md#octoprint_backups_create) | **POST** /api/octoprint/backups/ | 
[**octoprint_backups_list**](OctoprintApi.md#octoprint_backups_list) | **GET** /api/octoprint/backups/ | 
[**octoprint_backups_retrieve**](OctoprintApi.md#octoprint_backups_retrieve) | **GET** /api/octoprint/backups/{id}/ | 
[**octoprint_create**](OctoprintApi.md#octoprint_create) | **POST** /api/octoprint/ | 
[**octoprint_events_create**](OctoprintApi.md#octoprint_events_create) | **POST** /api/octoprint/events/ | 
[**octoprint_events_list**](OctoprintApi.md#octoprint_events_list) | **GET** /api/octoprint/events/ | 
[**octoprint_events_retrieve**](OctoprintApi.md#octoprint_events_retrieve) | **GET** /api/octoprint/events/{id}/ | 
[**octoprint_gcode_files_create**](OctoprintApi.md#octoprint_gcode_files_create) | **POST** /api/octoprint/gcode-files/ | 
[**octoprint_gcode_files_list**](OctoprintApi.md#octoprint_gcode_files_list) | **GET** /api/octoprint/gcode-files/ | 
[**octoprint_gcode_files_retrieve**](OctoprintApi.md#octoprint_gcode_files_retrieve) | **GET** /api/octoprint/gcode-files/{id}/ | 
[**octoprint_list**](OctoprintApi.md#octoprint_list) | **GET** /api/octoprint/ | 
[**octoprint_partial_update**](OctoprintApi.md#octoprint_partial_update) | **PATCH** /api/octoprint/{id}/ | 
[**octoprint_printer_profiles_create**](OctoprintApi.md#octoprint_printer_profiles_create) | **POST** /api/octoprint/printer-profiles/ | 
[**octoprint_printer_profiles_list**](OctoprintApi.md#octoprint_printer_profiles_list) | **GET** /api/octoprint/printer-profiles/ | 
[**octoprint_printer_profiles_partial_update**](OctoprintApi.md#octoprint_printer_profiles_partial_update) | **PATCH** /api/octoprint/printer-profiles/{id}/ | 
[**octoprint_printer_profiles_update**](OctoprintApi.md#octoprint_printer_profiles_update) | **PUT** /api/octoprint/printer-profiles/{id}/ | 
[**octoprint_profile_update_or_create**](OctoprintApi.md#octoprint_profile_update_or_create) | **POST** /api/octoprint/printer-profiles/update-or-create/ | 
[**octoprint_server_update_or_create**](OctoprintApi.md#octoprint_server_update_or_create) | **POST** /api/octoprint/update-or-create/ | 
[**octoprint_settings_create**](OctoprintApi.md#octoprint_settings_create) | **POST** /api/octoprint/settings/ | 
[**octoprint_settings_list**](OctoprintApi.md#octoprint_settings_list) | **GET** /api/octoprint/settings/ | 
[**octoprint_settings_partial_update**](OctoprintApi.md#octoprint_settings_partial_update) | **PATCH** /api/octoprint/settings/{id}/ | 
[**octoprint_settings_update**](OctoprintApi.md#octoprint_settings_update) | **PUT** /api/octoprint/settings/{id}/ | 
[**octoprint_settings_update_or_create**](OctoprintApi.md#octoprint_settings_update_or_create) | **POST** /api/octoprint/settings/update-or-create/ | 
[**octoprint_update**](OctoprintApi.md#octoprint_update) | **PUT** /api/octoprint/{id}/ | 
[**pis_octoprint_server_list**](OctoprintApi.md#pis_octoprint_server_list) | **GET** /api/pis/{pi_id}/octoprint-server/ | 



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


## octoprint_create

> crate::models::OctoPrintServer octoprint_create(octo_print_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_print_server_request** | [**OctoPrintServerRequest**](OctoPrintServerRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintServer**](OctoPrintServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_events_create

> crate::models::PolymorphicOctoPrintEvent octoprint_events_create(polymorphic_octo_print_event_request)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**polymorphic_octo_print_event_request** | Option<[**PolymorphicOctoPrintEventRequest**](PolymorphicOctoPrintEventRequest.md)> |  |  |

### Return type

[**crate::models::PolymorphicOctoPrintEvent**](PolymorphicOctoPrintEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_events_list

> crate::models::PaginatedPolymorphicOctoPrintEventList octoprint_events_list(page)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPolymorphicOctoPrintEventList**](PaginatedPolymorphicOctoPrintEventList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_events_retrieve

> crate::models::PolymorphicOctoPrintEvent octoprint_events_retrieve(id)


Interact with all events inheriting from BasePiEvent

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this base octo print event. | [required] |

### Return type

[**crate::models::PolymorphicOctoPrintEvent**](PolymorphicOctoPrintEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_gcode_files_create

> crate::models::GcodeFile octoprint_gcode_files_create(name, file, hash)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** |  | [required] |
**file** | **std::path::PathBuf** |  | [required] |
**hash** | **String** |  | [required] |

### Return type

[**crate::models::GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
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


## octoprint_list

> crate::models::PaginatedOctoPrintServerList octoprint_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedOctoPrintServerList**](PaginatedOctoPrintServerList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_partial_update

> crate::models::OctoPrintServer octoprint_partial_update(id, patched_octo_print_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print server. | [required] |
**patched_octo_print_server_request** | Option<[**PatchedOctoPrintServerRequest**](PatchedOctoPrintServerRequest.md)> |  |  |

### Return type

[**crate::models::OctoPrintServer**](OctoPrintServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

> crate::models::OctoPrinterProfile octoprint_printer_profiles_update(id, octo_printer_profile_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo printer profile. | [required] |
**octo_printer_profile_request** | [**OctoPrinterProfileRequest**](OctoPrinterProfileRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrinterProfile**](OctoPrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_profile_update_or_create

> crate::models::OctoPrinterProfile octoprint_profile_update_or_create(octo_printer_profile_request)


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


## octoprint_server_update_or_create

> crate::models::OctoPrintServer octoprint_server_update_or_create(octo_print_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_print_server_request** | [**OctoPrintServerRequest**](OctoPrintServerRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintServer**](OctoPrintServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_create

> crate::models::OctoPrintSettings octoprint_settings_create(octo_print_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_print_settings_request** | [**OctoPrintSettingsRequest**](OctoPrintSettingsRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintSettings**](OctoPrintSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_list

> crate::models::PaginatedOctoPrintSettingsList octoprint_settings_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedOctoPrintSettingsList**](PaginatedOctoPrintSettingsList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_partial_update

> crate::models::OctoPrintSettings octoprint_settings_partial_update(id, patched_octo_print_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print settings. | [required] |
**patched_octo_print_settings_request** | Option<[**PatchedOctoPrintSettingsRequest**](PatchedOctoPrintSettingsRequest.md)> |  |  |

### Return type

[**crate::models::OctoPrintSettings**](OctoPrintSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_update

> crate::models::OctoPrintSettings octoprint_settings_update(id, octo_print_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print settings. | [required] |
**octo_print_settings_request** | [**OctoPrintSettingsRequest**](OctoPrintSettingsRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintSettings**](OctoPrintSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_settings_update_or_create

> crate::models::OctoPrintSettings octoprint_settings_update_or_create(octo_print_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_print_settings_request** | [**OctoPrintSettingsRequest**](OctoPrintSettingsRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintSettings**](OctoPrintSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_update

> crate::models::OctoPrintServer octoprint_update(id, octo_print_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print server. | [required] |
**octo_print_server_request** | [**OctoPrintServerRequest**](OctoPrintServerRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintServer**](OctoPrintServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_octoprint_server_list

> crate::models::PaginatedOctoPrintServerList pis_octoprint_server_list(pi_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedOctoPrintServerList**](PaginatedOctoPrintServerList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

