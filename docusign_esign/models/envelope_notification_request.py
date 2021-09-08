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


class EnvelopeNotificationRequest(object):
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
        'expirations': 'Expirations',
        'reminders': 'Reminders',
        'use_account_defaults': 'str'
    }

    attribute_map = {
        'expirations': 'expirations',
        'reminders': 'reminders',
        'use_account_defaults': 'useAccountDefaults'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """EnvelopeNotificationRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._expirations = None
        self._reminders = None
        self._use_account_defaults = None
        self.discriminator = None

        setattr(self, "_{}".format('expirations'), kwargs.get('expirations', None))
        setattr(self, "_{}".format('reminders'), kwargs.get('reminders', None))
        setattr(self, "_{}".format('use_account_defaults'), kwargs.get('use_account_defaults', None))

    @property
    def expirations(self):
        """Gets the expirations of this EnvelopeNotificationRequest.  # noqa: E501


        :return: The expirations of this EnvelopeNotificationRequest.  # noqa: E501
        :rtype: Expirations
        """
        return self._expirations

    @expirations.setter
    def expirations(self, expirations):
        """Sets the expirations of this EnvelopeNotificationRequest.


        :param expirations: The expirations of this EnvelopeNotificationRequest.  # noqa: E501
        :type: Expirations
        """

        self._expirations = expirations

    @property
    def reminders(self):
        """Gets the reminders of this EnvelopeNotificationRequest.  # noqa: E501


        :return: The reminders of this EnvelopeNotificationRequest.  # noqa: E501
        :rtype: Reminders
        """
        return self._reminders

    @reminders.setter
    def reminders(self, reminders):
        """Sets the reminders of this EnvelopeNotificationRequest.


        :param reminders: The reminders of this EnvelopeNotificationRequest.  # noqa: E501
        :type: Reminders
        """

        self._reminders = reminders

    @property
    def use_account_defaults(self):
        """Gets the use_account_defaults of this EnvelopeNotificationRequest.  # noqa: E501

          # noqa: E501

        :return: The use_account_defaults of this EnvelopeNotificationRequest.  # noqa: E501
        :rtype: str
        """
        return self._use_account_defaults

    @use_account_defaults.setter
    def use_account_defaults(self, use_account_defaults):
        """Sets the use_account_defaults of this EnvelopeNotificationRequest.

          # noqa: E501

        :param use_account_defaults: The use_account_defaults of this EnvelopeNotificationRequest.  # noqa: E501
        :type: str
        """

        self._use_account_defaults = use_account_defaults

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
        if issubclass(EnvelopeNotificationRequest, dict):
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
        if not isinstance(other, EnvelopeNotificationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvelopeNotificationRequest):
            return True

        return self.to_dict() != other.to_dict()
