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

import com.print-nanny.client.models.TelemetryEventPolymorphic

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param count 
 * @param next 
 * @param previous 
 * @param results 
 */

data class PaginatedTelemetryEventPolymorphicList (

    @Json(name = "count")
    val count: kotlin.Int? = null,

    @Json(name = "next")
    val next: java.net.URI? = null,

    @Json(name = "previous")
    val previous: java.net.URI? = null,

    @Json(name = "results")
    val results: kotlin.collections.List<TelemetryEventPolymorphic>? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

