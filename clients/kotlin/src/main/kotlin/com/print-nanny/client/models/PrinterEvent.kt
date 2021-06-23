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
import com.print-nanny.client.models.EventSourceEnum
import com.print-nanny.client.models.PrinterEventEventTypeEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param eventType 
 * @param printNannyPluginVersion 
 * @param printNannyClientVersion 
 * @param octoprintVersion 
 * @param octoprintDevice 
 * @param id 
 * @param ts 
 * @param eventSource 
 * @param eventData 
 * @param octoprintEnvironment 
 * @param octoprintPrinterData 
 * @param temperature 
 * @param polymorphicCtype 
 * @param user 
 * @param printSession 
 */

data class PrinterEvent (
    @Json(name = "event_type")
    val eventType: PrinterEventEventTypeEnum,
    @Json(name = "print_nanny_plugin_version")
    val printNannyPluginVersion: kotlin.String,
    @Json(name = "print_nanny_client_version")
    val printNannyClientVersion: kotlin.String,
    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String,
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int,
    @Json(name = "id")
    val id: kotlin.Int? = null,
    @Json(name = "ts")
    val ts: java.time.OffsetDateTime? = null,
    @Json(name = "event_source")
    val eventSource: EventSourceEnum? = null,
    @Json(name = "event_data")
    val eventData: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "octoprint_environment")
    val octoprintEnvironment: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "octoprint_printer_data")
    val octoprintPrinterData: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "temperature")
    val temperature: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "polymorphic_ctype")
    val polymorphicCtype: kotlin.Int? = null,
    @Json(name = "user")
    val user: kotlin.Int? = null,
    @Json(name = "print_session")
    val printSession: kotlin.Int? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

