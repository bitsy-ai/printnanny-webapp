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
import com.print-nanny.client.models.PatchedOctoprintPrinterProfileRequest
import com.print-nanny.client.models.PatchedPrinterProfileRequest

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param name 
 * @param localWebcam 
 * @param controller 
 * @param device 
 * @param axesEInverted 
 * @param axesESpeed 
 * @param axesXSpeed 
 * @param axesXInverted 
 * @param axesYInverted 
 * @param axesYSpeed 
 * @param axesZInverted 
 * @param axesZSpeed 
 * @param extruderCount 
 * @param extruderNozzleDiameter 
 * @param extruderSharedNozzle 
 * @param heatedBed 
 * @param heatedChamber 
 * @param model 
 * @param volumeCustomBox 
 * @param volumeDepth 
 * @param volumeFormfactor 
 * @param volumeHeight 
 * @param volumeOrigin 
 * @param volumeWidth 
 * @param octoprintController 
 */

interface PatchedPrinterProfilePolymorphicRequest : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

    @Json(name = "name")
    val name: kotlin.String?
    @Json(name = "local_webcam")
    val localWebcam: kotlin.String?
    @Json(name = "controller")
    val controller: kotlin.Int?
    @Json(name = "device")
    val device: kotlin.Int?
    @Json(name = "axes_e_inverted")
    val axesEInverted: kotlin.Boolean?
    @Json(name = "axes_e_speed")
    val axesESpeed: kotlin.Int?
    @Json(name = "axes_x_speed")
    val axesXSpeed: kotlin.Int?
    @Json(name = "axes_x_inverted")
    val axesXInverted: kotlin.Boolean?
    @Json(name = "axes_y_inverted")
    val axesYInverted: kotlin.Boolean?
    @Json(name = "axes_y_speed")
    val axesYSpeed: kotlin.Int?
    @Json(name = "axes_z_inverted")
    val axesZInverted: kotlin.Boolean?
    @Json(name = "axes_z_speed")
    val axesZSpeed: kotlin.Int?
    @Json(name = "extruder_count")
    val extruderCount: kotlin.Int?
    @Json(name = "extruder_nozzle_diameter")
    val extruderNozzleDiameter: kotlin.Float?
    @Json(name = "extruder_shared_nozzle")
    val extruderSharedNozzle: kotlin.Boolean?
    @Json(name = "heated_bed")
    val heatedBed: kotlin.Boolean?
    @Json(name = "heated_chamber")
    val heatedChamber: kotlin.Boolean?
    @Json(name = "model")
    val model: kotlin.String?
    @Json(name = "volume_custom_box")
    val volumeCustomBox: kotlin.collections.Map<kotlin.String, AnyType>?
    @Json(name = "volume_depth")
    val volumeDepth: kotlin.Float?
    @Json(name = "volume_formfactor")
    val volumeFormfactor: kotlin.String?
    @Json(name = "volume_height")
    val volumeHeight: kotlin.Float?
    @Json(name = "volume_origin")
    val volumeOrigin: kotlin.String?
    @Json(name = "volume_width")
    val volumeWidth: kotlin.Float?
    @Json(name = "octoprint_controller")
    val octoprintController: kotlin.Int?
}

