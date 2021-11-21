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

import com.print-nanny.client.models.AnsibleExtraVars
import com.print-nanny.client.models.ReleaseChannelEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param id 
 * @param ansibleExtraVars 
 * @param createdDt 
 * @param releaseChannel 
 */

data class Release (

    @Json(name = "id")
    val id: kotlin.Int,

    @Json(name = "ansible_extra_vars")
    val ansibleExtraVars: AnsibleExtraVars,

    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime,

    @Json(name = "release_channel")
    val releaseChannel: ReleaseChannelEnum? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

