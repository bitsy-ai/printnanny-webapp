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
 * @param operational 
 * @param printing 
 * @param cancelling 
 * @param pausing 
 * @param resuming 
 * @param finishing 
 * @param closedOrError 
 * @param error 
 * @param paused 
 * @param ready 
 * @param sdReady 
 */

data class OctoprintPrinterFlags (
    @Json(name = "operational")
    val operational: kotlin.Boolean,
    @Json(name = "printing")
    val printing: kotlin.Boolean,
    @Json(name = "cancelling")
    val cancelling: kotlin.Boolean,
    @Json(name = "pausing")
    val pausing: kotlin.Boolean,
    @Json(name = "resuming")
    val resuming: kotlin.Boolean,
    @Json(name = "finishing")
    val finishing: kotlin.Boolean,
    @Json(name = "closed_or_error")
    val closedOrError: kotlin.Boolean,
    @Json(name = "error")
    val error: kotlin.Boolean,
    @Json(name = "paused")
    val paused: kotlin.Boolean,
    @Json(name = "ready")
    val ready: kotlin.Boolean,
    @Json(name = "sd_ready")
    val sdReady: kotlin.Boolean
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

