/**
 * print-nanny-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
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


import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param machineId Populated from /etc/machine-id
 * @param hardware Populated from /proc/cpuinfo HARDWARE
 * @param revision Populated from /proc/cpuinfo REVISION
 * @param model Populated from /proc/cpuinfo MODEL
 * @param serial Populated from /proc/cpuinfo SERIAL
 * @param cores 
 * @param ram 
 * @param imageVersion Print Nanny OS version string from /boot/image_version.txt
 * @param device 
 */

data class DeviceInfoRequest (

    /* Populated from /etc/machine-id */
    @Json(name = "machine_id")
    val machineId: kotlin.String,

    /* Populated from /proc/cpuinfo HARDWARE */
    @Json(name = "hardware")
    val hardware: kotlin.String,

    /* Populated from /proc/cpuinfo REVISION */
    @Json(name = "revision")
    val revision: kotlin.String,

    /* Populated from /proc/cpuinfo MODEL */
    @Json(name = "model")
    val model: kotlin.String,

    /* Populated from /proc/cpuinfo SERIAL */
    @Json(name = "serial")
    val serial: kotlin.String,

    @Json(name = "cores")
    val cores: kotlin.Int,

    @Json(name = "ram")
    val ram: kotlin.Long,

    /* Print Nanny OS version string from /boot/image_version.txt */
    @Json(name = "image_version")
    val imageVersion: kotlin.String,

    @Json(name = "device")
    val device: kotlin.Int

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

