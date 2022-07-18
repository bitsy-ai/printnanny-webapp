# StripeNextInvoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **i32** |  | [readonly]
**djstripe_created** | **String** |  | [readonly]
**djstripe_updated** | **String** |  | [readonly]
**livemode** | Option<**bool**> | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional]
**created** | Option<**String**> | The datetime this object was created in stripe. | [optional]
**metadata** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional]
**description** | Option<**String**> | A description of this object. | [optional]
**account_country** | Option<**String**> | The country of the business associated with this invoice, most often the business creating the invoice. | [optional]
**account_name** | Option<**String**> | The public name of the business associated with this invoice, most often the business creating the invoice. | [optional]
**amount_due** | **String** | Final amount due (as decimal) at this time for this invoice. If the invoice's total is smaller than the minimum charge amount, for example, or if there is account credit that can be applied to the invoice, the amount_due may be 0. If there is a positive starting_balance for the invoice (the customer owes money), the amount_due will also take that into account. The charge that gets generated for the invoice will be for the amount specified in amount_due. | 
**amount_paid** | Option<**String**> | The amount, (as decimal), that was paid. | [optional]
**amount_remaining** | Option<**String**> | The amount remaining, (as decimal), that is due. | [optional]
**application_fee_amount** | Option<**String**> | The fee (as decimal) that will be applied to the invoice and transferred to the application owner's Stripe account when the invoice is paid. | [optional]
**attempt_count** | **i32** | Number of payment attempts made for this invoice, from the perspective of the payment retry schedule. Any payment attempt counts as the first attempt, and subsequently only automatic retries increment the attempt count. In other words, manual payment attempts after the first attempt do not affect the retry schedule. | 
**attempted** | Option<**bool**> | Whether or not an attempt has been made to pay the invoice. An invoice is not attempted until 1 hour after the ``invoice.created`` webhook, for example, so you might not want to display that invoice as unpaid to your users. | [optional]
**auto_advance** | Option<**bool**> | Controls whether Stripe will perform automatic collection of the invoice. When false, the invoice's state will not automatically advance without an explicit action. | [optional]
**billing_reason** | Option<[**crate::models::OneOfBillingReasonEnumBlankEnum**](oneOf<BillingReasonEnum,BlankEnum>.md)> | Indicates the reason why the invoice was created. subscription_cycle indicates an invoice created by a subscription advancing into a new period. subscription_create indicates an invoice created due to creating a subscription. subscription_update indicates an invoice created due to updating a subscription. subscription is set for all old invoices to indicate either a change to a subscription or a period advancement. manual is set for all invoices unrelated to a subscription (for example: created via the invoice editor). The upcoming value is reserved for simulated invoices per the upcoming invoice endpoint. subscription_threshold indicates an invoice created due to a billing threshold being reached. | [optional]
**collection_method** | Option<[**crate::models::OneOfCollectionMethodEnumNullEnum**](oneOf<CollectionMethodEnum,NullEnum>.md)> | When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. | [optional]
**currency** | **String** | Three-letter ISO currency code | 
**customer_address** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | The customer's address. Until the invoice is finalized, this field will equal customer.address. Once the invoice is finalized, this field will no longer be updated. | [optional]
**customer_email** | Option<**String**> | The customer's email. Until the invoice is finalized, this field will equal customer.email. Once the invoice is finalized, this field will no longer be updated. | [optional]
**customer_name** | Option<**String**> | The customer's name. Until the invoice is finalized, this field will equal customer.name. Once the invoice is finalized, this field will no longer be updated. | [optional]
**customer_phone** | Option<**String**> | The customer's phone number. Until the invoice is finalized, this field will equal customer.phone. Once the invoice is finalized, this field will no longer be updated. | [optional]
**customer_shipping** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | The customer's shipping information. Until the invoice is finalized, this field will equal customer.shipping. Once the invoice is finalized, this field will no longer be updated. | [optional]
**customer_tax_exempt** | Option<[**crate::models::CustomerTaxExemptEnum**](CustomerTaxExemptEnum.md)> | The customer's tax exempt status. Until the invoice is finalized, this field will equal customer.tax_exempt. Once the invoice is finalized, this field will no longer be updated. | [optional]
**discount** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Describes the current discount applied to this subscription, if there is one. When billing, a discount applied to a subscription overrides a discount applied on a customer-wide basis. | [optional]
**due_date** | Option<**String**> | The date on which payment for this invoice is due. This value will be null for invoices where billing=charge_automatically. | [optional]
**ending_balance** | Option<**i64**> | Ending customer balance (in cents) after attempting to pay invoice. If the invoice has not been attempted yet, this will be null. | [optional]
**footer** | Option<**String**> | Footer displayed on the invoice. | [optional]
**hosted_invoice_url** | Option<**String**> | The URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been frozen yet, this will be null. | [optional]
**invoice_pdf** | Option<**String**> | The link to download the PDF for the invoice. If the invoice has not been frozen yet, this will be null. | [optional]
**next_payment_attempt** | Option<**String**> | The time at which payment will next be attempted. | [optional]
**number** | Option<**String**> | A unique, identifying string that appears on emails sent to the customer for this invoice. This starts with the customer's unique invoice_prefix if it is specified. | [optional]
**paid** | Option<**bool**> | Whether payment was successfully collected for this invoice. An invoice can be paid (most commonly) with a charge or with credit from the customer's account balance. | [optional]
**period_end** | **String** | End of the usage period during which invoice items were added to this invoice. | 
**period_start** | **String** | Start of the usage period during which invoice items were added to this invoice. | 
**post_payment_credit_notes_amount** | Option<**i64**> | Total amount (in cents) of all post-payment credit notes issued for this invoice. | [optional]
**pre_payment_credit_notes_amount** | Option<**i64**> | Total amount (in cents) of all pre-payment credit notes issued for this invoice. | [optional]
**receipt_number** | Option<**String**> | This is the transaction number that appears on email receipts sent for this invoice. | [optional]
**starting_balance** | **i64** | Starting customer balance (in cents) before attempting to pay invoice. If the invoice has not been attempted yet, this will be the current customer balance. | 
**statement_descriptor** | Option<**String**> | An arbitrary string to be displayed on your customer's credit card statement. The statement description may not include <>\"' characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped. While most banks display this information consistently, some may display it incorrectly or not at all. | [optional]
**status** | Option<[**crate::models::OneOfStripeNextInvoiceStatusEnumBlankEnum**](oneOf<StripeNextInvoiceStatusEnum,BlankEnum>.md)> | The status of the invoice, one of draft, open, paid, uncollectible, or void. | [optional]
**status_transitions** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**subscription_proration_date** | Option<**String**> | Only set for upcoming invoices that preview prorations. The time used to calculate prorations. | [optional]
**subtotal** | **String** | Total (as decimal) of all subscriptions, invoice items, and prorations on the invoice before any discount or tax is applied. | 
**tax** | Option<**String**> | The amount (as decimal) of tax included in the total, calculated from ``tax_percent`` and the subtotal. If no ``tax_percent`` is defined, this value will be null. | [optional]
**tax_percent** | Option<**String**> | This percentage of the subtotal has been added to the total amount of the invoice, including invoice line items and discounts. This field is inherited from the subscription's ``tax_percent`` field, but can be changed before the invoice is paid. This field defaults to null. | [optional]
**threshold_reason** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | If billing_reason is set to subscription_threshold this returns more information on which threshold rules triggered the invoice. | [optional]
**total** | **String** |  | 
**webhooks_delivered_at** | Option<**String**> | The time at which webhooks for this invoice were successfully delivered (if the invoice had no webhooks to deliver, this will match `date`). Invoice payment is delayed until webhooks are delivered, or until all webhook delivery attempts have been exhausted. | [optional]
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | [optional]
**charge** | Option<**i32**> | The latest charge generated for this invoice, if any. | [optional]
**customer** | **String** | The customer associated with this invoice. | 
**default_payment_method** | Option<**String**> | Default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings. | [optional]
**payment_intent** | Option<**i32**> | The PaymentIntent associated with this invoice. The PaymentIntent is generated when the invoice is finalized, and can then be used to pay the invoice.Note that voiding an invoice will cancel the PaymentIntent | [optional]
**subscription** | Option<**String**> | The subscription that this invoice was prepared for, if any. | [optional]
**default_source** | Option<**String**> | The default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


