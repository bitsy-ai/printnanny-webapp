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

import com.print-nanny.client.models.AnyType
import com.print-nanny.client.models.OctoprintJob
import com.print-nanny.client.models.OctoprintPrinterState
import com.print-nanny.client.models.OctoprintProgress

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param job 
 * @param state 
 * @param user 
 * @param currentZ 
 * @param progress 
 * @param resends 
 */

data class OctoprintPrinterData (
    @Json(name = "job")
    val job: OctoprintJob,
    @Json(name = "state")
    val state: OctoprintPrinterState,
    @Json(name = "user")
    val user: kotlin.String,
    @Json(name = "currentZ")
    val currentZ: kotlin.Float,
    @Json(name = "progress")
    val progress: OctoprintProgress,
    @Json(name = "resends")
    val resends: kotlin.collections.Map<kotlin.String, AnyType>
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

