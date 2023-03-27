# DjStripeCharge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **i32** |  | [readonly]
**failure_code** | [**crate::models::StripeApiErrorCode**](StripeApiErrorCode.md) |  | 
**djstripe_created** | **String** |  | [readonly]
**djstripe_updated** | **String** |  | [readonly]
**id** | **String** |  | 
**livemode** | Option<**bool**> | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional]
**created** | Option<**String**> | The datetime this object was created in stripe. | [optional]
**metadata** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional]
**description** | Option<**String**> | A description of this object. | [optional]
**amount** | **String** | Amount charged (as decimal). | 
**amount_captured** | Option<**String**> | Amount (as decimal) captured (can be less than the amount attribute on the charge if a partial capture was issued). | [optional]
**amount_refunded** | **String** | Amount (as decimal) refunded (can be less than the amount attribute on the charge if a partial refund was issued). | 
**application** | Option<**String**> | ID of the Connect application that created the charge. | [optional]
**application_fee_amount** | Option<**String**> | The amount (as decimal) of the application fee (if any) requested for the charge. | [optional]
**billing_details** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Billing information associated with the PaymentMethod at the time of the transaction. | [optional]
**calculated_statement_descriptor** | Option<**String**> | The full statement descriptor that is passed to card networks, and that is displayed on your customers' credit card and bank statements. Allows you to see what the statement descriptor looks like after the static and dynamic portions are combined. | [optional]
**captured** | Option<**bool**> | If the charge was created without capturing, this boolean represents whether or not it is still uncaptured or has since been captured. | [optional]
**currency** | **String** | The currency in which the charge was made. | 
**disputed** | Option<**bool**> | Whether the charge has been disputed. | [optional]
**failure_message** | Option<**String**> | Message to user further explaining reason for charge failure if available. | [optional]
**fraud_details** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Hash with information on fraud assessments for the charge. | [optional]
**outcome** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Details about whether or not the payment was accepted, and why. | [optional]
**paid** | Option<**bool**> | True if the charge succeeded, or was successfully authorized for later capture, False otherwise. | [optional]
**payment_method_details** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Details about the payment method at the time of the transaction. | [optional]
**receipt_email** | Option<**String**> | The email address that the receipt for this charge was sent to. | [optional]
**receipt_number** | Option<**String**> | The transaction number that appears on email receipts sent for this charge. | [optional]
**receipt_url** | Option<**String**> | This is the URL to view the receipt for this charge. The receipt is kept up-to-date to the latest state of the charge, including any refunds. If the charge is for an Invoice, the receipt will be stylized as an Invoice receipt. | [optional]
**refunded** | Option<**bool**> | Whether or not the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false. | [optional]
**shipping** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Shipping information for the charge | [optional]
**statement_descriptor** | Option<**String**> | For card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers' statements. Must contain at least one letter, maximum 22 characters. | [optional]
**statement_descriptor_suffix** | Option<**String**> | Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor. | [optional]
**status** | Option<[**crate::models::StripeSourceCodeVerificationStatus**](StripeSourceCodeVerificationStatus.md)> | The status of the payment.  * `failed` - Failed * `pending` - Pending * `succeeded` - Succeeded | 
**transfer_data** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | An optional dictionary including the account to automatically transfer to as part of a destination charge. | [optional]
**transfer_group** | Option<**String**> | A string that identifies this transaction as part of a group. | [optional]
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | [optional]
**application_fee** | Option<**String**> | The application fee (if any) for the charge. | [optional]
**balance_transaction** | Option<**String**> | The balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes). | [optional]
**customer** | Option<**String**> | The customer associated with this charge. | [optional]
**dispute** | Option<**String**> | Details about the dispute if the charge has been disputed. | [optional]
**invoice** | Option<**String**> | The invoice this charge is for if one exists. | [optional]
**on_behalf_of** | Option<**String**> | The account (if any) the charge was made on behalf of without triggering an automatic transfer. | [optional]
**payment_intent** | Option<**String**> | PaymentIntent associated with this charge, if one exists. | [optional]
**payment_method** | Option<**String**> | PaymentMethod used in this charge. | [optional]
**source** | Option<**String**> | The source used for this charge. | [optional]
**source_transfer** | Option<**String**> | The transfer which created this charge. Only present if the charge came from another Stripe account. | [optional]
**transfer** | Option<**String**> | The transfer to the `destination` account (only applicable if the charge was created using the `destination` parameter). | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


