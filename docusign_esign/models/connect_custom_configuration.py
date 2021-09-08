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


class ConnectCustomConfiguration(object):
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
        'allow_envelope_publish': 'str',
        'all_users': 'str',
        'configuration_type': 'str',
        'connect_id': 'str',
        'enable_log': 'str',
        'envelope_events': 'str',
        'include_certificate_of_completion': 'str',
        'include_cert_soap_header': 'str',
        'include_document_fields': 'str',
        'include_documents': 'str',
        'include_envelope_void_reason': 'str',
        'include_hmac': 'str',
        'include_sender_accountas_custom_field': 'str',
        'include_time_zone_information': 'str',
        'name': 'str',
        'recipient_events': 'str',
        'requires_acknowledgement': 'str',
        'sign_message_with_x509_certificate': 'str',
        'soap_namespace': 'str',
        'url_to_publish_to': 'str',
        'user_ids': 'str',
        'use_soap_interface': 'str'
    }

    attribute_map = {
        'allow_envelope_publish': 'allowEnvelopePublish',
        'all_users': 'allUsers',
        'configuration_type': 'configurationType',
        'connect_id': 'connectId',
        'enable_log': 'enableLog',
        'envelope_events': 'envelopeEvents',
        'include_certificate_of_completion': 'includeCertificateOfCompletion',
        'include_cert_soap_header': 'includeCertSoapHeader',
        'include_document_fields': 'includeDocumentFields',
        'include_documents': 'includeDocuments',
        'include_envelope_void_reason': 'includeEnvelopeVoidReason',
        'include_hmac': 'includeHMAC',
        'include_sender_accountas_custom_field': 'includeSenderAccountasCustomField',
        'include_time_zone_information': 'includeTimeZoneInformation',
        'name': 'name',
        'recipient_events': 'recipientEvents',
        'requires_acknowledgement': 'requiresAcknowledgement',
        'sign_message_with_x509_certificate': 'signMessageWithX509Certificate',
        'soap_namespace': 'soapNamespace',
        'url_to_publish_to': 'urlToPublishTo',
        'user_ids': 'userIds',
        'use_soap_interface': 'useSoapInterface'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ConnectCustomConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_envelope_publish = None
        self._all_users = None
        self._configuration_type = None
        self._connect_id = None
        self._enable_log = None
        self._envelope_events = None
        self._include_certificate_of_completion = None
        self._include_cert_soap_header = None
        self._include_document_fields = None
        self._include_documents = None
        self._include_envelope_void_reason = None
        self._include_hmac = None
        self._include_sender_accountas_custom_field = None
        self._include_time_zone_information = None
        self._name = None
        self._recipient_events = None
        self._requires_acknowledgement = None
        self._sign_message_with_x509_certificate = None
        self._soap_namespace = None
        self._url_to_publish_to = None
        self._user_ids = None
        self._use_soap_interface = None
        self.discriminator = None

        setattr(self, "_{}".format('allow_envelope_publish'), kwargs.get('allow_envelope_publish', None))
        setattr(self, "_{}".format('all_users'), kwargs.get('all_users', None))
        setattr(self, "_{}".format('configuration_type'), kwargs.get('configuration_type', None))
        setattr(self, "_{}".format('connect_id'), kwargs.get('connect_id', None))
        setattr(self, "_{}".format('enable_log'), kwargs.get('enable_log', None))
        setattr(self, "_{}".format('envelope_events'), kwargs.get('envelope_events', None))
        setattr(self, "_{}".format('include_certificate_of_completion'), kwargs.get('include_certificate_of_completion', None))
        setattr(self, "_{}".format('include_cert_soap_header'), kwargs.get('include_cert_soap_header', None))
        setattr(self, "_{}".format('include_document_fields'), kwargs.get('include_document_fields', None))
        setattr(self, "_{}".format('include_documents'), kwargs.get('include_documents', None))
        setattr(self, "_{}".format('include_envelope_void_reason'), kwargs.get('include_envelope_void_reason', None))
        setattr(self, "_{}".format('include_hmac'), kwargs.get('include_hmac', None))
        setattr(self, "_{}".format('include_sender_accountas_custom_field'), kwargs.get('include_sender_accountas_custom_field', None))
        setattr(self, "_{}".format('include_time_zone_information'), kwargs.get('include_time_zone_information', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('recipient_events'), kwargs.get('recipient_events', None))
        setattr(self, "_{}".format('requires_acknowledgement'), kwargs.get('requires_acknowledgement', None))
        setattr(self, "_{}".format('sign_message_with_x509_certificate'), kwargs.get('sign_message_with_x509_certificate', None))
        setattr(self, "_{}".format('soap_namespace'), kwargs.get('soap_namespace', None))
        setattr(self, "_{}".format('url_to_publish_to'), kwargs.get('url_to_publish_to', None))
        setattr(self, "_{}".format('user_ids'), kwargs.get('user_ids', None))
        setattr(self, "_{}".format('use_soap_interface'), kwargs.get('use_soap_interface', None))

    @property
    def allow_envelope_publish(self):
        """Gets the allow_envelope_publish of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, data is sent to the urlToPublishTo web address. This option can be set to false to stop sending data while maintaining the Connect configuration information.  # noqa: E501

        :return: The allow_envelope_publish of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._allow_envelope_publish

    @allow_envelope_publish.setter
    def allow_envelope_publish(self, allow_envelope_publish):
        """Sets the allow_envelope_publish of this ConnectCustomConfiguration.

        When set to **true**, data is sent to the urlToPublishTo web address. This option can be set to false to stop sending data while maintaining the Connect configuration information.  # noqa: E501

        :param allow_envelope_publish: The allow_envelope_publish of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._allow_envelope_publish = allow_envelope_publish

    @property
    def all_users(self):
        """Gets the all_users of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, the tracked envelope and recipient events for all users, including users that are added a later time, are sent through Connect.  # noqa: E501

        :return: The all_users of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._all_users

    @all_users.setter
    def all_users(self, all_users):
        """Sets the all_users of this ConnectCustomConfiguration.

        When set to **true**, the tracked envelope and recipient events for all users, including users that are added a later time, are sent through Connect.  # noqa: E501

        :param all_users: The all_users of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._all_users = all_users

    @property
    def configuration_type(self):
        """Gets the configuration_type of this ConnectCustomConfiguration.  # noqa: E501

        If merge field's are being used, specifies the type of the merge field. The only  supported value is **salesforce**.  # noqa: E501

        :return: The configuration_type of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._configuration_type

    @configuration_type.setter
    def configuration_type(self, configuration_type):
        """Sets the configuration_type of this ConnectCustomConfiguration.

        If merge field's are being used, specifies the type of the merge field. The only  supported value is **salesforce**.  # noqa: E501

        :param configuration_type: The configuration_type of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._configuration_type = configuration_type

    @property
    def connect_id(self):
        """Gets the connect_id of this ConnectCustomConfiguration.  # noqa: E501

         Specifies the DocuSign generated ID for the Connect configuration.    # noqa: E501

        :return: The connect_id of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._connect_id

    @connect_id.setter
    def connect_id(self, connect_id):
        """Sets the connect_id of this ConnectCustomConfiguration.

         Specifies the DocuSign generated ID for the Connect configuration.    # noqa: E501

        :param connect_id: The connect_id of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._connect_id = connect_id

    @property
    def enable_log(self):
        """Gets the enable_log of this ConnectCustomConfiguration.  # noqa: E501

        This turns Connect logging on or off. When set to **true**, logging is turned on.  # noqa: E501

        :return: The enable_log of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._enable_log

    @enable_log.setter
    def enable_log(self, enable_log):
        """Sets the enable_log of this ConnectCustomConfiguration.

        This turns Connect logging on or off. When set to **true**, logging is turned on.  # noqa: E501

        :param enable_log: The enable_log of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._enable_log = enable_log

    @property
    def envelope_events(self):
        """Gets the envelope_events of this ConnectCustomConfiguration.  # noqa: E501

        A comma separated list of Ã¯Â¿Â½EnvelopeÃ¯Â¿Â½ related events that are tracked through Connect. The possible event values are: Sent, Delivered, Completed, Declined, and Voided.  # noqa: E501

        :return: The envelope_events of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._envelope_events

    @envelope_events.setter
    def envelope_events(self, envelope_events):
        """Sets the envelope_events of this ConnectCustomConfiguration.

        A comma separated list of Ã¯Â¿Â½EnvelopeÃ¯Â¿Â½ related events that are tracked through Connect. The possible event values are: Sent, Delivered, Completed, Declined, and Voided.  # noqa: E501

        :param envelope_events: The envelope_events of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._envelope_events = envelope_events

    @property
    def include_certificate_of_completion(self):
        """Gets the include_certificate_of_completion of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, the Connect Service includes the Certificate of Completion with completed envelopes.   # noqa: E501

        :return: The include_certificate_of_completion of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._include_certificate_of_completion

    @include_certificate_of_completion.setter
    def include_certificate_of_completion(self, include_certificate_of_completion):
        """Sets the include_certificate_of_completion of this ConnectCustomConfiguration.

        When set to **true**, the Connect Service includes the Certificate of Completion with completed envelopes.   # noqa: E501

        :param include_certificate_of_completion: The include_certificate_of_completion of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._include_certificate_of_completion = include_certificate_of_completion

    @property
    def include_cert_soap_header(self):
        """Gets the include_cert_soap_header of this ConnectCustomConfiguration.  # noqa: E501

          # noqa: E501

        :return: The include_cert_soap_header of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._include_cert_soap_header

    @include_cert_soap_header.setter
    def include_cert_soap_header(self, include_cert_soap_header):
        """Sets the include_cert_soap_header of this ConnectCustomConfiguration.

          # noqa: E501

        :param include_cert_soap_header: The include_cert_soap_header of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._include_cert_soap_header = include_cert_soap_header

    @property
    def include_document_fields(self):
        """Gets the include_document_fields of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, the Document Fields associated with envelope documents are included in the data. Document Fields are optional custom name-value pairs added to documents using the API.   # noqa: E501

        :return: The include_document_fields of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._include_document_fields

    @include_document_fields.setter
    def include_document_fields(self, include_document_fields):
        """Sets the include_document_fields of this ConnectCustomConfiguration.

        When set to **true**, the Document Fields associated with envelope documents are included in the data. Document Fields are optional custom name-value pairs added to documents using the API.   # noqa: E501

        :param include_document_fields: The include_document_fields of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._include_document_fields = include_document_fields

    @property
    def include_documents(self):
        """Gets the include_documents of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, Connect will send the PDF document along with the update XML.  # noqa: E501

        :return: The include_documents of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._include_documents

    @include_documents.setter
    def include_documents(self, include_documents):
        """Sets the include_documents of this ConnectCustomConfiguration.

        When set to **true**, Connect will send the PDF document along with the update XML.  # noqa: E501

        :param include_documents: The include_documents of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._include_documents = include_documents

    @property
    def include_envelope_void_reason(self):
        """Gets the include_envelope_void_reason of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, Connect will include the voidedReason for voided envelopes.  # noqa: E501

        :return: The include_envelope_void_reason of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._include_envelope_void_reason

    @include_envelope_void_reason.setter
    def include_envelope_void_reason(self, include_envelope_void_reason):
        """Sets the include_envelope_void_reason of this ConnectCustomConfiguration.

        When set to **true**, Connect will include the voidedReason for voided envelopes.  # noqa: E501

        :param include_envelope_void_reason: The include_envelope_void_reason of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._include_envelope_void_reason = include_envelope_void_reason

    @property
    def include_hmac(self):
        """Gets the include_hmac of this ConnectCustomConfiguration.  # noqa: E501

          # noqa: E501

        :return: The include_hmac of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._include_hmac

    @include_hmac.setter
    def include_hmac(self, include_hmac):
        """Sets the include_hmac of this ConnectCustomConfiguration.

          # noqa: E501

        :param include_hmac: The include_hmac of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._include_hmac = include_hmac

    @property
    def include_sender_accountas_custom_field(self):
        """Gets the include_sender_accountas_custom_field of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, Connect will include the sender account as Custom Field in the data.  # noqa: E501

        :return: The include_sender_accountas_custom_field of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._include_sender_accountas_custom_field

    @include_sender_accountas_custom_field.setter
    def include_sender_accountas_custom_field(self, include_sender_accountas_custom_field):
        """Sets the include_sender_accountas_custom_field of this ConnectCustomConfiguration.

        When set to **true**, Connect will include the sender account as Custom Field in the data.  # noqa: E501

        :param include_sender_accountas_custom_field: The include_sender_accountas_custom_field of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._include_sender_accountas_custom_field = include_sender_accountas_custom_field

    @property
    def include_time_zone_information(self):
        """Gets the include_time_zone_information of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, Connect will include the envelope time zone information.  # noqa: E501

        :return: The include_time_zone_information of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._include_time_zone_information

    @include_time_zone_information.setter
    def include_time_zone_information(self, include_time_zone_information):
        """Sets the include_time_zone_information of this ConnectCustomConfiguration.

        When set to **true**, Connect will include the envelope time zone information.  # noqa: E501

        :param include_time_zone_information: The include_time_zone_information of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._include_time_zone_information = include_time_zone_information

    @property
    def name(self):
        """Gets the name of this ConnectCustomConfiguration.  # noqa: E501

        The name of the Connect configuration. The name helps identify the configuration in the list.  # noqa: E501

        :return: The name of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectCustomConfiguration.

        The name of the Connect configuration. The name helps identify the configuration in the list.  # noqa: E501

        :param name: The name of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def recipient_events(self):
        """Gets the recipient_events of this ConnectCustomConfiguration.  # noqa: E501

        A comma separated list of Ã¯Â¿Â½RecipientÃ¯Â¿Â½ related events that are tracked through Connect. The possible event values are: Sent, Delivered, Completed, Declined, AuthenticationFailed, and AutoResponded.  # noqa: E501

        :return: The recipient_events of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._recipient_events

    @recipient_events.setter
    def recipient_events(self, recipient_events):
        """Sets the recipient_events of this ConnectCustomConfiguration.

        A comma separated list of Ã¯Â¿Â½RecipientÃ¯Â¿Â½ related events that are tracked through Connect. The possible event values are: Sent, Delivered, Completed, Declined, AuthenticationFailed, and AutoResponded.  # noqa: E501

        :param recipient_events: The recipient_events of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._recipient_events = recipient_events

    @property
    def requires_acknowledgement(self):
        """Gets the requires_acknowledgement of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, and a publication message fails to be acknowledged, the message goes back into the queue and the system will retry delivery after a successful acknowledgement is received. If the delivery fails a second time, the message is not returned to the queue for sending until Connect receives a successful acknowledgement and it has been at least 24 hours since the previous retry. There is a maximum of ten retries Alternately, you can use Republish Connect Information to manually republish the envelope information.  # noqa: E501

        :return: The requires_acknowledgement of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._requires_acknowledgement

    @requires_acknowledgement.setter
    def requires_acknowledgement(self, requires_acknowledgement):
        """Sets the requires_acknowledgement of this ConnectCustomConfiguration.

        When set to **true**, and a publication message fails to be acknowledged, the message goes back into the queue and the system will retry delivery after a successful acknowledgement is received. If the delivery fails a second time, the message is not returned to the queue for sending until Connect receives a successful acknowledgement and it has been at least 24 hours since the previous retry. There is a maximum of ten retries Alternately, you can use Republish Connect Information to manually republish the envelope information.  # noqa: E501

        :param requires_acknowledgement: The requires_acknowledgement of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._requires_acknowledgement = requires_acknowledgement

    @property
    def sign_message_with_x509_certificate(self):
        """Gets the sign_message_with_x509_certificate of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, Connect messages are signed with an X509 certificate. This provides support for 2-way SSL.  # noqa: E501

        :return: The sign_message_with_x509_certificate of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._sign_message_with_x509_certificate

    @sign_message_with_x509_certificate.setter
    def sign_message_with_x509_certificate(self, sign_message_with_x509_certificate):
        """Sets the sign_message_with_x509_certificate of this ConnectCustomConfiguration.

        When set to **true**, Connect messages are signed with an X509 certificate. This provides support for 2-way SSL.  # noqa: E501

        :param sign_message_with_x509_certificate: The sign_message_with_x509_certificate of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._sign_message_with_x509_certificate = sign_message_with_x509_certificate

    @property
    def soap_namespace(self):
        """Gets the soap_namespace of this ConnectCustomConfiguration.  # noqa: E501

        The namespace of the SOAP interface.  The namespace value must be set if useSoapInterface is set to true.  # noqa: E501

        :return: The soap_namespace of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._soap_namespace

    @soap_namespace.setter
    def soap_namespace(self, soap_namespace):
        """Sets the soap_namespace of this ConnectCustomConfiguration.

        The namespace of the SOAP interface.  The namespace value must be set if useSoapInterface is set to true.  # noqa: E501

        :param soap_namespace: The soap_namespace of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._soap_namespace = soap_namespace

    @property
    def url_to_publish_to(self):
        """Gets the url_to_publish_to of this ConnectCustomConfiguration.  # noqa: E501

        This is the web address and name of your listener or Retrieving Service endpoint. You need to include HTTPS:// in the web address.  # noqa: E501

        :return: The url_to_publish_to of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._url_to_publish_to

    @url_to_publish_to.setter
    def url_to_publish_to(self, url_to_publish_to):
        """Sets the url_to_publish_to of this ConnectCustomConfiguration.

        This is the web address and name of your listener or Retrieving Service endpoint. You need to include HTTPS:// in the web address.  # noqa: E501

        :param url_to_publish_to: The url_to_publish_to of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._url_to_publish_to = url_to_publish_to

    @property
    def user_ids(self):
        """Gets the user_ids of this ConnectCustomConfiguration.  # noqa: E501

        A comma separated list of userIds. This sets the users associated with the tracked envelope and recipient events. When one of the event occurs for a set user, the information is sent through Connect.   ###### Note: If allUsers is set to Ã¯Â¿Â½falseÃ¯Â¿Â½ then you must provide a list of user idÃ¯Â¿Â½s.  # noqa: E501

        :return: The user_ids of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this ConnectCustomConfiguration.

        A comma separated list of userIds. This sets the users associated with the tracked envelope and recipient events. When one of the event occurs for a set user, the information is sent through Connect.   ###### Note: If allUsers is set to Ã¯Â¿Â½falseÃ¯Â¿Â½ then you must provide a list of user idÃ¯Â¿Â½s.  # noqa: E501

        :param user_ids: The user_ids of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._user_ids = user_ids

    @property
    def use_soap_interface(self):
        """Gets the use_soap_interface of this ConnectCustomConfiguration.  # noqa: E501

        When set to **true**, indicates that the `urlToPublishTo` property contains a SOAP endpoint.  # noqa: E501

        :return: The use_soap_interface of this ConnectCustomConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._use_soap_interface

    @use_soap_interface.setter
    def use_soap_interface(self, use_soap_interface):
        """Sets the use_soap_interface of this ConnectCustomConfiguration.

        When set to **true**, indicates that the `urlToPublishTo` property contains a SOAP endpoint.  # noqa: E501

        :param use_soap_interface: The use_soap_interface of this ConnectCustomConfiguration.  # noqa: E501
        :type: str
        """

        self._use_soap_interface = use_soap_interface

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
        if issubclass(ConnectCustomConfiguration, dict):
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
        if not isinstance(other, ConnectCustomConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectCustomConfiguration):
            return True

        return self.to_dict() != other.to_dict()
