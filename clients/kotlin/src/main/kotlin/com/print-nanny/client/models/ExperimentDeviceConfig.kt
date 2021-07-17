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

import com.print-nanny.client.models.Nested

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param id 
 * @param createdDt 
 * @param experiment 
 * @param artifact 
 */

data class ExperimentDeviceConfig (
    @Json(name = "id")
    val id: kotlin.Int,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime,
    @Json(name = "experiment")
    val experiment: Nested,
    @Json(name = "artifact")
    val artifact: Nested
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

