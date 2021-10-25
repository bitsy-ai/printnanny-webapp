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

import com.print-nanny.client.models.Camera
import com.print-nanny.client.models.CloudiotDevice
import com.print-nanny.client.models.CurrentState
import com.print-nanny.client.models.DesiredConfig
import com.print-nanny.client.models.DevicePublicKey
import com.print-nanny.client.models.PrinterController

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param hostname 
 * @param hardware 
 * @param revision 
 * @param model 
 * @param serial 
 * @param cores 
 * @param ram 
 * @param id 
 * @param cloudiotDevices 
 * @param cameras 
 * @param dashboardUrl 
 * @param desiredConfig 
 * @param desiredConfigTopic 
 * @param currentState 
 * @param currentStateTopic 
 * @param printerControllers 
 * @param publicKey 
 * @param user 
 * @param deleted 
 * @param createdDt 
 * @param updatedDt 
 */

data class Device (

    @Json(name = "hostname")
    val hostname: kotlin.String,

    @Json(name = "hardware")
    val hardware: kotlin.String,

    @Json(name = "revision")
    val revision: kotlin.String,

    @Json(name = "model")
    val model: kotlin.String,

    @Json(name = "serial")
    val serial: kotlin.String,

    @Json(name = "cores")
    val cores: kotlin.Int,

    @Json(name = "ram")
    val ram: kotlin.Long,

    @Json(name = "id")
    val id: kotlin.Int? = null,

    @Json(name = "cloudiot_devices")
    val cloudiotDevices: kotlin.collections.List<CloudiotDevice>? = null,

    @Json(name = "cameras")
    val cameras: kotlin.collections.List<Camera>? = null,

    @Json(name = "dashboard_url")
    val dashboardUrl: kotlin.String? = null,

    @Json(name = "desired_config")
    val desiredConfig: DesiredConfig? = null,

    @Json(name = "desired_config_topic")
    val desiredConfigTopic: kotlin.String? = null,

    @Json(name = "current_state")
    val currentState: CurrentState? = null,

    @Json(name = "current_state_topic")
    val currentStateTopic: kotlin.String? = null,

    @Json(name = "printer_controllers")
    val printerControllers: kotlin.collections.List<PrinterController>? = null,

    @Json(name = "public_key")
    val publicKey: DevicePublicKey? = null,

    @Json(name = "user")
    val user: kotlin.Int? = null,

    @Json(name = "deleted")
    val deleted: java.time.OffsetDateTime? = null,

    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,

    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

