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

import com.print-nanny.client.models.PrintSession

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param caCerts 
 * @param cloudiotDeviceConfigs 
 * @param cloudiotDeviceName 
 * @param cloudiotDeviceNumId 
 * @param cloudiotDevicePath 
 * @param cloudiotDevice 
 * @param cores 
 * @param createdDt 
 * @param fingerprint 
 * @param id 
 * @param manageUrl 
 * @param model 
 * @param monitoringActive 
 * @param name 
 * @param octoprintVersion 
 * @param pipVersion 
 * @param platform 
 * @param pluginVersion 
 * @param printNannyClientVersion 
 * @param privateKeyChecksum 
 * @param privateKey 
 * @param publicKeyChecksum 
 * @param publicKey 
 * @param pythonVersion 
 * @param ram 
 * @param serial 
 * @param user 
 * @param url 
 * @param activeSession 
 * @param cpuFlags 
 * @param hardware 
 * @param revision 
 */

data class OctoPrintDeviceKey (

    @Json(name = "ca_certs")
    val caCerts: kotlin.collections.Map<kotlin.String, kotlin.String>,

    @Json(name = "cloudiot_device_configs")
    val cloudiotDeviceConfigs: kotlin.String,

    @Json(name = "cloudiot_device_name")
    val cloudiotDeviceName: kotlin.String,

    @Json(name = "cloudiot_device_num_id")
    val cloudiotDeviceNumId: kotlin.Int,

    @Json(name = "cloudiot_device_path")
    val cloudiotDevicePath: kotlin.String,

    @Json(name = "cloudiot_device")
    val cloudiotDevice: kotlin.collections.Map<kotlin.String, kotlin.Any>,

    @Json(name = "cores")
    val cores: kotlin.Int,

    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime,

    @Json(name = "fingerprint")
    val fingerprint: kotlin.String,

    @Json(name = "id")
    val id: kotlin.Int,

    @Json(name = "manage_url")
    val manageUrl: java.net.URI,

    @Json(name = "model")
    val model: kotlin.String,

    @Json(name = "monitoring_active")
    val monitoringActive: kotlin.Boolean,

    @Json(name = "name")
    val name: kotlin.String,

    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String,

    @Json(name = "pip_version")
    val pipVersion: kotlin.String,

    @Json(name = "platform")
    val platform: kotlin.String,

    @Json(name = "plugin_version")
    val pluginVersion: kotlin.String,

    @Json(name = "print_nanny_client_version")
    val printNannyClientVersion: kotlin.String,

    @Json(name = "private_key_checksum")
    val privateKeyChecksum: kotlin.String,

    @Json(name = "private_key")
    val privateKey: kotlin.String,

    @Json(name = "public_key_checksum")
    val publicKeyChecksum: kotlin.String,

    @Json(name = "public_key")
    val publicKey: kotlin.String,

    @Json(name = "python_version")
    val pythonVersion: kotlin.String,

    @Json(name = "ram")
    val ram: kotlin.Int,

    @Json(name = "serial")
    val serial: kotlin.String,

    @Json(name = "user")
    val user: kotlin.Int,

    @Json(name = "url")
    val url: java.net.URI,

    @Json(name = "active_session")
    val activeSession: PrintSession? = null,

    @Json(name = "cpu_flags")
    val cpuFlags: kotlin.collections.List<kotlin.String>? = null,

    @Json(name = "hardware")
    val hardware: kotlin.String? = null,

    @Json(name = "revision")
    val revision: kotlin.String? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

