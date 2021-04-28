
# PatchedAlertSettingsPolymorphicRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertType** | [**AlertTypeEnum**](AlertTypeEnum.md) |  |  [optional]
**alertMethods** | [**kotlin.collections.List&lt;AlertMethodsEnum&gt;**](AlertMethodsEnum.md) |  |  [optional]
**enabled** | **kotlin.Boolean** | Enable or disable this alert type |  [optional]
**monitoringStop** | [**kotlin.collections.List&lt;MoveNozzleEnum&gt;**](MoveNozzleEnum.md) | Fires on &lt;strong&gt;MonitoringStop&lt;strong&gt; updates.   Helps debug unexpected Print Nanny crashes. |  [optional]
**monitoringStart** | [**kotlin.collections.List&lt;MoveNozzleEnum&gt;**](MoveNozzleEnum.md) | Fires on &lt;strong&gt;MonitoringStop&lt;/strong&gt; updates. Helpful if you want to confirm monitoring started without a problem. |  [optional]
**printStart** | [**kotlin.collections.List&lt;MoveNozzleEnum&gt;**](MoveNozzleEnum.md) | Fires on &lt;strong&gt;StartPrint&lt;/strong&gt; updates. Get notified as soon as a print job finishes.  |  [optional]
**printStop** | [**kotlin.collections.List&lt;MoveNozzleEnum&gt;**](MoveNozzleEnum.md) | Fires on &lt;strong&gt;PrintStart&lt;/strong&gt; command status changes. Helpful for verifying a print job started without a problem. |  [optional]
**printPause** | [**kotlin.collections.List&lt;MoveNozzleEnum&gt;**](MoveNozzleEnum.md) | Fires on &lt;strong&gt;PausePrint&lt;/strong&gt; command status changes. Helpful for verifying a print was paused successfully. |  [optional]
**printResume** | [**kotlin.collections.List&lt;MoveNozzleEnum&gt;**](MoveNozzleEnum.md) | Fires on &lt;strong&gt;ResumePrint&lt;/strong&gt; command status changes Helpful for verifying a print was resumed. |  [optional]
**moveNozzle** | [**kotlin.collections.List&lt;MoveNozzleEnum&gt;**](MoveNozzleEnum.md) | Fires on &lt;strong&gt;MoveNozzle&lt;/strong&gt;command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint |  [optional]
**onProgressPercent** | **kotlin.Int** | Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress |  [optional]



