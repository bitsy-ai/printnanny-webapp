# AlertSettingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_methods** | [**list[AlertMethodsEnum]**](AlertMethodsEnum.md) |  | [optional] 
**event_types** | [**list[EventTypesEnum]**](EventTypesEnum.md) |  | [optional] 
**discord_webhook** | **str** | Send notifications to a Discord channel. Please check out this guide to &lt;a href&#x3D;&#39;https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks&#39;&gt;generate a webhook&lt;/a&gt; url and paste it here. | [optional] 
**print_progress_percent** | **int** | Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


