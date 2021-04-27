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
package org.openapitools.client.models

import org.openapitools.client.models.AnyType
import org.openapitools.client.models.CommandEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param command 
 * @param user 
 * @param device 
 * @param id 
 * @param createdDt 
 * @param received 
 * @param success 
 * @param iotcoreResponse 
 * @param metadata 
 * @param url 
 * @param octoprintEventType 
 */

data class RemoteControlCommand (
    @Json(name = "command")
    val command: CommandEnum,
    @Json(name = "user")
    val user: kotlin.Int,
    @Json(name = "device")
    val device: kotlin.Int,
    @Json(name = "id")
    val id: kotlin.Int? = null,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "received")
    val received: kotlin.Boolean? = null,
    @Json(name = "success")
    val success: kotlin.Boolean? = null,
    @Json(name = "iotcore_response")
    val iotcoreResponse: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "metadata")
    val metadata: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "url")
    val url: java.net.URI? = null,
    @Json(name = "octoprint_event_type")
    val octoprintEventType: kotlin.String? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

