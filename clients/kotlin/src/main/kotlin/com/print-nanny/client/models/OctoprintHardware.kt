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
 * 
 * @param cores 
 * @param freq 
 * @param ram 
 * @param piModel 
 * @param throttleState 
 * @param octopiVersion 
 */

data class OctoprintHardware (
    @Json(name = "cores")
    val cores: kotlin.Int,
    @Json(name = "freq")
    val freq: kotlin.Float,
    @Json(name = "ram")
    val ram: kotlin.Int,
    @Json(name = "pi_model")
    val piModel: kotlin.String,
    @Json(name = "throttle_state")
    val throttleState: kotlin.String,
    @Json(name = "octopi_version")
    val octopiVersion: kotlin.String
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

