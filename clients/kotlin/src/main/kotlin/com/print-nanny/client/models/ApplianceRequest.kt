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

import com.print-nanny.client.models.AnsibleFactsRequest
import com.print-nanny.client.models.AppliancePKIRequest
import com.print-nanny.client.models.CameraRequest
import com.print-nanny.client.models.PrinterControllerRequest

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param pki 
 * @param ansibleFacts 
 * @param cameras 
 * @param printerControllers 
 * @param hostname 
 * @param user 
 */

data class ApplianceRequest (

    @Json(name = "pki")
    val pki: AppliancePKIRequest,

    @Json(name = "ansible_facts")
    val ansibleFacts: AnsibleFactsRequest,

    @Json(name = "cameras")
    val cameras: CameraRequest,

    @Json(name = "printer_controllers")
    val printerControllers: PrinterControllerRequest,

    @Json(name = "hostname")
    val hostname: kotlin.String,

    @Json(name = "user")
    val user: kotlin.Int

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

