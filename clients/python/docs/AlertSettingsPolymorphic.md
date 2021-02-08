# AlertSettingsPolymorphic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_dt** | **datetime** |  | [optional] [readonly] 
**updated_dt** | **datetime** |  | [optional] [readonly] 
**alert_type** | [**AlertTypeEnum**](AlertTypeEnum.md) |  | 
**alert_methods** | **list[str]** |  | [optional] 
**enabled** | **bool** | Enable or disable this alert channel | [optional] 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**snapshot** | **list[str]** | Fires on web camera &lt;strong&gt;Snapshot&lt;/strong&gt; command | [optional] 
**stop_monitoring** | **list[str]** | Fires on &lt;strong&gt;MonitoringStop&lt;strong&gt; updates.   Helps debug unexpected Print Nanny crashes. | [optional] 
**start_monitoring** | **list[str]** | Fires on &lt;strong&gt;MonitoringStop&lt;/strong&gt; updates. Helpful if you want to confirm monitoring started without a problem. | [optional] 
**stop_print** | **list[str]** | Fires on &lt;strong&gt;StopPrint&lt;/strong&gt; updates. Get notifed as soon as a print job finishes.  | [optional] 
**start_print** | **list[str]** | Fires on &lt;strong&gt;PrintStart&lt;/strong&gt; command status changes. Helpful for verifying a print job started without a problem. | [optional] 
**move_nozzle** | **list[str]** | Fires on &lt;strong&gt;MoveNozzle&lt;/strong&gt;command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint | [optional] 
**pause_print** | **list[str]** | Fires on &lt;strong&gt;PausePrint&lt;/strong&gt; command status changes. Helpful for verifying a print was paused successfully. | [optional] 
**resume_print** | **list[str]** | Fires on &lt;strong&gt;ResumePrint&lt;/strong&gt; command status changes Helpful for verifying a print was resumed. | [optional] 
**user** | **int** |  | [optional] [readonly] 
**on_progress_percent** | **int** | Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


