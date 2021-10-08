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

import com.print-nanny.client.models.Appliance
import com.print-nanny.client.models.ApplianceRequest
import com.print-nanny.client.models.CreateApplianceRequest
import com.print-nanny.client.models.PaginatedApplianceList
import com.print-nanny.client.models.PatchedApplianceRequest

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

class AppliancesApi(basePath: kotlin.String = defaultBasePath) : ApiClient(basePath) {
    companion object {
        @JvmStatic
        val defaultBasePath: String by lazy {
            System.getProperties().getProperty("com.print-nanny.client.baseUrl", "http://localhost")
        }
    }

    /**
    * 
    * 
    * @param createApplianceRequest  
    * @return Appliance
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun appliancesCreate(createApplianceRequest: CreateApplianceRequest) : Appliance {
        val localVariableConfig = appliancesCreateRequestConfig(createApplianceRequest = createApplianceRequest)

        val localVarResponse = request<CreateApplianceRequest, Appliance>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as Appliance
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
    * To obtain the request config of the operation appliancesCreate
    *
    * @param createApplianceRequest  
    * @return RequestConfig
    */
    fun appliancesCreateRequestConfig(createApplianceRequest: CreateApplianceRequest) : RequestConfig<CreateApplianceRequest> {
        val localVariableBody = createApplianceRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.POST,
            path = "/api/appliances/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
    * 
    * 
    * @param page A page number within the paginated result set. (optional)
    * @return PaginatedApplianceList
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun appliancesList(page: kotlin.Int?) : PaginatedApplianceList {
        val localVariableConfig = appliancesListRequestConfig(page = page)

        val localVarResponse = request<Unit, PaginatedApplianceList>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as PaginatedApplianceList
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
    * To obtain the request config of the operation appliancesList
    *
    * @param page A page number within the paginated result set. (optional)
    * @return RequestConfig
    */
    fun appliancesListRequestConfig(page: kotlin.Int?) : RequestConfig<Unit> {
        val localVariableBody = null
        val localVariableQuery: MultiValueMap = mutableMapOf<kotlin.String, List<kotlin.String>>()
            .apply {
                if (page != null) {
                    put("page", listOf(page.toString()))
                }
            }
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.GET,
            path = "/api/appliances/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
    * 
    * 
    * @param id A unique integer value identifying this appliance. 
    * @param patchedApplianceRequest  (optional)
    * @return Appliance
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun appliancesPartialUpdate(id: kotlin.Int, patchedApplianceRequest: PatchedApplianceRequest?) : Appliance {
        val localVariableConfig = appliancesPartialUpdateRequestConfig(id = id, patchedApplianceRequest = patchedApplianceRequest)

        val localVarResponse = request<PatchedApplianceRequest, Appliance>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as Appliance
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
    * To obtain the request config of the operation appliancesPartialUpdate
    *
    * @param id A unique integer value identifying this appliance. 
    * @param patchedApplianceRequest  (optional)
    * @return RequestConfig
    */
    fun appliancesPartialUpdateRequestConfig(id: kotlin.Int, patchedApplianceRequest: PatchedApplianceRequest?) : RequestConfig<PatchedApplianceRequest> {
        val localVariableBody = patchedApplianceRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.PATCH,
            path = "/api/appliances/{id}/".replace("{"+"id"+"}", "$id"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
    * 
    * 
    * @param id A unique integer value identifying this appliance. 
    * @return Appliance
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun appliancesRetrieve(id: kotlin.Int) : Appliance {
        val localVariableConfig = appliancesRetrieveRequestConfig(id = id)

        val localVarResponse = request<Unit, Appliance>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as Appliance
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
    * To obtain the request config of the operation appliancesRetrieve
    *
    * @param id A unique integer value identifying this appliance. 
    * @return RequestConfig
    */
    fun appliancesRetrieveRequestConfig(id: kotlin.Int) : RequestConfig<Unit> {
        val localVariableBody = null
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.GET,
            path = "/api/appliances/{id}/".replace("{"+"id"+"}", "$id"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
    * 
    * 
    * @param id A unique integer value identifying this appliance. 
    * @param applianceRequest  
    * @return Appliance
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun appliancesUpdate(id: kotlin.Int, applianceRequest: ApplianceRequest) : Appliance {
        val localVariableConfig = appliancesUpdateRequestConfig(id = id, applianceRequest = applianceRequest)

        val localVarResponse = request<ApplianceRequest, Appliance>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as Appliance
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
    * To obtain the request config of the operation appliancesUpdate
    *
    * @param id A unique integer value identifying this appliance. 
    * @param applianceRequest  
    * @return RequestConfig
    */
    fun appliancesUpdateRequestConfig(id: kotlin.Int, applianceRequest: ApplianceRequest) : RequestConfig<ApplianceRequest> {
        val localVariableBody = applianceRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()

        return RequestConfig(
            method = RequestMethod.PUT,
            path = "/api/appliances/{id}/".replace("{"+"id"+"}", "$id"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

}
