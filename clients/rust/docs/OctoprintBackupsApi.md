# \OctoprintBackupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**octoprint_backups_create**](OctoprintBackupsApi.md#octoprint_backups_create) | **POST** /api/octoprint-backups/ | 
[**octoprint_backups_list**](OctoprintBackupsApi.md#octoprint_backups_list) | **GET** /api/octoprint-backups/ | 
[**octoprint_backups_retrieve**](OctoprintBackupsApi.md#octoprint_backups_retrieve) | **GET** /api/octoprint-backups/{id}/ | 



## octoprint_backups_create

> crate::models::OctoPrintBackup octoprint_backups_create(hostname, octoprint_version, file)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hostname** | **String** |  | [required] |
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

