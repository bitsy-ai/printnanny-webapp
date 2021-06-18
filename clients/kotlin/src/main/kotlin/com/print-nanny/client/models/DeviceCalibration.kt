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
 * @param octoprintDevice 
 * @param id 
 * @param createdDt 
 * @param updatedDt 
 * @param fps 
 * @param xy 
 * @param height 
 * @param width 
 * @param url 
 */

data class DeviceCalibration (
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int,
    @Json(name = "id")
    val id: kotlin.Int? = null,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime? = null,
    @Json(name = "fps")
    val fps: kotlin.Float? = null,
    @Json(name = "xy")
    val xy: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "height")
    val height: kotlin.Int? = null,
    @Json(name = "width")
    val width: kotlin.Int? = null,
    @Json(name = "url")
    val url: java.net.URI? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

