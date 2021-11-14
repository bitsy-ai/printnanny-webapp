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

import com.print-nanny.client.models.CameraTypeEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param user 
 * @param device 
 * @param name 
 * @param cameraType 
 * @param cameraSource 
 */

data class PatchedCameraRequest (

    @Json(name = "user")
    val user: kotlin.Int? = null,

    @Json(name = "device")
    val device: kotlin.Int? = null,

    @Json(name = "name")
    val name: kotlin.String? = null,

    @Json(name = "camera_type")
    val cameraType: CameraTypeEnum? = null,

    @Json(name = "camera_source")
    val cameraSource: kotlin.String? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

