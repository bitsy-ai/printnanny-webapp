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


import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param model 
 * @param throttleState 
 * @param octopiVersion 
 */

data class OctoprintPiSupport (

    @Json(name = "model")
    val model: kotlin.String,

    @Json(name = "throttle_state")
    val throttleState: kotlin.String,

    @Json(name = "octopi_version")
    val octopiVersion: kotlin.String? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

