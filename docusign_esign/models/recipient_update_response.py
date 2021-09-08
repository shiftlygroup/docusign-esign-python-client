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


class RecipientUpdateResponse(object):
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
        'error_details': 'ErrorDetails',
        'recipient_id': 'str',
        'tabs': 'Tabs'
    }

    attribute_map = {
        'error_details': 'errorDetails',
        'recipient_id': 'recipientId',
        'tabs': 'tabs'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RecipientUpdateResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error_details = None
        self._recipient_id = None
        self._tabs = None
        self.discriminator = None

        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('recipient_id'), kwargs.get('recipient_id', None))
        setattr(self, "_{}".format('tabs'), kwargs.get('tabs', None))

    @property
    def error_details(self):
        """Gets the error_details of this RecipientUpdateResponse.  # noqa: E501


        :return: The error_details of this RecipientUpdateResponse.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this RecipientUpdateResponse.


        :param error_details: The error_details of this RecipientUpdateResponse.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def recipient_id(self):
        """Gets the recipient_id of this RecipientUpdateResponse.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this RecipientUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this RecipientUpdateResponse.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this RecipientUpdateResponse.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def tabs(self):
        """Gets the tabs of this RecipientUpdateResponse.  # noqa: E501


        :return: The tabs of this RecipientUpdateResponse.  # noqa: E501
        :rtype: Tabs
        """
        return self._tabs

    @tabs.setter
    def tabs(self, tabs):
        """Sets the tabs of this RecipientUpdateResponse.


        :param tabs: The tabs of this RecipientUpdateResponse.  # noqa: E501
        :type: Tabs
        """

        self._tabs = tabs

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
        if issubclass(RecipientUpdateResponse, dict):
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
        if not isinstance(other, RecipientUpdateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipientUpdateResponse):
            return True

        return self.to_dict() != other.to_dict()
