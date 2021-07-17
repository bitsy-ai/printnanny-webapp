/**
* 
* No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
*
* The version of the OpenAPI document: 0.0.0
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
package com.print-nanny.client.models


import com.squareup.moshi.Json
import java.io.Serializable

/**
 * Please do not include any personally-identifying info or sensitive info in partner serializers
 * @param name 
 * @param model 
 * @param platform 
 * @param octoprintVersion 
 * @param printNannyPluginVersion 
 * @param printNannyClientVersion 
 * @param verified 
 */

data class Partner3DGeeksMetadata (
    @Json(name = "name")
    val name: kotlin.String,
    @Json(name = "model")
    val model: kotlin.String,
    @Json(name = "platform")
    val platform: kotlin.String,
    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String,
    @Json(name = "print_nanny_plugin_version")
    val printNannyPluginVersion: kotlin.String,
    @Json(name = "print_nanny_client_version")
    val printNannyClientVersion: kotlin.String,
    @Json(name = "verified")
    val verified: kotlin.String
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

