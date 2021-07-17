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
import com.print-nanny.client.models.PrintSession

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param id 
 * @param deleted 
 * @param createdDt 
 * @param name 
 * @param user 
 * @param publicKey 
 * @param fingerprint 
 * @param cloudiotDevice 
 * @param cloudiotDeviceName 
 * @param cloudiotDevicePath 
 * @param cloudiotDeviceNumId 
 * @param model 
 * @param platform 
 * @param serial 
 * @param cores 
 * @param ram 
 * @param pythonVersion 
 * @param pipVersion 
 * @param octoprintVersion 
 * @param pluginVersion 
 * @param printNannyClientVersion 
 * @param url 
 * @param privateKey 
 * @param privateKeyChecksum 
 * @param publicKeyChecksum 
 * @param cloudiotDeviceConfigs 
 * @param caCerts 
 * @param manageUrl 
 * @param monitoringActive 
 * @param cpuFlags 
 * @param hardware 
 * @param revision 
 * @param virtualenv 
 * @param activeSession 
 */

data class OctoPrintDeviceKey (
    @Json(name = "id")
    val id: kotlin.Int,
    @Json(name = "deleted")
    val deleted: java.time.OffsetDateTime,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime,
    @Json(name = "name")
    val name: kotlin.String,
    @Json(name = "user")
    val user: kotlin.Int,
    @Json(name = "public_key")
    val publicKey: kotlin.String,
    @Json(name = "fingerprint")
    val fingerprint: kotlin.String,
    @Json(name = "cloudiot_device")
    val cloudiotDevice: kotlin.collections.Map<kotlin.String, AnyType>,
    @Json(name = "cloudiot_device_name")
    val cloudiotDeviceName: kotlin.String,
    @Json(name = "cloudiot_device_path")
    val cloudiotDevicePath: kotlin.String,
    @Json(name = "cloudiot_device_num_id")
    val cloudiotDeviceNumId: kotlin.Int,
    @Json(name = "model")
    val model: kotlin.String,
    @Json(name = "platform")
    val platform: kotlin.String,
    @Json(name = "serial")
    val serial: kotlin.String,
    @Json(name = "cores")
    val cores: kotlin.Int,
    @Json(name = "ram")
    val ram: kotlin.Int,
    @Json(name = "python_version")
    val pythonVersion: kotlin.String,
    @Json(name = "pip_version")
    val pipVersion: kotlin.String,
    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String,
    @Json(name = "plugin_version")
    val pluginVersion: kotlin.String,
    @Json(name = "print_nanny_client_version")
    val printNannyClientVersion: kotlin.String,
    @Json(name = "url")
    val url: java.net.URI,
    @Json(name = "private_key")
    val privateKey: kotlin.String,
    @Json(name = "private_key_checksum")
    val privateKeyChecksum: kotlin.String,
    @Json(name = "public_key_checksum")
    val publicKeyChecksum: kotlin.String,
    @Json(name = "cloudiot_device_configs")
    val cloudiotDeviceConfigs: kotlin.String,
    @Json(name = "ca_certs")
    val caCerts: kotlin.collections.Map<kotlin.String, kotlin.String>,
    @Json(name = "manage_url")
    val manageUrl: java.net.URI,
    @Json(name = "monitoring_active")
    val monitoringActive: kotlin.Boolean,
    @Json(name = "cpu_flags")
    val cpuFlags: kotlin.collections.List<kotlin.String>? = null,
    @Json(name = "hardware")
    val hardware: kotlin.String? = null,
    @Json(name = "revision")
    val revision: kotlin.String? = null,
    @Json(name = "virtualenv")
    val virtualenv: kotlin.String? = null,
    @Json(name = "active_session")
    val activeSession: PrintSession? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

