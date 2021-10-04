# \AppliancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appliances_list**](AppliancesApi.md#appliances_list) | **GET** /api/appliances/ | 
[**appliances_partial_update**](AppliancesApi.md#appliances_partial_update) | **PATCH** /api/appliances/{id}/ | 
[**appliances_retrieve**](AppliancesApi.md#appliances_retrieve) | **GET** /api/appliances/{id}/ | 
[**appliances_update**](AppliancesApi.md#appliances_update) | **PUT** /api/appliances/{id}/ | 
[**appliances_update_or_create**](AppliancesApi.md#appliances_update_or_create) | **POST** /api/appliances/ | 



## appliances_list

> crate::models::PaginatedApplianceList appliances_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedApplianceList**](PaginatedApplianceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_partial_update

> crate::models::Appliance appliances_partial_update(id, patched_appliance_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this appliance. | [required] |
**patched_appliance_request** | Option<[**PatchedApplianceRequest**](PatchedApplianceRequest.md)> |  |  |

### Return type

[**crate::models::Appliance**](Appliance.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_retrieve

> crate::models::Appliance appliances_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this appliance. | [required] |

### Return type

[**crate::models::Appliance**](Appliance.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_update

> crate::models::Appliance appliances_update(id, appliance_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this appliance. | [required] |
**appliance_request** | [**ApplianceRequest**](ApplianceRequest.md) |  | [required] |

### Return type

[**crate::models::Appliance**](Appliance.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## appliances_update_or_create

> crate::models::Appliance appliances_update_or_create(create_appliance_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**create_appliance_request** | [**CreateApplianceRequest**](CreateApplianceRequest.md) |  | [required] |

### Return type

[**crate::models::Appliance**](Appliance.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

