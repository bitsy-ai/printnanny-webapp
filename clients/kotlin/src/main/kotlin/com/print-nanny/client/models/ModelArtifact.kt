/**
 * print-nanny-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
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

import com.print-nanny.client.models.ArtifactTypesEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param id 
 * @param createdDt 
 * @param version 
 * @param labels 
 * @param artifacts 
 * @param artifactTypes 
 * @param metadata 
 * @param url 
 */

data class ModelArtifact (

    @Json(name = "id")
    val id: kotlin.Int? = null,

    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,

    @Json(name = "version")
    val version: kotlin.String? = null,

    @Json(name = "labels")
    val labels: java.net.URI? = null,

    @Json(name = "artifacts")
    val artifacts: java.net.URI? = null,

    @Json(name = "artifact_types")
    val artifactTypes: kotlin.collections.List<ArtifactTypesEnum>? = null,

    @Json(name = "metadata")
    val metadata: kotlin.collections.Map<kotlin.String, kotlin.Any>? = null,

    @Json(name = "url")
    val url: java.net.URI? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

