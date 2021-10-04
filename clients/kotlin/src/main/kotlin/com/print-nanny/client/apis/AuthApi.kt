/**
 * 
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 *
 * Please note:
 * This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * Do not edit this file manually.
 */

@file:Suppress(
    "ArrayInDataClass",
    "EnumEntryName",
    "RemoveRedundantQualifierName",
    "UnusedImport"
)

package com.print-nanny.client.apis

import com.print-nanny.client.models.CallbackTokenAuthRequest
import com.print-nanny.client.models.CallbackTokenVerification
import com.print-nanny.client.models.CallbackTokenVerificationRequest
import com.print-nanny.client.models.DetailResponse
import com.print-nanny.client.models.EmailAuthRequest
import com.print-nanny.client.models.MobileAuthRequest
import com.print-nanny.client.models.TokenResponse

import com.print-nanny.client.infrastructure.ApiClient
import com.print-nanny.client.infrastructure.ClientException
import com.print-nanny.client.infrastructure.ClientError
import com.print-nanny.client.infrastructure.ServerException
import com.print-nanny.client.infrastructure.ServerError
import com.print-nanny.client.infrastructure.MultiValueMap
import com.print-nanny.client.infrastructure.RequestConfig
import com.print-nanny.client.infrastructure.RequestMethod
import com.print-nanny.client.infrastructure.ResponseType
import com.print-nanny.client.infrastructure.Success
import com.print-nanny.client.infrastructure.toMultiValue

class AuthApi(basePath: kotlin.String = defaultBasePath) : ApiClient(basePath) {
    companion object {
        @JvmStatic
        val defaultBasePath: String by lazy {
            System.getProperties().getProperty("com.print-nanny.client.baseUrl", "http://localhost")
        }
    }

    /**
    * 
    * This returns a 6-digit callback token we can trade for a user&#39;s Auth Token.
    * @param emailAuthRequest  
    * @return DetailResponse
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun authEmailCreate(emailAuthRequest: EmailAuthRequest) : DetailResponse {
        val localVariableConfig = authEmailCreateRequestConfig(emailAuthRequest = emailAuthRequest)

        val localVarResponse = request<EmailAuthRequest, DetailResponse>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as DetailResponse
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
    * To obtain the request config of the operation authEmailCreate
    *
    * @param emailAuthRequest  
    * @return RequestConfig
    */
    fun authEmailCreateRequestConfig(emailAuthRequest: EmailAuthRequest) : RequestConfig<EmailAuthRequest> {
        val localVariableBody = emailAuthRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.POST,
            path = "/auth/email/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
    * 
    * This returns a 6-digit callback token we can trade for a user&#39;s Auth Token.
    * @param mobileAuthRequest  
    * @return DetailResponse
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun authMobileCreate(mobileAuthRequest: MobileAuthRequest) : DetailResponse {
        val localVariableConfig = authMobileCreateRequestConfig(mobileAuthRequest = mobileAuthRequest)

        val localVarResponse = request<MobileAuthRequest, DetailResponse>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as DetailResponse
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
    * To obtain the request config of the operation authMobileCreate
    *
    * @param mobileAuthRequest  
    * @return RequestConfig
    */
    fun authMobileCreateRequestConfig(mobileAuthRequest: MobileAuthRequest) : RequestConfig<MobileAuthRequest> {
        val localVariableBody = mobileAuthRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.POST,
            path = "/auth/mobile/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
    * 
    * This is a duplicate of rest_framework&#39;s own ObtainAuthToken method. Instead, this returns an Auth Token based on our callback token and source.
    * @param callbackTokenAuthRequest  
    * @return TokenResponse
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun authTokenCreate(callbackTokenAuthRequest: CallbackTokenAuthRequest) : TokenResponse {
        val localVariableConfig = authTokenCreateRequestConfig(callbackTokenAuthRequest = callbackTokenAuthRequest)

        val localVarResponse = request<CallbackTokenAuthRequest, TokenResponse>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as TokenResponse
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
    * To obtain the request config of the operation authTokenCreate
    *
    * @param callbackTokenAuthRequest  
    * @return RequestConfig
    */
    fun authTokenCreateRequestConfig(callbackTokenAuthRequest: CallbackTokenAuthRequest) : RequestConfig<CallbackTokenAuthRequest> {
        val localVariableBody = callbackTokenAuthRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.POST,
            path = "/auth/token/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
    * 
    * This verifies an alias on correct callback token entry using the same logic as auth. Should be refactored at some point.
    * @param callbackTokenVerificationRequest  
    * @return CallbackTokenVerification
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun authVerifyCreate(callbackTokenVerificationRequest: CallbackTokenVerificationRequest) : CallbackTokenVerification {
        val localVariableConfig = authVerifyCreateRequestConfig(callbackTokenVerificationRequest = callbackTokenVerificationRequest)

        val localVarResponse = request<CallbackTokenVerificationRequest, CallbackTokenVerification>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as CallbackTokenVerification
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
    * To obtain the request config of the operation authVerifyCreate
    *
    * @param callbackTokenVerificationRequest  
    * @return RequestConfig
    */
    fun authVerifyCreateRequestConfig(callbackTokenVerificationRequest: CallbackTokenVerificationRequest) : RequestConfig<CallbackTokenVerificationRequest> {
        val localVariableBody = callbackTokenVerificationRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.POST,
            path = "/auth/verify/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
    * 
    * This returns a 6-digit callback token we can trade for a user&#39;s Auth Token.
    * @return DetailResponse
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun authVerifyEmailCreate() : DetailResponse {
        val localVariableConfig = authVerifyEmailCreateRequestConfig()

        val localVarResponse = request<Unit, DetailResponse>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as DetailResponse
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
    * To obtain the request config of the operation authVerifyEmailCreate
    *
    * @return RequestConfig
    */
    fun authVerifyEmailCreateRequestConfig() : RequestConfig<Unit> {
        val localVariableBody = null
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.POST,
            path = "/auth/verify/email/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
    * 
    * This returns a 6-digit callback token we can trade for a user&#39;s Auth Token.
    * @return DetailResponse
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun authVerifyMobileCreate() : DetailResponse {
        val localVariableConfig = authVerifyMobileCreateRequestConfig()

        val localVarResponse = request<Unit, DetailResponse>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as DetailResponse
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
    * To obtain the request config of the operation authVerifyMobileCreate
    *
    * @return RequestConfig
    */
    fun authVerifyMobileCreateRequestConfig() : RequestConfig<Unit> {
        val localVariableBody = null
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.POST,
            path = "/auth/verify/mobile/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

}
