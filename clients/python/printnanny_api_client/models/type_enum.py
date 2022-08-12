# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.100.9
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


class TypeEnum(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ACSS_DEBIT = "acss_debit"
    AFTERPAY_CLEARPAY = "afterpay_clearpay"
    ALIPAY = "alipay"
    AU_BECS_DEBIT = "au_becs_debit"
    BACS_DEBIT = "bacs_debit"
    BANCONTACT = "bancontact"
    BOLETO = "boleto"
    CARD = "card"
    CARD_PRESENT = "card_present"
    EPS = "eps"
    FPX = "fpx"
    GIROPAY = "giropay"
    GRABPAY = "grabpay"
    IDEAL = "ideal"
    INTERAC_PRESENT = "interac_present"
    KLARNA = "klarna"
    OXXO = "oxxo"
    P24 = "p24"
    SEPA_DEBIT = "sepa_debit"
    SOFORT = "sofort"
    WECHAT_PAY = "wechat_pay"

    allowable_values = [ACSS_DEBIT, AFTERPAY_CLEARPAY, ALIPAY, AU_BECS_DEBIT, BACS_DEBIT, BANCONTACT, BOLETO, CARD, CARD_PRESENT, EPS, FPX, GIROPAY, GRABPAY, IDEAL, INTERAC_PRESENT, KLARNA, OXXO, P24, SEPA_DEBIT, SOFORT, WECHAT_PAY]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """TypeEnum - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, TypeEnum):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypeEnum):
            return True

        return self.to_dict() != other.to_dict()
