/**
* 
* No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
*
* The version of the OpenAPI document: 0.0.0
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
package com.print-nanny.client.apis

import com.print-nanny.client.models.CameraController
import com.print-nanny.client.models.CameraControllerRequest
import com.print-nanny.client.models.Device
import com.print-nanny.client.models.DeviceIdentity
import com.print-nanny.client.models.DeviceRequest
import com.print-nanny.client.models.PaginatedCameraControllerList
import com.print-nanny.client.models.PaginatedDeviceList
import com.print-nanny.client.models.PatchedCameraControllerRequest
import com.print-nanny.client.models.PatchedDeviceRequest

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

class DevicesApi(basePath: kotlin.String = defaultBasePath) : ApiClient(basePath) {
    companion object {
        @JvmStatic
        val defaultBasePath: String by lazy {
            System.getProperties().getProperty("com.print-nanny.client.baseUrl", "http://localhost")
        }
    }

    /**
    * 
    * 
    * @param deviceId  
    * @param cameraControllerRequest  
    * @return CameraController
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesCamerasCreate(deviceId: kotlin.Int, cameraControllerRequest: CameraControllerRequest) : CameraController {
        val localVariableConfig = devicesCamerasCreateRequestConfig(deviceId = deviceId, cameraControllerRequest = cameraControllerRequest)

        val localVarResponse = request<CameraController>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as CameraController
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
    * To obtain the request config of the operation devicesCamerasCreate
    *
    * @param deviceId  
    * @param cameraControllerRequest  
    * @return RequestConfig
    */
    fun devicesCamerasCreateRequestConfig(deviceId: kotlin.Int, cameraControllerRequest: CameraControllerRequest) : RequestConfig {
        val localVariableBody: kotlin.Any? = cameraControllerRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.POST,
            path = "/api/devices/{device_id}/cameras/".replace("{"+"device_id"+"}", "$deviceId"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

    /**
    * 
    * 
    * @param deviceId  
    * @param page A page number within the paginated result set. (optional)
    * @return PaginatedCameraControllerList
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesCamerasList(deviceId: kotlin.Int, page: kotlin.Int?) : PaginatedCameraControllerList {
        val localVariableConfig = devicesCamerasListRequestConfig(deviceId = deviceId, page = page)

        val localVarResponse = request<PaginatedCameraControllerList>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as PaginatedCameraControllerList
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
    * To obtain the request config of the operation devicesCamerasList
    *
    * @param deviceId  
    * @param page A page number within the paginated result set. (optional)
    * @return RequestConfig
    */
    fun devicesCamerasListRequestConfig(deviceId: kotlin.Int, page: kotlin.Int?) : RequestConfig {
        val localVariableBody: kotlin.Any? = null
        val localVariableQuery: MultiValueMap = mutableMapOf<kotlin.String, List<kotlin.String>>()
            .apply {
                if (page != null) {
                    put("page", listOf(page.toString()))
                }
            }
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.GET,
            path = "/api/devices/{device_id}/cameras/".replace("{"+"device_id"+"}", "$deviceId"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

    /**
    * 
    * 
    * @param deviceId  
    * @param id A unique integer value identifying this camera controller. 
    * @param patchedCameraControllerRequest  (optional)
    * @return CameraController
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesCamerasPartialUpdate(deviceId: kotlin.Int, id: kotlin.Int, patchedCameraControllerRequest: PatchedCameraControllerRequest?) : CameraController {
        val localVariableConfig = devicesCamerasPartialUpdateRequestConfig(deviceId = deviceId, id = id, patchedCameraControllerRequest = patchedCameraControllerRequest)

        val localVarResponse = request<CameraController>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as CameraController
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
    * To obtain the request config of the operation devicesCamerasPartialUpdate
    *
    * @param deviceId  
    * @param id A unique integer value identifying this camera controller. 
    * @param patchedCameraControllerRequest  (optional)
    * @return RequestConfig
    */
    fun devicesCamerasPartialUpdateRequestConfig(deviceId: kotlin.Int, id: kotlin.Int, patchedCameraControllerRequest: PatchedCameraControllerRequest?) : RequestConfig {
        val localVariableBody: kotlin.Any? = patchedCameraControllerRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.PATCH,
            path = "/api/devices/{device_id}/cameras/{id}/".replace("{"+"device_id"+"}", "$deviceId").replace("{"+"id"+"}", "$id"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

    /**
    * 
    * 
    * @param deviceId  
    * @param id A unique integer value identifying this camera controller. 
    * @return CameraController
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesCamerasRetrieve(deviceId: kotlin.Int, id: kotlin.Int) : CameraController {
        val localVariableConfig = devicesCamerasRetrieveRequestConfig(deviceId = deviceId, id = id)

        val localVarResponse = request<CameraController>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as CameraController
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
    * To obtain the request config of the operation devicesCamerasRetrieve
    *
    * @param deviceId  
    * @param id A unique integer value identifying this camera controller. 
    * @return RequestConfig
    */
    fun devicesCamerasRetrieveRequestConfig(deviceId: kotlin.Int, id: kotlin.Int) : RequestConfig {
        val localVariableBody: kotlin.Any? = null
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.GET,
            path = "/api/devices/{device_id}/cameras/{id}/".replace("{"+"device_id"+"}", "$deviceId").replace("{"+"id"+"}", "$id"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

    /**
    * 
    * 
    * @param deviceId  
    * @param id A unique integer value identifying this camera controller. 
    * @param cameraControllerRequest  
    * @return CameraController
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesCamerasUpdate(deviceId: kotlin.Int, id: kotlin.Int, cameraControllerRequest: CameraControllerRequest) : CameraController {
        val localVariableConfig = devicesCamerasUpdateRequestConfig(deviceId = deviceId, id = id, cameraControllerRequest = cameraControllerRequest)

        val localVarResponse = request<CameraController>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as CameraController
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
    * To obtain the request config of the operation devicesCamerasUpdate
    *
    * @param deviceId  
    * @param id A unique integer value identifying this camera controller. 
    * @param cameraControllerRequest  
    * @return RequestConfig
    */
    fun devicesCamerasUpdateRequestConfig(deviceId: kotlin.Int, id: kotlin.Int, cameraControllerRequest: CameraControllerRequest) : RequestConfig {
        val localVariableBody: kotlin.Any? = cameraControllerRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.PUT,
            path = "/api/devices/{device_id}/cameras/{id}/".replace("{"+"device_id"+"}", "$deviceId").replace("{"+"id"+"}", "$id"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

    /**
    * 
    * 
    * @param deviceRequest  
    * @return Device
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesCreate(deviceRequest: DeviceRequest) : Device {
        val localVariableConfig = devicesCreateRequestConfig(deviceRequest = deviceRequest)

        val localVarResponse = request<Device>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as Device
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
    * To obtain the request config of the operation devicesCreate
    *
    * @param deviceRequest  
    * @return RequestConfig
    */
    fun devicesCreateRequestConfig(deviceRequest: DeviceRequest) : RequestConfig {
        val localVariableBody: kotlin.Any? = deviceRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.POST,
            path = "/api/devices/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

    /**
    * 
    * 
    * @param page A page number within the paginated result set. (optional)
    * @return PaginatedDeviceList
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesList(page: kotlin.Int?) : PaginatedDeviceList {
        val localVariableConfig = devicesListRequestConfig(page = page)

        val localVarResponse = request<PaginatedDeviceList>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as PaginatedDeviceList
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
    * To obtain the request config of the operation devicesList
    *
    * @param page A page number within the paginated result set. (optional)
    * @return RequestConfig
    */
    fun devicesListRequestConfig(page: kotlin.Int?) : RequestConfig {
        val localVariableBody: kotlin.Any? = null
        val localVariableQuery: MultiValueMap = mutableMapOf<kotlin.String, List<kotlin.String>>()
            .apply {
                if (page != null) {
                    put("page", listOf(page.toString()))
                }
            }
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.GET,
            path = "/api/devices/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

    /**
    * 
    * 
    * @param id A unique integer value identifying this device. 
    * @param patchedDeviceRequest  (optional)
    * @return Device
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesPartialUpdate(id: kotlin.Int, patchedDeviceRequest: PatchedDeviceRequest?) : Device {
        val localVariableConfig = devicesPartialUpdateRequestConfig(id = id, patchedDeviceRequest = patchedDeviceRequest)

        val localVarResponse = request<Device>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as Device
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
    * To obtain the request config of the operation devicesPartialUpdate
    *
    * @param id A unique integer value identifying this device. 
    * @param patchedDeviceRequest  (optional)
    * @return RequestConfig
    */
    fun devicesPartialUpdateRequestConfig(id: kotlin.Int, patchedDeviceRequest: PatchedDeviceRequest?) : RequestConfig {
        val localVariableBody: kotlin.Any? = patchedDeviceRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.PATCH,
            path = "/api/devices/{id}/".replace("{"+"id"+"}", "$id"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

    /**
    * 
    * 
    * @param id A unique integer value identifying this device. 
    * @return Device
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesRetrieve(id: kotlin.Int) : Device {
        val localVariableConfig = devicesRetrieveRequestConfig(id = id)

        val localVarResponse = request<Device>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as Device
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
    * To obtain the request config of the operation devicesRetrieve
    *
    * @param id A unique integer value identifying this device. 
    * @return RequestConfig
    */
    fun devicesRetrieveRequestConfig(id: kotlin.Int) : RequestConfig {
        val localVariableBody: kotlin.Any? = null
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.GET,
            path = "/api/devices/{id}/".replace("{"+"id"+"}", "$id"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

    /**
    * 
    * 
    * @param id A unique integer value identifying this device. 
    * @param deviceRequest  
    * @return Device
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesUpdate(id: kotlin.Int, deviceRequest: DeviceRequest) : Device {
        val localVariableConfig = devicesUpdateRequestConfig(id = id, deviceRequest = deviceRequest)

        val localVarResponse = request<Device>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as Device
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
    * To obtain the request config of the operation devicesUpdate
    *
    * @param id A unique integer value identifying this device. 
    * @param deviceRequest  
    * @return RequestConfig
    */
    fun devicesUpdateRequestConfig(id: kotlin.Int, deviceRequest: DeviceRequest) : RequestConfig {
        val localVariableBody: kotlin.Any? = deviceRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.PUT,
            path = "/api/devices/{id}/".replace("{"+"id"+"}", "$id"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

    /**
    * 
    * 
    * @param deviceRequest  
    * @return DeviceIdentity
    * @throws UnsupportedOperationException If the API returns an informational or redirection response
    * @throws ClientException If the API returns a client error response
    * @throws ServerException If the API returns a server error response
    */
    @Suppress("UNCHECKED_CAST")
    @Throws(UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun devicesUpdateOrCreate(deviceRequest: DeviceRequest) : DeviceIdentity {
        val localVariableConfig = devicesUpdateOrCreateRequestConfig(deviceRequest = deviceRequest)

        val localVarResponse = request<DeviceIdentity>(
            localVariableConfig
        )

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as DeviceIdentity
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
    * To obtain the request config of the operation devicesUpdateOrCreate
    *
    * @param deviceRequest  
    * @return RequestConfig
    */
    fun devicesUpdateOrCreateRequestConfig(deviceRequest: DeviceRequest) : RequestConfig {
        val localVariableBody: kotlin.Any? = deviceRequest
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        
        val localVariableConfig = RequestConfig(
            method = RequestMethod.POST,
            path = "/api/devices/update-or-create/",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )

        return localVariableConfig
    }

}
