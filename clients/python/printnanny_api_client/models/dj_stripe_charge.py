import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stripe_api_error_code import StripeApiErrorCode
from ..models.stripe_source_code_verification_status import StripeSourceCodeVerificationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dj_stripe_charge_billing_details import DjStripeChargeBillingDetails
    from ..models.dj_stripe_charge_fraud_details import DjStripeChargeFraudDetails
    from ..models.dj_stripe_charge_metadata import DjStripeChargeMetadata
    from ..models.dj_stripe_charge_outcome import DjStripeChargeOutcome
    from ..models.dj_stripe_charge_payment_method_details import DjStripeChargePaymentMethodDetails
    from ..models.dj_stripe_charge_shipping import DjStripeChargeShipping
    from ..models.dj_stripe_charge_transfer_data import DjStripeChargeTransferData


T = TypeVar("T", bound="DjStripeCharge")


@attr.s(auto_attribs=True)
class DjStripeCharge:
    """
    Attributes:
        djstripe_id (int):
        failure_code (StripeApiErrorCode):
        djstripe_created (datetime.datetime):
        djstripe_updated (datetime.datetime):
        id (str):
        amount (str): Amount charged (as decimal).
        amount_refunded (str): Amount (as decimal) refunded (can be less than the amount attribute on the charge if a
            partial refund was issued).
        currency (str): The currency in which the charge was made.
        status (StripeSourceCodeVerificationStatus):
        livemode (Union[Unset, None, bool]): Null here indicates that the livemode status is unknown or was previously
            unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode
            operation.
        created (Union[Unset, None, datetime.datetime]): The datetime this object was created in stripe.
        metadata (Union[Unset, None, DjStripeChargeMetadata]): A set of key/value pairs that you can attach to an
            object. It can be useful for storing additional information about an object in a structured format.
        description (Union[Unset, None, str]): A description of this object.
        amount_captured (Union[Unset, None, str]): Amount (as decimal) captured (can be less than the amount attribute
            on the charge if a partial capture was issued).
        application (Union[Unset, str]): ID of the Connect application that created the charge.
        application_fee_amount (Union[Unset, None, str]): The amount (as decimal) of the application fee (if any)
            requested for the charge.
        billing_details (Union[Unset, None, DjStripeChargeBillingDetails]): Billing information associated with the
            PaymentMethod at the time of the transaction.
        calculated_statement_descriptor (Union[Unset, str]): The full statement descriptor that is passed to card
            networks, and that is displayed on your customers' credit card and bank statements. Allows you to see what the
            statement descriptor looks like after the static and dynamic portions are combined.
        captured (Union[Unset, bool]): If the charge was created without capturing, this boolean represents whether or
            not it is still uncaptured or has since been captured.
        disputed (Union[Unset, bool]): Whether the charge has been disputed.
        failure_message (Union[Unset, str]): Message to user further explaining reason for charge failure if available.
        fraud_details (Union[Unset, None, DjStripeChargeFraudDetails]): Hash with information on fraud assessments for
            the charge.
        outcome (Union[Unset, None, DjStripeChargeOutcome]): Details about whether or not the payment was accepted, and
            why.
        paid (Union[Unset, bool]): True if the charge succeeded, or was successfully authorized for later capture, False
            otherwise.
        payment_method_details (Union[Unset, None, DjStripeChargePaymentMethodDetails]): Details about the payment
            method at the time of the transaction.
        receipt_email (Union[Unset, str]): The email address that the receipt for this charge was sent to.
        receipt_number (Union[Unset, str]): The transaction number that appears on email receipts sent for this charge.
        receipt_url (Union[Unset, str]): This is the URL to view the receipt for this charge. The receipt is kept up-to-
            date to the latest state of the charge, including any refunds. If the charge is for an Invoice, the receipt will
            be stylized as an Invoice receipt.
        refunded (Union[Unset, bool]): Whether or not the charge has been fully refunded. If the charge is only
            partially refunded, this attribute will still be false.
        shipping (Union[Unset, None, DjStripeChargeShipping]): Shipping information for the charge
        statement_descriptor (Union[Unset, None, str]): For card charges, use statement_descriptor_suffix instead.
            Otherwise, you can use this value as the complete description of a charge on your customers' statements. Must
            contain at least one letter, maximum 22 characters.
        statement_descriptor_suffix (Union[Unset, None, str]): Provides information about the charge that customers see
            on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on
            the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
        transfer_data (Union[Unset, None, DjStripeChargeTransferData]): An optional dictionary including the account to
            automatically transfer to as part of a destination charge.
        transfer_group (Union[Unset, None, str]): A string that identifies this transaction as part of a group.
        djstripe_owner_account (Union[Unset, None, str]): The Stripe Account this object belongs to.
        application_fee (Union[Unset, None, str]): The application fee (if any) for the charge.
        balance_transaction (Union[Unset, None, str]): The balance transaction that describes the impact of this charge
            on your account balance (not including refunds or disputes).
        customer (Union[Unset, None, str]): The customer associated with this charge.
        dispute (Union[Unset, None, str]): Details about the dispute if the charge has been disputed.
        invoice (Union[Unset, None, str]): The invoice this charge is for if one exists.
        on_behalf_of (Union[Unset, None, str]): The account (if any) the charge was made on behalf of without triggering
            an automatic transfer.
        payment_intent (Union[Unset, None, str]): PaymentIntent associated with this charge, if one exists.
        payment_method (Union[Unset, None, str]): PaymentMethod used in this charge.
        source (Union[Unset, None, str]): The source used for this charge.
        source_transfer (Union[Unset, None, str]): The transfer which created this charge. Only present if the charge
            came from another Stripe account.
        transfer (Union[Unset, None, str]): The transfer to the `destination` account (only applicable if the charge was
            created using the `destination` parameter).
    """

    djstripe_id: int
    failure_code: StripeApiErrorCode
    djstripe_created: datetime.datetime
    djstripe_updated: datetime.datetime
    id: str
    amount: str
    amount_refunded: str
    currency: str
    status: StripeSourceCodeVerificationStatus
    livemode: Union[Unset, None, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, None, "DjStripeChargeMetadata"] = UNSET
    description: Union[Unset, None, str] = UNSET
    amount_captured: Union[Unset, None, str] = UNSET
    application: Union[Unset, str] = UNSET
    application_fee_amount: Union[Unset, None, str] = UNSET
    billing_details: Union[Unset, None, "DjStripeChargeBillingDetails"] = UNSET
    calculated_statement_descriptor: Union[Unset, str] = UNSET
    captured: Union[Unset, bool] = UNSET
    disputed: Union[Unset, bool] = UNSET
    failure_message: Union[Unset, str] = UNSET
    fraud_details: Union[Unset, None, "DjStripeChargeFraudDetails"] = UNSET
    outcome: Union[Unset, None, "DjStripeChargeOutcome"] = UNSET
    paid: Union[Unset, bool] = UNSET
    payment_method_details: Union[Unset, None, "DjStripeChargePaymentMethodDetails"] = UNSET
    receipt_email: Union[Unset, str] = UNSET
    receipt_number: Union[Unset, str] = UNSET
    receipt_url: Union[Unset, str] = UNSET
    refunded: Union[Unset, bool] = UNSET
    shipping: Union[Unset, None, "DjStripeChargeShipping"] = UNSET
    statement_descriptor: Union[Unset, None, str] = UNSET
    statement_descriptor_suffix: Union[Unset, None, str] = UNSET
    transfer_data: Union[Unset, None, "DjStripeChargeTransferData"] = UNSET
    transfer_group: Union[Unset, None, str] = UNSET
    djstripe_owner_account: Union[Unset, None, str] = UNSET
    application_fee: Union[Unset, None, str] = UNSET
    balance_transaction: Union[Unset, None, str] = UNSET
    customer: Union[Unset, None, str] = UNSET
    dispute: Union[Unset, None, str] = UNSET
    invoice: Union[Unset, None, str] = UNSET
    on_behalf_of: Union[Unset, None, str] = UNSET
    payment_intent: Union[Unset, None, str] = UNSET
    payment_method: Union[Unset, None, str] = UNSET
    source: Union[Unset, None, str] = UNSET
    source_transfer: Union[Unset, None, str] = UNSET
    transfer: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        djstripe_id = self.djstripe_id
        failure_code = self.failure_code.value

        djstripe_created = self.djstripe_created.isoformat()

        djstripe_updated = self.djstripe_updated.isoformat()

        id = self.id
        amount = self.amount
        amount_refunded = self.amount_refunded
        currency = self.currency
        status = self.status.value

        livemode = self.livemode
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        description = self.description
        amount_captured = self.amount_captured
        application = self.application
        application_fee_amount = self.application_fee_amount
        billing_details: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_details, Unset):
            billing_details = self.billing_details.to_dict() if self.billing_details else None

        calculated_statement_descriptor = self.calculated_statement_descriptor
        captured = self.captured
        disputed = self.disputed
        failure_message = self.failure_message
        fraud_details: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.fraud_details, Unset):
            fraud_details = self.fraud_details.to_dict() if self.fraud_details else None

        outcome: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.to_dict() if self.outcome else None

        paid = self.paid
        payment_method_details: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_details, Unset):
            payment_method_details = self.payment_method_details.to_dict() if self.payment_method_details else None

        receipt_email = self.receipt_email
        receipt_number = self.receipt_number
        receipt_url = self.receipt_url
        refunded = self.refunded
        shipping: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict() if self.shipping else None

        statement_descriptor = self.statement_descriptor
        statement_descriptor_suffix = self.statement_descriptor_suffix
        transfer_data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.transfer_data, Unset):
            transfer_data = self.transfer_data.to_dict() if self.transfer_data else None

        transfer_group = self.transfer_group
        djstripe_owner_account = self.djstripe_owner_account
        application_fee = self.application_fee
        balance_transaction = self.balance_transaction
        customer = self.customer
        dispute = self.dispute
        invoice = self.invoice
        on_behalf_of = self.on_behalf_of
        payment_intent = self.payment_intent
        payment_method = self.payment_method
        source = self.source
        source_transfer = self.source_transfer
        transfer = self.transfer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "djstripe_id": djstripe_id,
                "failure_code": failure_code,
                "djstripe_created": djstripe_created,
                "djstripe_updated": djstripe_updated,
                "id": id,
                "amount": amount,
                "amount_refunded": amount_refunded,
                "currency": currency,
                "status": status,
            }
        )
        if livemode is not UNSET:
            field_dict["livemode"] = livemode
        if created is not UNSET:
            field_dict["created"] = created
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if description is not UNSET:
            field_dict["description"] = description
        if amount_captured is not UNSET:
            field_dict["amount_captured"] = amount_captured
        if application is not UNSET:
            field_dict["application"] = application
        if application_fee_amount is not UNSET:
            field_dict["application_fee_amount"] = application_fee_amount
        if billing_details is not UNSET:
            field_dict["billing_details"] = billing_details
        if calculated_statement_descriptor is not UNSET:
            field_dict["calculated_statement_descriptor"] = calculated_statement_descriptor
        if captured is not UNSET:
            field_dict["captured"] = captured
        if disputed is not UNSET:
            field_dict["disputed"] = disputed
        if failure_message is not UNSET:
            field_dict["failure_message"] = failure_message
        if fraud_details is not UNSET:
            field_dict["fraud_details"] = fraud_details
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if paid is not UNSET:
            field_dict["paid"] = paid
        if payment_method_details is not UNSET:
            field_dict["payment_method_details"] = payment_method_details
        if receipt_email is not UNSET:
            field_dict["receipt_email"] = receipt_email
        if receipt_number is not UNSET:
            field_dict["receipt_number"] = receipt_number
        if receipt_url is not UNSET:
            field_dict["receipt_url"] = receipt_url
        if refunded is not UNSET:
            field_dict["refunded"] = refunded
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if statement_descriptor is not UNSET:
            field_dict["statement_descriptor"] = statement_descriptor
        if statement_descriptor_suffix is not UNSET:
            field_dict["statement_descriptor_suffix"] = statement_descriptor_suffix
        if transfer_data is not UNSET:
            field_dict["transfer_data"] = transfer_data
        if transfer_group is not UNSET:
            field_dict["transfer_group"] = transfer_group
        if djstripe_owner_account is not UNSET:
            field_dict["djstripe_owner_account"] = djstripe_owner_account
        if application_fee is not UNSET:
            field_dict["application_fee"] = application_fee
        if balance_transaction is not UNSET:
            field_dict["balance_transaction"] = balance_transaction
        if customer is not UNSET:
            field_dict["customer"] = customer
        if dispute is not UNSET:
            field_dict["dispute"] = dispute
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if on_behalf_of is not UNSET:
            field_dict["on_behalf_of"] = on_behalf_of
        if payment_intent is not UNSET:
            field_dict["payment_intent"] = payment_intent
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if source is not UNSET:
            field_dict["source"] = source
        if source_transfer is not UNSET:
            field_dict["source_transfer"] = source_transfer
        if transfer is not UNSET:
            field_dict["transfer"] = transfer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dj_stripe_charge_billing_details import DjStripeChargeBillingDetails
        from ..models.dj_stripe_charge_fraud_details import DjStripeChargeFraudDetails
        from ..models.dj_stripe_charge_metadata import DjStripeChargeMetadata
        from ..models.dj_stripe_charge_outcome import DjStripeChargeOutcome
        from ..models.dj_stripe_charge_payment_method_details import DjStripeChargePaymentMethodDetails
        from ..models.dj_stripe_charge_shipping import DjStripeChargeShipping
        from ..models.dj_stripe_charge_transfer_data import DjStripeChargeTransferData

        d = src_dict.copy()
        djstripe_id = d.pop("djstripe_id")

        failure_code = StripeApiErrorCode(d.pop("failure_code"))

        djstripe_created = isoparse(d.pop("djstripe_created"))

        djstripe_updated = isoparse(d.pop("djstripe_updated"))

        id = d.pop("id")

        amount = d.pop("amount")

        amount_refunded = d.pop("amount_refunded")

        currency = d.pop("currency")

        status = StripeSourceCodeVerificationStatus(d.pop("status"))

        livemode = d.pop("livemode", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, datetime.datetime]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, DjStripeChargeMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DjStripeChargeMetadata.from_dict(_metadata)

        description = d.pop("description", UNSET)

        amount_captured = d.pop("amount_captured", UNSET)

        application = d.pop("application", UNSET)

        application_fee_amount = d.pop("application_fee_amount", UNSET)

        _billing_details = d.pop("billing_details", UNSET)
        billing_details: Union[Unset, None, DjStripeChargeBillingDetails]
        if _billing_details is None:
            billing_details = None
        elif isinstance(_billing_details, Unset):
            billing_details = UNSET
        else:
            billing_details = DjStripeChargeBillingDetails.from_dict(_billing_details)

        calculated_statement_descriptor = d.pop("calculated_statement_descriptor", UNSET)

        captured = d.pop("captured", UNSET)

        disputed = d.pop("disputed", UNSET)

        failure_message = d.pop("failure_message", UNSET)

        _fraud_details = d.pop("fraud_details", UNSET)
        fraud_details: Union[Unset, None, DjStripeChargeFraudDetails]
        if _fraud_details is None:
            fraud_details = None
        elif isinstance(_fraud_details, Unset):
            fraud_details = UNSET
        else:
            fraud_details = DjStripeChargeFraudDetails.from_dict(_fraud_details)

        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, None, DjStripeChargeOutcome]
        if _outcome is None:
            outcome = None
        elif isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = DjStripeChargeOutcome.from_dict(_outcome)

        paid = d.pop("paid", UNSET)

        _payment_method_details = d.pop("payment_method_details", UNSET)
        payment_method_details: Union[Unset, None, DjStripeChargePaymentMethodDetails]
        if _payment_method_details is None:
            payment_method_details = None
        elif isinstance(_payment_method_details, Unset):
            payment_method_details = UNSET
        else:
            payment_method_details = DjStripeChargePaymentMethodDetails.from_dict(_payment_method_details)

        receipt_email = d.pop("receipt_email", UNSET)

        receipt_number = d.pop("receipt_number", UNSET)

        receipt_url = d.pop("receipt_url", UNSET)

        refunded = d.pop("refunded", UNSET)

        _shipping = d.pop("shipping", UNSET)
        shipping: Union[Unset, None, DjStripeChargeShipping]
        if _shipping is None:
            shipping = None
        elif isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = DjStripeChargeShipping.from_dict(_shipping)

        statement_descriptor = d.pop("statement_descriptor", UNSET)

        statement_descriptor_suffix = d.pop("statement_descriptor_suffix", UNSET)

        _transfer_data = d.pop("transfer_data", UNSET)
        transfer_data: Union[Unset, None, DjStripeChargeTransferData]
        if _transfer_data is None:
            transfer_data = None
        elif isinstance(_transfer_data, Unset):
            transfer_data = UNSET
        else:
            transfer_data = DjStripeChargeTransferData.from_dict(_transfer_data)

        transfer_group = d.pop("transfer_group", UNSET)

        djstripe_owner_account = d.pop("djstripe_owner_account", UNSET)

        application_fee = d.pop("application_fee", UNSET)

        balance_transaction = d.pop("balance_transaction", UNSET)

        customer = d.pop("customer", UNSET)

        dispute = d.pop("dispute", UNSET)

        invoice = d.pop("invoice", UNSET)

        on_behalf_of = d.pop("on_behalf_of", UNSET)

        payment_intent = d.pop("payment_intent", UNSET)

        payment_method = d.pop("payment_method", UNSET)

        source = d.pop("source", UNSET)

        source_transfer = d.pop("source_transfer", UNSET)

        transfer = d.pop("transfer", UNSET)

        dj_stripe_charge = cls(
            djstripe_id=djstripe_id,
            failure_code=failure_code,
            djstripe_created=djstripe_created,
            djstripe_updated=djstripe_updated,
            id=id,
            amount=amount,
            amount_refunded=amount_refunded,
            currency=currency,
            status=status,
            livemode=livemode,
            created=created,
            metadata=metadata,
            description=description,
            amount_captured=amount_captured,
            application=application,
            application_fee_amount=application_fee_amount,
            billing_details=billing_details,
            calculated_statement_descriptor=calculated_statement_descriptor,
            captured=captured,
            disputed=disputed,
            failure_message=failure_message,
            fraud_details=fraud_details,
            outcome=outcome,
            paid=paid,
            payment_method_details=payment_method_details,
            receipt_email=receipt_email,
            receipt_number=receipt_number,
            receipt_url=receipt_url,
            refunded=refunded,
            shipping=shipping,
            statement_descriptor=statement_descriptor,
            statement_descriptor_suffix=statement_descriptor_suffix,
            transfer_data=transfer_data,
            transfer_group=transfer_group,
            djstripe_owner_account=djstripe_owner_account,
            application_fee=application_fee,
            balance_transaction=balance_transaction,
            customer=customer,
            dispute=dispute,
            invoice=invoice,
            on_behalf_of=on_behalf_of,
            payment_intent=payment_intent,
            payment_method=payment_method,
            source=source,
            source_transfer=source_transfer,
            transfer=transfer,
        )

        dj_stripe_charge.additional_properties = d
        return dj_stripe_charge

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
