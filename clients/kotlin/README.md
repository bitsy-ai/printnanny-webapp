# com.print-nanny.client - Kotlin client library for 

## Requires

* Kotlin 1.4.30
* Gradle 6.8.3

## Build

First, create the gradle wrapper script:

```
gradle wrapper
```

Then, run:

```
./gradlew check assemble
```

This runs all tests and packages the library.

## Features/Implementation Notes

* Supports JSON inputs/outputs, File inputs, and Form inputs.
* Supports collection formats for query parameters: csv, tsv, ssv, pipes.
* Some Kotlin and Java types are fully qualified to avoid conflicts with types defined in OpenAPI definitions.
* Implementation of ApiClient is intended to reduce method counts, specifically to benefit Android targets.

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertsApi* | [**alertsList**](docs/AlertsApi.md#alertslist) | **GET** /api/alerts/ | 
*AlertsApi* | [**alertsPartialUpdate**](docs/AlertsApi.md#alertspartialupdate) | **PATCH** /api/alerts/{id}/ | 
*AlertsApi* | [**alertsRecent**](docs/AlertsApi.md#alertsrecent) | **GET** /api/alerts/recent/ | 
*AlertsApi* | [**alertsRetrieve**](docs/AlertsApi.md#alertsretrieve) | **GET** /api/alerts/{id}/ | 
*AlertsApi* | [**alertsSeen**](docs/AlertsApi.md#alertsseen) | **PATCH** /api/alerts/seen/ | 
*AlertsApi* | [**alertsUnread**](docs/AlertsApi.md#alertsunread) | **GET** /api/alerts/unread/ | 
*AlertsApi* | [**alertsUpdate**](docs/AlertsApi.md#alertsupdate) | **PUT** /api/alerts/{id}/ | 
*AuthTokenApi* | [**authTokenCreate**](docs/AuthTokenApi.md#authtokencreate) | **POST** /api/auth-token/ | 
*MlOpsApi* | [**deviceCalibrationUpdateOrCreate**](docs/MlOpsApi.md#devicecalibrationupdateorcreate) | **POST** /api/device-calibrations/update-or-create/ | 
*MlOpsApi* | [**deviceCalibrationsList**](docs/MlOpsApi.md#devicecalibrationslist) | **GET** /api/device-calibrations/ | 
*MlOpsApi* | [**deviceCalibrationsPartialUpdate**](docs/MlOpsApi.md#devicecalibrationspartialupdate) | **PATCH** /api/device-calibrations/{id}/ | 
*MlOpsApi* | [**deviceCalibrationsRetrieve**](docs/MlOpsApi.md#devicecalibrationsretrieve) | **GET** /api/device-calibrations/{id}/ | 
*MlOpsApi* | [**deviceCalibrationsUpdate**](docs/MlOpsApi.md#devicecalibrationsupdate) | **PUT** /api/device-calibrations/{id}/ | 
*MlOpsApi* | [**experimentDeviceConfigsList**](docs/MlOpsApi.md#experimentdeviceconfigslist) | **GET** /api/experiment-device-configs/ | 
*MlOpsApi* | [**experimentDeviceConfigsRetrieve**](docs/MlOpsApi.md#experimentdeviceconfigsretrieve) | **GET** /api/experiment-device-configs/{id}/ | 
*MlOpsApi* | [**experimentsList**](docs/MlOpsApi.md#experimentslist) | **GET** /api/experiments/ | 
*MlOpsApi* | [**experimentsRetrieve**](docs/MlOpsApi.md#experimentsretrieve) | **GET** /api/experiments/{id}/ | 
*MlOpsApi* | [**modelArtifactsList**](docs/MlOpsApi.md#modelartifactslist) | **GET** /api/model-artifacts/ | 
*MlOpsApi* | [**modelArtifactsRetrieve**](docs/MlOpsApi.md#modelartifactsretrieve) | **GET** /api/model-artifacts/{id}/ | 
*PartnersGeeks3Api* | [**alertsList2**](docs/PartnersGeeks3Api.md#alertslist2) | **GET** /api/partners/3d-geeks/{id}/alerts/ | 
*PartnersGeeks3dApi* | [**metadataRetrieve**](docs/PartnersGeeks3dApi.md#metadataretrieve) | **GET** /api/partners/3d-geeks/{id}/ | 
*RemoteControlApi* | [**commandsList**](docs/RemoteControlApi.md#commandslist) | **GET** /api/commands/ | 
*RemoteControlApi* | [**commandsPartialUpdate**](docs/RemoteControlApi.md#commandspartialupdate) | **PATCH** /api/commands/{id}/ | 
*RemoteControlApi* | [**commandsRetrieve**](docs/RemoteControlApi.md#commandsretrieve) | **GET** /api/commands/{id}/ | 
*RemoteControlApi* | [**commandsUpdate**](docs/RemoteControlApi.md#commandsupdate) | **PUT** /api/commands/{id}/ | 
*RemoteControlApi* | [**gcodeFilesCreate**](docs/RemoteControlApi.md#gcodefilescreate) | **POST** /api/gcode-files/ | 
*RemoteControlApi* | [**gcodeFilesList**](docs/RemoteControlApi.md#gcodefileslist) | **GET** /api/gcode-files/ | 
*RemoteControlApi* | [**gcodeFilesPartialUpdate**](docs/RemoteControlApi.md#gcodefilespartialupdate) | **PATCH** /api/gcode-files/{id}/ | 
*RemoteControlApi* | [**gcodeFilesRetrieve**](docs/RemoteControlApi.md#gcodefilesretrieve) | **GET** /api/gcode-files/{id}/ | 
*RemoteControlApi* | [**gcodeFilesUpdate**](docs/RemoteControlApi.md#gcodefilesupdate) | **PUT** /api/gcode-files/{id}/ | 
*RemoteControlApi* | [**gcodeFilesUpdateOrCreate**](docs/RemoteControlApi.md#gcodefilesupdateorcreate) | **POST** /api/gcode-files/update-or-create/ | 
*RemoteControlApi* | [**octoprintDevicesCreate**](docs/RemoteControlApi.md#octoprintdevicescreate) | **POST** /api/octoprint-devices/ | 
*RemoteControlApi* | [**octoprintDevicesList**](docs/RemoteControlApi.md#octoprintdeviceslist) | **GET** /api/octoprint-devices/ | 
*RemoteControlApi* | [**octoprintDevicesPartialUpdate**](docs/RemoteControlApi.md#octoprintdevicespartialupdate) | **PATCH** /api/octoprint-devices/{id}/ | 
*RemoteControlApi* | [**octoprintDevicesRetrieve**](docs/RemoteControlApi.md#octoprintdevicesretrieve) | **GET** /api/octoprint-devices/{id}/ | 
*RemoteControlApi* | [**octoprintDevicesUpdate**](docs/RemoteControlApi.md#octoprintdevicesupdate) | **PUT** /api/octoprint-devices/{id}/ | 
*RemoteControlApi* | [**octoprintDevicesUpdateOrCreate**](docs/RemoteControlApi.md#octoprintdevicesupdateorcreate) | **POST** /api/octoprint-devices/update-or-create/ | 
*RemoteControlApi* | [**printSessionPartialUpdate**](docs/RemoteControlApi.md#printsessionpartialupdate) | **PATCH** /api/print-sessions/{session}/ | 
*RemoteControlApi* | [**printSessionUpdate**](docs/RemoteControlApi.md#printsessionupdate) | **PUT** /api/print-sessions/{session}/ | 
*RemoteControlApi* | [**printSessionsCreate**](docs/RemoteControlApi.md#printsessionscreate) | **POST** /api/print-sessions/ | 
*RemoteControlApi* | [**printSessionsList**](docs/RemoteControlApi.md#printsessionslist) | **GET** /api/print-sessions/ | 
*RemoteControlApi* | [**printSessionsRetrieve**](docs/RemoteControlApi.md#printsessionsretrieve) | **GET** /api/print-sessions/{session}/ | 
*RemoteControlApi* | [**printerProfilesCreate**](docs/RemoteControlApi.md#printerprofilescreate) | **POST** /api/printer-profiles/ | 
*RemoteControlApi* | [**printerProfilesList**](docs/RemoteControlApi.md#printerprofileslist) | **GET** /api/printer-profiles/ | 
*RemoteControlApi* | [**printerProfilesPartialUpdate**](docs/RemoteControlApi.md#printerprofilespartialupdate) | **PATCH** /api/printer-profiles/{id}/ | 
*RemoteControlApi* | [**printerProfilesRetrieve**](docs/RemoteControlApi.md#printerprofilesretrieve) | **GET** /api/printer-profiles/{id}/ | 
*RemoteControlApi* | [**printerProfilesUpdate**](docs/RemoteControlApi.md#printerprofilesupdate) | **PUT** /api/printer-profiles/{id}/ | 
*RemoteControlApi* | [**printerProfilesUpdateOrCreate**](docs/RemoteControlApi.md#printerprofilesupdateorcreate) | **POST** /api/printer-profiles/update-or-create/ | 
*SchemaApi* | [**schemaRetrieve**](docs/SchemaApi.md#schemaretrieve) | **GET** /api/schema/ | 
*TelemetryApi* | [**telemetryList**](docs/TelemetryApi.md#telemetrylist) | **GET** /api/telemetry/ | 
*TelemetryApi* | [**telemetryOctoprintEventsCreate**](docs/TelemetryApi.md#telemetryoctoprinteventscreate) | **POST** /api/telemetry/octoprint-events/ | 
*TelemetryApi* | [**telemetryOctoprintEventsList**](docs/TelemetryApi.md#telemetryoctoprinteventslist) | **GET** /api/telemetry/octoprint-events/ | 
*TelemetryApi* | [**telemetryOctoprintEventsRetrieve**](docs/TelemetryApi.md#telemetryoctoprinteventsretrieve) | **GET** /api/telemetry/octoprint-events/{id}/ | 
*TelemetryApi* | [**telemetryPrintNannyPluginEventsList**](docs/TelemetryApi.md#telemetryprintnannyplugineventslist) | **GET** /api/telemetry/print-nanny-plugin-events/ | 
*TelemetryApi* | [**telemetryPrintNannyPluginEventsRetrieve**](docs/TelemetryApi.md#telemetryprintnannyplugineventsretrieve) | **GET** /api/telemetry/print-nanny-plugin-events/{id}/ | 
*TelemetryApi* | [**telemetryPrintStatusEventsList**](docs/TelemetryApi.md#telemetryprintstatuseventslist) | **GET** /api/telemetry/print-status-events/ | 
*TelemetryApi* | [**telemetryPrintStatusEventsRetrieve**](docs/TelemetryApi.md#telemetryprintstatuseventsretrieve) | **GET** /api/telemetry/print-status-events/{id}/ | 
*TelemetryApi* | [**telemetryRetrieve**](docs/TelemetryApi.md#telemetryretrieve) | **GET** /api/telemetry/{id}/ | 
*UsersApi* | [**usersList**](docs/UsersApi.md#userslist) | **GET** /api/users/ | 
*UsersApi* | [**usersMeRetrieve**](docs/UsersApi.md#usersmeretrieve) | **GET** /api/users/me/ | 
*UsersApi* | [**usersPartialUpdate**](docs/UsersApi.md#userspartialupdate) | **PATCH** /api/users/{id}/ | 
*UsersApi* | [**usersRetrieve**](docs/UsersApi.md#usersretrieve) | **GET** /api/users/{id}/ | 
*UsersApi* | [**usersUpdate**](docs/UsersApi.md#usersupdate) | **PUT** /api/users/{id}/ | 


<a name="documentation-for-models"></a>
## Documentation for Models

 - [com.print-nanny.client.models.Alert](docs/Alert.md)
 - [com.print-nanny.client.models.AlertBulkResponse](docs/AlertBulkResponse.md)
 - [com.print-nanny.client.models.AlertEventTypeEnum](docs/AlertEventTypeEnum.md)
 - [com.print-nanny.client.models.AlertMethodEnum](docs/AlertMethodEnum.md)
 - [com.print-nanny.client.models.AlertRequest](docs/AlertRequest.md)
 - [com.print-nanny.client.models.ArtifactTypesEnum](docs/ArtifactTypesEnum.md)
 - [com.print-nanny.client.models.AuthToken](docs/AuthToken.md)
 - [com.print-nanny.client.models.AuthTokenRequest](docs/AuthTokenRequest.md)
 - [com.print-nanny.client.models.CommandEnum](docs/CommandEnum.md)
 - [com.print-nanny.client.models.DeviceCalibration](docs/DeviceCalibration.md)
 - [com.print-nanny.client.models.DeviceCalibrationRequest](docs/DeviceCalibrationRequest.md)
 - [com.print-nanny.client.models.EventSourceEnum](docs/EventSourceEnum.md)
 - [com.print-nanny.client.models.Experiment](docs/Experiment.md)
 - [com.print-nanny.client.models.ExperimentDeviceConfig](docs/ExperimentDeviceConfig.md)
 - [com.print-nanny.client.models.GcodeFile](docs/GcodeFile.md)
 - [com.print-nanny.client.models.ModelArtifact](docs/ModelArtifact.md)
 - [com.print-nanny.client.models.MonitoringModeEnum](docs/MonitoringModeEnum.md)
 - [com.print-nanny.client.models.Nested](docs/Nested.md)
 - [com.print-nanny.client.models.OctoPrintDevice](docs/OctoPrintDevice.md)
 - [com.print-nanny.client.models.OctoPrintDeviceKey](docs/OctoPrintDeviceKey.md)
 - [com.print-nanny.client.models.OctoPrintDeviceRequest](docs/OctoPrintDeviceRequest.md)
 - [com.print-nanny.client.models.OctoPrintEvent](docs/OctoPrintEvent.md)
 - [com.print-nanny.client.models.OctoPrintEventEventTypeEnum](docs/OctoPrintEventEventTypeEnum.md)
 - [com.print-nanny.client.models.OctoPrintEventRequest](docs/OctoPrintEventRequest.md)
 - [com.print-nanny.client.models.OctoprintEnvironment](docs/OctoprintEnvironment.md)
 - [com.print-nanny.client.models.OctoprintFile](docs/OctoprintFile.md)
 - [com.print-nanny.client.models.OctoprintHardware](docs/OctoprintHardware.md)
 - [com.print-nanny.client.models.OctoprintJob](docs/OctoprintJob.md)
 - [com.print-nanny.client.models.OctoprintPlatform](docs/OctoprintPlatform.md)
 - [com.print-nanny.client.models.OctoprintPython](docs/OctoprintPython.md)
 - [com.print-nanny.client.models.PaginatedAlertList](docs/PaginatedAlertList.md)
 - [com.print-nanny.client.models.PaginatedDeviceCalibrationList](docs/PaginatedDeviceCalibrationList.md)
 - [com.print-nanny.client.models.PaginatedExperimentDeviceConfigList](docs/PaginatedExperimentDeviceConfigList.md)
 - [com.print-nanny.client.models.PaginatedExperimentList](docs/PaginatedExperimentList.md)
 - [com.print-nanny.client.models.PaginatedGcodeFileList](docs/PaginatedGcodeFileList.md)
 - [com.print-nanny.client.models.PaginatedModelArtifactList](docs/PaginatedModelArtifactList.md)
 - [com.print-nanny.client.models.PaginatedOctoPrintDeviceList](docs/PaginatedOctoPrintDeviceList.md)
 - [com.print-nanny.client.models.PaginatedOctoPrintEventList](docs/PaginatedOctoPrintEventList.md)
 - [com.print-nanny.client.models.PaginatedPrintNannyPluginEventList](docs/PaginatedPrintNannyPluginEventList.md)
 - [com.print-nanny.client.models.PaginatedPrintSessionList](docs/PaginatedPrintSessionList.md)
 - [com.print-nanny.client.models.PaginatedPrintStatusEventList](docs/PaginatedPrintStatusEventList.md)
 - [com.print-nanny.client.models.PaginatedPrinterProfileList](docs/PaginatedPrinterProfileList.md)
 - [com.print-nanny.client.models.PaginatedRemoteControlCommandList](docs/PaginatedRemoteControlCommandList.md)
 - [com.print-nanny.client.models.PaginatedTelemetryEventList](docs/PaginatedTelemetryEventList.md)
 - [com.print-nanny.client.models.PaginatedUserList](docs/PaginatedUserList.md)
 - [com.print-nanny.client.models.Partner3DGeeksAlert](docs/Partner3DGeeksAlert.md)
 - [com.print-nanny.client.models.Partner3DGeeksMetadata](docs/Partner3DGeeksMetadata.md)
 - [com.print-nanny.client.models.PatchedAlertBulkRequestRequest](docs/PatchedAlertBulkRequestRequest.md)
 - [com.print-nanny.client.models.PatchedAlertRequest](docs/PatchedAlertRequest.md)
 - [com.print-nanny.client.models.PatchedDeviceCalibrationRequest](docs/PatchedDeviceCalibrationRequest.md)
 - [com.print-nanny.client.models.PatchedOctoPrintDeviceRequest](docs/PatchedOctoPrintDeviceRequest.md)
 - [com.print-nanny.client.models.PatchedPrintSessionRequest](docs/PatchedPrintSessionRequest.md)
 - [com.print-nanny.client.models.PatchedPrinterProfileRequest](docs/PatchedPrinterProfileRequest.md)
 - [com.print-nanny.client.models.PatchedRemoteControlCommandRequest](docs/PatchedRemoteControlCommandRequest.md)
 - [com.print-nanny.client.models.PatchedUserRequest](docs/PatchedUserRequest.md)
 - [com.print-nanny.client.models.PrintNannyPluginEvent](docs/PrintNannyPluginEvent.md)
 - [com.print-nanny.client.models.PrintNannyPluginEventEventTypeEnum](docs/PrintNannyPluginEventEventTypeEnum.md)
 - [com.print-nanny.client.models.PrintSession](docs/PrintSession.md)
 - [com.print-nanny.client.models.PrintSessionRequest](docs/PrintSessionRequest.md)
 - [com.print-nanny.client.models.PrintStatusEvent](docs/PrintStatusEvent.md)
 - [com.print-nanny.client.models.PrintStatusEventEventTypeEnum](docs/PrintStatusEventEventTypeEnum.md)
 - [com.print-nanny.client.models.PrinterProfile](docs/PrinterProfile.md)
 - [com.print-nanny.client.models.PrinterProfileRequest](docs/PrinterProfileRequest.md)
 - [com.print-nanny.client.models.RemoteControlCommand](docs/RemoteControlCommand.md)
 - [com.print-nanny.client.models.RemoteControlCommandRequest](docs/RemoteControlCommandRequest.md)
 - [com.print-nanny.client.models.StatusEnum](docs/StatusEnum.md)
 - [com.print-nanny.client.models.TelemetryEvent](docs/TelemetryEvent.md)
 - [com.print-nanny.client.models.TelemetryEventEventTypeEnum](docs/TelemetryEventEventTypeEnum.md)
 - [com.print-nanny.client.models.User](docs/User.md)
 - [com.print-nanny.client.models.UserRequest](docs/UserRequest.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="cookieAuth"></a>
### cookieAuth

- **Type**: API key
- **API key parameter name**: Session
- **Location**: 

<a name="tokenAuth"></a>
### tokenAuth

- **Type**: HTTP basic authentication

