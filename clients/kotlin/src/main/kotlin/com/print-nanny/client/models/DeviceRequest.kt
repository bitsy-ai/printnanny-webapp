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
 * @param hardware 
 * @param revision 
 * @param model 
 * @param serial 
 */

data class DeviceRequest (
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

