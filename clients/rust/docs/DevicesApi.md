# \DevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudiot_device_update_or_create**](DevicesApi.md#cloudiot_device_update_or_create) | **POST** /api/devices/{device_id}/cloudiot/update-or-create/ | 
[**devices_cloudiot_create**](DevicesApi.md#devices_cloudiot_create) | **POST** /api/devices/{device_id}/cloudiot/ | 
[**devices_cloudiot_list**](DevicesApi.md#devices_cloudiot_list) | **GET** /api/devices/{device_id}/cloudiot/ | 
[**devices_cloudiot_partial_update**](DevicesApi.md#devices_cloudiot_partial_update) | **PATCH** /api/devices/{device_id}/cloudiot/{id}/ | 
[**devices_cloudiot_retrieve**](DevicesApi.md#devices_cloudiot_retrieve) | **GET** /api/devices/{device_id}/cloudiot/{id}/ | 
[**devices_cloudiot_update**](DevicesApi.md#devices_cloudiot_update) | **PUT** /api/devices/{device_id}/cloudiot/{id}/ | 
[**devices_config_download_retrieve**](DevicesApi.md#devices_config_download_retrieve) | **GET** /api/devices/{device_id}/config/download/ | 
[**devices_create**](DevicesApi.md#devices_create) | **POST** /api/devices/ | 
[**devices_list**](DevicesApi.md#devices_list) | **GET** /api/devices/ | 
[**devices_partial_update**](DevicesApi.md#devices_partial_update) | **PATCH** /api/devices/{id}/ | 
[**devices_public_keys_create**](DevicesApi.md#devices_public_keys_create) | **POST** /api/devices/{device_id}/public-keys/ | 
[**devices_public_keys_list**](DevicesApi.md#devices_public_keys_list) | **GET** /api/devices/{device_id}/public-keys/ | 
[**devices_public_keys_partial_update**](DevicesApi.md#devices_public_keys_partial_update) | **PATCH** /api/devices/{device_id}/public-keys/{id}/ | 
[**devices_public_keys_retrieve**](DevicesApi.md#devices_public_keys_retrieve) | **GET** /api/devices/{device_id}/public-keys/{id}/ | 
[**devices_public_keys_update**](DevicesApi.md#devices_public_keys_update) | **PUT** /api/devices/{device_id}/public-keys/{id}/ | 
[**devices_retrieve**](DevicesApi.md#devices_retrieve) | **GET** /api/devices/{id}/ | 
[**devices_retrieve_hostname**](DevicesApi.md#devices_retrieve_hostname) | **GET** /api/devices/{hostname} | 
[**devices_settings_create**](DevicesApi.md#devices_settings_create) | **POST** /api/devices/{device_id}/settings/ | 
[**devices_settings_list**](DevicesApi.md#devices_settings_list) | **GET** /api/devices/{device_id}/settings/ | 
[**devices_settings_partial_update**](DevicesApi.md#devices_settings_partial_update) | **PATCH** /api/devices/{device_id}/settings/{id}/ | 
[**devices_settings_retrieve**](DevicesApi.md#devices_settings_retrieve) | **GET** /api/devices/{device_id}/settings/{id}/ | 
[**devices_settings_update**](DevicesApi.md#devices_settings_update) | **PUT** /api/devices/{device_id}/settings/{id}/ | 
[**devices_system_info_create**](DevicesApi.md#devices_system_info_create) | **POST** /api/devices/{device_id}/system-info/ | 
[**devices_system_info_list**](DevicesApi.md#devices_system_info_list) | **GET** /api/devices/{device_id}/system-info/ | 
[**devices_system_info_partial_update**](DevicesApi.md#devices_system_info_partial_update) | **PATCH** /api/devices/{device_id}/system-info/{id}/ | 
[**devices_system_info_retrieve**](DevicesApi.md#devices_system_info_retrieve) | **GET** /api/devices/{device_id}/system-info/{id}/ | 
[**devices_system_info_update**](DevicesApi.md#devices_system_info_update) | **PUT** /api/devices/{device_id}/system-info/{id}/ | 
[**devices_update**](DevicesApi.md#devices_update) | **PUT** /api/devices/{id}/ | 
[**devices_webrtc_streams_create**](DevicesApi.md#devices_webrtc_streams_create) | **POST** /api/devices/{device_id}/webrtc-streams/ | 
[**devices_webrtc_streams_list**](DevicesApi.md#devices_webrtc_streams_list) | **GET** /api/devices/{device_id}/webrtc-streams/ | 
[**devices_webrtc_streams_partial_update**](DevicesApi.md#devices_webrtc_streams_partial_update) | **PATCH** /api/devices/{device_id}/webrtc-streams/{id}/ | 
[**devices_webrtc_streams_retrieve**](DevicesApi.md#devices_webrtc_streams_retrieve) | **GET** /api/devices/{device_id}/webrtc-streams/{id}/ | 
[**devices_webrtc_streams_update**](DevicesApi.md#devices_webrtc_streams_update) | **PUT** /api/devices/{device_id}/webrtc-streams/{id}/ | 
[**public_key_update_or_create**](DevicesApi.md#public_key_update_or_create) | **POST** /api/devices/{device_id}/public-keys/update-or-create/ | 
[**system_info_update_or_create**](DevicesApi.md#system_info_update_or_create) | **POST** /api/devices/{device_id}/system-info/update-or-create/ | 



## cloudiot_device_update_or_create

> crate::models::CloudiotDevice cloudiot_device_update_or_create(device_id, cloudiot_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**cloudiot_device_request** | [**CloudiotDeviceRequest**](CloudiotDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::CloudiotDevice**](CloudiotDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloudiot_create

> crate::models::CloudiotDevice devices_cloudiot_create(device_id, cloudiot_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**cloudiot_device_request** | [**CloudiotDeviceRequest**](CloudiotDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::CloudiotDevice**](CloudiotDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloudiot_list

> crate::models::PaginatedCloudiotDeviceList devices_cloudiot_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedCloudiotDeviceList**](PaginatedCloudiotDeviceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloudiot_partial_update

> crate::models::CloudiotDevice devices_cloudiot_partial_update(device_id, id, patched_cloudiot_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **String** |  | [required] |
**patched_cloudiot_device_request** | Option<[**PatchedCloudiotDeviceRequest**](PatchedCloudiotDeviceRequest.md)> |  |  |

### Return type

[**crate::models::CloudiotDevice**](CloudiotDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloudiot_retrieve

> crate::models::CloudiotDevice devices_cloudiot_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** |  | [required] |

### Return type

[**crate::models::CloudiotDevice**](CloudiotDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_cloudiot_update

> crate::models::CloudiotDevice devices_cloudiot_update(device_id, id, cloudiot_device_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **String** |  | [required] |
**cloudiot_device_request** | [**CloudiotDeviceRequest**](CloudiotDeviceRequest.md) |  | [required] |

### Return type

[**crate::models::CloudiotDevice**](CloudiotDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_config_download_retrieve

> crate::models::Config devices_config_download_retrieve(device_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |

### Return type

[**crate::models::Config**](Config.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_create

> crate::models::Device devices_create(device_request)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_request** | [**DeviceRequest**](DeviceRequest.md) |  | [required] |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_list

> crate::models::PaginatedDeviceList devices_list(page)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedDeviceList**](PaginatedDeviceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_partial_update

> crate::models::Device devices_partial_update(id, patched_device_request)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this device. | [required] |
**patched_device_request** | Option<[**PatchedDeviceRequest**](PatchedDeviceRequest.md)> |  |  |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_public_keys_create

> crate::models::PublicKey devices_public_keys_create(device_id, public_key_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**public_key_request** | [**PublicKeyRequest**](PublicKeyRequest.md) |  | [required] |

### Return type

[**crate::models::PublicKey**](PublicKey.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_public_keys_list

> crate::models::PaginatedPublicKeyList devices_public_keys_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPublicKeyList**](PaginatedPublicKeyList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_public_keys_partial_update

> crate::models::PublicKey devices_public_keys_partial_update(device_id, id, patched_public_key_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this public key. | [required] |
**patched_public_key_request** | Option<[**PatchedPublicKeyRequest**](PatchedPublicKeyRequest.md)> |  |  |

### Return type

[**crate::models::PublicKey**](PublicKey.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_public_keys_retrieve

> crate::models::PublicKey devices_public_keys_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this public key. | [required] |

### Return type

[**crate::models::PublicKey**](PublicKey.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_public_keys_update

> crate::models::PublicKey devices_public_keys_update(device_id, id, public_key_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this public key. | [required] |
**public_key_request** | [**PublicKeyRequest**](PublicKeyRequest.md) |  | [required] |

### Return type

[**crate::models::PublicKey**](PublicKey.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_retrieve

> crate::models::Device devices_retrieve(id)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this device. | [required] |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_retrieve_hostname

> crate::models::Device devices_retrieve_hostname(hostname)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hostname** | **String** |  | [required] |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_settings_create

> crate::models::DeviceSettings devices_settings_create(device_id, device_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**device_settings_request** | [**DeviceSettingsRequest**](DeviceSettingsRequest.md) |  | [required] |

### Return type

[**crate::models::DeviceSettings**](DeviceSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_settings_list

> crate::models::PaginatedDeviceSettingsList devices_settings_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedDeviceSettingsList**](PaginatedDeviceSettingsList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_settings_partial_update

> crate::models::DeviceSettings devices_settings_partial_update(device_id, id, patched_device_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this device settings. | [required] |
**patched_device_settings_request** | Option<[**PatchedDeviceSettingsRequest**](PatchedDeviceSettingsRequest.md)> |  |  |

### Return type

[**crate::models::DeviceSettings**](DeviceSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_settings_retrieve

> crate::models::DeviceSettings devices_settings_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this device settings. | [required] |

### Return type

[**crate::models::DeviceSettings**](DeviceSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_settings_update

> crate::models::DeviceSettings devices_settings_update(device_id, id, device_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this device settings. | [required] |
**device_settings_request** | [**DeviceSettingsRequest**](DeviceSettingsRequest.md) |  | [required] |

### Return type

[**crate::models::DeviceSettings**](DeviceSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_system_info_create

> crate::models::SystemInfo devices_system_info_create(device_id, system_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**system_info_request** | [**SystemInfoRequest**](SystemInfoRequest.md) |  | [required] |

### Return type

[**crate::models::SystemInfo**](SystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_system_info_list

> crate::models::PaginatedSystemInfoList devices_system_info_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedSystemInfoList**](PaginatedSystemInfoList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_system_info_partial_update

> crate::models::SystemInfo devices_system_info_partial_update(device_id, id, patched_system_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this system info. | [required] |
**patched_system_info_request** | Option<[**PatchedSystemInfoRequest**](PatchedSystemInfoRequest.md)> |  |  |

### Return type

[**crate::models::SystemInfo**](SystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_system_info_retrieve

> crate::models::SystemInfo devices_system_info_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this system info. | [required] |

### Return type

[**crate::models::SystemInfo**](SystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_system_info_update

> crate::models::SystemInfo devices_system_info_update(device_id, id, system_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this system info. | [required] |
**system_info_request** | [**SystemInfoRequest**](SystemInfoRequest.md) |  | [required] |

### Return type

[**crate::models::SystemInfo**](SystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_update

> crate::models::Device devices_update(id, device_request)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this device. | [required] |
**device_request** | Option<[**DeviceRequest**](DeviceRequest.md)> |  |  |

### Return type

[**crate::models::Device**](Device.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_webrtc_streams_create

> crate::models::WebrtcStream devices_webrtc_streams_create(device_id, webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**webrtc_stream_request** | Option<[**WebrtcStreamRequest**](WebrtcStreamRequest.md)> |  |  |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_webrtc_streams_list

> crate::models::PaginatedWebrtcStreamList devices_webrtc_streams_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedWebrtcStreamList**](PaginatedWebrtcStreamList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_webrtc_streams_partial_update

> crate::models::WebrtcStream devices_webrtc_streams_partial_update(device_id, id, patched_webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this webrtc stream. | [required] |
**patched_webrtc_stream_request** | Option<[**PatchedWebrtcStreamRequest**](PatchedWebrtcStreamRequest.md)> |  |  |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_webrtc_streams_retrieve

> crate::models::WebrtcStream devices_webrtc_streams_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this webrtc stream. | [required] |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_webrtc_streams_update

> crate::models::WebrtcStream devices_webrtc_streams_update(device_id, id, webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this webrtc stream. | [required] |
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

> crate::models::PublicKey public_key_update_or_create(device_id, public_key_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
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

> crate::models::SystemInfo system_info_update_or_create(device_id, system_info_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**system_info_request** | [**SystemInfoRequest**](SystemInfoRequest.md) |  | [required] |

### Return type

[**crate::models::SystemInfo**](SystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

