# \BillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_cancel_create**](BillingApi.md#billing_cancel_create) | **POST** /api/billing/{subscription_id}/cancel/ | 
[**billing_reactivate_create**](BillingApi.md#billing_reactivate_create) | **POST** /api/billing/{subscription_id}/reactivate/ | 
[**billing_summary_retrieve**](BillingApi.md#billing_summary_retrieve) | **GET** /api/billing/summary | 



## billing_cancel_create

> crate::models::BillingSummary billing_cancel_create(subscription_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**subscription_id** | **i32** |  | [required] |

### Return type

[**crate::models::BillingSummary**](BillingSummary.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## billing_reactivate_create

> crate::models::BillingSummary billing_reactivate_create(subscription_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**subscription_id** | **String** |  | [required] |

### Return type

[**crate::models::BillingSummary**](BillingSummary.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## billing_summary_retrieve

> crate::models::BillingSummary billing_summary_retrieve()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::BillingSummary**](BillingSummary.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

