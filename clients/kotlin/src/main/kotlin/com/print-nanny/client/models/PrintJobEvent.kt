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

import com.print-nanny.client.models.EventSourceEnum
import com.print-nanny.client.models.EventTypeD9eEnum
import com.print-nanny.client.models.OctoprintEnvironment
import com.print-nanny.client.models.OctoprintPrinterData

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param id 
 * @param eventType 
 * @param octoprintEnvironment 
 * @param octoprintPrinterData 
 * @param eventSource 
 * @param printNannyPluginVersion 
 * @param printNannyClientVersion 
 * @param octoprintVersion 
 * @param polymorphicCtype 
 * @param octoprintDevice 
 * @param user 
 * @param ts 
 * @param eventData 
 * @param temperature 
 * @param printSession 
 */

data class PrintJobEvent (

    @Json(name = "id")
    val id: kotlin.Int,

    @Json(name = "event_type")
    val eventType: EventTypeD9eEnum,

    @Json(name = "octoprint_environment")
    val octoprintEnvironment: OctoprintEnvironment,

    @Json(name = "octoprint_printer_data")
    val octoprintPrinterData: OctoprintPrinterData,

    @Json(name = "event_source")
    val eventSource: EventSourceEnum?,

    @Json(name = "print_nanny_plugin_version")
    val printNannyPluginVersion: kotlin.String,

    @Json(name = "print_nanny_client_version")
    val printNannyClientVersion: kotlin.String,

    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String,

    @Json(name = "polymorphic_ctype")
    val polymorphicCtype: kotlin.Int,

    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int,

    @Json(name = "user")
    val user: kotlin.Int,

    @Json(name = "ts")
    val ts: kotlin.Float? = null,

    @Json(name = "event_data")
    val eventData: kotlin.collections.Map<kotlin.String, kotlin.Any>? = null,

    @Json(name = "temperature")
    val temperature: kotlin.collections.Map<kotlin.String, kotlin.Any>? = null,

    @Json(name = "print_session")
    val printSession: kotlin.Int? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

