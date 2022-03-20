# \PartnersGeeks3dApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_list2**](PartnersGeeks3dApi.md#alerts_list2) | **GET** /api/partners/3d-geeks/{id}/alerts/ | 
[**metadata_retrieve**](PartnersGeeks3dApi.md#metadata_retrieve) | **GET** /api/partners/3d-geeks/{id}/ | 



## alerts_list2

> crate::models::Partner3DGeeksAlert alerts_list2(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** |  | [required] |

### Return type

[**crate::models::Partner3DGeeksAlert**](Partner3DGeeksAlert.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## metadata_retrieve

> crate::models::Partner3DGeeksMetadata metadata_retrieve(id)


3D Geeks calls this endpoint to validate token & fetch printer metadata

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** |  | [required] |

### Return type

[**crate::models::Partner3DGeeksMetadata**](Partner3DGeeksMetadata.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

