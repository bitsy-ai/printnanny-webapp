# AlertSettingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_methods** | Option<[**Vec<crate::models::AlertMethodsEnum>**](AlertMethodsEnum.md)> |  | [optional]
**event_types** | Option<[**Vec<crate::models::EventTypesEnum>**](EventTypesEnum.md)> |  | [optional]
**discord_webhook** | Option<**String**> | Send notifications to a Discord channel. Please check out this guide to <a href='https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks'>generate a webhook</a> url and paste it here. | [optional]
**print_progress_percent** | Option<**i32**> | Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


