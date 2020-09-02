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

from cardpay.model.authentication_data import AuthenticationData  # noqa: F401,E501
from cardpay.model.payment_request_card_account import (
    PaymentRequestCardAccount,
)  # noqa: F401,E501
from cardpay.model.payment_request_cryptocurrency_account import (
    PaymentRequestCryptocurrencyAccount,
)  # noqa: F401,E501
from cardpay.model.payment_request_customer import (
    PaymentRequestCustomer,
)  # noqa: F401,E501
from cardpay.model.payment_request_e_wallet_account import (
    PaymentRequestEWalletAccount,
)  # noqa: F401,E501
from cardpay.model.payment_request_merchant_order import (
    PaymentRequestMerchantOrder,
)  # noqa: F401,E501
from cardpay.model.payment_request_payment_data import (
    PaymentRequestPaymentData,
)  # noqa: F401,E501
from cardpay.model.request import Request  # noqa: F401,E501
from cardpay.model.return_urls import ReturnUrls  # noqa: F401,E501


class PaymentRequest(object):
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
        "request": "Request",
        "authentication_data": "AuthenticationData",
        "card_account": "PaymentRequestCardAccount",
        "cryptocurrency_account": "PaymentRequestCryptocurrencyAccount",
        "customer": "PaymentRequestCustomer",
        "ewallet_account": "PaymentRequestEWalletAccount",
        "merchant_order": "PaymentRequestMerchantOrder",
        "payment_by_authentication": "bool",
        "payment_data": "PaymentRequestPaymentData",
        "payment_method": "str",
        "payment_methods": "list[str]",
        "return_urls": "ReturnUrls",
    }

    attribute_map = {
        "request": "request",
        "authentication_data": "authentication_data",
        "card_account": "card_account",
        "cryptocurrency_account": "cryptocurrency_account",
        "customer": "customer",
        "ewallet_account": "ewallet_account",
        "merchant_order": "merchant_order",
        "payment_by_authentication": "payment_by_authentication",
        "payment_data": "payment_data",
        "payment_method": "payment_method",
        "payment_methods": "payment_methods",
        "return_urls": "return_urls",
    }

    def __init__(
        self,
        request=None,
        authentication_data=None,
        card_account=None,
        cryptocurrency_account=None,
        customer=None,
        ewallet_account=None,
        merchant_order=None,
        payment_by_authentication=None,
        payment_data=None,
        payment_method=None,
        payment_methods=None,
        return_urls=None,
    ):  # noqa: E501
        """PaymentRequest - a model defined in Swagger"""  # noqa: E501

        self._request = None
        self._authentication_data = None
        self._card_account = None
        self._cryptocurrency_account = None
        self._customer = None
        self._ewallet_account = None
        self._merchant_order = None
        self._payment_by_authentication = None
        self._payment_data = None
        self._payment_method = None
        self._payment_methods = None
        self._return_urls = None
        self.discriminator = None

        self.request = request
        if authentication_data is not None:
            self.authentication_data = authentication_data
        self.card_account = card_account
        if cryptocurrency_account is not None:
            self.cryptocurrency_account = cryptocurrency_account
        self.customer = customer
        if ewallet_account is not None:
            self.ewallet_account = ewallet_account
        self.merchant_order = merchant_order
        if payment_by_authentication is not None:
            self.payment_by_authentication = payment_by_authentication
        self.payment_data = payment_data
        if payment_method is not None:
            self.payment_method = payment_method
        if payment_methods is not None:
            self.payment_methods = payment_methods
        if return_urls is not None:
            self.return_urls = return_urls

    @property
    def request(self):
        """Gets the request of this PaymentRequest.  # noqa: E501

        Request  # noqa: E501

        :return: The request of this PaymentRequest.  # noqa: E501
        :rtype: Request
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this PaymentRequest.

        Request  # noqa: E501

        :param request: The request of this PaymentRequest.  # noqa: E501
        :type: Request
        """
        if request is None:
            raise ValueError(
                "Invalid value for `request`, must not be `None`"
            )  # noqa: E501

        self._request = request

    @property
    def authentication_data(self):
        """Gets the authentication_data of this PaymentRequest.  # noqa: E501

        Authentication data  # noqa: E501

        :return: The authentication_data of this PaymentRequest.  # noqa: E501
        :rtype: AuthenticationData
        """
        return self._authentication_data

    @authentication_data.setter
    def authentication_data(self, authentication_data):
        """Sets the authentication_data of this PaymentRequest.

        Authentication data  # noqa: E501

        :param authentication_data: The authentication_data of this PaymentRequest.  # noqa: E501
        :type: AuthenticationData
        """

        self._authentication_data = authentication_data

    @property
    def card_account(self):
        """Gets the card_account of this PaymentRequest.  # noqa: E501

        Information about card *(for BANKCARD payment method only)*  # noqa: E501

        :return: The card_account of this PaymentRequest.  # noqa: E501
        :rtype: PaymentRequestCardAccount
        """
        return self._card_account

    @card_account.setter
    def card_account(self, card_account):
        """Sets the card_account of this PaymentRequest.

        Information about card *(for BANKCARD payment method only)*  # noqa: E501

        :param card_account: The card_account of this PaymentRequest.  # noqa: E501
        :type: PaymentRequestCardAccount
        """
        if card_account is None:
            raise ValueError(
                "Invalid value for `card_account`, must not be `None`"
            )  # noqa: E501

        self._card_account = card_account

    @property
    def cryptocurrency_account(self):
        """Gets the cryptocurrency_account of this PaymentRequest.  # noqa: E501

        Cryptocurrency data *(for BITCOIN payment method only)*  # noqa: E501

        :return: The cryptocurrency_account of this PaymentRequest.  # noqa: E501
        :rtype: PaymentRequestCryptocurrencyAccount
        """
        return self._cryptocurrency_account

    @cryptocurrency_account.setter
    def cryptocurrency_account(self, cryptocurrency_account):
        """Sets the cryptocurrency_account of this PaymentRequest.

        Cryptocurrency data *(for BITCOIN payment method only)*  # noqa: E501

        :param cryptocurrency_account: The cryptocurrency_account of this PaymentRequest.  # noqa: E501
        :type: PaymentRequestCryptocurrencyAccount
        """

        self._cryptocurrency_account = cryptocurrency_account

    @property
    def customer(self):
        """Gets the customer of this PaymentRequest.  # noqa: E501

        Customer data  # noqa: E501

        :return: The customer of this PaymentRequest.  # noqa: E501
        :rtype: PaymentRequestCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this PaymentRequest.

        Customer data  # noqa: E501

        :param customer: The customer of this PaymentRequest.  # noqa: E501
        :type: PaymentRequestCustomer
        """
        if customer is None:
            raise ValueError(
                "Invalid value for `customer`, must not be `None`"
            )  # noqa: E501

        self._customer = customer

    @property
    def ewallet_account(self):
        """Gets the ewallet_account of this PaymentRequest.  # noqa: E501

        eWallet account data *(for all payment method, excluding BANKCARD, BITCOIN, DIRECTBANKINGEU)  # noqa: E501

        :return: The ewallet_account of this PaymentRequest.  # noqa: E501
        :rtype: PaymentRequestEWalletAccount
        """
        return self._ewallet_account

    @ewallet_account.setter
    def ewallet_account(self, ewallet_account):
        """Sets the ewallet_account of this PaymentRequest.

        eWallet account data *(for all payment method, excluding BANKCARD, BITCOIN, DIRECTBANKINGEU)  # noqa: E501

        :param ewallet_account: The ewallet_account of this PaymentRequest.  # noqa: E501
        :type: PaymentRequestEWalletAccount
        """

        self._ewallet_account = ewallet_account

    @property
    def merchant_order(self):
        """Gets the merchant_order of this PaymentRequest.  # noqa: E501

        Merchant order data  # noqa: E501

        :return: The merchant_order of this PaymentRequest.  # noqa: E501
        :rtype: PaymentRequestMerchantOrder
        """
        return self._merchant_order

    @merchant_order.setter
    def merchant_order(self, merchant_order):
        """Sets the merchant_order of this PaymentRequest.

        Merchant order data  # noqa: E501

        :param merchant_order: The merchant_order of this PaymentRequest.  # noqa: E501
        :type: PaymentRequestMerchantOrder
        """
        if merchant_order is None:
            raise ValueError(
                "Invalid value for `merchant_order`, must not be `None`"
            )  # noqa: E501

        self._merchant_order = merchant_order

    @property
    def payment_by_authentication(self):
        """Gets the payment_by_authentication of this PaymentRequest.  # noqa: E501


        :return: The payment_by_authentication of this PaymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._payment_by_authentication

    @payment_by_authentication.setter
    def payment_by_authentication(self, payment_by_authentication):
        """Sets the payment_by_authentication of this PaymentRequest.


        :param payment_by_authentication: The payment_by_authentication of this PaymentRequest.  # noqa: E501
        :type: bool
        """

        self._payment_by_authentication = payment_by_authentication

    @property
    def payment_data(self):
        """Gets the payment_data of this PaymentRequest.  # noqa: E501

        Payment data  # noqa: E501

        :return: The payment_data of this PaymentRequest.  # noqa: E501
        :rtype: PaymentRequestPaymentData
        """
        return self._payment_data

    @payment_data.setter
    def payment_data(self, payment_data):
        """Sets the payment_data of this PaymentRequest.

        Payment data  # noqa: E501

        :param payment_data: The payment_data of this PaymentRequest.  # noqa: E501
        :type: PaymentRequestPaymentData
        """
        if payment_data is None:
            raise ValueError(
                "Invalid value for `payment_data`, must not be `None`"
            )  # noqa: E501

        self._payment_data = payment_data

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentRequest.  # noqa: E501

        Used payment method type name from payment methods list  # noqa: E501

        :return: The payment_method of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentRequest.

        Used payment method type name from payment methods list  # noqa: E501

        :param payment_method: The payment_method of this PaymentRequest.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def payment_methods(self):
        """Gets the payment_methods of this PaymentRequest.  # noqa: E501

        Array of payment methods to display on Checkout Page. If it is not set then all available methods will be displayed  # noqa: E501

        :return: The payment_methods of this PaymentRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """Sets the payment_methods of this PaymentRequest.

        Array of payment methods to display on Checkout Page. If it is not set then all available methods will be displayed  # noqa: E501

        :param payment_methods: The payment_methods of this PaymentRequest.  # noqa: E501
        :type: list[str]
        """

        self._payment_methods = payment_methods

    @property
    def return_urls(self):
        """Gets the return_urls of this PaymentRequest.  # noqa: E501

        Return URLs are the URLs where Customer returns by pressing 'Back to the shop' or 'Cancel' button in Payment page mode and redirected automatically in Gateway mode  # noqa: E501

        :return: The return_urls of this PaymentRequest.  # noqa: E501
        :rtype: ReturnUrls
        """
        return self._return_urls

    @return_urls.setter
    def return_urls(self, return_urls):
        """Sets the return_urls of this PaymentRequest.

        Return URLs are the URLs where Customer returns by pressing 'Back to the shop' or 'Cancel' button in Payment page mode and redirected automatically in Gateway mode  # noqa: E501

        :param return_urls: The return_urls of this PaymentRequest.  # noqa: E501
        :type: ReturnUrls
        """

        self._return_urls = return_urls

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
        if issubclass(PaymentRequest, dict):
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
        if not isinstance(other, PaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
