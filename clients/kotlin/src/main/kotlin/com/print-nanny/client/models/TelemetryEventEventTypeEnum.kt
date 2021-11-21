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
 * Values: pluginOctoprintNannyMonitoringStart,pluginOctoprintNannyMonitoringStop,pluginOctoprintNannyMonitoringReset,pluginOctoprintNannyDeviceRegisterStart,pluginOctoprintNannyDeviceRegisterDone,pluginOctoprintNannyDeviceRegisterFailed,pluginOctoprintNannyDeviceReset,pluginOctoprintNannyPrinterProfileSyncStart,pluginOctoprintNannyPrinterProfileSyncDone,pluginOctoprintNannyPrinterProfileSyncFailed,pluginOctoprintNannyConnectTestRestApi,pluginOctoprintNannyConnectTestRestApiFailed,pluginOctoprintNannyConnectTestRestApiSuccess,pluginOctoprintNannyConnectTestMqttPing,pluginOctoprintNannyConnectTestMqttPingFailed,pluginOctoprintNannyConnectTestMqttPingSuccess,pluginOctoprintNannyConnectTestMqttPong,pluginOctoprintNannyConnectTestMqttPongFailed,pluginOctoprintNannyConnectTestMqttPongSuccess,connectTestNoop,clientAuthed,clientClosed,clientDeauthed,clientOpened,settingsUpdated,userLoggedIn,userLoggedOut,fileAdded,fileRemoved,folderAdded,folderRemoved,transferDone,transferFailed,transferStarted,updatedFiles,upload,captureDone,captureFailed,captureStart,movieDone,movieFailed,movieRendering,postRollEnd,postRollStart,slicingCancelled,slicingDone,slicingFailed,slicingProfileAdded,slicingProfileDeleted,slicingProfileModified,slicingStarted,connected,disconnected,printerReset,firmwareData,printerProfileAdded,printerProfileDeleted,printerProfileModified,printProgress,pluginPiSupportThrottleState,shutdown,startup,remoteCommandReceived,remoteCommandFailed,remoteCommandSuccess,printCancelled,printCancelling,printDone,printFailed,printPaused,printResumed,printStarted,printerStateChanged
 */

enum class TelemetryEventEventTypeEnum(val value: kotlin.String) {

    @Json(name = "plugin_octoprint_nanny_monitoring_start")
    pluginOctoprintNannyMonitoringStart("plugin_octoprint_nanny_monitoring_start"),

    @Json(name = "plugin_octoprint_nanny_monitoring_stop")
    pluginOctoprintNannyMonitoringStop("plugin_octoprint_nanny_monitoring_stop"),

    @Json(name = "plugin_octoprint_nanny_monitoring_reset")
    pluginOctoprintNannyMonitoringReset("plugin_octoprint_nanny_monitoring_reset"),

    @Json(name = "plugin_octoprint_nanny_device_register_start")
    pluginOctoprintNannyDeviceRegisterStart("plugin_octoprint_nanny_device_register_start"),

    @Json(name = "plugin_octoprint_nanny_device_register_done")
    pluginOctoprintNannyDeviceRegisterDone("plugin_octoprint_nanny_device_register_done"),

    @Json(name = "plugin_octoprint_nanny_device_register_failed")
    pluginOctoprintNannyDeviceRegisterFailed("plugin_octoprint_nanny_device_register_failed"),

    @Json(name = "plugin_octoprint_nanny_device_reset")
    pluginOctoprintNannyDeviceReset("plugin_octoprint_nanny_device_reset"),

    @Json(name = "plugin_octoprint_nanny_printer_profile_sync_start")
    pluginOctoprintNannyPrinterProfileSyncStart("plugin_octoprint_nanny_printer_profile_sync_start"),

    @Json(name = "plugin_octoprint_nanny_printer_profile_sync_done")
    pluginOctoprintNannyPrinterProfileSyncDone("plugin_octoprint_nanny_printer_profile_sync_done"),

    @Json(name = "plugin_octoprint_nanny_printer_profile_sync_failed")
    pluginOctoprintNannyPrinterProfileSyncFailed("plugin_octoprint_nanny_printer_profile_sync_failed"),

    @Json(name = "plugin_octoprint_nanny_connect_test_rest_api")
    pluginOctoprintNannyConnectTestRestApi("plugin_octoprint_nanny_connect_test_rest_api"),

    @Json(name = "plugin_octoprint_nanny_connect_test_rest_api_failed")
    pluginOctoprintNannyConnectTestRestApiFailed("plugin_octoprint_nanny_connect_test_rest_api_failed"),

    @Json(name = "plugin_octoprint_nanny_connect_test_rest_api_success")
    pluginOctoprintNannyConnectTestRestApiSuccess("plugin_octoprint_nanny_connect_test_rest_api_success"),

    @Json(name = "plugin_octoprint_nanny_connect_test_mqtt_ping")
    pluginOctoprintNannyConnectTestMqttPing("plugin_octoprint_nanny_connect_test_mqtt_ping"),

    @Json(name = "plugin_octoprint_nanny_connect_test_mqtt_ping_failed")
    pluginOctoprintNannyConnectTestMqttPingFailed("plugin_octoprint_nanny_connect_test_mqtt_ping_failed"),

    @Json(name = "plugin_octoprint_nanny_connect_test_mqtt_ping_success")
    pluginOctoprintNannyConnectTestMqttPingSuccess("plugin_octoprint_nanny_connect_test_mqtt_ping_success"),

    @Json(name = "plugin_octoprint_nanny_connect_test_mqtt_pong")
    pluginOctoprintNannyConnectTestMqttPong("plugin_octoprint_nanny_connect_test_mqtt_pong"),

