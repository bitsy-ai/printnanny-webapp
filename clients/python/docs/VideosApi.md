# printnanny_api_client.VideosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_recordings_create**](VideosApi.md#video_recordings_create) | **POST** /api/video-recordings/ | 
[**video_recordings_list**](VideosApi.md#video_recordings_list) | **GET** /api/video-recordings/ | 
[**video_recordings_partial_update**](VideosApi.md#video_recordings_partial_update) | **PATCH** /api/video-recordings/{id}/ | 
[**video_recordings_retrieve**](VideosApi.md#video_recordings_retrieve) | **GET** /api/video-recordings/{id}/ | 
[**video_recordings_update**](VideosApi.md#video_recordings_update) | **PUT** /api/video-recordings/{id}/ | 
[**video_recordings_update_or_create**](VideosApi.md#video_recordings_update_or_create) | **POST** /api/video-recordings/update-or-create/ | 


# **video_recordings_create**
> VideoRecording video_recordings_create(id=id, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    id = 'id_example' # str |  (optional)
recording_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_status = printnanny_api_client.RecordingStatusEnum() # RecordingStatusEnum |  (optional)
cloud_sync_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_status = printnanny_api_client.CloudSyncStatusEnum() # CloudSyncStatusEnum |  (optional)
gcode_file_name = 'gcode_file_name_example' # str |  (optional)
mp4_file = '/path/to/file' # file |  (optional)

    try:
        api_response = api_instance.video_recordings_create(id=id, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_create: %s\n" % e)
```

* Bearer Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    id = 'id_example' # str |  (optional)
recording_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_status = printnanny_api_client.RecordingStatusEnum() # RecordingStatusEnum |  (optional)
cloud_sync_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_status = printnanny_api_client.CloudSyncStatusEnum() # CloudSyncStatusEnum |  (optional)
gcode_file_name = 'gcode_file_name_example' # str |  (optional)
mp4_file = '/path/to/file' # file |  (optional)

    try:
        api_response = api_instance.video_recordings_create(id=id, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **recording_start** | **datetime**|  | [optional] 
 **recording_end** | **datetime**|  | [optional] 
 **recording_status** | [**RecordingStatusEnum**](RecordingStatusEnum.md)|  | [optional] 
 **cloud_sync_start** | **datetime**|  | [optional] 
 **cloud_sync_end** | **datetime**|  | [optional] 
 **cloud_sync_status** | [**CloudSyncStatusEnum**](CloudSyncStatusEnum.md)|  | [optional] 
 **gcode_file_name** | **str**|  | [optional] 
 **mp4_file** | **file**|  | [optional] 

### Return type

[**VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**409** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_recordings_list**
> PaginatedVideoRecordingList video_recordings_list(page=page)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.video_recordings_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_list: %s\n" % e)
```

* Bearer Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.video_recordings_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedVideoRecordingList**](PaginatedVideoRecordingList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_recordings_partial_update**
> VideoRecording video_recordings_partial_update(id, id2=id2, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    id = 'id_example' # str | A UUID string identifying this video recording.
id2 = 'id_example' # str |  (optional)
recording_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_status = printnanny_api_client.RecordingStatusEnum() # RecordingStatusEnum |  (optional)
cloud_sync_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_status = printnanny_api_client.CloudSyncStatusEnum() # CloudSyncStatusEnum |  (optional)
gcode_file_name = 'gcode_file_name_example' # str |  (optional)
mp4_file = '/path/to/file' # file |  (optional)

    try:
        api_response = api_instance.video_recordings_partial_update(id, id2=id2, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_partial_update: %s\n" % e)
```

* Bearer Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    id = 'id_example' # str | A UUID string identifying this video recording.
id2 = 'id_example' # str |  (optional)
recording_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_status = printnanny_api_client.RecordingStatusEnum() # RecordingStatusEnum |  (optional)
cloud_sync_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_status = printnanny_api_client.CloudSyncStatusEnum() # CloudSyncStatusEnum |  (optional)
gcode_file_name = 'gcode_file_name_example' # str |  (optional)
mp4_file = '/path/to/file' # file |  (optional)

    try:
        api_response = api_instance.video_recordings_partial_update(id, id2=id2, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this video recording. | 
 **id2** | **str**|  | [optional] 
 **recording_start** | **datetime**|  | [optional] 
 **recording_end** | **datetime**|  | [optional] 
 **recording_status** | [**RecordingStatusEnum**](RecordingStatusEnum.md)|  | [optional] 
 **cloud_sync_start** | **datetime**|  | [optional] 
 **cloud_sync_end** | **datetime**|  | [optional] 
 **cloud_sync_status** | [**CloudSyncStatusEnum**](CloudSyncStatusEnum.md)|  | [optional] 
 **gcode_file_name** | **str**|  | [optional] 
 **mp4_file** | **file**|  | [optional] 

### Return type

[**VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**409** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_recordings_retrieve**
> VideoRecording video_recordings_retrieve(id)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    id = 'id_example' # str | A UUID string identifying this video recording.

    try:
        api_response = api_instance.video_recordings_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_retrieve: %s\n" % e)
```

* Bearer Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    id = 'id_example' # str | A UUID string identifying this video recording.

    try:
        api_response = api_instance.video_recordings_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this video recording. | 

### Return type

[**VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_recordings_update**
> VideoRecording video_recordings_update(id, id2=id2, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    id = 'id_example' # str | A UUID string identifying this video recording.
id2 = 'id_example' # str |  (optional)
recording_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_status = printnanny_api_client.RecordingStatusEnum() # RecordingStatusEnum |  (optional)
cloud_sync_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_status = printnanny_api_client.CloudSyncStatusEnum() # CloudSyncStatusEnum |  (optional)
gcode_file_name = 'gcode_file_name_example' # str |  (optional)
mp4_file = '/path/to/file' # file |  (optional)

    try:
        api_response = api_instance.video_recordings_update(id, id2=id2, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_update: %s\n" % e)
```

* Bearer Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    id = 'id_example' # str | A UUID string identifying this video recording.
id2 = 'id_example' # str |  (optional)
recording_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_status = printnanny_api_client.RecordingStatusEnum() # RecordingStatusEnum |  (optional)
cloud_sync_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_status = printnanny_api_client.CloudSyncStatusEnum() # CloudSyncStatusEnum |  (optional)
gcode_file_name = 'gcode_file_name_example' # str |  (optional)
mp4_file = '/path/to/file' # file |  (optional)

    try:
        api_response = api_instance.video_recordings_update(id, id2=id2, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this video recording. | 
 **id2** | **str**|  | [optional] 
 **recording_start** | **datetime**|  | [optional] 
 **recording_end** | **datetime**|  | [optional] 
 **recording_status** | [**RecordingStatusEnum**](RecordingStatusEnum.md)|  | [optional] 
 **cloud_sync_start** | **datetime**|  | [optional] 
 **cloud_sync_end** | **datetime**|  | [optional] 
 **cloud_sync_status** | [**CloudSyncStatusEnum**](CloudSyncStatusEnum.md)|  | [optional] 
 **gcode_file_name** | **str**|  | [optional] 
 **mp4_file** | **file**|  | [optional] 

### Return type

[**VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**409** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_recordings_update_or_create**
> VideoRecording video_recordings_update_or_create(id=id, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    id = 'id_example' # str |  (optional)
recording_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_status = printnanny_api_client.RecordingStatusEnum() # RecordingStatusEnum |  (optional)
cloud_sync_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_status = printnanny_api_client.CloudSyncStatusEnum() # CloudSyncStatusEnum |  (optional)
gcode_file_name = 'gcode_file_name_example' # str |  (optional)
mp4_file = '/path/to/file' # file |  (optional)

    try:
        api_response = api_instance.video_recordings_update_or_create(id=id, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_update_or_create: %s\n" % e)
```

* Bearer Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import printnanny_api_client
from printnanny_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = printnanny_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.VideosApi(api_client)
    id = 'id_example' # str |  (optional)
recording_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
recording_status = printnanny_api_client.RecordingStatusEnum() # RecordingStatusEnum |  (optional)
cloud_sync_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
cloud_sync_status = printnanny_api_client.CloudSyncStatusEnum() # CloudSyncStatusEnum |  (optional)
gcode_file_name = 'gcode_file_name_example' # str |  (optional)
mp4_file = '/path/to/file' # file |  (optional)

    try:
        api_response = api_instance.video_recordings_update_or_create(id=id, recording_start=recording_start, recording_end=recording_end, recording_status=recording_status, cloud_sync_start=cloud_sync_start, cloud_sync_end=cloud_sync_end, cloud_sync_status=cloud_sync_status, gcode_file_name=gcode_file_name, mp4_file=mp4_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideosApi->video_recordings_update_or_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **recording_start** | **datetime**|  | [optional] 
 **recording_end** | **datetime**|  | [optional] 
 **recording_status** | [**RecordingStatusEnum**](RecordingStatusEnum.md)|  | [optional] 
 **cloud_sync_start** | **datetime**|  | [optional] 
 **cloud_sync_end** | **datetime**|  | [optional] 
 **cloud_sync_status** | [**CloudSyncStatusEnum**](CloudSyncStatusEnum.md)|  | [optional] 
 **gcode_file_name** | **str**|  | [optional] 
 **mp4_file** | **file**|  | [optional] 

### Return type

[**VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**202** |  |  -  |
**409** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**500** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

