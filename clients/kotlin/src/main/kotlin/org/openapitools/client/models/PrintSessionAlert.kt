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

import org.openapitools.client.models.AlertMethodsEnum
import org.openapitools.client.models.AlertTypeEnum
import org.openapitools.client.models.PrintSessionAlertAlertSubtypeEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param annotatedVideo 
 * @param printSession 
 * @param id 
 * @param time 
 * @param alertMethods 
 * @param alertType 
 * @param createdDt 
 * @param updatedDt 
 * @param seen 
 * @param sent 
 * @param needsReview 
 * @param alertSubtype 
 * @param polymorphicCtype 
 * @param user 
 * @param octoprintDevice 
 */

data class PrintSessionAlert (
    @Json(name = "annotated_video")
    val annotatedVideo: java.net.URI,
    @Json(name = "print_session")
    val printSession: kotlin.Int,
    @Json(name = "id")
    val id: kotlin.Int? = null,
    @Json(name = "time")
    val time: kotlin.String? = null,
    @Json(name = "alert_methods")
    val alertMethods: kotlin.collections.List<AlertMethodsEnum>? = null,
    @Json(name = "alert_type")
    val alertType: AlertTypeEnum? = null,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime? = null,
    @Json(name = "seen")
    val seen: kotlin.Boolean? = null,
    @Json(name = "sent")
    val sent: kotlin.Boolean? = null,
    @Json(name = "needs_review")
    val needsReview: kotlin.Boolean? = null,
    @Json(name = "alert_subtype")
    val alertSubtype: PrintSessionAlertAlertSubtypeEnum? = null,
    @Json(name = "polymorphic_ctype")
    val polymorphicCtype: kotlin.Int? = null,
    @Json(name = "user")
    val user: kotlin.Int? = null,
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

