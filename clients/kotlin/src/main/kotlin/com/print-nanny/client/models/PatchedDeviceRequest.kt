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

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param user 
 * @param name 
 * @param publicKey 
 * @param fingerprint 
 * @param cloudiotDevice 
 * @param cloudiotDeviceName 
 * @param cloudiotDevicePath 
 * @param cloudiotDeviceNumId 
 * @param osVersion 
 * @param os 
 * @param kernelVersion 
 * @param hardware 
 * @param revision 
 * @param model 
 * @param serial 
 * @param cores 
 * @param ram 
 * @param cpuFlags 
 */

data class PatchedDeviceRequest (
    @Json(name = "user")
    val user: kotlin.Int? = null,
    @Json(name = "name")
    val name: kotlin.String? = null,
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
    val cloudiotDeviceNumId: kotlin.Long? = null,
    @Json(name = "os_version")
    val osVersion: kotlin.String? = null,
    @Json(name = "os")
    val os: kotlin.String? = null,
    @Json(name = "kernel_version")
    val kernelVersion: kotlin.String? = null,
    @Json(name = "hardware")
    val hardware: kotlin.String? = null,
    @Json(name = "revision")
    val revision: kotlin.String? = null,
    @Json(name = "model")
    val model: kotlin.String? = null,
    @Json(name = "serial")
    val serial: kotlin.String? = null,
    @Json(name = "cores")
    val cores: kotlin.Int? = null,
    @Json(name = "ram")
    val ram: kotlin.Int? = null,
    @Json(name = "cpu_flags")
    val cpuFlags: kotlin.String? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

