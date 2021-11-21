
# Device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **kotlin.Int** |  |  [readonly]
**cloudiotDevice** | [**CloudiotDevice**](CloudiotDevice.md) |  |  [readonly]
**cameras** | [**kotlin.collections.List&lt;Camera&gt;**](Camera.md) |  |  [readonly]
**dashboardUrl** | **kotlin.String** |  |  [readonly]
**bootstrapRelease** | [**Release**](Release.md) |  |  [readonly]
**printerControllers** | [**kotlin.collections.List&lt;PrinterController&gt;**](PrinterController.md) |  |  [readonly]
**user** | [**User**](User.md) |  |  [readonly]
**activeLicense** | [**License**](License.md) |  |  [readonly]
**deleted** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**createdDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**updatedDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**releaseChannel** | [**ReleaseChannelEnum**](ReleaseChannelEnum.md) |  |  [optional]
**hostname** | **kotlin.String** | Please enter the hostname you set in the Raspberry Pi Imager&#39;s Advanced Options menu (without .local extension) |  [optional]



