# \DemosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**demos_create**](DemosApi.md#demos_create) | **POST** /api/demos/ | 
[**demos_feedback_partial_update**](DemosApi.md#demos_feedback_partial_update) | **PATCH** /api/demos/feedback/{id}/ | 
[**demos_feedback_retrieve**](DemosApi.md#demos_feedback_retrieve) | **GET** /api/demos/feedback/{id}/ | 
[**demos_feedback_update**](DemosApi.md#demos_feedback_update) | **PUT** /api/demos/feedback/{id}/ | 
[**demos_retrieve**](DemosApi.md#demos_retrieve) | **GET** /api/demos/{id}/ | 



## demos_create

> crate::models::DemoSubmission demos_create(email, submission)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**email** | **String** |  | [required] |
**submission** | **std::path::PathBuf** |  | [required] |

### Return type

[**crate::models::DemoSubmission**](DemoSubmission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## demos_feedback_partial_update

> crate::models::DemoSubmission demos_feedback_partial_update(id, patched_demo_submission_feedback_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this demo submission. | [required] |
**patched_demo_submission_feedback_request** | Option<[**PatchedDemoSubmissionFeedbackRequest**](PatchedDemoSubmissionFeedbackRequest.md)> |  |  |

### Return type

[**crate::models::DemoSubmission**](DemoSubmission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## demos_feedback_retrieve

> crate::models::DemoSubmission demos_feedback_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this demo submission. | [required] |

### Return type

[**crate::models::DemoSubmission**](DemoSubmission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## demos_feedback_update

> crate::models::DemoSubmission demos_feedback_update(id, demo_submission_feedback_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this demo submission. | [required] |
**demo_submission_feedback_request** | Option<[**DemoSubmissionFeedbackRequest**](DemoSubmissionFeedbackRequest.md)> |  |  |

### Return type

[**crate::models::DemoSubmission**](DemoSubmission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## demos_retrieve

> crate::models::DemoSubmission demos_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this demo submission. | [required] |

### Return type

[**crate::models::DemoSubmission**](DemoSubmission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

