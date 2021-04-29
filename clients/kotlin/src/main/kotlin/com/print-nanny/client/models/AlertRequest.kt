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

import com.print-nanny.client.models.AlertMethodEnum
import com.print-nanny.client.models.OneOfLessThanAlertEventTypeEnumCommaNullEnumGreaterThan

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param alertMethod 
 * @param eventType 
 * @param annotatedVideo 
 * @param seen 
 * @param sent 
 * @param printSession 
 * @param octoprintDevice 
 */

data class AlertRequest (
    @Json(name = "alert_method")
    val alertMethod: AlertMethodEnum,
    @Json(name = "event_type")
    val eventType: OneOfLessThanAlertEventTypeEnumCommaNullEnumGreaterThan? = null,
    @Json(name = "annotated_video")
    val annotatedVideo: java.io.File? = null,
    @Json(name = "seen")
    val seen: kotlin.Boolean? = null,
    @Json(name = "sent")
    val sent: kotlin.Boolean? = null,
    @Json(name = "print_session")
    val printSession: kotlin.Int? = null,
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

