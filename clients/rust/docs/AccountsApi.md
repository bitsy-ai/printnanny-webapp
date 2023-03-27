# \AccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts2fa_auth_email_create**](AccountsApi.md#accounts2fa_auth_email_create) | **POST** /accounts/2fa-auth/email/ | 
[**accounts2fa_auth_session_create**](AccountsApi.md#accounts2fa_auth_session_create) | **POST** /accounts/2fa-auth/session/ | 
[**accounts2fa_auth_token_create**](AccountsApi.md#accounts2fa_auth_token_create) | **POST** /accounts/2fa-auth/token/ | 
[**accounts_auth_login_create**](AccountsApi.md#accounts_auth_login_create) | **POST** /api/accounts/auth/login/ | 
[**accounts_auth_logout_create**](AccountsApi.md#accounts_auth_logout_create) | **POST** /api/accounts/auth/logout/ | 
[**accounts_auth_password_change_create**](AccountsApi.md#accounts_auth_password_change_create) | **POST** /api/accounts/auth/password/change/ | 
[**accounts_auth_password_reset_confirm_create**](AccountsApi.md#accounts_auth_password_reset_confirm_create) | **POST** /api/accounts/auth/password/reset/confirm/ | 
[**accounts_auth_password_reset_create**](AccountsApi.md#accounts_auth_password_reset_create) | **POST** /api/accounts/auth/password/reset/ | 
[**accounts_auth_user_partial_update**](AccountsApi.md#accounts_auth_user_partial_update) | **PATCH** /api/accounts/auth/user/ | 
[**accounts_auth_user_retrieve**](AccountsApi.md#accounts_auth_user_retrieve) | **GET** /api/accounts/auth/user/ | 
[**accounts_auth_user_update**](AccountsApi.md#accounts_auth_user_update) | **PUT** /api/accounts/auth/user/ | 
[**accounts_email_waitlist_create**](AccountsApi.md#accounts_email_waitlist_create) | **POST** /api/accounts/email-waitlist/ | 
[**accounts_registration_create**](AccountsApi.md#accounts_registration_create) | **POST** /api/accounts/registration/ | 
[**accounts_registration_resend_email_create**](AccountsApi.md#accounts_registration_resend_email_create) | **POST** /api/accounts/registration/resend-email/ | 
[**accounts_registration_verify_email_create**](AccountsApi.md#accounts_registration_verify_email_create) | **POST** /api/accounts/registration/verify-email/ | 
[**accounts_user_nkey_retrieve**](AccountsApi.md#accounts_user_nkey_retrieve) | **GET** /api/accounts/user/nkey | 



## accounts2fa_auth_email_create

> crate::models::EmailAuth accounts2fa_auth_email_create(email_auth_request)


This returns a 6-digit callback token we can trade for a user's Auth Token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**email_auth_request** | [**EmailAuthRequest**](EmailAuthRequest.md) |  | [required] |

### Return type

[**crate::models::EmailAuth**](EmailAuth.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts2fa_auth_session_create

> crate::models::CallbackTokenAuth accounts2fa_auth_session_create(callback_token_auth_request)


Persist a user id and a backend in the request. This way a user doesn't have to reauthenticate on every request. Note that data set during the anonymous session is retained when the user logs in.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**callback_token_auth_request** | [**CallbackTokenAuthRequest**](CallbackTokenAuthRequest.md) |  | [required] |

### Return type

[**crate::models::CallbackTokenAuth**](CallbackTokenAuth.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts2fa_auth_token_create

> crate::models::CallbackTokenAuth accounts2fa_auth_token_create(callback_token_auth_request)


This is a duplicate of rest_framework's own ObtainAuthToken method. Instead, this returns an Auth Token based on our callback token and source.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**callback_token_auth_request** | [**CallbackTokenAuthRequest**](CallbackTokenAuthRequest.md) |  | [required] |

### Return type

[**crate::models::CallbackTokenAuth**](CallbackTokenAuth.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_auth_login_create

> crate::models::Token accounts_auth_login_create(login_request)


Check the credentials and return the REST Token if the credentials are valid and authenticated. Calls Django Auth login method to register User ID in Django session framework  Accept the following POST parameters: username, password Return the REST Framework Token Object's key.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**login_request** | [**LoginRequest**](LoginRequest.md) |  | [required] |

### Return type

[**crate::models::Token**](Token.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_auth_logout_create

> crate::models::RestAuthDetail accounts_auth_logout_create()


Calls Django logout method and delete the Token object assigned to the current User object.  Accepts/Returns nothing.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::RestAuthDetail**](RestAuthDetail.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_auth_password_change_create

> crate::models::RestAuthDetail accounts_auth_password_change_create(password_change_request)


Calls Django Auth SetPasswordForm save method.  Accepts the following POST parameters: new_password1, new_password2 Returns the success/fail message.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**password_change_request** | [**PasswordChangeRequest**](PasswordChangeRequest.md) |  | [required] |

### Return type

[**crate::models::RestAuthDetail**](RestAuthDetail.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_auth_password_reset_confirm_create

> crate::models::RestAuthDetail accounts_auth_password_reset_confirm_create(password_reset_confirm_request)


Password reset e-mail link is confirmed, therefore this resets the user's password.  Accepts the following POST parameters: token, uid,     new_password1, new_password2 Returns the success/fail message.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**password_reset_confirm_request** | [**PasswordResetConfirmRequest**](PasswordResetConfirmRequest.md) |  | [required] |

### Return type

[**crate::models::RestAuthDetail**](RestAuthDetail.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_auth_password_reset_create

> crate::models::RestAuthDetail accounts_auth_password_reset_create(password_reset_request)


Calls Django Auth PasswordResetForm save method.  Accepts the following POST parameters: email Returns the success/fail message.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**password_reset_request** | [**PasswordResetRequest**](PasswordResetRequest.md) |  | [required] |

### Return type

[**crate::models::RestAuthDetail**](RestAuthDetail.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_auth_user_partial_update

> crate::models::User accounts_auth_user_partial_update(patched_user_request)


Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**patched_user_request** | Option<[**PatchedUserRequest**](PatchedUserRequest.md)> |  |  |

### Return type

[**crate::models::User**](User.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_auth_user_retrieve

> crate::models::User accounts_auth_user_retrieve()


Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::User**](User.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_auth_user_update

> crate::models::User accounts_auth_user_update(user_request)


Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**user_request** | [**UserRequest**](UserRequest.md) |  | [required] |

### Return type

[**crate::models::User**](User.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_email_waitlist_create

> crate::models::EmailWaitlist accounts_email_waitlist_create(email_waitlist_request)


A device (Raspberry Pi) running Print Nanny OS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**email_waitlist_request** | [**EmailWaitlistRequest**](EmailWaitlistRequest.md) |  | [required] |

### Return type

[**crate::models::EmailWaitlist**](EmailWaitlist.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_registration_create

> crate::models::Token accounts_registration_create(register_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**register_request** | [**RegisterRequest**](RegisterRequest.md) |  | [required] |

### Return type

[**crate::models::Token**](Token.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_registration_resend_email_create

> crate::models::RestAuthDetail accounts_registration_resend_email_create(resend_email_verification_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**resend_email_verification_request** | [**ResendEmailVerificationRequest**](ResendEmailVerificationRequest.md) |  | [required] |

### Return type

[**crate::models::RestAuthDetail**](RestAuthDetail.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_registration_verify_email_create

> crate::models::RestAuthDetail accounts_registration_verify_email_create(verify_email_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**verify_email_request** | [**VerifyEmailRequest**](VerifyEmailRequest.md) |  | [required] |

### Return type

[**crate::models::RestAuthDetail**](RestAuthDetail.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## accounts_user_nkey_retrieve

> crate::models::NatsOrganizationUser accounts_user_nkey_retrieve()


Providers user nkey credentials

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::NatsOrganizationUser**](NatsOrganizationUser.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

