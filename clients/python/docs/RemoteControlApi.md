# print_nanny_client.RemoteControlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commands_list**](RemoteControlApi.md#commands_list) | **GET** /api/commands/ | 
[**commands_partial_update**](RemoteControlApi.md#commands_partial_update) | **PATCH** /api/commands/{id}/ | 
[**commands_retrieve**](RemoteControlApi.md#commands_retrieve) | **GET** /api/commands/{id}/ | 
[**commands_update**](RemoteControlApi.md#commands_update) | **PUT** /api/commands/{id}/ | 
[**gcode_files_create**](RemoteControlApi.md#gcode_files_create) | **POST** /api/gcode-files/ | 
[**gcode_files_list**](RemoteControlApi.md#gcode_files_list) | **GET** /api/gcode-files/ | 
[**gcode_files_partial_update**](RemoteControlApi.md#gcode_files_partial_update) | **PATCH** /api/gcode-files/{id}/ | 
[**gcode_files_retrieve**](RemoteControlApi.md#gcode_files_retrieve) | **GET** /api/gcode-files/{id}/ | 
[**gcode_files_update**](RemoteControlApi.md#gcode_files_update) | **PUT** /api/gcode-files/{id}/ | 
[**gcode_files_update_or_create**](RemoteControlApi.md#gcode_files_update_or_create) | **POST** /api/gcode-files/update-or-create/ | 
[**octoprint_devices_create**](RemoteControlApi.md#octoprint_devices_create) | **POST** /api/octoprint-devices/ | 
[**octoprint_devices_list**](RemoteControlApi.md#octoprint_devices_list) | **GET** /api/octoprint-devices/ | 
[**octoprint_devices_partial_update**](RemoteControlApi.md#octoprint_devices_partial_update) | **PATCH** /api/octoprint-devices/{id}/ | 
[**octoprint_devices_retrieve**](RemoteControlApi.md#octoprint_devices_retrieve) | **GET** /api/octoprint-devices/{id}/ | 
[**octoprint_devices_update**](RemoteControlApi.md#octoprint_devices_update) | **PUT** /api/octoprint-devices/{id}/ | 
[**octoprint_devices_update_or_create**](RemoteControlApi.md#octoprint_devices_update_or_create) | **POST** /api/octoprint-devices/update-or-create/ | 
[**print_jobs_create**](RemoteControlApi.md#print_jobs_create) | **POST** /api/print-jobs/ | 
[**print_jobs_list**](RemoteControlApi.md#print_jobs_list) | **GET** /api/print-jobs/ | 
[**print_jobs_partial_update**](RemoteControlApi.md#print_jobs_partial_update) | **PATCH** /api/print-jobs/{id}/ | 
[**print_jobs_retrieve**](RemoteControlApi.md#print_jobs_retrieve) | **GET** /api/print-jobs/{id}/ | 
[**print_jobs_update**](RemoteControlApi.md#print_jobs_update) | **PUT** /api/print-jobs/{id}/ | 
[**printer_profiles_create**](RemoteControlApi.md#printer_profiles_create) | **POST** /api/printer-profiles/ | 
[**printer_profiles_list**](RemoteControlApi.md#printer_profiles_list) | **GET** /api/printer-profiles/ | 
[**printer_profiles_partial_update**](RemoteControlApi.md#printer_profiles_partial_update) | **PATCH** /api/printer-profiles/{id}/ | 
[**printer_profiles_retrieve**](RemoteControlApi.md#printer_profiles_retrieve) | **GET** /api/printer-profiles/{id}/ | 
[**printer_profiles_update**](RemoteControlApi.md#printer_profiles_update) | **PUT** /api/printer-profiles/{id}/ | 
[**printer_profiles_update_or_create**](RemoteControlApi.md#printer_profiles_update_or_create) | **POST** /api/printer-profiles/update-or-create/ | 
[**snapshots_create**](RemoteControlApi.md#snapshots_create) | **POST** /api/snapshots/ | 
[**snapshots_list**](RemoteControlApi.md#snapshots_list) | **GET** /api/snapshots/ | 
[**snapshots_partial_update**](RemoteControlApi.md#snapshots_partial_update) | **PATCH** /api/snapshots/{id}/ | 
[**snapshots_retrieve**](RemoteControlApi.md#snapshots_retrieve) | **GET** /api/snapshots/{id}/ | 
[**snapshots_update**](RemoteControlApi.md#snapshots_update) | **PUT** /api/snapshots/{id}/ | 
[**valid_commands_retrieve**](RemoteControlApi.md#valid_commands_retrieve) | **GET** /api/commands/valid/ | 


# **commands_list**
> PaginatedRemoteControlCommandList commands_list(page=page)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.commands_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->commands_list: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.commands_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->commands_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedRemoteControlCommandList**](PaginatedRemoteControlCommandList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_partial_update**
> RemoteControlCommand commands_partial_update(id, patched_remote_control_command_request=patched_remote_control_command_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control command.
patched_remote_control_command_request = print_nanny_client.PatchedRemoteControlCommandRequest() # PatchedRemoteControlCommandRequest |  (optional)

    try:
        api_response = api_instance.commands_partial_update(id, patched_remote_control_command_request=patched_remote_control_command_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->commands_partial_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control command.
patched_remote_control_command_request = print_nanny_client.PatchedRemoteControlCommandRequest() # PatchedRemoteControlCommandRequest |  (optional)

    try:
        api_response = api_instance.commands_partial_update(id, patched_remote_control_command_request=patched_remote_control_command_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->commands_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this remote control command. | 
 **patched_remote_control_command_request** | [**PatchedRemoteControlCommandRequest**](PatchedRemoteControlCommandRequest.md)|  | [optional] 

### Return type

[**RemoteControlCommand**](RemoteControlCommand.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_retrieve**
> RemoteControlCommand commands_retrieve(id)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control command.

    try:
        api_response = api_instance.commands_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->commands_retrieve: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control command.

    try:
        api_response = api_instance.commands_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->commands_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this remote control command. | 

### Return type

[**RemoteControlCommand**](RemoteControlCommand.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_update**
> RemoteControlCommand commands_update(id, remote_control_command_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control command.
remote_control_command_request = print_nanny_client.RemoteControlCommandRequest() # RemoteControlCommandRequest | 

    try:
        api_response = api_instance.commands_update(id, remote_control_command_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->commands_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control command.
remote_control_command_request = print_nanny_client.RemoteControlCommandRequest() # RemoteControlCommandRequest | 

    try:
        api_response = api_instance.commands_update(id, remote_control_command_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->commands_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this remote control command. | 
 **remote_control_command_request** | [**RemoteControlCommandRequest**](RemoteControlCommandRequest.md)|  | 

### Return type

[**RemoteControlCommand**](RemoteControlCommand.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gcode_files_create**
> GcodeFile gcode_files_create(name, file, file_hash, octoprint_device)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    name = 'name_example' # str | 
file = '/path/to/file' # file | 
file_hash = 'file_hash_example' # str | 
octoprint_device = 'octoprint_device_example' # str | 

    try:
        api_response = api_instance.gcode_files_create(name, file, file_hash, octoprint_device)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_create: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    name = 'name_example' # str | 
file = '/path/to/file' # file | 
file_hash = 'file_hash_example' # str | 
octoprint_device = 'octoprint_device_example' # str | 

    try:
        api_response = api_instance.gcode_files_create(name, file, file_hash, octoprint_device)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **file** | **file**|  | 
 **file_hash** | **str**|  | 
 **octoprint_device** | **str**|  | 

### Return type

[**GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gcode_files_list**
> PaginatedGcodeFileList gcode_files_list(page=page)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.gcode_files_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_list: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.gcode_files_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedGcodeFileList**](PaginatedGcodeFileList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gcode_files_partial_update**
> GcodeFile gcode_files_partial_update(id, name=name, file=file, file_hash=file_hash, octoprint_device=octoprint_device)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this gcode file.
name = 'name_example' # str |  (optional)
file = '/path/to/file' # file |  (optional)
file_hash = 'file_hash_example' # str |  (optional)
octoprint_device = 'octoprint_device_example' # str |  (optional)

    try:
        api_response = api_instance.gcode_files_partial_update(id, name=name, file=file, file_hash=file_hash, octoprint_device=octoprint_device)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_partial_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this gcode file.
name = 'name_example' # str |  (optional)
file = '/path/to/file' # file |  (optional)
file_hash = 'file_hash_example' # str |  (optional)
octoprint_device = 'octoprint_device_example' # str |  (optional)

    try:
        api_response = api_instance.gcode_files_partial_update(id, name=name, file=file, file_hash=file_hash, octoprint_device=octoprint_device)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this gcode file. | 
 **name** | **str**|  | [optional] 
 **file** | **file**|  | [optional] 
 **file_hash** | **str**|  | [optional] 
 **octoprint_device** | **str**|  | [optional] 

### Return type

[**GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gcode_files_retrieve**
> GcodeFile gcode_files_retrieve(id)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this gcode file.

    try:
        api_response = api_instance.gcode_files_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_retrieve: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this gcode file.

    try:
        api_response = api_instance.gcode_files_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this gcode file. | 

### Return type

[**GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gcode_files_update**
> GcodeFile gcode_files_update(id, name, file, file_hash, octoprint_device)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this gcode file.
name = 'name_example' # str | 
file = '/path/to/file' # file | 
file_hash = 'file_hash_example' # str | 
octoprint_device = 'octoprint_device_example' # str | 

    try:
        api_response = api_instance.gcode_files_update(id, name, file, file_hash, octoprint_device)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this gcode file.
name = 'name_example' # str | 
file = '/path/to/file' # file | 
file_hash = 'file_hash_example' # str | 
octoprint_device = 'octoprint_device_example' # str | 

    try:
        api_response = api_instance.gcode_files_update(id, name, file, file_hash, octoprint_device)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this gcode file. | 
 **name** | **str**|  | 
 **file** | **file**|  | 
 **file_hash** | **str**|  | 
 **octoprint_device** | **str**|  | 

### Return type

[**GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gcode_files_update_or_create**
> GcodeFile gcode_files_update_or_create(name, file, file_hash, octoprint_device)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    name = 'name_example' # str | 
file = '/path/to/file' # file | 
file_hash = 'file_hash_example' # str | 
octoprint_device = 'octoprint_device_example' # str | 

    try:
        api_response = api_instance.gcode_files_update_or_create(name, file, file_hash, octoprint_device)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_update_or_create: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    name = 'name_example' # str | 
file = '/path/to/file' # file | 
file_hash = 'file_hash_example' # str | 
octoprint_device = 'octoprint_device_example' # str | 

    try:
        api_response = api_instance.gcode_files_update_or_create(name, file, file_hash, octoprint_device)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->gcode_files_update_or_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **file** | **file**|  | 
 **file_hash** | **str**|  | 
 **octoprint_device** | **str**|  | 

### Return type

[**GcodeFile**](GcodeFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** |  |  -  |
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octoprint_devices_create**
> OctoPrintDevice octoprint_devices_create(octo_print_device_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    octo_print_device_request = print_nanny_client.OctoPrintDeviceRequest() # OctoPrintDeviceRequest | 

    try:
        api_response = api_instance.octoprint_devices_create(octo_print_device_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_create: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    octo_print_device_request = print_nanny_client.OctoPrintDeviceRequest() # OctoPrintDeviceRequest | 

    try:
        api_response = api_instance.octoprint_devices_create(octo_print_device_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **octo_print_device_request** | [**OctoPrintDeviceRequest**](OctoPrintDeviceRequest.md)|  | 

### Return type

[**OctoPrintDevice**](OctoPrintDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octoprint_devices_list**
> PaginatedOctoPrintDeviceList octoprint_devices_list(page=page)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.octoprint_devices_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_list: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.octoprint_devices_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedOctoPrintDeviceList**](PaginatedOctoPrintDeviceList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octoprint_devices_partial_update**
> OctoPrintDevice octoprint_devices_partial_update(id, patched_octo_print_device_request=patched_octo_print_device_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this octo print device.
patched_octo_print_device_request = print_nanny_client.PatchedOctoPrintDeviceRequest() # PatchedOctoPrintDeviceRequest |  (optional)

    try:
        api_response = api_instance.octoprint_devices_partial_update(id, patched_octo_print_device_request=patched_octo_print_device_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_partial_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this octo print device.
patched_octo_print_device_request = print_nanny_client.PatchedOctoPrintDeviceRequest() # PatchedOctoPrintDeviceRequest |  (optional)

    try:
        api_response = api_instance.octoprint_devices_partial_update(id, patched_octo_print_device_request=patched_octo_print_device_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this octo print device. | 
 **patched_octo_print_device_request** | [**PatchedOctoPrintDeviceRequest**](PatchedOctoPrintDeviceRequest.md)|  | [optional] 

### Return type

[**OctoPrintDevice**](OctoPrintDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** |  |  -  |
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octoprint_devices_retrieve**
> OctoPrintDevice octoprint_devices_retrieve(id)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this octo print device.

    try:
        api_response = api_instance.octoprint_devices_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_retrieve: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this octo print device.

    try:
        api_response = api_instance.octoprint_devices_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this octo print device. | 

### Return type

[**OctoPrintDevice**](OctoPrintDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octoprint_devices_update**
> OctoPrintDevice octoprint_devices_update(id, octo_print_device_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this octo print device.
octo_print_device_request = print_nanny_client.OctoPrintDeviceRequest() # OctoPrintDeviceRequest | 

    try:
        api_response = api_instance.octoprint_devices_update(id, octo_print_device_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this octo print device.
octo_print_device_request = print_nanny_client.OctoPrintDeviceRequest() # OctoPrintDeviceRequest | 

    try:
        api_response = api_instance.octoprint_devices_update(id, octo_print_device_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this octo print device. | 
 **octo_print_device_request** | [**OctoPrintDeviceRequest**](OctoPrintDeviceRequest.md)|  | 

### Return type

[**OctoPrintDevice**](OctoPrintDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** |  |  -  |
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octoprint_devices_update_or_create**
> OctoPrintDevice octoprint_devices_update_or_create(octo_print_device_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    octo_print_device_request = print_nanny_client.OctoPrintDeviceRequest() # OctoPrintDeviceRequest | 

    try:
        api_response = api_instance.octoprint_devices_update_or_create(octo_print_device_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_update_or_create: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    octo_print_device_request = print_nanny_client.OctoPrintDeviceRequest() # OctoPrintDeviceRequest | 

    try:
        api_response = api_instance.octoprint_devices_update_or_create(octo_print_device_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->octoprint_devices_update_or_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **octo_print_device_request** | [**OctoPrintDeviceRequest**](OctoPrintDeviceRequest.md)|  | 

### Return type

[**OctoPrintDevice**](OctoPrintDevice.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** |  |  -  |
**201** |  |  -  |
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **print_jobs_create**
> PrintJob print_jobs_create(print_job_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    print_job_request = print_nanny_client.PrintJobRequest() # PrintJobRequest | 

    try:
        api_response = api_instance.print_jobs_create(print_job_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->print_jobs_create: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    print_job_request = print_nanny_client.PrintJobRequest() # PrintJobRequest | 

    try:
        api_response = api_instance.print_jobs_create(print_job_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->print_jobs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_job_request** | [**PrintJobRequest**](PrintJobRequest.md)|  | 

### Return type

[**PrintJob**](PrintJob.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **print_jobs_list**
> PaginatedPrintJobList print_jobs_list(page=page)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.print_jobs_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->print_jobs_list: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.print_jobs_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->print_jobs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedPrintJobList**](PaginatedPrintJobList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **print_jobs_partial_update**
> PrintJob print_jobs_partial_update(id, patched_print_job_request=patched_print_job_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this print job.
patched_print_job_request = print_nanny_client.PatchedPrintJobRequest() # PatchedPrintJobRequest |  (optional)

    try:
        api_response = api_instance.print_jobs_partial_update(id, patched_print_job_request=patched_print_job_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->print_jobs_partial_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this print job.
patched_print_job_request = print_nanny_client.PatchedPrintJobRequest() # PatchedPrintJobRequest |  (optional)

    try:
        api_response = api_instance.print_jobs_partial_update(id, patched_print_job_request=patched_print_job_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->print_jobs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this print job. | 
 **patched_print_job_request** | [**PatchedPrintJobRequest**](PatchedPrintJobRequest.md)|  | [optional] 

### Return type

[**PrintJob**](PrintJob.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **print_jobs_retrieve**
> PrintJob print_jobs_retrieve(id)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this print job.

    try:
        api_response = api_instance.print_jobs_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->print_jobs_retrieve: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this print job.

    try:
        api_response = api_instance.print_jobs_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->print_jobs_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this print job. | 

### Return type

[**PrintJob**](PrintJob.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **print_jobs_update**
> PrintJob print_jobs_update(id, print_job_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this print job.
print_job_request = print_nanny_client.PrintJobRequest() # PrintJobRequest | 

    try:
        api_response = api_instance.print_jobs_update(id, print_job_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->print_jobs_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this print job.
print_job_request = print_nanny_client.PrintJobRequest() # PrintJobRequest | 

    try:
        api_response = api_instance.print_jobs_update(id, print_job_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->print_jobs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this print job. | 
 **print_job_request** | [**PrintJobRequest**](PrintJobRequest.md)|  | 

### Return type

[**PrintJob**](PrintJob.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **printer_profiles_create**
> PrintJob printer_profiles_create(printer_profile_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    printer_profile_request = print_nanny_client.PrinterProfileRequest() # PrinterProfileRequest | 

    try:
        api_response = api_instance.printer_profiles_create(printer_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_create: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    printer_profile_request = print_nanny_client.PrinterProfileRequest() # PrinterProfileRequest | 

    try:
        api_response = api_instance.printer_profiles_create(printer_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **printer_profile_request** | [**PrinterProfileRequest**](PrinterProfileRequest.md)|  | 

### Return type

[**PrintJob**](PrintJob.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **printer_profiles_list**
> PaginatedPrinterProfileList printer_profiles_list(name=name, page=page, user=user)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    name = 'name_example' # str | name (optional)
page = 56 # int | A page number within the paginated result set. (optional)
user = 'user_example' # str | user (optional)

    try:
        api_response = api_instance.printer_profiles_list(name=name, page=page, user=user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_list: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    name = 'name_example' # str | name (optional)
page = 56 # int | A page number within the paginated result set. (optional)
user = 'user_example' # str | user (optional)

    try:
        api_response = api_instance.printer_profiles_list(name=name, page=page, user=user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **user** | **str**| user | [optional] 

### Return type

[**PaginatedPrinterProfileList**](PaginatedPrinterProfileList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **printer_profiles_partial_update**
> PrinterProfile printer_profiles_partial_update(id, patched_printer_profile_request=patched_printer_profile_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this printer profile.
patched_printer_profile_request = print_nanny_client.PatchedPrinterProfileRequest() # PatchedPrinterProfileRequest |  (optional)

    try:
        api_response = api_instance.printer_profiles_partial_update(id, patched_printer_profile_request=patched_printer_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_partial_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this printer profile.
patched_printer_profile_request = print_nanny_client.PatchedPrinterProfileRequest() # PatchedPrinterProfileRequest |  (optional)

    try:
        api_response = api_instance.printer_profiles_partial_update(id, patched_printer_profile_request=patched_printer_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this printer profile. | 
 **patched_printer_profile_request** | [**PatchedPrinterProfileRequest**](PatchedPrinterProfileRequest.md)|  | [optional] 

### Return type

[**PrinterProfile**](PrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **printer_profiles_retrieve**
> PrinterProfile printer_profiles_retrieve(id)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this printer profile.

    try:
        api_response = api_instance.printer_profiles_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_retrieve: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this printer profile.

    try:
        api_response = api_instance.printer_profiles_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this printer profile. | 

### Return type

[**PrinterProfile**](PrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **printer_profiles_update**
> PrinterProfile printer_profiles_update(id, printer_profile_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this printer profile.
printer_profile_request = print_nanny_client.PrinterProfileRequest() # PrinterProfileRequest | 

    try:
        api_response = api_instance.printer_profiles_update(id, printer_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this printer profile.
printer_profile_request = print_nanny_client.PrinterProfileRequest() # PrinterProfileRequest | 

    try:
        api_response = api_instance.printer_profiles_update(id, printer_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this printer profile. | 
 **printer_profile_request** | [**PrinterProfileRequest**](PrinterProfileRequest.md)|  | 

### Return type

[**PrinterProfile**](PrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **printer_profiles_update_or_create**
> PrinterProfile printer_profiles_update_or_create(printer_profile_request)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    printer_profile_request = print_nanny_client.PrinterProfileRequest() # PrinterProfileRequest | 

    try:
        api_response = api_instance.printer_profiles_update_or_create(printer_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_update_or_create: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    printer_profile_request = print_nanny_client.PrinterProfileRequest() # PrinterProfileRequest | 

    try:
        api_response = api_instance.printer_profiles_update_or_create(printer_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->printer_profiles_update_or_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **printer_profile_request** | [**PrinterProfileRequest**](PrinterProfileRequest.md)|  | 

### Return type

[**PrinterProfile**](PrinterProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** |  |  -  |
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_create**
> RemoteControlSnapshotCreateResponse snapshots_create(image, command)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    image = '/path/to/file' # file | 
command = 56 # int | 

    try:
        api_response = api_instance.snapshots_create(image, command)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->snapshots_create: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    image = '/path/to/file' # file | 
command = 56 # int | 

    try:
        api_response = api_instance.snapshots_create(image, command)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->snapshots_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**|  | 
 **command** | **int**|  | 

### Return type

[**RemoteControlSnapshotCreateResponse**](RemoteControlSnapshotCreateResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_list**
> PaginatedRemoteControlSnapshotList snapshots_list(page=page)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.snapshots_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->snapshots_list: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.snapshots_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->snapshots_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedRemoteControlSnapshotList**](PaginatedRemoteControlSnapshotList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_partial_update**
> RemoteControlSnapshot snapshots_partial_update(id, image=image, command=command)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control snapshot.
image = '/path/to/file' # file |  (optional)
command = 56 # int |  (optional)

    try:
        api_response = api_instance.snapshots_partial_update(id, image=image, command=command)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->snapshots_partial_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control snapshot.
image = '/path/to/file' # file |  (optional)
command = 56 # int |  (optional)

    try:
        api_response = api_instance.snapshots_partial_update(id, image=image, command=command)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->snapshots_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this remote control snapshot. | 
 **image** | **file**|  | [optional] 
 **command** | **int**|  | [optional] 

### Return type

[**RemoteControlSnapshot**](RemoteControlSnapshot.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_retrieve**
> RemoteControlSnapshot snapshots_retrieve(id)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control snapshot.

    try:
        api_response = api_instance.snapshots_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->snapshots_retrieve: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control snapshot.

    try:
        api_response = api_instance.snapshots_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->snapshots_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this remote control snapshot. | 

### Return type

[**RemoteControlSnapshot**](RemoteControlSnapshot.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_update**
> RemoteControlSnapshot snapshots_update(id, image, command)



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control snapshot.
image = '/path/to/file' # file | 
command = 56 # int | 

    try:
        api_response = api_instance.snapshots_update(id, image, command)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->snapshots_update: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    id = 56 # int | A unique integer value identifying this remote control snapshot.
image = '/path/to/file' # file | 
command = 56 # int | 

    try:
        api_response = api_instance.snapshots_update(id, image, command)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->snapshots_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this remote control snapshot. | 
 **image** | **file**|  | 
 **command** | **int**|  | 

### Return type

[**RemoteControlSnapshot**](RemoteControlSnapshot.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **valid_commands_retrieve**
> str valid_commands_retrieve()



### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    
    try:
        api_response = api_instance.valid_commands_retrieve()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->valid_commands_retrieve: %s\n" % e)
```

* Bearer (Bearer) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import print_nanny_client
from print_nanny_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = print_nanny_client.Configuration(
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

# Configure Bearer authorization (Bearer): tokenAuth
configuration = print_nanny_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with print_nanny_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = print_nanny_client.RemoteControlApi(api_client)
    
    try:
        api_response = api_instance.valid_commands_retrieve()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RemoteControlApi->valid_commands_retrieve: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

