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
package com.print-nanny.client.models

import com.print-nanny.client.models.AnyType
import com.print-nanny.client.models.CommandEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param id 
 * @param createdDt 
 * @param command 
 * @param user 
 * @param device 
 * @param url 
 * @param octoprintEventType 
 * @param received 
 * @param success 
 * @param iotcoreResponse 
 * @param metadata 
 */

data class RemoteControlCommand (
    @Json(name = "id")
    val id: kotlin.Int,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime,
    @Json(name = "command")
    val command: CommandEnum,
    @Json(name = "user")
    val user: kotlin.Int,
    @Json(name = "device")
    val device: kotlin.Int,
    @Json(name = "url")
    val url: java.net.URI,
    @Json(name = "octoprint_event_type")
    val octoprintEventType: kotlin.String,
    @Json(name = "received")
    val received: kotlin.Boolean? = null,
    @Json(name = "success")
    val success: kotlin.Boolean? = null,
    @Json(name = "iotcore_response")
    val iotcoreResponse: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "metadata")
    val metadata: kotlin.collections.Map<kotlin.String, AnyType>? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

