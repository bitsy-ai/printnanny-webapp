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
 * @param email 
 * @param url 
 * @param id 
 */

data class User (
    @Json(name = "email")
    val email: kotlin.String,
    @Json(name = "url")
    val url: java.net.URI,
    @Json(name = "id")
    val id: kotlin.Int
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

