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
 * @param completion 
 * @param filepos 
 * @param printTime 
 * @param printTimeLeft 
 * @param printTimeOrigin 
 */

data class OctoprintProgressRequest (

    @Json(name = "completion")
    val completion: kotlin.Float?,

    @Json(name = "filepos")
    val filepos: kotlin.Int?,

    @Json(name = "printTime")
    val printTime: kotlin.Int?,

    @Json(name = "printTimeLeft")
    val printTimeLeft: kotlin.Int?,

    @Json(name = "printTimeOrigin")
    val printTimeOrigin: kotlin.String? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

