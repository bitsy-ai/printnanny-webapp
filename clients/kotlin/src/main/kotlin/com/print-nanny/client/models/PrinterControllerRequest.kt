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

import com.print-nanny.client.models.SoftwareEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param software 
 */

data class PrinterControllerRequest (

    @Json(name = "software")
    val software: SoftwareEnum

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

