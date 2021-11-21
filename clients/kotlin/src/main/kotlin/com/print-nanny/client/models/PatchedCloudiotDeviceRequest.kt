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


import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param numId 
 * @param name 
 * @param id 
 * @param device 
 */

data class PatchedCloudiotDeviceRequest (

    @Json(name = "num_id")
    val numId: kotlin.Long? = null,

    @Json(name = "name")
    val name: kotlin.String? = null,

    @Json(name = "id")
    val id: kotlin.String? = null,

    @Json(name = "device")
    val device: kotlin.Int? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

