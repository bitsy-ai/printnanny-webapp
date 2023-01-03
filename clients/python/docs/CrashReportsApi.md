# printnanny_api_client.CrashReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crash_reports_create**](CrashReportsApi.md#crash_reports_create) | **POST** /api/crash-reports/ | 


# **crash_reports_create**
> CrashReport crash_reports_create(description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, user=user, pi=pi, related_crash_report=related_crash_report)



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
user = 56 # int |  (optional)
pi = 56 # int |  (optional)
related_crash_report = 'related_crash_report_example' # str |  (optional)

    try:
        api_response = api_instance.crash_reports_create(description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, user=user, pi=pi, related_crash_report=related_crash_report)
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
user = 56 # int |  (optional)
pi = 56 # int |  (optional)
related_crash_report = 'related_crash_report_example' # str |  (optional)

    try:
        api_response = api_instance.crash_reports_create(description=description, email=email, os_version=os_version, os_logs=os_logs, browser_version=browser_version, browser_logs=browser_logs, serial=serial, posthog_session=posthog_session, user=user, pi=pi, related_crash_report=related_crash_report)
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
 **user** | **int**|  | [optional] 
 **pi** | **int**|  | [optional] 
 **related_crash_report** | **str**|  | [optional] 

### Return type

[**CrashReport**](CrashReport.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
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

