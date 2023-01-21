# printnanny_api_client.CrashReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crash_reports_create**](CrashReportsApi.md#crash_reports_create) | **POST** /api/crash-reports/ | 
[**crash_reports_list**](CrashReportsApi.md#crash_reports_list) | **GET** /api/crash-reports/ | 
[**crash_reports_partial_update**](CrashReportsApi.md#crash_reports_partial_update) | **PATCH** /api/crash-reports/{id}/ | 
[**crash_reports_retrieve**](CrashReportsApi.md#crash_reports_retrieve) | **GET** /api/crash-reports/{id}/ | 
[**crash_reports_update**](CrashReportsApi.md#crash_reports_update) | **PUT** /api/crash-reports/{id}/ | 


# **crash_reports_create**
> CrashReport crash_reports_create(description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, status=status, support_comment=support_comment, pi=pi)



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
    api_instance = printnanny_api_client.CrashReportsApi(api_client)
    description = 'description_example' # str |  (optional)
email = 'email_example' # str |  (optional)
os_version = 'os_version_example' # str |  (optional)
os_logs = '/path/to/file' # file |  (optional)
browser_version = 'browser_version_example' # str |  (optional)
browser_logs = '/path/to/file' # file |  (optional)
serial = 'serial_example' # str |  (optional)
posthog_session = 'posthog_session_example' # str |  (optional)
status = printnanny_api_client.CrashReportStatusEnum() # CrashReportStatusEnum |  (optional)
support_comment = 'support_comment_example' # str |  (optional)
pi = 56 # int |  (optional)

    try:
        api_response = api_instance.crash_reports_create(description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, status=status, support_comment=support_comment, pi=pi)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CrashReportsApi->crash_reports_create: %s\n" % e)
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
    api_instance = printnanny_api_client.CrashReportsApi(api_client)
    description = 'description_example' # str |  (optional)
email = 'email_example' # str |  (optional)
os_version = 'os_version_example' # str |  (optional)
os_logs = '/path/to/file' # file |  (optional)
browser_version = 'browser_version_example' # str |  (optional)
browser_logs = '/path/to/file' # file |  (optional)
serial = 'serial_example' # str |  (optional)
posthog_session = 'posthog_session_example' # str |  (optional)
status = printnanny_api_client.CrashReportStatusEnum() # CrashReportStatusEnum |  (optional)
support_comment = 'support_comment_example' # str |  (optional)
pi = 56 # int |  (optional)

    try:
        api_response = api_instance.crash_reports_create(description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, status=status, support_comment=support_comment, pi=pi)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CrashReportsApi->crash_reports_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **os_version** | **str**|  | [optional] 
 **os_logs** | **file**|  | [optional] 
 **browser_version** | **str**|  | [optional] 
 **browser_logs** | **file**|  | [optional] 
 **serial** | **str**|  | [optional] 
 **posthog_session** | **str**|  | [optional] 
 **status** | [**CrashReportStatusEnum**](CrashReportStatusEnum.md)|  | [optional] 
 **support_comment** | **str**|  | [optional] 
 **pi** | **int**|  | [optional] 

### Return type

[**CrashReport**](CrashReport.md)

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

# **crash_reports_list**
> PaginatedCrashReportList crash_reports_list(page=page)



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
    api_instance = printnanny_api_client.CrashReportsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.crash_reports_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CrashReportsApi->crash_reports_list: %s\n" % e)
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
    api_instance = printnanny_api_client.CrashReportsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.crash_reports_list(page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CrashReportsApi->crash_reports_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedCrashReportList**](PaginatedCrashReportList.md)

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

# **crash_reports_partial_update**
> CrashReport crash_reports_partial_update(id, description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, status=status, support_comment=support_comment, pi=pi)



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
    api_instance = printnanny_api_client.CrashReportsApi(api_client)
    id = 'id_example' # str | A UUID string identifying this crash report.
description = 'description_example' # str |  (optional)
email = 'email_example' # str |  (optional)
os_version = 'os_version_example' # str |  (optional)
os_logs = '/path/to/file' # file |  (optional)
browser_version = 'browser_version_example' # str |  (optional)
browser_logs = '/path/to/file' # file |  (optional)
serial = 'serial_example' # str |  (optional)
posthog_session = 'posthog_session_example' # str |  (optional)
status = printnanny_api_client.CrashReportStatusEnum() # CrashReportStatusEnum |  (optional)
support_comment = 'support_comment_example' # str |  (optional)
pi = 56 # int |  (optional)

    try:
        api_response = api_instance.crash_reports_partial_update(id, description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, status=status, support_comment=support_comment, pi=pi)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CrashReportsApi->crash_reports_partial_update: %s\n" % e)
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
    api_instance = printnanny_api_client.CrashReportsApi(api_client)
    id = 'id_example' # str | A UUID string identifying this crash report.
description = 'description_example' # str |  (optional)
email = 'email_example' # str |  (optional)
os_version = 'os_version_example' # str |  (optional)
os_logs = '/path/to/file' # file |  (optional)
browser_version = 'browser_version_example' # str |  (optional)
browser_logs = '/path/to/file' # file |  (optional)
serial = 'serial_example' # str |  (optional)
posthog_session = 'posthog_session_example' # str |  (optional)
status = printnanny_api_client.CrashReportStatusEnum() # CrashReportStatusEnum |  (optional)
support_comment = 'support_comment_example' # str |  (optional)
pi = 56 # int |  (optional)

    try:
        api_response = api_instance.crash_reports_partial_update(id, description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, status=status, support_comment=support_comment, pi=pi)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CrashReportsApi->crash_reports_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this crash report. | 
 **description** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **os_version** | **str**|  | [optional] 
 **os_logs** | **file**|  | [optional] 
 **browser_version** | **str**|  | [optional] 
 **browser_logs** | **file**|  | [optional] 
 **serial** | **str**|  | [optional] 
 **posthog_session** | **str**|  | [optional] 
 **status** | [**CrashReportStatusEnum**](CrashReportStatusEnum.md)|  | [optional] 
 **support_comment** | **str**|  | [optional] 
 **pi** | **int**|  | [optional] 

### Return type

[**CrashReport**](CrashReport.md)

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

# **crash_reports_retrieve**
> CrashReport crash_reports_retrieve(id)



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
    api_instance = printnanny_api_client.CrashReportsApi(api_client)
    id = 'id_example' # str | A UUID string identifying this crash report.

    try:
        api_response = api_instance.crash_reports_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CrashReportsApi->crash_reports_retrieve: %s\n" % e)
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
    api_instance = printnanny_api_client.CrashReportsApi(api_client)
    id = 'id_example' # str | A UUID string identifying this crash report.

    try:
        api_response = api_instance.crash_reports_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CrashReportsApi->crash_reports_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this crash report. | 

### Return type

[**CrashReport**](CrashReport.md)

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

# **crash_reports_update**
> CrashReport crash_reports_update(id, description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, status=status, support_comment=support_comment, pi=pi)



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
    api_instance = printnanny_api_client.CrashReportsApi(api_client)
    id = 'id_example' # str | A UUID string identifying this crash report.
description = 'description_example' # str |  (optional)
email = 'email_example' # str |  (optional)
os_version = 'os_version_example' # str |  (optional)
os_logs = '/path/to/file' # file |  (optional)
browser_version = 'browser_version_example' # str |  (optional)
browser_logs = '/path/to/file' # file |  (optional)
serial = 'serial_example' # str |  (optional)
posthog_session = 'posthog_session_example' # str |  (optional)
status = printnanny_api_client.CrashReportStatusEnum() # CrashReportStatusEnum |  (optional)
support_comment = 'support_comment_example' # str |  (optional)
pi = 56 # int |  (optional)

    try:
        api_response = api_instance.crash_reports_update(id, description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, status=status, support_comment=support_comment, pi=pi)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CrashReportsApi->crash_reports_update: %s\n" % e)
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
    api_instance = printnanny_api_client.CrashReportsApi(api_client)
    id = 'id_example' # str | A UUID string identifying this crash report.
description = 'description_example' # str |  (optional)
email = 'email_example' # str |  (optional)
os_version = 'os_version_example' # str |  (optional)
os_logs = '/path/to/file' # file |  (optional)
browser_version = 'browser_version_example' # str |  (optional)
browser_logs = '/path/to/file' # file |  (optional)
serial = 'serial_example' # str |  (optional)
posthog_session = 'posthog_session_example' # str |  (optional)
status = printnanny_api_client.CrashReportStatusEnum() # CrashReportStatusEnum |  (optional)
support_comment = 'support_comment_example' # str |  (optional)
pi = 56 # int |  (optional)

    try:
        api_response = api_instance.crash_reports_update(id, description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, status=status, support_comment=support_comment, pi=pi)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CrashReportsApi->crash_reports_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this crash report. | 
 **description** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **os_version** | **str**|  | [optional] 
 **os_logs** | **file**|  | [optional] 
 **browser_version** | **str**|  | [optional] 
 **browser_logs** | **file**|  | [optional] 
 **serial** | **str**|  | [optional] 
 **posthog_session** | **str**|  | [optional] 
 **status** | [**CrashReportStatusEnum**](CrashReportStatusEnum.md)|  | [optional] 
 **support_comment** | **str**|  | [optional] 
 **pi** | **int**|  | [optional] 

### Return type

[**CrashReport**](CrashReport.md)

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

