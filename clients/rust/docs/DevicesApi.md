# \DevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pis_create**](DevicesApi.md#pis_create) | **POST** /api/pis/ | 
[**pis_destroy**](DevicesApi.md#pis_destroy) | **DELETE** /api/pis/{id}/ | 
[**pis_license_cloud_api_retrieve**](DevicesApi.md#pis_license_cloud_api_retrieve) | **GET** /api/pis/{pi_id}/license/cloud-api/ | 
[**pis_license_zip_retrieve**](DevicesApi.md#pis_license_zip_retrieve) | **GET** /api/pis/{pi_id}/license/zip/ | 
[**pis_list**](DevicesApi.md#pis_list) | **GET** /api/pis/ | 
[**pis_partial_update**](DevicesApi.md#pis_partial_update) | **PATCH** /api/pis/{id}/ | 
[**pis_public_keys_create**](DevicesApi.md#pis_public_keys_create) | **POST** /api/pis/{pi_id}/public-keys/ | 
[**pis_public_keys_list**](DevicesApi.md#pis_public_keys_list) | **GET** /api/pis/{pi_id}/public-keys/ | 
[**pis_public_keys_partial_update**](DevicesApi.md#pis_public_keys_partial_update) | **PATCH** /api/pis/{pi_id}/public-keys/{id}/ | 
[**pis_public_keys_retrieve**](DevicesApi.md#pis_public_keys_retrieve) | **GET** /api/pis/{pi_id}/public-keys/{id}/ | 
[**pis_public_keys_update**](DevicesApi.md#pis_public_keys_update) | **PUT** /api/pis/{pi_id}/public-keys/{id}/ | 
[**pis_retrieve**](DevicesApi.md#pis_retrieve) | **GET** /api/pis/{id}/ | 
[**pis_settings_create**](DevicesApi.md#pis_settings_create) | **POST** /api/pis/{pi_id}/settings/ | 
[**pis_settings_list**](DevicesApi.md#pis_settings_list) | **GET** /api/pis/{pi_id}/settings/ | 
[**pis_settings_partial_update**](DevicesApi.md#pis_settings_partial_update) | **PATCH** /api/pis/{pi_id}/settings/{id}/ | 
[**pis_settings_retrieve**](DevicesApi.md#pis_settings_retrieve) | **GET** /api/pis/{pi_id}/settings/{id}/ | 
[**pis_settings_update**](DevicesApi.md#pis_settings_update) | **PUT** /api/pis/{pi_id}/settings/{id}/ | 
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
[**public_key_update_or_create**](DevicesApi.md#public_key_update_or_create) | **POST** /api/pis/{pi_id}/public-keys/update-or-create/ | 
[**system_info_update_or_create**](DevicesApi.md#system_info_update_or_create) | **POST** /api/pis/{pi_id}/system-info/update-or-create/ | 



## pis_create

> crate::models::Pi pis_create(pi_request)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_request** | [**PiRequest**](PiRequest.md) |  | [required] |

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


## pis_license_cloud_api_retrieve

> crate::models::PrintNannyLicense pis_license_cloud_api_retrieve(pi_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |

### Return type

[**crate::models::PrintNannyLicense**](PrintNannyLicense.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

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


## pis_public_keys_create

> crate::models::PublicKey pis_public_keys_create(pi_id, public_key_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**public_key_request** | [**PublicKeyRequest**](PublicKeyRequest.md) |  | [required] |

### Return type

[**crate::models::PublicKey**](PublicKey.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_public_keys_list

> crate::models::PaginatedPublicKeyList pis_public_keys_list(pi_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPublicKeyList**](PaginatedPublicKeyList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_public_keys_partial_update

> crate::models::PublicKey pis_public_keys_partial_update(id, pi_id, patched_public_key_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this public key. | [required] |
**pi_id** | **i32** |  | [required] |
**patched_public_key_request** | Option<[**PatchedPublicKeyRequest**](PatchedPublicKeyRequest.md)> |  |  |

### Return type

[**crate::models::PublicKey**](PublicKey.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_public_keys_retrieve

> crate::models::PublicKey pis_public_keys_retrieve(id, pi_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this public key. | [required] |
**pi_id** | **i32** |  | [required] |

### Return type

[**crate::models::PublicKey**](PublicKey.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_public_keys_update

> crate::models::PublicKey pis_public_keys_update(id, pi_id, public_key_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this public key. | [required] |
**pi_id** | **i32** |  | [required] |
**public_key_request** | [**PublicKeyRequest**](PublicKeyRequest.md) |  | [required] |

### Return type

[**crate::models::PublicKey**](PublicKey.md)

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


## pis_settings_create

> crate::models::PiSettings pis_settings_create(pi_id, pi_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**pi_settings_request** | [**PiSettingsRequest**](PiSettingsRequest.md) |  | [required] |

### Return type

[**crate::models::PiSettings**](PiSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_settings_list

> crate::models::PaginatedPiSettingsList pis_settings_list(pi_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPiSettingsList**](PaginatedPiSettingsList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_settings_partial_update

> crate::models::PiSettings pis_settings_partial_update(id, pi_id, patched_pi_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this pi settings. | [required] |
**pi_id** | **i32** |  | [required] |
**patched_pi_settings_request** | Option<[**PatchedPiSettingsRequest**](PatchedPiSettingsRequest.md)> |  |  |

### Return type

[**crate::models::PiSettings**](PiSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_settings_retrieve

> crate::models::PiSettings pis_settings_retrieve(id, pi_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this pi settings. | [required] |
**pi_id** | **i32** |  | [required] |

### Return type

[**crate::models::PiSettings**](PiSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_settings_update

> crate::models::PiSettings pis_settings_update(id, pi_id, pi_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this pi settings. | [required] |
**pi_id** | **i32** |  | [required] |
**pi_settings_request** | [**PiSettingsRequest**](PiSettingsRequest.md) |  | [required] |

### Return type

[**crate::models::PiSettings**](PiSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
**pi_request** | [**PiRequest**](PiRequest.md) |  | [required] |

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


## public_key_update_or_create

> crate::models::PublicKey public_key_update_or_create(pi_id, public_key_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**public_key_request** | [**PublicKeyRequest**](PublicKeyRequest.md) |  | [required] |

### Return type

[**crate::models::PublicKey**](PublicKey.md)

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

