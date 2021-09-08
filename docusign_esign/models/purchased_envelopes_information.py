# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class PurchasedEnvelopesInformation(object):
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
        'amount': 'str',
        'app_name': 'str',
        'currency_code': 'str',
        'platform': 'str',
        'product_id': 'str',
        'quantity': 'str',
        'receipt_data': 'str',
        'store_name': 'str',
        'transaction_id': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'app_name': 'appName',
        'currency_code': 'currencyCode',
        'platform': 'platform',
        'product_id': 'productId',
        'quantity': 'quantity',
        'receipt_data': 'receiptData',
        'store_name': 'storeName',
        'transaction_id': 'transactionId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """PurchasedEnvelopesInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._app_name = None
        self._currency_code = None
        self._platform = None
        self._product_id = None
        self._quantity = None
        self._receipt_data = None
        self._store_name = None
        self._transaction_id = None
        self.discriminator = None

        setattr(self, "_{}".format('amount'), kwargs.get('amount', None))
        setattr(self, "_{}".format('app_name'), kwargs.get('app_name', None))
        setattr(self, "_{}".format('currency_code'), kwargs.get('currency_code', None))
        setattr(self, "_{}".format('platform'), kwargs.get('platform', None))
        setattr(self, "_{}".format('product_id'), kwargs.get('product_id', None))
        setattr(self, "_{}".format('quantity'), kwargs.get('quantity', None))
        setattr(self, "_{}".format('receipt_data'), kwargs.get('receipt_data', None))
        setattr(self, "_{}".format('store_name'), kwargs.get('store_name', None))
        setattr(self, "_{}".format('transaction_id'), kwargs.get('transaction_id', None))

    @property
    def amount(self):
        """Gets the amount of this PurchasedEnvelopesInformation.  # noqa: E501

        The total amount of the purchase.  # noqa: E501

        :return: The amount of this PurchasedEnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PurchasedEnvelopesInformation.

        The total amount of the purchase.  # noqa: E501

        :param amount: The amount of this PurchasedEnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def app_name(self):
        """Gets the app_name of this PurchasedEnvelopesInformation.  # noqa: E501

        The AppName of the client application.  # noqa: E501

        :return: The app_name of this PurchasedEnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this PurchasedEnvelopesInformation.

        The AppName of the client application.  # noqa: E501

        :param app_name: The app_name of this PurchasedEnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._app_name = app_name

    @property
    def currency_code(self):
        """Gets the currency_code of this PurchasedEnvelopesInformation.  # noqa: E501

        Specifies the ISO currency code of the purchase. This is based on the ISO 4217 currency code information.  # noqa: E501

        :return: The currency_code of this PurchasedEnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this PurchasedEnvelopesInformation.

        Specifies the ISO currency code of the purchase. This is based on the ISO 4217 currency code information.  # noqa: E501

        :param currency_code: The currency_code of this PurchasedEnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def platform(self):
        """Gets the platform of this PurchasedEnvelopesInformation.  # noqa: E501

        The Platform of the client application  # noqa: E501

        :return: The platform of this PurchasedEnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this PurchasedEnvelopesInformation.

        The Platform of the client application  # noqa: E501

        :param platform: The platform of this PurchasedEnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def product_id(self):
        """Gets the product_id of this PurchasedEnvelopesInformation.  # noqa: E501

        The Product ID from the AppStore.  # noqa: E501

        :return: The product_id of this PurchasedEnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this PurchasedEnvelopesInformation.

        The Product ID from the AppStore.  # noqa: E501

        :param product_id: The product_id of this PurchasedEnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def quantity(self):
        """Gets the quantity of this PurchasedEnvelopesInformation.  # noqa: E501

        The quantity of envelopes to add to the account.  # noqa: E501

        :return: The quantity of this PurchasedEnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PurchasedEnvelopesInformation.

        The quantity of envelopes to add to the account.  # noqa: E501

        :param quantity: The quantity of this PurchasedEnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._quantity = quantity

    @property
    def receipt_data(self):
        """Gets the receipt_data of this PurchasedEnvelopesInformation.  # noqa: E501

        The encrypted Base64 encoded receipt data.  # noqa: E501

        :return: The receipt_data of this PurchasedEnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._receipt_data

    @receipt_data.setter
    def receipt_data(self, receipt_data):
        """Sets the receipt_data of this PurchasedEnvelopesInformation.

        The encrypted Base64 encoded receipt data.  # noqa: E501

        :param receipt_data: The receipt_data of this PurchasedEnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._receipt_data = receipt_data

    @property
    def store_name(self):
        """Gets the store_name of this PurchasedEnvelopesInformation.  # noqa: E501

        The name of the AppStore.  # noqa: E501

        :return: The store_name of this PurchasedEnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        """Sets the store_name of this PurchasedEnvelopesInformation.

        The name of the AppStore.  # noqa: E501

        :param store_name: The store_name of this PurchasedEnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._store_name = store_name

    @property
    def transaction_id(self):
        """Gets the transaction_id of this PurchasedEnvelopesInformation.  # noqa: E501

        Specifies the Transaction ID from the AppStore.  # noqa: E501

        :return: The transaction_id of this PurchasedEnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this PurchasedEnvelopesInformation.

        Specifies the Transaction ID from the AppStore.  # noqa: E501

        :param transaction_id: The transaction_id of this PurchasedEnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PurchasedEnvelopesInformation, dict):
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
        if not isinstance(other, PurchasedEnvelopesInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PurchasedEnvelopesInformation):
            return True

        return self.to_dict() != other.to_dict()
