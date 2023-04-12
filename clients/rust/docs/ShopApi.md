# \ShopApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloud_plans_retrieve**](ShopApi.md#cloud_plans_retrieve) | **GET** /api/shop/products/cloud-plans/ | 
[**shop_checkout_success_retrieve**](ShopApi.md#shop_checkout_success_retrieve) | **GET** /api/shop/checkout/success/{stripe_checkout_session_id} | 
[**shop_orders_create**](ShopApi.md#shop_orders_create) | **POST** /api/shop/orders | 
[**shop_products_list**](ShopApi.md#shop_products_list) | **GET** /api/shop/products/ | 



## cloud_plans_retrieve

> crate::models::PaginatedProductList cloud_plans_retrieve(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedProductList**](PaginatedProductList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## shop_checkout_success_retrieve

> crate::models::Order shop_checkout_success_retrieve(stripe_checkout_session_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**stripe_checkout_session_id** | **String** |  | [required] |

### Return type

[**crate::models::Order**](Order.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## shop_orders_create

> crate::models::Order shop_orders_create(order_checkout_request_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**order_checkout_request_request** | [**OrderCheckoutRequestRequest**](OrderCheckoutRequestRequest.md) |  | [required] |

### Return type

[**crate::models::Order**](Order.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## shop_products_list

> crate::models::PaginatedProductList shop_products_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedProductList**](PaginatedProductList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

