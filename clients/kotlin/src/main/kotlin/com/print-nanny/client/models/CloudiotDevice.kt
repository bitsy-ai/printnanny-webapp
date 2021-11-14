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


import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 *
 * @param numId 
 * @param name 
 * @param id 
 * @param device 
 * @param desiredConfigTopic 
 * @param currentStateTopic 
 * @param gcpProjectId 
 * @param gcpRegion 
 * @param gcpCloudiotDeviceRegistry 
 * @param mqttBridgeHostname 
 * @param mqttBridgePort 
 * @param mqttClientId 
 * @param deleted 
 */

data class CloudiotDevice (

    @Json(name = "num_id")
    val numId: kotlin.Long,

    @Json(name = "name")
    val name: kotlin.String,

    @Json(name = "id")
    val id: kotlin.String,

    @Json(name = "device")
    val device: kotlin.Int,

    @Json(name = "desired_config_topic")
    val desiredConfigTopic: kotlin.String? = null,

    @Json(name = "current_state_topic")
    val currentStateTopic: kotlin.String? = null,

    @Json(name = "gcp_project_id")
    val gcpProjectId: kotlin.String? = null,

    @Json(name = "gcp_region")
    val gcpRegion: kotlin.String? = null,

    @Json(name = "gcp_cloudiot_device_registry")
    val gcpCloudiotDeviceRegistry: kotlin.String? = null,

    @Json(name = "mqtt_bridge_hostname")
    val mqttBridgeHostname: kotlin.String? = null,

    @Json(name = "mqtt_bridge_port")
    val mqttBridgePort: kotlin.Int? = null,

    @Json(name = "mqtt_client_id")
    val mqttClientId: kotlin.String? = null,

    @Json(name = "deleted")
    val deleted: java.time.OffsetDateTime? = null

) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

