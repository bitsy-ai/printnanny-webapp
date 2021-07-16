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
*AlertsApi* | [**alertsRecent**](docs/AlertsApi.md#alertsrecent) | **GET** /api/alerts/recent/ | 
*AlertsApi* | [**alertsSeen**](docs/AlertsApi.md#alertsseen) | **PATCH** /api/alerts/seen/ | 
*AlertsApi* | [**alertsUnread**](docs/AlertsApi.md#alertsunread) | **GET** /api/alerts/unread/ | 
*ApiApi* | [**apiAlertsList**](docs/ApiApi.md#apialertslist) | **GET** /api/alerts/ | 
*ApiApi* | [**apiAlertsPartialUpdate**](docs/ApiApi.md#apialertspartialupdate) | **PATCH** /api/alerts/{id}/ | 
*ApiApi* | [**apiAlertsRetrieve**](docs/ApiApi.md#apialertsretrieve) | **GET** /api/alerts/{id}/ | 
*ApiApi* | [**apiAlertsUpdate**](docs/ApiApi.md#apialertsupdate) | **PUT** /api/alerts/{id}/ | 
*ApiApi* | [**apiAuthTokenCreate**](docs/ApiApi.md#apiauthtokencreate) | **POST** /api/auth-token/ | 
*ApiApi* | [**apiSchemaRetrieve**](docs/ApiApi.md#apischemaretrieve) | **GET** /api/schema/ | 
*AuthApi* | [**authEmailCreate**](docs/AuthApi.md#authemailcreate) | **POST** /auth/email/ | 
*AuthApi* | [**authMobileCreate**](docs/AuthApi.md#authmobilecreate) | **POST** /auth/mobile/ | 
*AuthApi* | [**authTokenCreate**](docs/AuthApi.md#authtokencreate) | **POST** /auth/token/ | 
*AuthApi* | [**authVerifyCreate**](docs/AuthApi.md#authverifycreate) | **POST** /auth/verify/ | 
*AuthApi* | [**authVerifyEmailCreate**](docs/AuthApi.md#authverifyemailcreate) | **POST** /auth/verify/email/ | 
*AuthApi* | [**authVerifyMobileCreate**](docs/AuthApi.md#authverifymobilecreate) | **POST** /auth/verify/mobile/ | 
*DevicesApi* | [**apiDevicesCreate**](docs/DevicesApi.md#apidevicescreate) | **POST** /api/devices/ | 
*DevicesApi* | [**apiDevicesList**](docs/DevicesApi.md#apideviceslist) | **GET** /api/devices/ | 
*DevicesApi* | [**apiDevicesRetrieve**](docs/DevicesApi.md#apidevicesretrieve) | **GET** /api/devices/{id}/ | 
*DevicesApi* | [**devicesPartialUpdate**](docs/DevicesApi.md#devicespartialupdate) | **PATCH** /api/devices/{id}/ | 
*DevicesApi* | [**devicesUpdate**](docs/DevicesApi.md#devicesupdate) | **PUT** /api/devices/{id}/ | 
*DevicesApi* | [**devicesUpdateOrCreate**](docs/DevicesApi.md#devicesupdateorcreate) | **POST** /api/devices/update-or-create/ | 
*MlOpsApi* | [**apiDeviceCalibrationsList**](docs/MlOpsApi.md#apidevicecalibrationslist) | **GET** /api/device-calibrations/ | 
*MlOpsApi* | [**apiDeviceCalibrationsPartialUpdate**](docs/MlOpsApi.md#apidevicecalibrationspartialupdate) | **PATCH** /api/device-calibrations/{id}/ | 
*MlOpsApi* | [**apiDeviceCalibrationsRetrieve**](docs/MlOpsApi.md#apidevicecalibrationsretrieve) | **GET** /api/device-calibrations/{id}/ | 
*MlOpsApi* | [**apiDeviceCalibrationsUpdate**](docs/MlOpsApi.md#apidevicecalibrationsupdate) | **PUT** /api/device-calibrations/{id}/ | 
*MlOpsApi* | [**apiExperimentDeviceConfigsList**](docs/MlOpsApi.md#apiexperimentdeviceconfigslist) | **GET** /api/experiment-device-configs/ | 
*MlOpsApi* | [**apiExperimentDeviceConfigsRetrieve**](docs/MlOpsApi.md#apiexperimentdeviceconfigsretrieve) | **GET** /api/experiment-device-configs/{id}/ | 
*MlOpsApi* | [**apiExperimentsList**](docs/MlOpsApi.md#apiexperimentslist) | **GET** /api/experiments/ | 
*MlOpsApi* | [**apiExperimentsRetrieve**](docs/MlOpsApi.md#apiexperimentsretrieve) | **GET** /api/experiments/{id}/ | 
*MlOpsApi* | [**apiModelArtifactsList**](docs/MlOpsApi.md#apimodelartifactslist) | **GET** /api/model-artifacts/ | 
*MlOpsApi* | [**apiModelArtifactsRetrieve**](docs/MlOpsApi.md#apimodelartifactsretrieve) | **GET** /api/model-artifacts/{id}/ | 
*MlOpsApi* | [**deviceCalibrationUpdateOrCreate**](docs/MlOpsApi.md#devicecalibrationupdateorcreate) | **POST** /api/device-calibrations/update-or-create/ | 
*PartnersGeeks3Api* | [**alertsList**](docs/PartnersGeeks3Api.md#alertslist) | **GET** /api/partners/3d-geeks/{id}/alerts/ | 
*PartnersGeeks3dApi* | [**metadataRetrieve**](docs/PartnersGeeks3dApi.md#metadataretrieve) | **GET** /api/partners/3d-geeks/{id}/ | 
*RemoteControlApi* | [**apiCommandsList**](docs/RemoteControlApi.md#apicommandslist) | **GET** /api/commands/ | 
*RemoteControlApi* | [**apiCommandsPartialUpdate**](docs/RemoteControlApi.md#apicommandspartialupdate) | **PATCH** /api/commands/{id}/ | 
*RemoteControlApi* | [**apiCommandsRetrieve**](docs/RemoteControlApi.md#apicommandsretrieve) | **GET** /api/commands/{id}/ | 
*RemoteControlApi* | [**apiCommandsUpdate**](docs/RemoteControlApi.md#apicommandsupdate) | **PUT** /api/commands/{id}/ | 
*RemoteControlApi* | [**apiGcodeFilesList**](docs/RemoteControlApi.md#apigcodefileslist) | **GET** /api/gcode-files/ | 
*RemoteControlApi* | [**apiGcodeFilesPartialUpdate**](docs/RemoteControlApi.md#apigcodefilespartialupdate) | **PATCH** /api/gcode-files/{id}/ | 
*RemoteControlApi* | [**apiGcodeFilesRetrieve**](docs/RemoteControlApi.md#apigcodefilesretrieve) | **GET** /api/gcode-files/{id}/ | 
*RemoteControlApi* | [**apiGcodeFilesUpdate**](docs/RemoteControlApi.md#apigcodefilesupdate) | **PUT** /api/gcode-files/{id}/ | 
*RemoteControlApi* | [**apiOctoprintDevicesCreate**](docs/RemoteControlApi.md#apioctoprintdevicescreate) | **POST** /api/octoprint-devices/ | 
*RemoteControlApi* | [**apiOctoprintDevicesList**](docs/RemoteControlApi.md#apioctoprintdeviceslist) | **GET** /api/octoprint-devices/ | 
*RemoteControlApi* | [**apiOctoprintDevicesRetrieve**](docs/RemoteControlApi.md#apioctoprintdevicesretrieve) | **GET** /api/octoprint-devices/{id}/ | 
*RemoteControlApi* | [**apiPrintSessionsCreate**](docs/RemoteControlApi.md#apiprintsessionscreate) | **POST** /api/print-sessions/ | 
*RemoteControlApi* | [**apiPrintSessionsList**](docs/RemoteControlApi.md#apiprintsessionslist) | **GET** /api/print-sessions/ | 
*RemoteControlApi* | [**apiPrintSessionsRetrieve**](docs/RemoteControlApi.md#apiprintsessionsretrieve) | **GET** /api/print-sessions/{session}/ | 
*RemoteControlApi* | [**apiPrinterProfilesList**](docs/RemoteControlApi.md#apiprinterprofileslist) | **GET** /api/printer-profiles/ | 
*RemoteControlApi* | [**apiPrinterProfilesPartialUpdate**](docs/RemoteControlApi.md#apiprinterprofilespartialupdate) | **PATCH** /api/printer-profiles/{id}/ | 
*RemoteControlApi* | [**apiPrinterProfilesRetrieve**](docs/RemoteControlApi.md#apiprinterprofilesretrieve) | **GET** /api/printer-profiles/{id}/ | 
*RemoteControlApi* | [**apiPrinterProfilesUpdate**](docs/RemoteControlApi.md#apiprinterprofilesupdate) | **PUT** /api/printer-profiles/{id}/ | 
*RemoteControlApi* | [**gcodeFilesCreate**](docs/RemoteControlApi.md#gcodefilescreate) | **POST** /api/gcode-files/ | 
*RemoteControlApi* | [**gcodeFilesUpdateOrCreate**](docs/RemoteControlApi.md#gcodefilesupdateorcreate) | **POST** /api/gcode-files/update-or-create/ | 
*RemoteControlApi* | [**octoprintDevicesPartialUpdate**](docs/RemoteControlApi.md#octoprintdevicespartialupdate) | **PATCH** /api/octoprint-devices/{id}/ | 
*RemoteControlApi* | [**octoprintDevicesUpdate**](docs/RemoteControlApi.md#octoprintdevicesupdate) | **PUT** /api/octoprint-devices/{id}/ | 
*RemoteControlApi* | [**octoprintDevicesUpdateOrCreate**](docs/RemoteControlApi.md#octoprintdevicesupdateorcreate) | **POST** /api/octoprint-devices/update-or-create/ | 
*RemoteControlApi* | [**printSessionPartialUpdate**](docs/RemoteControlApi.md#printsessionpartialupdate) | **PATCH** /api/print-sessions/{session}/ | 
*RemoteControlApi* | [**printSessionUpdate**](docs/RemoteControlApi.md#printsessionupdate) | **PUT** /api/print-sessions/{session}/ | 
*RemoteControlApi* | [**printerProfilesCreate**](docs/RemoteControlApi.md#printerprofilescreate) | **POST** /api/printer-profiles/ | 
*RemoteControlApi* | [**printerProfilesUpdateOrCreate**](docs/RemoteControlApi.md#printerprofilesupdateorcreate) | **POST** /api/printer-profiles/update-or-create/ | 
*TelemetryApi* | [**apiOctoprintEventsCreate**](docs/TelemetryApi.md#apioctoprinteventscreate) | **POST** /api/octoprint-events/ | 
*TelemetryApi* | [**apiOctoprintEventsList**](docs/TelemetryApi.md#apioctoprinteventslist) | **GET** /api/octoprint-events/ | 
*TelemetryApi* | [**apiOctoprintEventsRetrieve**](docs/TelemetryApi.md#apioctoprinteventsretrieve) | **GET** /api/octoprint-events/{id}/ | 
*TelemetryApi* | [**apiPrintJobEventsList**](docs/TelemetryApi.md#apiprintjobeventslist) | **GET** /api/print-job-events/ | 
*TelemetryApi* | [**apiPrintJobEventsRetrieve**](docs/TelemetryApi.md#apiprintjobeventsretrieve) | **GET** /api/print-job-events/{id}/ | 
*TelemetryApi* | [**apiPrintNannyPluginEventsList**](docs/TelemetryApi.md#apiprintnannyplugineventslist) | **GET** /api/print-nanny-plugin-events/ | 
*TelemetryApi* | [**apiPrintNannyPluginEventsRetrieve**](docs/TelemetryApi.md#apiprintnannyplugineventsretrieve) | **GET** /api/print-nanny-plugin-events/{id}/ | 
*TelemetryApi* | [**apiRemoteCommandEventsList**](docs/TelemetryApi.md#apiremotecommandeventslist) | **GET** /api/remote-command-events/ | 
*TelemetryApi* | [**apiRemoteCommandEventsRetrieve**](docs/TelemetryApi.md#apiremotecommandeventsretrieve) | **GET** /api/remote-command-events/{id}/ | 
*TelemetryApi* | [**apiTelemetryEventsList**](docs/TelemetryApi.md#apitelemetryeventslist) | **GET** /api/telemetry-events/ | 
*TelemetryApi* | [**apiTelemetryEventsRetrieve**](docs/TelemetryApi.md#apitelemetryeventsretrieve) | **GET** /api/telemetry-events/{id}/ | 
*UsersApi* | [**apiUsersList**](docs/UsersApi.md#apiuserslist) | **GET** /api/users/ | 
*UsersApi* | [**apiUsersMeRetrieve**](docs/UsersApi.md#apiusersmeretrieve) | **GET** /api/users/me/ | 
*UsersApi* | [**apiUsersPartialUpdate**](docs/UsersApi.md#apiuserspartialupdate) | **PATCH** /api/users/{id}/ | 
*UsersApi* | [**apiUsersRetrieve**](docs/UsersApi.md#apiusersretrieve) | **GET** /api/users/{id}/ | 
*UsersApi* | [**apiUsersUpdate**](docs/UsersApi.md#apiusersupdate) | **PUT** /api/users/{id}/ | 


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
 - [com.print-nanny.client.models.CallbackTokenAuthRequest](docs/CallbackTokenAuthRequest.md)
 - [com.print-nanny.client.models.CallbackTokenVerification](docs/CallbackTokenVerification.md)
 - [com.print-nanny.client.models.CallbackTokenVerificationRequest](docs/CallbackTokenVerificationRequest.md)
 - [com.print-nanny.client.models.CommandEnum](docs/CommandEnum.md)
 - [com.print-nanny.client.models.DetailResponse](docs/DetailResponse.md)
 - [com.print-nanny.client.models.Device](docs/Device.md)
 - [com.print-nanny.client.models.DeviceCalibration](docs/DeviceCalibration.md)
 - [com.print-nanny.client.models.DeviceCalibrationRequest](docs/DeviceCalibrationRequest.md)
 - [com.print-nanny.client.models.DeviceIdentity](docs/DeviceIdentity.md)
 - [com.print-nanny.client.models.DeviceIdentityCaCerts](docs/DeviceIdentityCaCerts.md)
 - [com.print-nanny.client.models.DeviceRequest](docs/DeviceRequest.md)
 - [com.print-nanny.client.models.EmailAuthRequest](docs/EmailAuthRequest.md)
 - [com.print-nanny.client.models.EventSourceEnum](docs/EventSourceEnum.md)
 - [com.print-nanny.client.models.EventType0c4Enum](docs/EventType0c4Enum.md)
 - [com.print-nanny.client.models.EventTypeD9eEnum](docs/EventTypeD9eEnum.md)
 - [com.print-nanny.client.models.Experiment](docs/Experiment.md)
 - [com.print-nanny.client.models.ExperimentDeviceConfig](docs/ExperimentDeviceConfig.md)
 - [com.print-nanny.client.models.GcodeFile](docs/GcodeFile.md)
 - [com.print-nanny.client.models.MobileAuthRequest](docs/MobileAuthRequest.md)
 - [com.print-nanny.client.models.ModelArtifact](docs/ModelArtifact.md)
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
 - [com.print-nanny.client.models.OctoprintPiSupport](docs/OctoprintPiSupport.md)
 - [com.print-nanny.client.models.OctoprintPlatform](docs/OctoprintPlatform.md)
 - [com.print-nanny.client.models.OctoprintPrinterData](docs/OctoprintPrinterData.md)
 - [com.print-nanny.client.models.OctoprintPrinterFlags](docs/OctoprintPrinterFlags.md)
 - [com.print-nanny.client.models.OctoprintPrinterState](docs/OctoprintPrinterState.md)
 - [com.print-nanny.client.models.OctoprintProgress](docs/OctoprintProgress.md)
 - [com.print-nanny.client.models.OctoprintPython](docs/OctoprintPython.md)
 - [com.print-nanny.client.models.PaginatedAlertList](docs/PaginatedAlertList.md)
 - [com.print-nanny.client.models.PaginatedDeviceCalibrationList](docs/PaginatedDeviceCalibrationList.md)
 - [com.print-nanny.client.models.PaginatedDeviceList](docs/PaginatedDeviceList.md)
 - [com.print-nanny.client.models.PaginatedExperimentDeviceConfigList](docs/PaginatedExperimentDeviceConfigList.md)
 - [com.print-nanny.client.models.PaginatedExperimentList](docs/PaginatedExperimentList.md)
 - [com.print-nanny.client.models.PaginatedGcodeFileList](docs/PaginatedGcodeFileList.md)
 - [com.print-nanny.client.models.PaginatedModelArtifactList](docs/PaginatedModelArtifactList.md)
 - [com.print-nanny.client.models.PaginatedOctoPrintDeviceList](docs/PaginatedOctoPrintDeviceList.md)
 - [com.print-nanny.client.models.PaginatedOctoPrintEventList](docs/PaginatedOctoPrintEventList.md)
 - [com.print-nanny.client.models.PaginatedPrintJobEventList](docs/PaginatedPrintJobEventList.md)
 - [com.print-nanny.client.models.PaginatedPrintNannyPluginEventList](docs/PaginatedPrintNannyPluginEventList.md)
 - [com.print-nanny.client.models.PaginatedPrintSessionList](docs/PaginatedPrintSessionList.md)
 - [com.print-nanny.client.models.PaginatedPrinterProfileList](docs/PaginatedPrinterProfileList.md)
 - [com.print-nanny.client.models.PaginatedRemoteCommandEventList](docs/PaginatedRemoteCommandEventList.md)
 - [com.print-nanny.client.models.PaginatedRemoteControlCommandList](docs/PaginatedRemoteControlCommandList.md)
 - [com.print-nanny.client.models.PaginatedTelemetryEventPolymorphicList](docs/PaginatedTelemetryEventPolymorphicList.md)
 - [com.print-nanny.client.models.PaginatedUserList](docs/PaginatedUserList.md)
 - [com.print-nanny.client.models.Partner3DGeeksAlert](docs/Partner3DGeeksAlert.md)
 - [com.print-nanny.client.models.Partner3DGeeksMetadata](docs/Partner3DGeeksMetadata.md)
 - [com.print-nanny.client.models.PatchedAlertBulkRequestRequest](docs/PatchedAlertBulkRequestRequest.md)
 - [com.print-nanny.client.models.PatchedAlertRequest](docs/PatchedAlertRequest.md)
 - [com.print-nanny.client.models.PatchedDeviceCalibrationRequest](docs/PatchedDeviceCalibrationRequest.md)
 - [com.print-nanny.client.models.PatchedDeviceRequest](docs/PatchedDeviceRequest.md)
 - [com.print-nanny.client.models.PatchedOctoPrintDeviceRequest](docs/PatchedOctoPrintDeviceRequest.md)
 - [com.print-nanny.client.models.PatchedPrintSessionRequest](docs/PatchedPrintSessionRequest.md)
 - [com.print-nanny.client.models.PatchedPrinterProfileRequest](docs/PatchedPrinterProfileRequest.md)
 - [com.print-nanny.client.models.PatchedRemoteControlCommandRequest](docs/PatchedRemoteControlCommandRequest.md)
 - [com.print-nanny.client.models.PatchedUserRequest](docs/PatchedUserRequest.md)
 - [com.print-nanny.client.models.PrintJobEvent](docs/PrintJobEvent.md)
 - [com.print-nanny.client.models.PrintJobStatusEnum](docs/PrintJobStatusEnum.md)
 - [com.print-nanny.client.models.PrintNannyPluginEvent](docs/PrintNannyPluginEvent.md)
 - [com.print-nanny.client.models.PrintNannyPluginEventEventTypeEnum](docs/PrintNannyPluginEventEventTypeEnum.md)
 - [com.print-nanny.client.models.PrintSession](docs/PrintSession.md)
 - [com.print-nanny.client.models.PrintSessionRequest](docs/PrintSessionRequest.md)
 - [com.print-nanny.client.models.PrinterEvent](docs/PrinterEvent.md)
 - [com.print-nanny.client.models.PrinterProfile](docs/PrinterProfile.md)
 - [com.print-nanny.client.models.PrinterProfileRequest](docs/PrinterProfileRequest.md)
 - [com.print-nanny.client.models.PrinterStateEnum](docs/PrinterStateEnum.md)
 - [com.print-nanny.client.models.RemoteCommandEvent](docs/RemoteCommandEvent.md)
 - [com.print-nanny.client.models.RemoteCommandEventEventTypeEnum](docs/RemoteCommandEventEventTypeEnum.md)
 - [com.print-nanny.client.models.RemoteControlCommand](docs/RemoteControlCommand.md)
 - [com.print-nanny.client.models.RemoteControlCommandRequest](docs/RemoteControlCommandRequest.md)
 - [com.print-nanny.client.models.TelemetryEvent](docs/TelemetryEvent.md)
 - [com.print-nanny.client.models.TelemetryEventEventTypeEnum](docs/TelemetryEventEventTypeEnum.md)
 - [com.print-nanny.client.models.TelemetryEventPolymorphic](docs/TelemetryEventPolymorphic.md)
 - [com.print-nanny.client.models.TokenResponse](docs/TokenResponse.md)
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

