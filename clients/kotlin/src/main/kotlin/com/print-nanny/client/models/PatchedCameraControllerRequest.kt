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

import com.print-nanny.client.models.CameraSourceTypeEnum
import com.print-nanny.client.models.CameraTypeEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param name 
 * @param cameraType 
 * @param cameraSource 
 * @param cameraSourceType 
 * @param device 
 */

data class PatchedCameraControllerRequest (
    @Json(name = "name")
    val name: kotlin.String? = null,
    @Json(name = "camera_type")
    val cameraType: CameraTypeEnum? = null,
    @Json(name = "camera_source")
    val cameraSource: kotlin.String? = null,
    @Json(name = "camera_source_type")
    val cameraSourceType: CameraSourceTypeEnum? = null,
    @Json(name = "device")
    val device: kotlin.Int? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

