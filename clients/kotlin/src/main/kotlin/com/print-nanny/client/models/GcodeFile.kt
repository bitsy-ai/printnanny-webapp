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
 * @param name 
 * @param file 
 * @param fileHash 
 * @param octoprintDevice 
 * @param id 
 * @param user 
 * @param url 
 */

data class GcodeFile (

    @Json(name = "name")
    val name: kotlin.String,

    @Json(name = "file")
    val file: java.net.URI,

    @Json(name = "file_hash")
    val fileHash: kotlin.String,

    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.String,

    @Json(name = "id")
    val id: kotlin.Int? = null,

    @Json(name = "user")
    val user: kotlin.Int? = null,

    @Json(name = "url")
    val url: java.net.URI? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

