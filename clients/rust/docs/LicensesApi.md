# \LicensesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licenses_partial_update**](LicensesApi.md#licenses_partial_update) | **PATCH** /api/licenses/{id}/ | 
[**licenses_retrieve**](LicensesApi.md#licenses_retrieve) | **GET** /api/licenses/{id}/ | 
[**licenses_update**](LicensesApi.md#licenses_update) | **PUT** /api/licenses/{id}/ | 



## licenses_partial_update

> crate::models::License licenses_partial_update(id, patched_license_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this license. | [required] |
**patched_license_request** | Option<[**PatchedLicenseRequest**](PatchedLicenseRequest.md)> |  |  |

### Return type

[**crate::models::License**](License.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## licenses_retrieve

> crate::models::License licenses_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this license. | [required] |

### Return type

[**crate::models::License**](License.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## licenses_update

> crate::models::License licenses_update(id, license_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this license. | [required] |
**license_request** | [**LicenseRequest**](LicenseRequest.md) |  | [required] |

### Return type

[**crate::models::License**](License.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

