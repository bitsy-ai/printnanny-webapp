# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.100.3
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from printnanny_api_client.configuration import Configuration


class StripePaymentMethod(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'djstripe_id': 'int',
        'djstripe_created': 'datetime',
        'djstripe_updated': 'datetime',
        'id': 'str',
        'livemode': 'bool',
        'created': 'datetime',
        'metadata': 'dict(str, object)',
        'billing_details': 'dict(str, object)',
        'type': 'TypeEnum',
        'acss_debit': 'dict(str, object)',
        'afterpay_clearpay': 'dict(str, object)',
        'alipay': 'dict(str, object)',
        'au_becs_debit': 'dict(str, object)',
        'bacs_debit': 'dict(str, object)',
        'bancontact': 'dict(str, object)',
        'boleto': 'dict(str, object)',
        'card': 'dict(str, object)',
        'card_present': 'dict(str, object)',
        'eps': 'dict(str, object)',
        'fpx': 'dict(str, object)',
        'giropay': 'dict(str, object)',
        'grabpay': 'dict(str, object)',
        'ideal': 'dict(str, object)',
        'interac_present': 'dict(str, object)',
        'oxxo': 'dict(str, object)',
        'p24': 'dict(str, object)',
        'sepa_debit': 'dict(str, object)',
        'sofort': 'dict(str, object)',
        'wechat_pay': 'dict(str, object)',
        'djstripe_owner_account': 'str',
        'customer': 'str'
    }

    attribute_map = {
        'djstripe_id': 'djstripe_id',
        'djstripe_created': 'djstripe_created',
        'djstripe_updated': 'djstripe_updated',
        'id': 'id',
        'livemode': 'livemode',
        'created': 'created',
        'metadata': 'metadata',
        'billing_details': 'billing_details',
        'type': 'type',
        'acss_debit': 'acss_debit',
        'afterpay_clearpay': 'afterpay_clearpay',
        'alipay': 'alipay',
        'au_becs_debit': 'au_becs_debit',
        'bacs_debit': 'bacs_debit',
        'bancontact': 'bancontact',
        'boleto': 'boleto',
        'card': 'card',
        'card_present': 'card_present',
        'eps': 'eps',
        'fpx': 'fpx',
        'giropay': 'giropay',
        'grabpay': 'grabpay',
        'ideal': 'ideal',
        'interac_present': 'interac_present',
        'oxxo': 'oxxo',
        'p24': 'p24',
        'sepa_debit': 'sepa_debit',
        'sofort': 'sofort',
        'wechat_pay': 'wechat_pay',
        'djstripe_owner_account': 'djstripe_owner_account',
        'customer': 'customer'
    }

    def __init__(self, djstripe_id=None, djstripe_created=None, djstripe_updated=None, id=None, livemode=None, created=None, metadata=None, billing_details=None, type=None, acss_debit=None, afterpay_clearpay=None, alipay=None, au_becs_debit=None, bacs_debit=None, bancontact=None, boleto=None, card=None, card_present=None, eps=None, fpx=None, giropay=None, grabpay=None, ideal=None, interac_present=None, oxxo=None, p24=None, sepa_debit=None, sofort=None, wechat_pay=None, djstripe_owner_account=None, customer=None, local_vars_configuration=None):  # noqa: E501
        """StripePaymentMethod - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._djstripe_id = None
        self._djstripe_created = None
        self._djstripe_updated = None
        self._id = None
        self._livemode = None
        self._created = None
        self._metadata = None
        self._billing_details = None
        self._type = None
        self._acss_debit = None
        self._afterpay_clearpay = None
        self._alipay = None
        self._au_becs_debit = None
        self._bacs_debit = None
        self._bancontact = None
        self._boleto = None
        self._card = None
        self._card_present = None
        self._eps = None
        self._fpx = None
        self._giropay = None
        self._grabpay = None
        self._ideal = None
        self._interac_present = None
        self._oxxo = None
        self._p24 = None
        self._sepa_debit = None
        self._sofort = None
        self._wechat_pay = None
        self._djstripe_owner_account = None
        self._customer = None
        self.discriminator = None

        self.djstripe_id = djstripe_id
        self.djstripe_created = djstripe_created
        self.djstripe_updated = djstripe_updated
        self.id = id
        self.livemode = livemode
        self.created = created
        self.metadata = metadata
        self.billing_details = billing_details
        self.type = type
        self.acss_debit = acss_debit
        self.afterpay_clearpay = afterpay_clearpay
        self.alipay = alipay
        self.au_becs_debit = au_becs_debit
        self.bacs_debit = bacs_debit
        self.bancontact = bancontact
        self.boleto = boleto
        self.card = card
        self.card_present = card_present
        self.eps = eps
        self.fpx = fpx
        self.giropay = giropay
        self.grabpay = grabpay
        self.ideal = ideal
        self.interac_present = interac_present
        self.oxxo = oxxo
        self.p24 = p24
        self.sepa_debit = sepa_debit
        self.sofort = sofort
        self.wechat_pay = wechat_pay
        self.djstripe_owner_account = djstripe_owner_account
        self.customer = customer

    @property
    def djstripe_id(self):
        """Gets the djstripe_id of this StripePaymentMethod.  # noqa: E501


        :return: The djstripe_id of this StripePaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._djstripe_id

    @djstripe_id.setter
    def djstripe_id(self, djstripe_id):
        """Sets the djstripe_id of this StripePaymentMethod.


        :param djstripe_id: The djstripe_id of this StripePaymentMethod.  # noqa: E501
        :type djstripe_id: int
        """
        if self.local_vars_configuration.client_side_validation and djstripe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_id`, must not be `None`")  # noqa: E501

        self._djstripe_id = djstripe_id

    @property
    def djstripe_created(self):
        """Gets the djstripe_created of this StripePaymentMethod.  # noqa: E501


        :return: The djstripe_created of this StripePaymentMethod.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_created

    @djstripe_created.setter
    def djstripe_created(self, djstripe_created):
        """Sets the djstripe_created of this StripePaymentMethod.


        :param djstripe_created: The djstripe_created of this StripePaymentMethod.  # noqa: E501
        :type djstripe_created: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_created is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_created`, must not be `None`")  # noqa: E501

        self._djstripe_created = djstripe_created

    @property
    def djstripe_updated(self):
        """Gets the djstripe_updated of this StripePaymentMethod.  # noqa: E501


        :return: The djstripe_updated of this StripePaymentMethod.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_updated

    @djstripe_updated.setter
    def djstripe_updated(self, djstripe_updated):
        """Sets the djstripe_updated of this StripePaymentMethod.


        :param djstripe_updated: The djstripe_updated of this StripePaymentMethod.  # noqa: E501
        :type djstripe_updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_updated`, must not be `None`")  # noqa: E501

        self._djstripe_updated = djstripe_updated

    @property
    def id(self):
        """Gets the id of this StripePaymentMethod.  # noqa: E501


        :return: The id of this StripePaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StripePaymentMethod.


        :param id: The id of this StripePaymentMethod.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 255):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501

        self._id = id

    @property
    def livemode(self):
        """Gets the livemode of this StripePaymentMethod.  # noqa: E501

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :return: The livemode of this StripePaymentMethod.  # noqa: E501
        :rtype: bool
        """
        return self._livemode

    @livemode.setter
    def livemode(self, livemode):
        """Sets the livemode of this StripePaymentMethod.

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :param livemode: The livemode of this StripePaymentMethod.  # noqa: E501
        :type livemode: bool
        """

        self._livemode = livemode

    @property
    def created(self):
        """Gets the created of this StripePaymentMethod.  # noqa: E501

        The datetime this object was created in stripe.  # noqa: E501

        :return: The created of this StripePaymentMethod.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this StripePaymentMethod.

        The datetime this object was created in stripe.  # noqa: E501

        :param created: The created of this StripePaymentMethod.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def metadata(self):
        """Gets the metadata of this StripePaymentMethod.  # noqa: E501

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :return: The metadata of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this StripePaymentMethod.

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :param metadata: The metadata of this StripePaymentMethod.  # noqa: E501
        :type metadata: dict(str, object)
        """

        self._metadata = metadata

    @property
    def billing_details(self):
        """Gets the billing_details of this StripePaymentMethod.  # noqa: E501

        Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.  # noqa: E501

        :return: The billing_details of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._billing_details

    @billing_details.setter
    def billing_details(self, billing_details):
        """Sets the billing_details of this StripePaymentMethod.

        Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.  # noqa: E501

        :param billing_details: The billing_details of this StripePaymentMethod.  # noqa: E501
        :type billing_details: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and billing_details is None:  # noqa: E501
            raise ValueError("Invalid value for `billing_details`, must not be `None`")  # noqa: E501

        self._billing_details = billing_details

    @property
    def type(self):
        """Gets the type of this StripePaymentMethod.  # noqa: E501

        The type of the PaymentMethod.  # noqa: E501

        :return: The type of this StripePaymentMethod.  # noqa: E501
        :rtype: TypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StripePaymentMethod.

        The type of the PaymentMethod.  # noqa: E501

        :param type: The type of this StripePaymentMethod.  # noqa: E501
        :type type: TypeEnum
        """

        self._type = type

    @property
    def acss_debit(self):
        """Gets the acss_debit of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `acss_debit`  # noqa: E501

        :return: The acss_debit of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._acss_debit

    @acss_debit.setter
    def acss_debit(self, acss_debit):
        """Sets the acss_debit of this StripePaymentMethod.

        Additional information for payment methods of type `acss_debit`  # noqa: E501

        :param acss_debit: The acss_debit of this StripePaymentMethod.  # noqa: E501
        :type acss_debit: dict(str, object)
        """

        self._acss_debit = acss_debit

    @property
    def afterpay_clearpay(self):
        """Gets the afterpay_clearpay of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `afterpay_clearpay`  # noqa: E501

        :return: The afterpay_clearpay of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._afterpay_clearpay

    @afterpay_clearpay.setter
    def afterpay_clearpay(self, afterpay_clearpay):
        """Sets the afterpay_clearpay of this StripePaymentMethod.

        Additional information for payment methods of type `afterpay_clearpay`  # noqa: E501

        :param afterpay_clearpay: The afterpay_clearpay of this StripePaymentMethod.  # noqa: E501
        :type afterpay_clearpay: dict(str, object)
        """

        self._afterpay_clearpay = afterpay_clearpay

    @property
    def alipay(self):
        """Gets the alipay of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `alipay`  # noqa: E501

        :return: The alipay of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._alipay

    @alipay.setter
    def alipay(self, alipay):
        """Sets the alipay of this StripePaymentMethod.

        Additional information for payment methods of type `alipay`  # noqa: E501

        :param alipay: The alipay of this StripePaymentMethod.  # noqa: E501
        :type alipay: dict(str, object)
        """

        self._alipay = alipay

    @property
    def au_becs_debit(self):
        """Gets the au_becs_debit of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `au_becs_debit`  # noqa: E501

        :return: The au_becs_debit of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._au_becs_debit

    @au_becs_debit.setter
    def au_becs_debit(self, au_becs_debit):
        """Sets the au_becs_debit of this StripePaymentMethod.

        Additional information for payment methods of type `au_becs_debit`  # noqa: E501

        :param au_becs_debit: The au_becs_debit of this StripePaymentMethod.  # noqa: E501
        :type au_becs_debit: dict(str, object)
        """

        self._au_becs_debit = au_becs_debit

    @property
    def bacs_debit(self):
        """Gets the bacs_debit of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `bacs_debit`  # noqa: E501

        :return: The bacs_debit of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._bacs_debit

    @bacs_debit.setter
    def bacs_debit(self, bacs_debit):
        """Sets the bacs_debit of this StripePaymentMethod.

        Additional information for payment methods of type `bacs_debit`  # noqa: E501

        :param bacs_debit: The bacs_debit of this StripePaymentMethod.  # noqa: E501
        :type bacs_debit: dict(str, object)
        """

        self._bacs_debit = bacs_debit

    @property
    def bancontact(self):
        """Gets the bancontact of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `bancontact`  # noqa: E501

        :return: The bancontact of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._bancontact

    @bancontact.setter
    def bancontact(self, bancontact):
        """Sets the bancontact of this StripePaymentMethod.

        Additional information for payment methods of type `bancontact`  # noqa: E501

        :param bancontact: The bancontact of this StripePaymentMethod.  # noqa: E501
        :type bancontact: dict(str, object)
        """

        self._bancontact = bancontact

    @property
    def boleto(self):
        """Gets the boleto of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `boleto`  # noqa: E501

        :return: The boleto of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._boleto

    @boleto.setter
    def boleto(self, boleto):
        """Sets the boleto of this StripePaymentMethod.

        Additional information for payment methods of type `boleto`  # noqa: E501

        :param boleto: The boleto of this StripePaymentMethod.  # noqa: E501
        :type boleto: dict(str, object)
        """

        self._boleto = boleto

    @property
    def card(self):
        """Gets the card of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `card`  # noqa: E501

        :return: The card of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this StripePaymentMethod.

        Additional information for payment methods of type `card`  # noqa: E501

        :param card: The card of this StripePaymentMethod.  # noqa: E501
        :type card: dict(str, object)
        """

        self._card = card

    @property
    def card_present(self):
        """Gets the card_present of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `card_present`  # noqa: E501

        :return: The card_present of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._card_present

    @card_present.setter
    def card_present(self, card_present):
        """Sets the card_present of this StripePaymentMethod.

        Additional information for payment methods of type `card_present`  # noqa: E501

        :param card_present: The card_present of this StripePaymentMethod.  # noqa: E501
        :type card_present: dict(str, object)
        """

        self._card_present = card_present

    @property
    def eps(self):
        """Gets the eps of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `eps`  # noqa: E501

        :return: The eps of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._eps

    @eps.setter
    def eps(self, eps):
        """Sets the eps of this StripePaymentMethod.

        Additional information for payment methods of type `eps`  # noqa: E501

        :param eps: The eps of this StripePaymentMethod.  # noqa: E501
        :type eps: dict(str, object)
        """

        self._eps = eps

    @property
    def fpx(self):
        """Gets the fpx of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `fpx`  # noqa: E501

        :return: The fpx of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._fpx

    @fpx.setter
    def fpx(self, fpx):
        """Sets the fpx of this StripePaymentMethod.

        Additional information for payment methods of type `fpx`  # noqa: E501

        :param fpx: The fpx of this StripePaymentMethod.  # noqa: E501
        :type fpx: dict(str, object)
        """

        self._fpx = fpx

    @property
    def giropay(self):
        """Gets the giropay of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `giropay`  # noqa: E501

        :return: The giropay of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._giropay

    @giropay.setter
    def giropay(self, giropay):
        """Sets the giropay of this StripePaymentMethod.

        Additional information for payment methods of type `giropay`  # noqa: E501

        :param giropay: The giropay of this StripePaymentMethod.  # noqa: E501
        :type giropay: dict(str, object)
        """

        self._giropay = giropay

    @property
    def grabpay(self):
        """Gets the grabpay of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `grabpay`  # noqa: E501

        :return: The grabpay of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._grabpay

    @grabpay.setter
    def grabpay(self, grabpay):
        """Sets the grabpay of this StripePaymentMethod.

        Additional information for payment methods of type `grabpay`  # noqa: E501

        :param grabpay: The grabpay of this StripePaymentMethod.  # noqa: E501
        :type grabpay: dict(str, object)
        """

        self._grabpay = grabpay

    @property
    def ideal(self):
        """Gets the ideal of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `ideal`  # noqa: E501

        :return: The ideal of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._ideal

    @ideal.setter
    def ideal(self, ideal):
        """Sets the ideal of this StripePaymentMethod.

        Additional information for payment methods of type `ideal`  # noqa: E501

        :param ideal: The ideal of this StripePaymentMethod.  # noqa: E501
        :type ideal: dict(str, object)
        """

        self._ideal = ideal

    @property
    def interac_present(self):
        """Gets the interac_present of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `interac_present`  # noqa: E501

        :return: The interac_present of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._interac_present

    @interac_present.setter
    def interac_present(self, interac_present):
        """Sets the interac_present of this StripePaymentMethod.

        Additional information for payment methods of type `interac_present`  # noqa: E501

        :param interac_present: The interac_present of this StripePaymentMethod.  # noqa: E501
        :type interac_present: dict(str, object)
        """

        self._interac_present = interac_present

    @property
    def oxxo(self):
        """Gets the oxxo of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `oxxo`  # noqa: E501

        :return: The oxxo of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._oxxo

    @oxxo.setter
    def oxxo(self, oxxo):
        """Sets the oxxo of this StripePaymentMethod.

        Additional information for payment methods of type `oxxo`  # noqa: E501

        :param oxxo: The oxxo of this StripePaymentMethod.  # noqa: E501
        :type oxxo: dict(str, object)
        """

        self._oxxo = oxxo

    @property
    def p24(self):
        """Gets the p24 of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `p24`  # noqa: E501

        :return: The p24 of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._p24

    @p24.setter
    def p24(self, p24):
        """Sets the p24 of this StripePaymentMethod.

        Additional information for payment methods of type `p24`  # noqa: E501

        :param p24: The p24 of this StripePaymentMethod.  # noqa: E501
        :type p24: dict(str, object)
        """

        self._p24 = p24

    @property
    def sepa_debit(self):
        """Gets the sepa_debit of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `sepa_debit`  # noqa: E501

        :return: The sepa_debit of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._sepa_debit

    @sepa_debit.setter
    def sepa_debit(self, sepa_debit):
        """Sets the sepa_debit of this StripePaymentMethod.

        Additional information for payment methods of type `sepa_debit`  # noqa: E501

        :param sepa_debit: The sepa_debit of this StripePaymentMethod.  # noqa: E501
        :type sepa_debit: dict(str, object)
        """

        self._sepa_debit = sepa_debit

    @property
    def sofort(self):
        """Gets the sofort of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `sofort`  # noqa: E501

        :return: The sofort of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._sofort

    @sofort.setter
    def sofort(self, sofort):
        """Sets the sofort of this StripePaymentMethod.

        Additional information for payment methods of type `sofort`  # noqa: E501

        :param sofort: The sofort of this StripePaymentMethod.  # noqa: E501
        :type sofort: dict(str, object)
        """

        self._sofort = sofort

    @property
    def wechat_pay(self):
        """Gets the wechat_pay of this StripePaymentMethod.  # noqa: E501

        Additional information for payment methods of type `wechat_pay`  # noqa: E501

        :return: The wechat_pay of this StripePaymentMethod.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._wechat_pay

    @wechat_pay.setter
    def wechat_pay(self, wechat_pay):
        """Sets the wechat_pay of this StripePaymentMethod.

        Additional information for payment methods of type `wechat_pay`  # noqa: E501

        :param wechat_pay: The wechat_pay of this StripePaymentMethod.  # noqa: E501
        :type wechat_pay: dict(str, object)
        """

        self._wechat_pay = wechat_pay

    @property
    def djstripe_owner_account(self):
        """Gets the djstripe_owner_account of this StripePaymentMethod.  # noqa: E501

        The Stripe Account this object belongs to.  # noqa: E501

        :return: The djstripe_owner_account of this StripePaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._djstripe_owner_account

    @djstripe_owner_account.setter
    def djstripe_owner_account(self, djstripe_owner_account):
        """Sets the djstripe_owner_account of this StripePaymentMethod.

        The Stripe Account this object belongs to.  # noqa: E501

        :param djstripe_owner_account: The djstripe_owner_account of this StripePaymentMethod.  # noqa: E501
        :type djstripe_owner_account: str
        """

        self._djstripe_owner_account = djstripe_owner_account

    @property
    def customer(self):
        """Gets the customer of this StripePaymentMethod.  # noqa: E501

        Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.  # noqa: E501

        :return: The customer of this StripePaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this StripePaymentMethod.

        Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.  # noqa: E501

        :param customer: The customer of this StripePaymentMethod.  # noqa: E501
        :type customer: str
        """

        self._customer = customer

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StripePaymentMethod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StripePaymentMethod):
            return True

        return self.to_dict() != other.to_dict()
