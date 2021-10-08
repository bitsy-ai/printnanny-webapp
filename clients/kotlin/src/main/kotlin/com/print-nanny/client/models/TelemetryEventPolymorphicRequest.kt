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
import com.print-nanny.client.models.OctoPrintEventRequest
import com.print-nanny.client.models.OctoprintEnvironmentRequest
import com.print-nanny.client.models.OctoprintPrinterDataRequest
import com.print-nanny.client.models.PrintJobEventRequest
import com.print-nanny.client.models.PrintNannyPluginEventEventTypeEnum
import com.print-nanny.client.models.PrintNannyPluginEventRequest
import com.print-nanny.client.models.PrinterEventRequest
import com.print-nanny.client.models.PrinterStateEnum
import com.print-nanny.client.models.RemoteCommandEventRequest
import com.print-nanny.client.models.TelemetryEventRequest

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param eventType 
 * @param octoprintEnvironment 
 * @param octoprintPrinterData 
 * @param printNannyPluginVersion 
 * @param printNannyClientVersion 
 * @param octoprintVersion 
 * @param octoprintDevice 
 * @param ts 
 * @param eventSource 
 * @param eventData 
 * @param temperature 
 * @param printSession 
 * @param printerState 
 */

interface TelemetryEventPolymorphicRequest : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

    @Json(name = "event_type")
    val eventType: PrintNannyPluginEventEventTypeEnum
    @Json(name = "octoprint_environment")
    val octoprintEnvironment: OctoprintEnvironmentRequest
    @Json(name = "octoprint_printer_data")
    val octoprintPrinterData: OctoprintPrinterDataRequest
    @Json(name = "print_nanny_plugin_version")
    val printNannyPluginVersion: kotlin.String
    @Json(name = "print_nanny_client_version")
    val printNannyClientVersion: kotlin.String
    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int
    @Json(name = "ts")
    val ts: kotlin.Float?
    @Json(name = "event_source")
    val eventSource: EventSourceEnum?
    @Json(name = "event_data")
    val eventData: kotlin.collections.Map<kotlin.String, kotlin.Any>?
    @Json(name = "temperature")
    val temperature: kotlin.collections.Map<kotlin.String, kotlin.Any>?
    @Json(name = "print_session")
    val printSession: kotlin.Int?
    @Json(name = "printer_state")
    val printerState: PrinterStateEnum?
}

