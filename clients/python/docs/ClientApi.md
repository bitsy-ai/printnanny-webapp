# printnanny_api_client.ClientApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_config_retreive**](ClientApi.md#api_config_retreive) | **GET** /api/client | 


# **api_config_retreive**
> PrintNannyApiConfig api_config_retreive()



### Example

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


# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.ClientApi(api_client)
    
    try:
        api_response = api_instance.api_config_retreive()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientApi->api_config_retreive: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrintNannyApiConfig**](PrintNannyApiConfig.md)

### Authorization

No authorization required

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

