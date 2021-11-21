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

import com.print-nanny.client.models.LicenseCredentials

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param id 
 * @param credentials 
 * @param deleted 
 * @param publicKey 
 * @param publicKeyChecksum 
 * @param fingerprint 
 * @param createdDt 
 * @param device 
 */

data class License (

    @Json(name = "id")
    val id: kotlin.Int,

    @Json(name = "credentials")
    val credentials: LicenseCredentials,

    @Json(name = "deleted")
    val deleted: java.time.OffsetDateTime,

    @Json(name = "public_key")
    val publicKey: kotlin.String,

    @Json(name = "public_key_checksum")
    val publicKeyChecksum: kotlin.String,

    @Json(name = "fingerprint")
    val fingerprint: kotlin.String,

    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime,

    @Json(name = "device")
    val device: kotlin.Int

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

