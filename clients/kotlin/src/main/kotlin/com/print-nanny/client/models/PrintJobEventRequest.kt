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
import com.print-nanny.client.models.EventTypeD9eEnum
import com.print-nanny.client.models.OctoprintEnvironmentRequest
import com.print-nanny.client.models.OctoprintPrinterDataRequest

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param eventType 
 * @param octoprintEnvironment 
 * @param octoprintPrinterData 
 * @param printNannyPluginVersion 
 * @param printNannyClientVersion 
 * @param octoprintVersion 
 * @param octoprintDevice 
 * @param ts 
 * @param eventData 
 * @param temperature 
 * @param printSession 
 */

data class PrintJobEventRequest (
    @Json(name = "event_type")
    val eventType: EventTypeD9eEnum,
    @Json(name = "octoprint_environment")
    val octoprintEnvironment: OctoprintEnvironmentRequest,
    @Json(name = "octoprint_printer_data")
    val octoprintPrinterData: OctoprintPrinterDataRequest,
    @Json(name = "print_nanny_plugin_version")
    val printNannyPluginVersion: kotlin.String,
    @Json(name = "print_nanny_client_version")
    val printNannyClientVersion: kotlin.String,
    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String,
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int,
    @Json(name = "ts")
    val ts: kotlin.Float? = null,
    @Json(name = "event_data")
    val eventData: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "temperature")
    val temperature: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "print_session")
    val printSession: kotlin.Int? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

