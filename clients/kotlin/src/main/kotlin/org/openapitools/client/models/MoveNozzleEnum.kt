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
package org.openapitools.client.models


import com.squareup.moshi.Json

/**
* 
* Values: rECEIVED,fAILED,sUCCESS
*/

enum class MoveNozzleEnum(val value: kotlin.String){


    @Json(name = "RECEIVED")
    rECEIVED("RECEIVED"),


    @Json(name = "FAILED")
    fAILED("FAILED"),


    @Json(name = "SUCCESS")
    sUCCESS("SUCCESS");



    /**
    This override toString avoids using the enum var name and uses the actual api value instead.
    In cases the var name and value are different, the client would send incorrect enums to the server.
    **/
    override fun toString(): String {
        return value
    }

}

