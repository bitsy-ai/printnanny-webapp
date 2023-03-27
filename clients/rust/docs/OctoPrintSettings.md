# OctoPrintSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**octoprint_enabled** | Option<**bool**> | Start OctoPrint service | [optional]
**events_enabled** | Option<**bool**> | Send OctoPrint events related to print job status/progress to PrintNanny Cloud https://docs.octoprint.org/en/master/events/index.html | [optional]
**sync_gcode** | Option<**bool**> | Sync Gcode files to/from PrintNanny Cloud | [optional]
**sync_printer_profiles** | Option<**bool**> | Sync Printer Profiles to/from PrintNanny Cloud | [optional]
**sync_backups** | Option<**bool**> | Upload OctoPrint backups to PrintNanny Cloud | [optional]
**auto_backup** | Option<**String**> |  | [optional]
**updated_dt** | **String** |  | [readonly]
**octoprint_server** | **i32** |  | 
**user** | Option<**i32**> |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


