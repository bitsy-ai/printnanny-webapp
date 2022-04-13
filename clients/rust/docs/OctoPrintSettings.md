# OctoPrintSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**events_enabled** | Option<**bool**> | Send OctoPrint events to PrintNanny Cloud https://docs.octoprint.org/en/master/events/index.html | [optional]
**telemetry_enabled** | Option<**bool**> | Send telemetry data to PrintNanny Cloud for debugging/analytics purposes | [optional]
**sync_gcode** | Option<**bool**> | Sync Gcode files to/from PrintNanny Cloud | [optional]
**sync_printer_profiles** | Option<**bool**> | Sync Printer Profiles to/from PrintNanny Cloud | [optional]
**sync_backups** | Option<**bool**> | Upload OctoPrint backups to PrintNanny Cloud | [optional]
**auto_backup** | Option<**String**> |  | [optional]
**monitoring_auto_start** | Option<**bool**> | Start PrintNanny monitoring automatically when a print job begins | [optional]
**monitoring_auto_pause** | Option<**bool**> | Pause failing print jobs automatically | [optional]
**octoprint_install** | **i32** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


