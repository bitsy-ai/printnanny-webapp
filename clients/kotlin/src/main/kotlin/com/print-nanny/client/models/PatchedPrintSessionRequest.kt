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

import com.print-nanny.client.models.PrintJobEventType

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param createdDt 
 * @param octoprintDevice 
 * @param active 
 * @param session 
 * @param filepos 
 * @param printProgress 
 * @param timeElapsed 
 * @param timeRemaining 
 * @param printerProfile 
 * @param gcodeFile 
 * @param gcodeFilename 
 * @param octoprintJob 
 * @param printJobStatus 
 */

data class PatchedPrintSessionRequest (

    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,

    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int? = null,

    @Json(name = "active")
    val active: kotlin.Boolean? = null,

    @Json(name = "session")
    val session: kotlin.String? = null,

    @Json(name = "filepos")
    val filepos: kotlin.Int? = null,

    @Json(name = "print_progress")
    val printProgress: kotlin.Int? = null,

    @Json(name = "time_elapsed")
    val timeElapsed: kotlin.Int? = null,

    @Json(name = "time_remaining")
    val timeRemaining: kotlin.Int? = null,

    @Json(name = "printer_profile")
    val printerProfile: kotlin.Int? = null,

    @Json(name = "gcode_file")
    val gcodeFile: kotlin.Int? = null,

    @Json(name = "gcode_filename")
    val gcodeFilename: kotlin.String? = null,

    @Json(name = "octoprint_job")
    val octoprintJob: kotlin.collections.Map<kotlin.String, kotlin.Any>? = null,

    @Json(name = "print_job_status")
    val printJobStatus: PrintJobEventType? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

