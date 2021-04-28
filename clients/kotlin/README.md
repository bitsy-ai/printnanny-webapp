# com.print-nanny.client - Kotlin client library for 

## Requires

* Kotlin 1.3.61
* Gradle 4.9

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
*AlertSettingsApi* | [**alertSettingsList**](docs/AlertSettingsApi.md#alertsettingslist) | **GET** /api/alert_settings/ | 
*AlertSettingsApi* | [**alertSettingsMethodsRetrieve**](docs/AlertSettingsApi.md#alertsettingsmethodsretrieve) | **GET** /api/alert_settings/methods/ | 
*AlertSettingsApi* | [**alertSettingsPartialUpdate**](docs/AlertSettingsApi.md#alertsettingspartialupdate) | **PATCH** /api/alert_settings/{id}/ | 
*AlertSettingsApi* | [**alertSettingsRetrieve**](docs/AlertSettingsApi.md#alertsettingsretrieve) | **GET** /api/alert_settings/{id}/ | 
*AlertSettingsApi* | [**alertSettingsUpdate**](docs/AlertSettingsApi.md#alertsettingsupdate) | **PUT** /api/alert_settings/{id}/ | 
*AlertsApi* | [**alertsList**](docs/AlertsApi.md#alertslist) | **GET** /api/alerts/ | 
*AlertsApi* | [**alertsPartialUpdate**](docs/AlertsApi.md#alertspartialupdate) | **PATCH** /api/alerts/{id}/ | 
*AlertsApi* | [**alertsRecent**](docs/AlertsApi.md#alertsrecent) | **GET** /api/alerts/recent/ | 
*AlertsApi* | [**alertsRetrieve**](docs/AlertsApi.md#alertsretrieve) | **GET** /api/alerts/{id}/ | 
*AlertsApi* | [**alertsSeen**](docs/AlertsApi.md#alertsseen) | **PATCH** /api/alerts/seen/ | 
*AlertsApi* | [**alertsUnread**](docs/AlertsApi.md#alertsunread) | **GET** /api/alerts/unread/ | 
*AlertsApi* | [**alertsUpdate**](docs/AlertsApi.md#alertsupdate) | **PUT** /api/alerts/{id}/ | 
*AlertsApi* | [**printSessionAlertCreate**](docs/AlertsApi.md#printsessionalertcreate) | **POST** /api/print-session-alerts/ | 
*AuthTokenApi* | [**authTokenCreate**](docs/AuthTokenApi.md#authtokencreate) | **POST** /api/auth-token/ | 
*EventsApi* | [**octoprintCoreEventsEnumRetrieve**](docs/EventsApi.md#octoprintcoreeventsenumretrieve) | **GET** /api/octoprint-events/enum/ | 
*EventsApi* | [**octoprintEventsCreate**](docs/EventsApi.md#octoprinteventscreate) | **POST** /api/octoprint-events/ | 
*EventsApi* | [**octoprintEventsList**](docs/EventsApi.md#octoprinteventslist) | **GET** /api/octoprint-events/ | 
*EventsApi* | [**octoprintEventsRetrieve**](docs/EventsApi.md#octoprinteventsretrieve) | **GET** /api/octoprint-events/{id}/ | 
*EventsApi* | [**pluginEventsEnumRetrieve**](docs/EventsApi.md#plugineventsenumretrieve) | **GET** /api/plugin-events/enum/ | 
*EventsApi* | [**pluginEventsList**](docs/EventsApi.md#plugineventslist) | **GET** /api/plugin-events/ | 
*EventsApi* | [**pluginEventsRetrieve**](docs/EventsApi.md#plugineventsretrieve) | **GET** /api/plugin-events/{id}/ | 
*EventsApi* | [**printJobStatesList**](docs/EventsApi.md#printjobstateslist) | **GET** /api/print-job-states/ | 
*EventsApi* | [**printJobStatesRetrieve**](docs/EventsApi.md#printjobstatesretrieve) | **GET** /api/print-job-states/{id}/ | 
*EventsApi* | [**printSessionEventEnumRetrieve**](docs/EventsApi.md#printsessioneventenumretrieve) | **GET** /api/print-job-states/enum/ | 
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
*PartnersGeeks3dApi* | [**metadataRetrieve**](docs/PartnersGeeks3dApi.md#metadataretrieve) | **GET** /api/partners/3d-geeks/{id}/ | 
*PrintSessionAlertsApi* | [**printSessionAlertsList**](docs/PrintSessionAlertsApi.md#printsessionalertslist) | **GET** /api/print-session-alerts/ | 
*PrintSessionAlertsApi* | [**printSessionAlertsRetrieve**](docs/PrintSessionAlertsApi.md#printsessionalertsretrieve) | **GET** /api/print-session-alerts/{id}/ | 
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
*RemoteControlApi* | [**validCommandsRetrieve**](docs/RemoteControlApi.md#validcommandsretrieve) | **GET** /api/commands/valid/ | 
*SchemaApi* | [**schemaRetrieve**](docs/SchemaApi.md#schemaretrieve) | **GET** /api/schema/ | 
*UsersApi* | [**usersList**](docs/UsersApi.md#userslist) | **GET** /api/users/ | 
*UsersApi* | [**usersMeRetrieve**](docs/UsersApi.md#usersmeretrieve) | **GET** /api/users/me/ | 
*UsersApi* | [**usersPartialUpdate**](docs/UsersApi.md#userspartialupdate) | **PATCH** /api/users/{id}/ | 
*UsersApi* | [**usersRetrieve**](docs/UsersApi.md#usersretrieve) | **GET** /api/users/{id}/ | 
*UsersApi* | [**usersUpdate**](docs/UsersApi.md#usersupdate) | **PUT** /api/users/{id}/ | 


<a name="documentation-for-models"></a>
## Documentation for Models

 - [com.print-nanny.client.models.Alert](docs/Alert.md)
 - [com.print-nanny.client.models.AlertBulkResponse](docs/AlertBulkResponse.md)
 - [com.print-nanny.client.models.AlertMethod](docs/AlertMethod.md)
 - [com.print-nanny.client.models.AlertMethodEnum](docs/AlertMethodEnum.md)
 - [com.print-nanny.client.models.AlertMethodsEnum](docs/AlertMethodsEnum.md)
 - [com.print-nanny.client.models.AlertPolymorphic](docs/AlertPolymorphic.md)
 - [com.print-nanny.client.models.AlertPolymorphicRequest](docs/AlertPolymorphicRequest.md)
 - [com.print-nanny.client.models.AlertRequest](docs/AlertRequest.md)
 - [com.print-nanny.client.models.AlertSettings](docs/AlertSettings.md)
 - [com.print-nanny.client.models.AlertSettingsPolymorphic](docs/AlertSettingsPolymorphic.md)
 - [com.print-nanny.client.models.AlertSettingsPolymorphicRequest](docs/AlertSettingsPolymorphicRequest.md)
 - [com.print-nanny.client.models.AlertSettingsRequest](docs/AlertSettingsRequest.md)
 - [com.print-nanny.client.models.AlertTypeEnum](docs/AlertTypeEnum.md)
 - [com.print-nanny.client.models.ArtifactTypesEnum](docs/ArtifactTypesEnum.md)
 - [com.print-nanny.client.models.AuthToken](docs/AuthToken.md)
 - [com.print-nanny.client.models.AuthTokenRequest](docs/AuthTokenRequest.md)
 - [com.print-nanny.client.models.CommandAlertSettings](docs/CommandAlertSettings.md)
 - [com.print-nanny.client.models.CommandAlertSettingsRequest](docs/CommandAlertSettingsRequest.md)
 - [com.print-nanny.client.models.CommandEnum](docs/CommandEnum.md)
 - [com.print-nanny.client.models.CreatePrintSessionAlertRequest](docs/CreatePrintSessionAlertRequest.md)
 - [com.print-nanny.client.models.DeviceCalibration](docs/DeviceCalibration.md)
 - [com.print-nanny.client.models.DeviceCalibrationRequest](docs/DeviceCalibrationRequest.md)
 - [com.print-nanny.client.models.Experiment](docs/Experiment.md)
 - [com.print-nanny.client.models.ExperimentDeviceConfig](docs/ExperimentDeviceConfig.md)
 - [com.print-nanny.client.models.GcodeFile](docs/GcodeFile.md)
 - [com.print-nanny.client.models.GcodeFileRequest](docs/GcodeFileRequest.md)
 - [com.print-nanny.client.models.ManualVideoUploadAlert](docs/ManualVideoUploadAlert.md)
 - [com.print-nanny.client.models.ManualVideoUploadAlertRequest](docs/ManualVideoUploadAlertRequest.md)
 - [com.print-nanny.client.models.ModelArtifact](docs/ModelArtifact.md)
 - [com.print-nanny.client.models.MonitoringModeEnum](docs/MonitoringModeEnum.md)
 - [com.print-nanny.client.models.MoveNozzleEnum](docs/MoveNozzleEnum.md)
 - [com.print-nanny.client.models.Nested](docs/Nested.md)
 - [com.print-nanny.client.models.OctoPrintDevice](docs/OctoPrintDevice.md)
 - [com.print-nanny.client.models.OctoPrintDeviceKey](docs/OctoPrintDeviceKey.md)
 - [com.print-nanny.client.models.OctoPrintDeviceRequest](docs/OctoPrintDeviceRequest.md)
 - [com.print-nanny.client.models.OctoPrintEvent](docs/OctoPrintEvent.md)
 - [com.print-nanny.client.models.OctoPrintEventEventTypeEnum](docs/OctoPrintEventEventTypeEnum.md)
 - [com.print-nanny.client.models.OctoPrintEventRequest](docs/OctoPrintEventRequest.md)
 - [com.print-nanny.client.models.PaginatedAlertPolymorphicList](docs/PaginatedAlertPolymorphicList.md)
 - [com.print-nanny.client.models.PaginatedAlertSettingsPolymorphicList](docs/PaginatedAlertSettingsPolymorphicList.md)
 - [com.print-nanny.client.models.PaginatedDeviceCalibrationList](docs/PaginatedDeviceCalibrationList.md)
 - [com.print-nanny.client.models.PaginatedExperimentDeviceConfigList](docs/PaginatedExperimentDeviceConfigList.md)
 - [com.print-nanny.client.models.PaginatedExperimentList](docs/PaginatedExperimentList.md)
 - [com.print-nanny.client.models.PaginatedGcodeFileList](docs/PaginatedGcodeFileList.md)
 - [com.print-nanny.client.models.PaginatedModelArtifactList](docs/PaginatedModelArtifactList.md)
 - [com.print-nanny.client.models.PaginatedOctoPrintDeviceList](docs/PaginatedOctoPrintDeviceList.md)
 - [com.print-nanny.client.models.PaginatedOctoPrintEventList](docs/PaginatedOctoPrintEventList.md)
 - [com.print-nanny.client.models.PaginatedPluginEventList](docs/PaginatedPluginEventList.md)
 - [com.print-nanny.client.models.PaginatedPrintSessionAlertList](docs/PaginatedPrintSessionAlertList.md)
 - [com.print-nanny.client.models.PaginatedPrintSessionList](docs/PaginatedPrintSessionList.md)
 - [com.print-nanny.client.models.PaginatedPrintSessionStateList](docs/PaginatedPrintSessionStateList.md)
 - [com.print-nanny.client.models.PaginatedPrinterProfileList](docs/PaginatedPrinterProfileList.md)
 - [com.print-nanny.client.models.PaginatedRemoteControlCommandList](docs/PaginatedRemoteControlCommandList.md)
 - [com.print-nanny.client.models.PaginatedUserList](docs/PaginatedUserList.md)
 - [com.print-nanny.client.models.PartnerOctoPrintDevice](docs/PartnerOctoPrintDevice.md)
 - [com.print-nanny.client.models.PatchedAlertBulkRequestRequest](docs/PatchedAlertBulkRequestRequest.md)
 - [com.print-nanny.client.models.PatchedAlertPolymorphicRequest](docs/PatchedAlertPolymorphicRequest.md)
 - [com.print-nanny.client.models.PatchedAlertRequest](docs/PatchedAlertRequest.md)
 - [com.print-nanny.client.models.PatchedAlertSettingsPolymorphicRequest](docs/PatchedAlertSettingsPolymorphicRequest.md)
 - [com.print-nanny.client.models.PatchedAlertSettingsRequest](docs/PatchedAlertSettingsRequest.md)
 - [com.print-nanny.client.models.PatchedCommandAlertSettingsRequest](docs/PatchedCommandAlertSettingsRequest.md)
 - [com.print-nanny.client.models.PatchedDeviceCalibrationRequest](docs/PatchedDeviceCalibrationRequest.md)
 - [com.print-nanny.client.models.PatchedGcodeFileRequest](docs/PatchedGcodeFileRequest.md)
 - [com.print-nanny.client.models.PatchedManualVideoUploadAlertRequest](docs/PatchedManualVideoUploadAlertRequest.md)
 - [com.print-nanny.client.models.PatchedOctoPrintDeviceRequest](docs/PatchedOctoPrintDeviceRequest.md)
 - [com.print-nanny.client.models.PatchedPrintSessionAlertRequest](docs/PatchedPrintSessionAlertRequest.md)
 - [com.print-nanny.client.models.PatchedPrintSessionRequest](docs/PatchedPrintSessionRequest.md)
 - [com.print-nanny.client.models.PatchedPrinterProfileRequest](docs/PatchedPrinterProfileRequest.md)
 - [com.print-nanny.client.models.PatchedProgressAlertRequest](docs/PatchedProgressAlertRequest.md)
 - [com.print-nanny.client.models.PatchedProgressAlertSettingsRequest](docs/PatchedProgressAlertSettingsRequest.md)
 - [com.print-nanny.client.models.PatchedRemoteControlCommandAlertRequest](docs/PatchedRemoteControlCommandAlertRequest.md)
 - [com.print-nanny.client.models.PatchedRemoteControlCommandRequest](docs/PatchedRemoteControlCommandRequest.md)
 - [com.print-nanny.client.models.PatchedUserRequest](docs/PatchedUserRequest.md)
 - [com.print-nanny.client.models.PluginEvent](docs/PluginEvent.md)
 - [com.print-nanny.client.models.PluginEventEventTypeEnum](docs/PluginEventEventTypeEnum.md)
 - [com.print-nanny.client.models.PrintSession](docs/PrintSession.md)
 - [com.print-nanny.client.models.PrintSessionAlert](docs/PrintSessionAlert.md)
 - [com.print-nanny.client.models.PrintSessionAlertAlertSubtypeEnum](docs/PrintSessionAlertAlertSubtypeEnum.md)
 - [com.print-nanny.client.models.PrintSessionAlertRequest](docs/PrintSessionAlertRequest.md)
 - [com.print-nanny.client.models.PrintSessionRequest](docs/PrintSessionRequest.md)
 - [com.print-nanny.client.models.PrintSessionState](docs/PrintSessionState.md)
 - [com.print-nanny.client.models.PrintSessionStateEventTypeEnum](docs/PrintSessionStateEventTypeEnum.md)
 - [com.print-nanny.client.models.PrinterProfile](docs/PrinterProfile.md)
 - [com.print-nanny.client.models.PrinterProfileRequest](docs/PrinterProfileRequest.md)
 - [com.print-nanny.client.models.ProgressAlert](docs/ProgressAlert.md)
 - [com.print-nanny.client.models.ProgressAlertRequest](docs/ProgressAlertRequest.md)
 - [com.print-nanny.client.models.ProgressAlertSettings](docs/ProgressAlertSettings.md)
 - [com.print-nanny.client.models.ProgressAlertSettingsRequest](docs/ProgressAlertSettingsRequest.md)
 - [com.print-nanny.client.models.RemoteControlCommand](docs/RemoteControlCommand.md)
 - [com.print-nanny.client.models.RemoteControlCommandAlert](docs/RemoteControlCommandAlert.md)
 - [com.print-nanny.client.models.RemoteControlCommandAlertAlertSubtypeEnum](docs/RemoteControlCommandAlertAlertSubtypeEnum.md)
 - [com.print-nanny.client.models.RemoteControlCommandAlertRequest](docs/RemoteControlCommandAlertRequest.md)
 - [com.print-nanny.client.models.RemoteControlCommandRequest](docs/RemoteControlCommandRequest.md)
 - [com.print-nanny.client.models.StatusEnum](docs/StatusEnum.md)
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

