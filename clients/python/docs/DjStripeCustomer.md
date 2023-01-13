# DjStripeCustomer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **int** |  | [readonly] 
**djstripe_created** | **datetime** |  | [readonly] 
**djstripe_updated** | **datetime** |  | [readonly] 
**id** | **str** |  | 
**livemode** | **bool** | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional] 
**created** | **datetime** | The datetime this object was created in stripe. | [optional] 
**metadata** | **dict(str, object)** | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional] 
**description** | **str** | A description of this object. | [optional] 
**address** | **dict(str, object)** | The customer&#39;s address. | [optional] 
**balance** | **int** | Current balance (in cents), if any, being stored on the customer&#39;s account. If negative, the customer has credit to apply to the next invoice. If positive, the customer has an amount owed that will be added to the next invoice. The balance does not refer to any unpaid invoices; it solely takes into account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account for recurring billing purposes (i.e., subscriptions, invoices, invoice items). | [optional] 
**currency** | **str** | The currency the customer can be charged in for recurring billing purposes | [optional] 
**delinquent** | **bool** | Whether or not the latest charge for the customer&#39;s latest invoice has failed. | [optional] 
**deleted** | **bool** | Whether the Customer instance has been deleted upstream in Stripe or not. | [optional] 
**coupon_start** | **datetime** | If a coupon is present, the date at which it was applied. | [readonly] 
**coupon_end** | **datetime** | If a coupon is present and has a limited duration, the date that the discount will end. | [readonly] 
**email** | **str** |  | [optional] 
**invoice_prefix** | **str** | The prefix for the customer used to generate unique invoice numbers. | [optional] 
**invoice_settings** | **dict(str, object)** | The customer&#39;s default invoice settings. | [optional] 
**name** | **str** | The customer&#39;s full name or business name. | [optional] 
**phone** | **str** | The customer&#39;s phone number. | [optional] 
**preferred_locales** | **dict(str, object)** | The customer&#39;s preferred locales (languages), ordered by preference. | [optional] 
**shipping** | **dict(str, object)** | Shipping information associated with the customer. | [optional] 
**tax_exempt** | [**StripeCustomerTaxExempt**](StripeCustomerTaxExempt.md) | Describes the customer&#39;s tax exemption status. When set to reverse, invoice and receipt PDFs include the text \&quot;Reverse charge\&quot;. | [optional] 
**date_purged** | **datetime** |  | [readonly] 
**djstripe_owner_account** | **str** | The Stripe Account this object belongs to. | 
**default_source** | **str** |  | [optional] 
**coupon** | **int** |  | [optional] 
**default_payment_method** | **str** | default payment method used for subscriptions and invoices for the customer. | [optional] 
**subscriber** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


