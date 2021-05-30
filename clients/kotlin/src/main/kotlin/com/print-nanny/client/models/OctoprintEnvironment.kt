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

import com.print-nanny.client.models.OctoprintHardware
import com.print-nanny.client.models.OctoprintPlatform
import com.print-nanny.client.models.OctoprintPython

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param os 
 * @param python 
 * @param hardware 
 */

data class OctoprintEnvironment (
    @Json(name = "os")
    val os: OctoprintPlatform,
    @Json(name = "python")
    val python: OctoprintPython,
    @Json(name = "hardware")
    val hardware: OctoprintHardware
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

