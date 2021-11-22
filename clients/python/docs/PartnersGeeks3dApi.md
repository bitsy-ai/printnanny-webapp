# printnanny_api_client.PartnersGeeks3dApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_retrieve**](PartnersGeeks3dApi.md#metadata_retrieve) | **GET** /api/partners/3d-geeks/{id}/ | 


# **metadata_retrieve**
> Partner3DGeeksMetadata metadata_retrieve(id)



3D Geeks calls this endpoint to validate token & fetch printer metadata

### Example

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

# Configure Bearer authorization: tokenAuth
configuration = printnanny_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with printnanny_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = printnanny_api_client.PartnersGeeks3dApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.metadata_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartnersGeeks3dApi->metadata_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Partner3DGeeksMetadata**](Partner3DGeeksMetadata.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

