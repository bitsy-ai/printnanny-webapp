# \DevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_settings_create**](DevicesApi.md#network_settings_create) | **POST** /api/network-settings/ | 
[**network_settings_partial_update**](DevicesApi.md#network_settings_partial_update) | **PATCH** /api/network-settings/{id} | 
[**network_settings_retrieve**](DevicesApi.md#network_settings_retrieve) | **GET** /api/network-settings/ | 
[**network_settings_update**](DevicesApi.md#network_settings_update) | **PUT** /api/network-settings/{id} | 
[**pi_update_or_create**](DevicesApi.md#pi_update_or_create) | **POST** /api/pis/update-or-create/ | 
[**pis_create**](DevicesApi.md#pis_create) | **POST** /api/pis/ | 
[**pis_destroy**](DevicesApi.md#pis_destroy) | **DELETE** /api/pis/{id}/ | 
[**pis_license_zip_retrieve**](DevicesApi.md#pis_license_zip_retrieve) | **GET** /api/pis/{pi_id}/license/zip/ | 
[**pis_list**](DevicesApi.md#pis_list) | **GET** /api/pis/ | 
[**pis_partial_update**](DevicesApi.md#pis_partial_update) | **PATCH** /api/pis/{id}/ | 
[**pis_retrieve**](DevicesApi.md#pis_retrieve) | **GET** /api/pis/{id}/ | 
[**pis_system_info_create**](DevicesApi.md#pis_system_info_create) | **POST** /api/pis/{pi_id}/system-info/ | 
[**pis_system_info_list**](DevicesApi.md#pis_system_info_list) | **GET** /api/pis/{pi_id}/system-info/ | 
[**pis_system_info_partial_update**](DevicesApi.md#pis_system_info_partial_update) | **PATCH** /api/pis/{pi_id}/system-info/{id}/ | 
[**pis_system_info_retrieve**](DevicesApi.md#pis_system_info_retrieve) | **GET** /api/pis/{pi_id}/system-info/{id}/ | 
[**pis_system_info_update**](DevicesApi.md#pis_system_info_update) | **PUT** /api/pis/{pi_id}/system-info/{id}/ | 
[**pis_update**](DevicesApi.md#pis_update) | **PUT** /api/pis/{id}/ | 
[**pis_webrtc_streams_create**](DevicesApi.md#pis_webrtc_streams_create) | **POST** /api/pis/{pi_id}/webrtc-streams/ | 
[**pis_webrtc_streams_list**](DevicesApi.md#pis_webrtc_streams_list) | **GET** /api/pis/{pi_id}/webrtc-streams/ | 
[**pis_webrtc_streams_partial_update**](DevicesApi.md#pis_webrtc_streams_partial_update) | **PATCH** /api/pis/{pi_id}/webrtc-streams/{id}/ | 
[**pis_webrtc_streams_retrieve**](DevicesApi.md#pis_webrtc_streams_retrieve) | **GET** /api/pis/{pi_id}/webrtc-streams/{id}/ | 
[**pis_webrtc_streams_update**](DevicesApi.md#pis_webrtc_streams_update) | **PUT** /api/pis/{pi_id}/webrtc-streams/{id}/ | 
[**system_info_update_or_create**](DevicesApi.md#system_info_update_or_create) | **POST** /api/pis/{pi_id}/system-info/update-or-create/ | 
[**webrtc_stream_update_or_create**](DevicesApi.md#webrtc_stream_update_or_create) | **POST** /api/pis/{pi_id}/webrtc-streams/update-or-create/ | 



## network_settings_create

> crate::models::NetworkSettings network_settings_create(network_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**network_settings_request** | [**NetworkSettingsRequest**](NetworkSettingsRequest.md) |  | [required] |

### Return type

[**crate::models::NetworkSettings**](NetworkSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## network_settings_partial_update

> crate::models::NetworkSettings network_settings_partial_update(id, patched_network_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** |  | [required] |
**patched_network_settings_request** | Option<[**PatchedNetworkSettingsRequest**](PatchedNetworkSettingsRequest.md)> |  |  |

### Return type

[**crate::models::NetworkSettings**](NetworkSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## network_settings_retrieve

> crate::models::NetworkSettings network_settings_retrieve()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::NetworkSettings**](NetworkSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## network_settings_update

> crate::models::NetworkSettings network_settings_update(id, network_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** |  | [required] |
**network_settings_request** | [**NetworkSettingsRequest**](NetworkSettingsRequest.md) |  | [required] |

### Return type

[**crate::models::NetworkSettings**](NetworkSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pi_update_or_create

> crate::models::Pi pi_update_or_create(pi_request)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_request** | Option<[**PiRequest**](PiRequest.md)> |  |  |

### Return type

[**crate::models::Pi**](Pi.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_create

> crate::models::Pi pis_create(pi_request)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_request** | Option<[**PiRequest**](PiRequest.md)> |  |  |

### Return type

[**crate::models::Pi**](Pi.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_destroy

> pis_destroy(id)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this pi. | [required] |

### Return type

 (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_license_zip_retrieve

> std::path::PathBuf pis_license_zip_retrieve(pi_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |

### Return type

[**std::path::PathBuf**](std::path::PathBuf.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_list

> crate::models::PaginatedPiList pis_list(page)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPiList**](PaginatedPiList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_partial_update

> crate::models::Pi pis_partial_update(id, patched_pi_request)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this pi. | [required] |
**patched_pi_request** | Option<[**PatchedPiRequest**](PatchedPiRequest.md)> |  |  |

### Return type

[**crate::models::Pi**](Pi.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_retrieve

> crate::models::Pi pis_retrieve(id)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this pi. | [required] |

### Return type

[**crate::models::Pi**](Pi.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_system_info_create

> crate::models::SystemInfo pis_system_info_create(pi_id, system_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**system_info_request** | [**SystemInfoRequest**](SystemInfoRequest.md) |  | [required] |

### Return type

[**crate::models::SystemInfo**](SystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_system_info_list

> crate::models::PaginatedSystemInfoList pis_system_info_list(pi_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedSystemInfoList**](PaginatedSystemInfoList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_system_info_partial_update

> crate::models::SystemInfo pis_system_info_partial_update(id, pi_id, patched_system_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this system info. | [required] |
**pi_id** | **i32** |  | [required] |
**patched_system_info_request** | Option<[**PatchedSystemInfoRequest**](PatchedSystemInfoRequest.md)> |  |  |

### Return type

[**crate::models::SystemInfo**](SystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_system_info_retrieve

> crate::models::SystemInfo pis_system_info_retrieve(id, pi_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this system info. | [required] |
**pi_id** | **i32** |  | [required] |

### Return type

[**crate::models::SystemInfo**](SystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_system_info_update

> crate::models::SystemInfo pis_system_info_update(id, pi_id, system_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this system info. | [required] |
**pi_id** | **i32** |  | [required] |
**system_info_request** | [**SystemInfoRequest**](SystemInfoRequest.md) |  | [required] |

### Return type

[**crate::models::SystemInfo**](SystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_update

> crate::models::Pi pis_update(id, pi_request)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this pi. | [required] |
**pi_request** | Option<[**PiRequest**](PiRequest.md)> |  |  |

### Return type

[**crate::models::Pi**](Pi.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_webrtc_streams_create

> crate::models::WebrtcStream pis_webrtc_streams_create(pi_id, webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**webrtc_stream_request** | Option<[**WebrtcStreamRequest**](WebrtcStreamRequest.md)> |  |  |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_webrtc_streams_list

> crate::models::PaginatedWebrtcStreamList pis_webrtc_streams_list(pi_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedWebrtcStreamList**](PaginatedWebrtcStreamList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_webrtc_streams_partial_update

> crate::models::WebrtcStream pis_webrtc_streams_partial_update(id, pi_id, patched_webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this webrtc stream. | [required] |
**pi_id** | **i32** |  | [required] |
**patched_webrtc_stream_request** | Option<[**PatchedWebrtcStreamRequest**](PatchedWebrtcStreamRequest.md)> |  |  |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_webrtc_streams_retrieve

> crate::models::WebrtcStream pis_webrtc_streams_retrieve(id, pi_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this webrtc stream. | [required] |
**pi_id** | **i32** |  | [required] |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_webrtc_streams_update

> crate::models::WebrtcStream pis_webrtc_streams_update(id, pi_id, webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this webrtc stream. | [required] |
**pi_id** | **i32** |  | [required] |
**webrtc_stream_request** | Option<[**WebrtcStreamRequest**](WebrtcStreamRequest.md)> |  |  |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## system_info_update_or_create

> crate::models::SystemInfo system_info_update_or_create(pi_id, system_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**system_info_request** | [**SystemInfoRequest**](SystemInfoRequest.md) |  | [required] |

### Return type

[**crate::models::SystemInfo**](SystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## webrtc_stream_update_or_create

> crate::models::WebrtcStream webrtc_stream_update_or_create(pi_id, webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**webrtc_stream_request** | Option<[**WebrtcStreamRequest**](WebrtcStreamRequest.md)> |  |  |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

