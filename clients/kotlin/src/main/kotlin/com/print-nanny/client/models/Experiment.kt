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

import com.print-nanny.client.models.Nested

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param id 
 * @param createdDt 
 * @param name 
 * @param hypothesis 
 * @param control 
 * @param treatments 
 * @param active 
 * @param notionUrl 
 */

data class Experiment (

    @Json(name = "id")
    val id: kotlin.Int,

    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime,

    @Json(name = "name")
    val name: kotlin.String,

    @Json(name = "hypothesis")
    val hypothesis: kotlin.String,

    @Json(name = "control")
    val control: Nested?,

    @Json(name = "treatments")
    val treatments: kotlin.collections.List<Nested>,

    @Json(name = "active")
    val active: kotlin.Boolean? = null,

    @Json(name = "notion_url")
    val notionUrl: kotlin.String? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

