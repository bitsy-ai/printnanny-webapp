# printnanny_api_client.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_events_create**](EventsApi.md#devices_events_create) | **POST** /api/devices/{device_id}/events/ | 
[**devices_events_list**](EventsApi.md#devices_events_list) | **GET** /api/devices/{device_id}/events/ | 
[**devices_events_partial_update**](EventsApi.md#devices_events_partial_update) | **PATCH** /api/devices/{device_id}/events/{id}/ | 
[**devices_events_retrieve**](EventsApi.md#devices_events_retrieve) | **GET** /api/devices/{device_id}/events/{id}/ | 
[**devices_events_update**](EventsApi.md#devices_events_update) | **PUT** /api/devices/{device_id}/events/{id}/ | 


# **devices_events_create**
> PolymorphicEvent devices_events_create(device_id, polymorphic_event_request=polymorphic_event_request)



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
    api_instance = printnanny_api_client.EventsApi(api_client)
    device_id = 56 # int | 
polymorphic_event_request = printnanny_api_client.PolymorphicEventRequest() # PolymorphicEventRequest |  (optional)

    try:
        api_response = api_instance.devices_events_create(device_id, polymorphic_event_request=polymorphic_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->devices_events_create: %s\n" % e)
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
    api_instance = printnanny_api_client.EventsApi(api_client)
    device_id = 56 # int | 
polymorphic_event_request = printnanny_api_client.PolymorphicEventRequest() # PolymorphicEventRequest |  (optional)

    try:
        api_response = api_instance.devices_events_create(device_id, polymorphic_event_request=polymorphic_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->devices_events_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **polymorphic_event_request** | [**PolymorphicEventRequest**](PolymorphicEventRequest.md)|  | [optional] 

### Return type

[**PolymorphicEvent**](PolymorphicEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_events_list**
> PaginatedPolymorphicEventList devices_events_list(device_id, page=page)



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
    api_instance = printnanny_api_client.EventsApi(api_client)
    device_id = 56 # int | 
page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.devices_events_list(device_id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->devices_events_list: %s\n" % e)
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
    api_instance = printnanny_api_client.EventsApi(api_client)
    device_id = 56 # int | 
page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.devices_events_list(device_id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->devices_events_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedPolymorphicEventList**](PaginatedPolymorphicEventList.md)

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

# **devices_events_partial_update**
> PolymorphicEvent devices_events_partial_update(device_id, id, patched_polymorphic_event_request=patched_polymorphic_event_request)



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
    api_instance = printnanny_api_client.EventsApi(api_client)
    device_id = 56 # int | 
id = 56 # int | A unique integer value identifying this device event.
patched_polymorphic_event_request = printnanny_api_client.PatchedPolymorphicEventRequest() # PatchedPolymorphicEventRequest |  (optional)

    try:
        api_response = api_instance.devices_events_partial_update(device_id, id, patched_polymorphic_event_request=patched_polymorphic_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->devices_events_partial_update: %s\n" % e)
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
    api_instance = printnanny_api_client.EventsApi(api_client)
    device_id = 56 # int | 
id = 56 # int | A unique integer value identifying this device event.
patched_polymorphic_event_request = printnanny_api_client.PatchedPolymorphicEventRequest() # PatchedPolymorphicEventRequest |  (optional)

    try:
        api_response = api_instance.devices_events_partial_update(device_id, id, patched_polymorphic_event_request=patched_polymorphic_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->devices_events_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**| A unique integer value identifying this device event. | 
 **patched_polymorphic_event_request** | [**PatchedPolymorphicEventRequest**](PatchedPolymorphicEventRequest.md)|  | [optional] 

### Return type

[**PolymorphicEvent**](PolymorphicEvent.md)

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

# **devices_events_retrieve**
> PolymorphicEvent devices_events_retrieve(device_id, id)



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
    api_instance = printnanny_api_client.EventsApi(api_client)
    device_id = 56 # int | 
id = 56 # int | A unique integer value identifying this device event.

    try:
        api_response = api_instance.devices_events_retrieve(device_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->devices_events_retrieve: %s\n" % e)
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
    api_instance = printnanny_api_client.EventsApi(api_client)
    device_id = 56 # int | 
id = 56 # int | A unique integer value identifying this device event.

    try:
        api_response = api_instance.devices_events_retrieve(device_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->devices_events_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**| A unique integer value identifying this device event. | 

### Return type

[**PolymorphicEvent**](PolymorphicEvent.md)

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

# **devices_events_update**
> PolymorphicEvent devices_events_update(device_id, id, polymorphic_event_request=polymorphic_event_request)



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
    api_instance = printnanny_api_client.EventsApi(api_client)
    device_id = 56 # int | 
id = 56 # int | A unique integer value identifying this device event.
polymorphic_event_request = printnanny_api_client.PolymorphicEventRequest() # PolymorphicEventRequest |  (optional)

    try:
        api_response = api_instance.devices_events_update(device_id, id, polymorphic_event_request=polymorphic_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->devices_events_update: %s\n" % e)
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
    api_instance = printnanny_api_client.EventsApi(api_client)
    device_id = 56 # int | 
id = 56 # int | A unique integer value identifying this device event.
polymorphic_event_request = printnanny_api_client.PolymorphicEventRequest() # PolymorphicEventRequest |  (optional)

    try:
        api_response = api_instance.devices_events_update(device_id, id, polymorphic_event_request=polymorphic_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->devices_events_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**| A unique integer value identifying this device event. | 
 **polymorphic_event_request** | [**PolymorphicEventRequest**](PolymorphicEventRequest.md)|  | [optional] 

### Return type

[**PolymorphicEvent**](PolymorphicEvent.md)

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