    @Json(name = "plugin_octoprint_nanny_connect_test_mqtt_pong_failed")
    pluginOctoprintNannyConnectTestMqttPongFailed("plugin_octoprint_nanny_connect_test_mqtt_pong_failed"),

    @Json(name = "plugin_octoprint_nanny_connect_test_mqtt_pong_success")
    pluginOctoprintNannyConnectTestMqttPongSuccess("plugin_octoprint_nanny_connect_test_mqtt_pong_success"),

    @Json(name = "connect_test_noop")
    connectTestNoop("connect_test_noop"),

    @Json(name = "ClientAuthed")
    clientAuthed("ClientAuthed"),

    @Json(name = "ClientClosed")
    clientClosed("ClientClosed"),

    @Json(name = "ClientDeauthed")
    clientDeauthed("ClientDeauthed"),

    @Json(name = "ClientOpened")
    clientOpened("ClientOpened"),

    @Json(name = "SettingsUpdated")
    settingsUpdated("SettingsUpdated"),

    @Json(name = "UserLoggedIn")
    userLoggedIn("UserLoggedIn"),

    @Json(name = "UserLoggedOut")
    userLoggedOut("UserLoggedOut"),

    @Json(name = "FileAdded")
    fileAdded("FileAdded"),

    @Json(name = "FileRemoved")
    fileRemoved("FileRemoved"),

    @Json(name = "FolderAdded")
    folderAdded("FolderAdded"),

    @Json(name = "FolderRemoved")
    folderRemoved("FolderRemoved"),

    @Json(name = "TransferDone")
    transferDone("TransferDone"),

    @Json(name = "TransferFailed")
    transferFailed("TransferFailed"),

    @Json(name = "TransferStarted")
    transferStarted("TransferStarted"),

    @Json(name = "UpdatedFiles")
    updatedFiles("UpdatedFiles"),

    @Json(name = "Upload")
    upload("Upload"),

    @Json(name = "CaptureDone")
    captureDone("CaptureDone"),

    @Json(name = "CaptureFailed")
    captureFailed("CaptureFailed"),

    @Json(name = "CaptureStart")
    captureStart("CaptureStart"),

    @Json(name = "MovieDone")
    movieDone("MovieDone"),

    @Json(name = "MovieFailed")
    movieFailed("MovieFailed"),

    @Json(name = "MovieRendering")
    movieRendering("MovieRendering"),

    @Json(name = "PostRollEnd")
    postRollEnd("PostRollEnd"),

    @Json(name = "PostRollStart")
    postRollStart("PostRollStart"),

    @Json(name = "SlicingCancelled")
    slicingCancelled("SlicingCancelled"),

    @Json(name = "SlicingDone")
    slicingDone("SlicingDone"),

    @Json(name = "SlicingFailed")
    slicingFailed("SlicingFailed"),

    @Json(name = "SlicingProfileAdded")
    slicingProfileAdded("SlicingProfileAdded"),

    @Json(name = "SlicingProfileDeleted")
    slicingProfileDeleted("SlicingProfileDeleted"),

    @Json(name = "SlicingProfileModified")
    slicingProfileModified("SlicingProfileModified"),

    @Json(name = "SlicingStarted")
    slicingStarted("SlicingStarted"),

    @Json(name = "Connected")
    connected("Connected"),

    @Json(name = "Disconnected")
    disconnected("Disconnected"),

    @Json(name = "PrinterReset")
    printerReset("PrinterReset"),

    @Json(name = "FirmwareData")
    firmwareData("FirmwareData"),

    @Json(name = "PrinterProfileAdded")
    printerProfileAdded("PrinterProfileAdded"),

    @Json(name = "PrinterProfileDeleted")
    printerProfileDeleted("PrinterProfileDeleted"),

    @Json(name = "PrinterProfileModified")
    printerProfileModified("PrinterProfileModified"),

    @Json(name = "PrintProgress")
    printProgress("PrintProgress"),

    @Json(name = "plugin_pi_support_throttle_state")
    pluginPiSupportThrottleState("plugin_pi_support_throttle_state"),

    @Json(name = "Shutdown")
    shutdown("Shutdown"),

    @Json(name = "Startup")
    startup("Startup"),

    @Json(name = "remote_command_received")
    remoteCommandReceived("remote_command_received"),

    @Json(name = "remote_command_failed")
    remoteCommandFailed("remote_command_failed"),

    @Json(name = "remote_command_success")
    remoteCommandSuccess("remote_command_success"),

    @Json(name = "PrintCancelled")
    printCancelled("PrintCancelled"),

    @Json(name = "PrintCancelling")
    printCancelling("PrintCancelling"),

    @Json(name = "PrintDone")
    printDone("PrintDone"),

    @Json(name = "PrintFailed")
    printFailed("PrintFailed"),

    @Json(name = "PrintPaused")
    printPaused("PrintPaused"),

    @Json(name = "PrintResumed")
    printResumed("PrintResumed"),

    @Json(name = "PrintStarted")
    printStarted("PrintStarted"),

    @Json(name = "PrinterStateChanged")
    printerStateChanged("PrinterStateChanged");

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
        fun encode(data: Any?): kotlin.String? = if (data is TelemetryEventEventTypeEnum) "$data" else null

        /**
         * Returns a valid [TelemetryEventEventTypeEnum] for [data], null otherwise.
         */
        fun decode(data: Any?): TelemetryEventEventTypeEnum? = data?.let {
          val normalizedData = "$it".lowercase()
          values().firstOrNull { value ->
            it == value || normalizedData == "$value".lowercase()
          }
        }
    }
}

