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

import com.print-nanny.client.models.Camera
import com.print-nanny.client.models.CloudiotDevice
import com.print-nanny.client.models.License
import com.print-nanny.client.models.PrinterController
import com.print-nanny.client.models.Release
import com.print-nanny.client.models.ReleaseChannelEnum
import com.print-nanny.client.models.User

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param id 
 * @param cloudiotDevice 
 * @param cameras 
 * @param dashboardUrl 
 * @param bootstrapRelease 
 * @param printerControllers 
 * @param releaseChannel 
 * @param user 
 * @param activeLicense 
 * @param deleted 
 * @param createdDt 
 * @param updatedDt 
 * @param hostname Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)
 */

data class Device (

    @Json(name = "id")
    val id: kotlin.Int? = null,

    @Json(name = "cloudiot_device")
    val cloudiotDevice: CloudiotDevice? = null,

    @Json(name = "cameras")
    val cameras: kotlin.collections.List<Camera>? = null,

    @Json(name = "dashboard_url")
    val dashboardUrl: kotlin.String? = null,

    @Json(name = "bootstrap_release")
    val bootstrapRelease: Release? = null,

    @Json(name = "printer_controllers")
    val printerControllers: kotlin.collections.List<PrinterController>? = null,

    @Json(name = "release_channel")
    val releaseChannel: ReleaseChannelEnum? = null,

    @Json(name = "user")
    val user: User? = null,

    @Json(name = "active_license")
    val activeLicense: License? = null,

    @Json(name = "deleted")
    val deleted: java.time.OffsetDateTime? = null,

    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,

    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime? = null,

    /* Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension) */
    @Json(name = "hostname")
    val hostname: kotlin.String? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

