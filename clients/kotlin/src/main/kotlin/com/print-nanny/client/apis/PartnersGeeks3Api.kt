/**
 * print-nanny-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
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

import com.print-nanny.client.models.Partner3DGeeksAlert

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

class PartnersGeeks3Api(basePath: kotlin.String = defaultBasePath) : ApiClient(basePath) {
    companion object {
        @JvmStatic
        val defaultBasePath: String by lazy {
            System.getProperties().getProperty("com.print-nanny.client.baseUrl", "http://localhost")
        }
    }

    /**
    * 
    * 
    * @param id  
    * @return Partner3DGeeksAlert
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun alertsList2(id: kotlin.String) : Partner3DGeeksAlert {
        val localVariableConfig = alertsList2RequestConfig(id = id)

        val localVarResponse = request<Unit, Partner3DGeeksAlert>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as Partner3DGeeksAlert
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
    * To obtain the request config of the operation alertsList2
    *
    * @param id  
    * @return RequestConfig
    */
    fun alertsList2RequestConfig(id: kotlin.String) : RequestConfig<Unit> {
        val localVariableBody = null
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.GET,
            path = "/api/partners/3d-geeks/{id}/alerts/".replace("{"+"id"+"}", "$id"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

}
