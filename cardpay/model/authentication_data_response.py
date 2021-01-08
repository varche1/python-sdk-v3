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

from cardpay.model.authentication_customer import (
    AuthenticationCustomer,
)  # noqa: F401,E501
from cardpay.model.authentication_data import AuthenticationData  # noqa: F401,E501
from cardpay.model.payment_response_card_account import (
    PaymentResponseCardAccount,
)  # noqa: F401,E501
from cardpay.model.transaction_response_merchant_order import (
    TransactionResponseMerchantOrder,
)  # noqa: F401,E501


class AuthenticationDataResponse(object):
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
    swagger_types = {
        "merchant_order": "TransactionResponseMerchantOrder",
        "payment_method": "str",
        "authentication_data": "AuthenticationData",
        "card_account": "PaymentResponseCardAccount",
        "customer": "AuthenticationCustomer",
    }

    attribute_map = {
        "merchant_order": "merchant_order",
        "payment_method": "payment_method",
        "authentication_data": "authentication_data",
        "card_account": "card_account",
        "customer": "customer",
    }

    def __init__(
        self,
        merchant_order=None,
        payment_method=None,
        authentication_data=None,
        card_account=None,
        customer=None,
    ):  # noqa: E501
        """AuthenticationDataResponse - a model defined in Swagger"""  # noqa: E501

        self._merchant_order = None
        self._payment_method = None
        self._authentication_data = None
        self._card_account = None
        self._customer = None
        self.discriminator = None

        if merchant_order is not None:
            self.merchant_order = merchant_order
        if payment_method is not None:
            self.payment_method = payment_method
        if authentication_data is not None:
            self.authentication_data = authentication_data
        if card_account is not None:
            self.card_account = card_account
        if customer is not None:
            self.customer = customer

    @property
    def merchant_order(self):
        """Gets the merchant_order of this AuthenticationDataResponse.  # noqa: E501

        Merchant order data  # noqa: E501

        :return: The merchant_order of this AuthenticationDataResponse.  # noqa: E501
        :rtype: TransactionResponseMerchantOrder
        """
        return self._merchant_order

    @merchant_order.setter
    def merchant_order(self, merchant_order):
        """Sets the merchant_order of this AuthenticationDataResponse.

        Merchant order data  # noqa: E501

        :param merchant_order: The merchant_order of this AuthenticationDataResponse.  # noqa: E501
        :type: TransactionResponseMerchantOrder
        """

        self._merchant_order = merchant_order

    @property
    def payment_method(self):
        """Gets the payment_method of this AuthenticationDataResponse.  # noqa: E501

        Used payment method type name from payment methods list  # noqa: E501

        :return: The payment_method of this AuthenticationDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this AuthenticationDataResponse.

        Used payment method type name from payment methods list  # noqa: E501

        :param payment_method: The payment_method of this AuthenticationDataResponse.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def authentication_data(self):
        """Gets the authentication_data of this AuthenticationDataResponse.  # noqa: E501

        Payment authentication data  # noqa: E501

        :return: The authentication_data of this AuthenticationDataResponse.  # noqa: E501
        :rtype: AuthenticationData
        """
        return self._authentication_data

    @authentication_data.setter
    def authentication_data(self, authentication_data):
        """Sets the authentication_data of this AuthenticationDataResponse.

        Payment authentication data  # noqa: E501

        :param authentication_data: The authentication_data of this AuthenticationDataResponse.  # noqa: E501
        :type: AuthenticationData
        """

        self._authentication_data = authentication_data

    @property
    def card_account(self):
        """Gets the card_account of this AuthenticationDataResponse.  # noqa: E501

        Bank card data *(for BANKCARD payment method only)*  # noqa: E501

        :return: The card_account of this AuthenticationDataResponse.  # noqa: E501
        :rtype: PaymentResponseCardAccount
        """
        return self._card_account

    @card_account.setter
    def card_account(self, card_account):
        """Sets the card_account of this AuthenticationDataResponse.

        Bank card data *(for BANKCARD payment method only)*  # noqa: E501

        :param card_account: The card_account of this AuthenticationDataResponse.  # noqa: E501
        :type: PaymentResponseCardAccount
        """

        self._card_account = card_account

    @property
    def customer(self):
        """Gets the customer of this AuthenticationDataResponse.  # noqa: E501

        Customer data  # noqa: E501

        :return: The customer of this AuthenticationDataResponse.  # noqa: E501
        :rtype: AuthenticationCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this AuthenticationDataResponse.

        Customer data  # noqa: E501

        :param customer: The customer of this AuthenticationDataResponse.  # noqa: E501
        :type: AuthenticationCustomer
        """

        self._customer = customer

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
        if issubclass(AuthenticationDataResponse, dict):
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
        if not isinstance(other, AuthenticationDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
