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

import com.print-nanny.client.models.DeviceIdentityCaCerts

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param id 
 * @param deleted 
 * @param createdDt 
 * @param updatedDt 
 * @param user 
 * @param name 
 * @param publicKey 
 * @param fingerprint 
 * @param cloudiotDeviceName 
 * @param cloudiotDevicePath 
 * @param cloudiotDeviceNumId 
 * @param osVersion 
 * @param os 
 * @param kernelVersion 
 * @param cores 
 * @param ram 
 * @param cpuFlags 
 * @param url 
 * @param privateKey 
 * @param privateKeyChecksum 
 * @param publicKeyChecksum 
 * @param cloudiotDeviceConfigs 
 * @param caCerts 
 * @param hardware 
 * @param revision 
 * @param model 
 * @param serial 
 */

data class DeviceIdentity (
    @Json(name = "id")
    val id: kotlin.Int,
    @Json(name = "deleted")
    val deleted: java.time.OffsetDateTime,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime,
    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime,
    @Json(name = "user")
    val user: kotlin.Int,
    @Json(name = "name")
    val name: kotlin.String,
    @Json(name = "public_key")
    val publicKey: kotlin.String,
    @Json(name = "fingerprint")
    val fingerprint: kotlin.String,
    @Json(name = "cloudiot_device_name")
    val cloudiotDeviceName: kotlin.String,
    @Json(name = "cloudiot_device_path")
    val cloudiotDevicePath: kotlin.String,
    @Json(name = "cloudiot_device_num_id")
    val cloudiotDeviceNumId: kotlin.Long,
    @Json(name = "os_version")
    val osVersion: kotlin.String,
    @Json(name = "os")
    val os: kotlin.String,
    @Json(name = "kernel_version")
    val kernelVersion: kotlin.String,
    @Json(name = "cores")
    val cores: kotlin.Int,
    @Json(name = "ram")
    val ram: kotlin.Long,
    @Json(name = "cpu_flags")
    val cpuFlags: kotlin.collections.List<kotlin.String>,
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
    val caCerts: DeviceIdentityCaCerts,
    @Json(name = "hardware")
    val hardware: kotlin.String? = null,
    @Json(name = "revision")
    val revision: kotlin.String? = null,
    @Json(name = "model")
    val model: kotlin.String? = null,
    @Json(name = "serial")
    val serial: kotlin.String? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

