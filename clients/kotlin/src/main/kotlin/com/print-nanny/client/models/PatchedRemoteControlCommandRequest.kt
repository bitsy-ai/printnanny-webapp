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

package com.print-nanny.client.models

import com.print-nanny.client.models.RemoteControlCommandCommandEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param command 
 * @param user 
 * @param device 
 * @param received 
 * @param success 
 * @param iotcoreResponse 
 * @param metadata 
 */

data class PatchedRemoteControlCommandRequest (

    @Json(name = "command")
    val command: RemoteControlCommandCommandEnum? = null,

    @Json(name = "user")
    val user: kotlin.Int? = null,

    @Json(name = "device")
    val device: kotlin.Int? = null,

    @Json(name = "received")
    val received: kotlin.Boolean? = null,

    @Json(name = "success")
    val success: kotlin.Boolean? = null,

    @Json(name = "iotcore_response")
    val iotcoreResponse: kotlin.collections.Map<kotlin.String, kotlin.Any>? = null,

    @Json(name = "metadata")
    val metadata: kotlin.collections.Map<kotlin.String, kotlin.Any>? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

