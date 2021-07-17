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
import com.print-nanny.client.models.DeviceIdentityCaCerts

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param name 
 * @param osVersion 
 * @param os 
 * @param kernelVersion 
 * @param cores 
 * @param ram 
 * @param cpuFlags 
 * @param id 
 * @param deleted 
 * @param createdDt 
 * @param updatedDt 
 * @param user 
 * @param publicKey 
 * @param fingerprint 
 * @param cloudiotDevice 
 * @param cloudiotDeviceName 
 * @param cloudiotDevicePath 
 * @param cloudiotDeviceNumId 
 * @param hardware 
 * @param revision 
 * @param model 
 * @param serial 
 * @param url 
 * @param privateKey 
 * @param privateKeyChecksum 
 * @param publicKeyChecksum 
 * @param cloudiotDeviceConfigs 
 * @param caCerts 
 * @param manageUrl 
 */

data class DeviceIdentity (
    @Json(name = "name")
    val name: kotlin.String,
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
    @Json(name = "id")
    val id: kotlin.Int? = null,
    @Json(name = "deleted")
    val deleted: java.time.OffsetDateTime? = null,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime? = null,
    @Json(name = "user")
    val user: kotlin.Int? = null,
    @Json(name = "public_key")
    val publicKey: kotlin.String? = null,
    @Json(name = "fingerprint")
    val fingerprint: kotlin.String? = null,
    @Json(name = "cloudiot_device")
    val cloudiotDevice: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "cloudiot_device_name")
    val cloudiotDeviceName: kotlin.String? = null,
    @Json(name = "cloudiot_device_path")
    val cloudiotDevicePath: kotlin.String? = null,
    @Json(name = "cloudiot_device_num_id")
    val cloudiotDeviceNumId: kotlin.Int? = null,
    @Json(name = "hardware")
    val hardware: kotlin.String? = null,
    @Json(name = "revision")
    val revision: kotlin.String? = null,
    @Json(name = "model")
    val model: kotlin.String? = null,
    @Json(name = "serial")
    val serial: kotlin.String? = null,
    @Json(name = "url")
    val url: java.net.URI? = null,
    @Json(name = "private_key")
    val privateKey: kotlin.String? = null,
    @Json(name = "private_key_checksum")
    val privateKeyChecksum: kotlin.String? = null,
    @Json(name = "public_key_checksum")
    val publicKeyChecksum: kotlin.String? = null,
    @Json(name = "cloudiot_device_configs")
    val cloudiotDeviceConfigs: kotlin.String? = null,
    @Json(name = "ca_certs")
    val caCerts: DeviceIdentityCaCerts? = null,
    @Json(name = "manage_url")
    val manageUrl: java.net.URI? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

