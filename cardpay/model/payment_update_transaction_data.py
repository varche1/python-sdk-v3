# coding: utf-8

"""
    CardPay REST API

    Welcome to the CardPay REST API. The CardPay API uses HTTP verbs and a [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) resources endpoint structure (see more info about REST). Request and response payloads are formatted as JSON. Merchant uses API to create payments, refunds, payouts or recurrings, check or update transaction status and get information about created transactions. In API authentication process based on [OAuth 2.0](https://oauth.net/2/) standard. For recent changes see changelog section.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PaymentUpdateTransactionData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"amount": "float", "status_to": "str"}

    attribute_map = {"amount": "amount", "status_to": "status_to"}

    def __init__(self, amount=None, status_to=None):  # noqa: E501
        """PaymentUpdateTransactionData - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._status_to = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if status_to is not None:
            self.status_to = status_to

    @property
    def amount(self):
        """Gets the amount of this PaymentUpdateTransactionData.  # noqa: E501

        The total transaction amount in selected currency with dot as a decimal separator, must be less than 100 millions  # noqa: E501

        :return: The amount of this PaymentUpdateTransactionData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentUpdateTransactionData.

        The total transaction amount in selected currency with dot as a decimal separator, must be less than 100 millions  # noqa: E501

        :param amount: The amount of this PaymentUpdateTransactionData.  # noqa: E501
        :type: float
        """

        self._amount = amount

    class StatusTo(object):
        REVERSE = "REVERSE"
        COMPLETE = "COMPLETE"
        TERMINATE = "TERMINATE"

    @property
    def status_to(self):
        """Gets the status_to of this PaymentUpdateTransactionData.  # noqa: E501

        Payment, one-click recurring: `COMPLETE` or `REVERSE` status to be set. Refund, payout: `REVERSE` status to be set.  # noqa: E501

        :return: The status_to of this PaymentUpdateTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._status_to

    @status_to.setter
    def status_to(self, status_to):
        """Sets the status_to of this PaymentUpdateTransactionData.

        Payment, one-click recurring: `COMPLETE` or `REVERSE` status to be set. Refund, payout: `REVERSE` status to be set.  # noqa: E501

        :param status_to: The status_to of this PaymentUpdateTransactionData.  # noqa: E501
        :type: str
        """
        allowed_values = ["REVERSE", "COMPLETE", "TERMINATE"]  # noqa: E501
        if status_to not in allowed_values:
            raise ValueError(
                "Invalid value for `status_to` ({0}), must be one of {1}".format(  # noqa: E501
                    status_to, allowed_values
                )
            )

        self._status_to = status_to

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                if value is not None:
                    result[attr] = value
        if issubclass(PaymentUpdateTransactionData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentUpdateTransactionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
