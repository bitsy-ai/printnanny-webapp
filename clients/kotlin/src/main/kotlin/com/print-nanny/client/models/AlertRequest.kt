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

package com.print-nanny.client.models

import com.print-nanny.client.models.AlertEventTypeEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param octoprintDevice 
 * @param eventType 
 * @param seen 
 * @param sent 
 */

data class AlertRequest (

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

