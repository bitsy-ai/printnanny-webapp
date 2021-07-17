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

import com.print-nanny.client.models.AlertEventTypeEnum
import com.print-nanny.client.models.AlertMethodEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param id 
 * @param time 
 * @param gcodeFile 
 * @param printProgress 
 * @param timeElapsed 
 * @param timeRemaining 
 * @param manageDeviceUrl 
 * @param user 
 * @param alertMethod 
 * @param createdDt 
 * @param updatedDt 
 * @param message 
 * @param octoprintDevice 
 * @param eventType 
 * @param seen 
 * @param sent 
 */

data class Alert (
    @Json(name = "id")
    val id: kotlin.Int,
    @Json(name = "time")
    val time: kotlin.String,
    @Json(name = "gcode_file")
    val gcodeFile: kotlin.String,
    @Json(name = "print_progress")
    val printProgress: kotlin.String,
    @Json(name = "time_elapsed")
    val timeElapsed: kotlin.String,
    @Json(name = "time_remaining")
    val timeRemaining: kotlin.String,
    @Json(name = "manage_device_url")
    val manageDeviceUrl: kotlin.String?,
    @Json(name = "user")
    val user: kotlin.Int,
    @Json(name = "alert_method")
    val alertMethod: AlertMethodEnum,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime,
    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime,
    @Json(name = "message")
    val message: kotlin.String,
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int? = null,
    @Json(name = "event_type")
    val eventType: AlertEventTypeEnum? = null,
    @Json(name = "seen")
    val seen: kotlin.Boolean? = null,
    @Json(name = "sent")
    val sent: kotlin.Boolean? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

