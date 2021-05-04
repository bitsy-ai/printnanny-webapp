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

import com.print-nanny.client.models.EventType92fEnum
import com.print-nanny.client.models.PartnerOctoPrintDevice

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param octoprintDevice 
 * @param eventType 
 * @param seen 
 * @param sent 
 * @param manageDeviceUrl 
 * @param time 
 * @param token 
 * @param timeRemaining 
 * @param timeElapsed 
 * @param progress 
 * @param gcodeFile 
 */

data class PartnerAlert (
    @Json(name = "octoprint_device")
    val octoprintDevice: PartnerOctoPrintDevice,
    @Json(name = "event_type")
    val eventType: EventType92fEnum? = null,
    @Json(name = "seen")
    val seen: kotlin.Boolean? = null,
    @Json(name = "sent")
    val sent: kotlin.Boolean? = null,
    @Json(name = "manage_device_url")
    val manageDeviceUrl: kotlin.String? = null,
    @Json(name = "time")
    val time: kotlin.String? = null,
    @Json(name = "token")
    val token: kotlin.String? = null,
    @Json(name = "time_remaining")
    val timeRemaining: kotlin.String? = null,
    @Json(name = "time_elapsed")
    val timeElapsed: kotlin.String? = null,
    @Json(name = "progress")
    val progress: kotlin.String? = null,
    @Json(name = "gcode_file")
    val gcodeFile: kotlin.String? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

