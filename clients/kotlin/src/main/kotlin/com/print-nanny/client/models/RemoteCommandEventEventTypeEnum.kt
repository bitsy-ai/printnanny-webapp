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

/**
 * 
 *
 * Values: received,failed,success
 */

enum class RemoteCommandEventEventTypeEnum(val value: kotlin.String) {

    @Json(name = "remote_command_received")
    received("remote_command_received"),

    @Json(name = "remote_command_failed")
    failed("remote_command_failed"),

    @Json(name = "remote_command_success")
    success("remote_command_success");

    /**
     * Override toString() to avoid using the enum variable name as the value, and instead use
     * the actual value defined in the API spec file.
     *
     * This solves a problem when the variable name and its value are different, and ensures that
     * the client sends the correct enum values to the server always.
     */
    override fun toString(): String = value

    companion object {
        /**
         * Converts the provided [data] to a [String] on success, null otherwise.
         */
        fun encode(data: Any?): kotlin.String? = if (data is RemoteCommandEventEventTypeEnum) "$data" else null

        /**
         * Returns a valid [RemoteCommandEventEventTypeEnum] for [data], null otherwise.
         */
        fun decode(data: Any?): RemoteCommandEventEventTypeEnum? = data?.let {
          val normalizedData = "$it".lowercase()
          values().firstOrNull { value ->
            it == value || normalizedData == "$value".lowercase()
          }
        }
    }
}

