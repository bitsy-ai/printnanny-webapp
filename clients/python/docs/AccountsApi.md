# printnanny_api_client.AccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts2fa_auth_email_create**](AccountsApi.md#accounts2fa_auth_email_create) | **POST** /accounts/2fa-auth/email/ | 
[**accounts2fa_auth_session_create**](AccountsApi.md#accounts2fa_auth_session_create) | **POST** /accounts/2fa-auth/session/ | 
[**accounts2fa_auth_token_create**](AccountsApi.md#accounts2fa_auth_token_create) | **POST** /accounts/2fa-auth/token/ | 
[**accounts_email_waitlist_create**](AccountsApi.md#accounts_email_waitlist_create) | **POST** /api/accounts/email-waitlist/ | 
[**accounts_login_create**](AccountsApi.md#accounts_login_create) | **POST** /api/accounts/login/ | 
[**accounts_logout_create**](AccountsApi.md#accounts_logout_create) | **POST** /api/accounts/logout/ | 
[**accounts_password_change_create**](AccountsApi.md#accounts_password_change_create) | **POST** /api/accounts/password/change/ | 
[**accounts_password_reset_confirm_create**](AccountsApi.md#accounts_password_reset_confirm_create) | **POST** /api/accounts/password/reset/confirm/ | 
[**accounts_password_reset_create**](AccountsApi.md#accounts_password_reset_create) | **POST** /api/accounts/password/reset/ | 
[**accounts_registration_create**](AccountsApi.md#accounts_registration_create) | **POST** /api/accounts/registration/ | 
[**accounts_registration_resend_email_create**](AccountsApi.md#accounts_registration_resend_email_create) | **POST** /api/accounts/registration/resend-email/ | 
[**accounts_registration_verify_email_create**](AccountsApi.md#accounts_registration_verify_email_create) | **POST** /api/accounts/registration/verify-email/ | 
[**accounts_user_nkey_retrieve**](AccountsApi.md#accounts_user_nkey_retrieve) | **GET** /api/accounts/user/nkey | 
[**accounts_user_partial_update**](AccountsApi.md#accounts_user_partial_update) | **PATCH** /api/accounts/user/ | 
[**accounts_user_retrieve**](AccountsApi.md#accounts_user_retrieve) | **GET** /api/accounts/user/ | 
[**accounts_user_update**](AccountsApi.md#accounts_user_update) | **PUT** /api/accounts/user/ | 


# **accounts2fa_auth_email_create**
> EmailAuth accounts2fa_auth_email_create(email_auth_request)



This returns a 6-digit callback token we can trade for a user's Auth Token.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    email_auth_request = printnanny_api_client.EmailAuthRequest() # EmailAuthRequest | 

    try:
        api_response = api_instance.accounts2fa_auth_email_create(email_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts2fa_auth_email_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    email_auth_request = printnanny_api_client.EmailAuthRequest() # EmailAuthRequest | 

    try:
        api_response = api_instance.accounts2fa_auth_email_create(email_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts2fa_auth_email_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_auth_request** | [**EmailAuthRequest**](EmailAuthRequest.md)|  | 

### Return type

[**EmailAuth**](EmailAuth.md)

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

# **accounts2fa_auth_session_create**
> CallbackTokenAuth accounts2fa_auth_session_create(callback_token_auth_request)



Persist a user id and a backend in the request. This way a user doesn't have to reauthenticate on every request. Note that data set during the anonymous session is retained when the user logs in.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    callback_token_auth_request = printnanny_api_client.CallbackTokenAuthRequest() # CallbackTokenAuthRequest | 

    try:
        api_response = api_instance.accounts2fa_auth_session_create(callback_token_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts2fa_auth_session_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    callback_token_auth_request = printnanny_api_client.CallbackTokenAuthRequest() # CallbackTokenAuthRequest | 

    try:
        api_response = api_instance.accounts2fa_auth_session_create(callback_token_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts2fa_auth_session_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_token_auth_request** | [**CallbackTokenAuthRequest**](CallbackTokenAuthRequest.md)|  | 

### Return type

[**CallbackTokenAuth**](CallbackTokenAuth.md)

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

# **accounts2fa_auth_token_create**
> CallbackTokenAuth accounts2fa_auth_token_create(callback_token_auth_request)



This is a duplicate of rest_framework's own ObtainAuthToken method. Instead, this returns an Auth Token based on our callback token and source.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    callback_token_auth_request = printnanny_api_client.CallbackTokenAuthRequest() # CallbackTokenAuthRequest | 

    try:
        api_response = api_instance.accounts2fa_auth_token_create(callback_token_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts2fa_auth_token_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    callback_token_auth_request = printnanny_api_client.CallbackTokenAuthRequest() # CallbackTokenAuthRequest | 

    try:
        api_response = api_instance.accounts2fa_auth_token_create(callback_token_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts2fa_auth_token_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_token_auth_request** | [**CallbackTokenAuthRequest**](CallbackTokenAuthRequest.md)|  | 

### Return type

[**CallbackTokenAuth**](CallbackTokenAuth.md)

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

# **accounts_email_waitlist_create**
> EmailWaitlist accounts_email_waitlist_create(email_waitlist_request)



A device (Raspberry Pi) running Print Nanny OS

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    email_waitlist_request = printnanny_api_client.EmailWaitlistRequest() # EmailWaitlistRequest | 

    try:
        api_response = api_instance.accounts_email_waitlist_create(email_waitlist_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_email_waitlist_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    email_waitlist_request = printnanny_api_client.EmailWaitlistRequest() # EmailWaitlistRequest | 

    try:
        api_response = api_instance.accounts_email_waitlist_create(email_waitlist_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_email_waitlist_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_waitlist_request** | [**EmailWaitlistRequest**](EmailWaitlistRequest.md)|  | 

### Return type

[**EmailWaitlist**](EmailWaitlist.md)

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

# **accounts_login_create**
> Token accounts_login_create(login_request)



Check the credentials and return the REST Token if the credentials are valid and authenticated. Calls Django Auth login method to register User ID in Django session framework  Accept the following POST parameters: username, password Return the REST Framework Token Object's key.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    login_request = printnanny_api_client.LoginRequest() # LoginRequest | 

    try:
        api_response = api_instance.accounts_login_create(login_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_login_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    login_request = printnanny_api_client.LoginRequest() # LoginRequest | 

    try:
        api_response = api_instance.accounts_login_create(login_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_login_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**Token**](Token.md)

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

# **accounts_logout_create**
> RestAuthDetail accounts_logout_create()



Calls Django logout method and delete the Token object assigned to the current User object.  Accepts/Returns nothing.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    
    try:
        api_response = api_instance.accounts_logout_create()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_logout_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    
    try:
        api_response = api_instance.accounts_logout_create()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_logout_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RestAuthDetail**](RestAuthDetail.md)

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

# **accounts_password_change_create**
> RestAuthDetail accounts_password_change_create(password_change_request)



Calls Django Auth SetPasswordForm save method.  Accepts the following POST parameters: new_password1, new_password2 Returns the success/fail message.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    password_change_request = printnanny_api_client.PasswordChangeRequest() # PasswordChangeRequest | 

    try:
        api_response = api_instance.accounts_password_change_create(password_change_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_password_change_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    password_change_request = printnanny_api_client.PasswordChangeRequest() # PasswordChangeRequest | 

    try:
        api_response = api_instance.accounts_password_change_create(password_change_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_password_change_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_change_request** | [**PasswordChangeRequest**](PasswordChangeRequest.md)|  | 

### Return type

[**RestAuthDetail**](RestAuthDetail.md)

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

# **accounts_password_reset_confirm_create**
> RestAuthDetail accounts_password_reset_confirm_create(password_reset_confirm_request)



Password reset e-mail link is confirmed, therefore this resets the user's password.  Accepts the following POST parameters: token, uid,     new_password1, new_password2 Returns the success/fail message.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    password_reset_confirm_request = printnanny_api_client.PasswordResetConfirmRequest() # PasswordResetConfirmRequest | 

    try:
        api_response = api_instance.accounts_password_reset_confirm_create(password_reset_confirm_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_password_reset_confirm_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    password_reset_confirm_request = printnanny_api_client.PasswordResetConfirmRequest() # PasswordResetConfirmRequest | 

    try:
        api_response = api_instance.accounts_password_reset_confirm_create(password_reset_confirm_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_password_reset_confirm_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset_confirm_request** | [**PasswordResetConfirmRequest**](PasswordResetConfirmRequest.md)|  | 

### Return type

[**RestAuthDetail**](RestAuthDetail.md)

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

# **accounts_password_reset_create**
> RestAuthDetail accounts_password_reset_create(password_reset_request)



Calls Django Auth PasswordResetForm save method.  Accepts the following POST parameters: email Returns the success/fail message.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    password_reset_request = printnanny_api_client.PasswordResetRequest() # PasswordResetRequest | 

    try:
        api_response = api_instance.accounts_password_reset_create(password_reset_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_password_reset_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    password_reset_request = printnanny_api_client.PasswordResetRequest() # PasswordResetRequest | 

    try:
        api_response = api_instance.accounts_password_reset_create(password_reset_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_password_reset_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset_request** | [**PasswordResetRequest**](PasswordResetRequest.md)|  | 

### Return type

[**RestAuthDetail**](RestAuthDetail.md)

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

# **accounts_registration_create**
> Token accounts_registration_create(register_request)



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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    register_request = printnanny_api_client.RegisterRequest() # RegisterRequest | 

    try:
        api_response = api_instance.accounts_registration_create(register_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_registration_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    register_request = printnanny_api_client.RegisterRequest() # RegisterRequest | 

    try:
        api_response = api_instance.accounts_registration_create(register_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_registration_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

[**Token**](Token.md)

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

# **accounts_registration_resend_email_create**
> RestAuthDetail accounts_registration_resend_email_create(resend_email_verification_request)



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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    resend_email_verification_request = printnanny_api_client.ResendEmailVerificationRequest() # ResendEmailVerificationRequest | 

    try:
        api_response = api_instance.accounts_registration_resend_email_create(resend_email_verification_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_registration_resend_email_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    resend_email_verification_request = printnanny_api_client.ResendEmailVerificationRequest() # ResendEmailVerificationRequest | 

    try:
        api_response = api_instance.accounts_registration_resend_email_create(resend_email_verification_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_registration_resend_email_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_email_verification_request** | [**ResendEmailVerificationRequest**](ResendEmailVerificationRequest.md)|  | 

### Return type

[**RestAuthDetail**](RestAuthDetail.md)

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

# **accounts_registration_verify_email_create**
> RestAuthDetail accounts_registration_verify_email_create(verify_email_request)



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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    verify_email_request = printnanny_api_client.VerifyEmailRequest() # VerifyEmailRequest | 

    try:
        api_response = api_instance.accounts_registration_verify_email_create(verify_email_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_registration_verify_email_create: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    verify_email_request = printnanny_api_client.VerifyEmailRequest() # VerifyEmailRequest | 

    try:
        api_response = api_instance.accounts_registration_verify_email_create(verify_email_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_registration_verify_email_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_email_request** | [**VerifyEmailRequest**](VerifyEmailRequest.md)|  | 

### Return type

[**RestAuthDetail**](RestAuthDetail.md)

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

# **accounts_user_nkey_retrieve**
> NatsOrganizationUser accounts_user_nkey_retrieve()



Providers user nkey credentials

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    
    try:
        api_response = api_instance.accounts_user_nkey_retrieve()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_user_nkey_retrieve: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    
    try:
        api_response = api_instance.accounts_user_nkey_retrieve()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_user_nkey_retrieve: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NatsOrganizationUser**](NatsOrganizationUser.md)

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

# **accounts_user_partial_update**
> User accounts_user_partial_update(patched_user_request=patched_user_request)



Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    patched_user_request = printnanny_api_client.PatchedUserRequest() # PatchedUserRequest |  (optional)

    try:
        api_response = api_instance.accounts_user_partial_update(patched_user_request=patched_user_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_user_partial_update: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    patched_user_request = printnanny_api_client.PatchedUserRequest() # PatchedUserRequest |  (optional)

    try:
        api_response = api_instance.accounts_user_partial_update(patched_user_request=patched_user_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_user_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_user_request** | [**PatchedUserRequest**](PatchedUserRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

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

# **accounts_user_retrieve**
> User accounts_user_retrieve()



Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    
    try:
        api_response = api_instance.accounts_user_retrieve()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_user_retrieve: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    
    try:
        api_response = api_instance.accounts_user_retrieve()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_user_retrieve: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

# **accounts_user_update**
> User accounts_user_update(user_request)



Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.

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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    user_request = printnanny_api_client.UserRequest() # UserRequest | 

    try:
        api_response = api_instance.accounts_user_update(user_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_user_update: %s\n" % e)
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
    api_instance = printnanny_api_client.AccountsApi(api_client)
    user_request = printnanny_api_client.UserRequest() # UserRequest | 

    try:
        api_response = api_instance.accounts_user_update(user_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_user_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_request** | [**UserRequest**](UserRequest.md)|  | 

### Return type

[**User**](User.md)

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

