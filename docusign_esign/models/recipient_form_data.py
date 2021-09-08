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


class RecipientFormData(object):
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
        'declined_time': 'str',
        'delivered_time': 'str',
        'email': 'str',
        'form_data': 'list[NameValue]',
        'name': 'str',
        'recipient_id': 'str',
        'sent_time': 'str',
        'signed_time': 'str'
    }

    attribute_map = {
        'declined_time': 'declinedTime',
        'delivered_time': 'deliveredTime',
        'email': 'email',
        'form_data': 'formData',
        'name': 'name',
        'recipient_id': 'recipientId',
        'sent_time': 'sentTime',
        'signed_time': 'signedTime'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RecipientFormData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._declined_time = None
        self._delivered_time = None
        self._email = None
        self._form_data = None
        self._name = None
        self._recipient_id = None
        self._sent_time = None
        self._signed_time = None
        self.discriminator = None

        setattr(self, "_{}".format('declined_time'), kwargs.get('declined_time', None))
        setattr(self, "_{}".format('delivered_time'), kwargs.get('delivered_time', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('form_data'), kwargs.get('form_data', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('recipient_id'), kwargs.get('recipient_id', None))
        setattr(self, "_{}".format('sent_time'), kwargs.get('sent_time', None))
        setattr(self, "_{}".format('signed_time'), kwargs.get('signed_time', None))

    @property
    def declined_time(self):
        """Gets the declined_time of this RecipientFormData.  # noqa: E501

          # noqa: E501

        :return: The declined_time of this RecipientFormData.  # noqa: E501
        :rtype: str
        """
        return self._declined_time

    @declined_time.setter
    def declined_time(self, declined_time):
        """Sets the declined_time of this RecipientFormData.

          # noqa: E501

        :param declined_time: The declined_time of this RecipientFormData.  # noqa: E501
        :type: str
        """

        self._declined_time = declined_time

    @property
    def delivered_time(self):
        """Gets the delivered_time of this RecipientFormData.  # noqa: E501

          # noqa: E501

        :return: The delivered_time of this RecipientFormData.  # noqa: E501
        :rtype: str
        """
        return self._delivered_time

    @delivered_time.setter
    def delivered_time(self, delivered_time):
        """Sets the delivered_time of this RecipientFormData.

          # noqa: E501

        :param delivered_time: The delivered_time of this RecipientFormData.  # noqa: E501
        :type: str
        """

        self._delivered_time = delivered_time

    @property
    def email(self):
        """Gets the email of this RecipientFormData.  # noqa: E501

          # noqa: E501

        :return: The email of this RecipientFormData.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RecipientFormData.

          # noqa: E501

        :param email: The email of this RecipientFormData.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def form_data(self):
        """Gets the form_data of this RecipientFormData.  # noqa: E501

          # noqa: E501

        :return: The form_data of this RecipientFormData.  # noqa: E501
        :rtype: list[NameValue]
        """
        return self._form_data

    @form_data.setter
    def form_data(self, form_data):
        """Sets the form_data of this RecipientFormData.

          # noqa: E501

        :param form_data: The form_data of this RecipientFormData.  # noqa: E501
        :type: list[NameValue]
        """

        self._form_data = form_data

    @property
    def name(self):
        """Gets the name of this RecipientFormData.  # noqa: E501

          # noqa: E501

        :return: The name of this RecipientFormData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecipientFormData.

          # noqa: E501

        :param name: The name of this RecipientFormData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def recipient_id(self):
        """Gets the recipient_id of this RecipientFormData.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this RecipientFormData.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this RecipientFormData.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this RecipientFormData.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def sent_time(self):
        """Gets the sent_time of this RecipientFormData.  # noqa: E501

          # noqa: E501

        :return: The sent_time of this RecipientFormData.  # noqa: E501
        :rtype: str
        """
        return self._sent_time

    @sent_time.setter
    def sent_time(self, sent_time):
        """Sets the sent_time of this RecipientFormData.

          # noqa: E501

        :param sent_time: The sent_time of this RecipientFormData.  # noqa: E501
        :type: str
        """

        self._sent_time = sent_time

    @property
    def signed_time(self):
        """Gets the signed_time of this RecipientFormData.  # noqa: E501

          # noqa: E501

        :return: The signed_time of this RecipientFormData.  # noqa: E501
        :rtype: str
        """
        return self._signed_time

    @signed_time.setter
    def signed_time(self, signed_time):
        """Sets the signed_time of this RecipientFormData.

          # noqa: E501

        :param signed_time: The signed_time of this RecipientFormData.  # noqa: E501
        :type: str
        """

        self._signed_time = signed_time

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
        if issubclass(RecipientFormData, dict):
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
        if not isinstance(other, RecipientFormData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipientFormData):
            return True

        return self.to_dict() != other.to_dict()
