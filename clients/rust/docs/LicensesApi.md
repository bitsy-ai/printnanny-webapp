# \LicensesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**license_activate**](LicensesApi.md#license_activate) | **POST** /api/licenses/{id}/activate/ | 
[**licenses_list**](LicensesApi.md#licenses_list) | **GET** /api/licenses/ | 
[**licenses_retrieve**](LicensesApi.md#licenses_retrieve) | **GET** /api/licenses/{id}/ | 



## license_activate

> crate::models::License license_activate(id, license_request)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this license. | [required] |
**license_request** | [**LicenseRequest**](LicenseRequest.md) |  | [required] |

### Return type

[**crate::models::License**](License.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## licenses_list

> crate::models::PaginatedLicenseList licenses_list(page)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedLicenseList**](PaginatedLicenseList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## licenses_retrieve

> crate::models::License licenses_retrieve(id)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this license. | [required] |

### Return type

[**crate::models::License**](License.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

