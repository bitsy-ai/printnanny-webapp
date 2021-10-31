# \ReleasesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**releases_latest_retrieve**](ReleasesApi.md#releases_latest_retrieve) | **GET** /api/releases/{release_channel}/latest/ | 
[**releases_list**](ReleasesApi.md#releases_list) | **GET** /api/releases/ | 
[**releases_retrieve**](ReleasesApi.md#releases_retrieve) | **GET** /api/releases/{id}/ | 



## releases_latest_retrieve

> crate::models::Release releases_latest_retrieve(release_channel)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**release_channel** | **String** |  | [required] |

### Return type

[**crate::models::Release**](Release.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## releases_list

> crate::models::PaginatedReleaseList releases_list(page)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedReleaseList**](PaginatedReleaseList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## releases_retrieve

> crate::models::Release releases_retrieve(id)


All-in-one Print Nanny installation via print-nanny-main-<platform>-<cpu>.img

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this release. | [required] |

### Return type

[**crate::models::Release**](Release.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

