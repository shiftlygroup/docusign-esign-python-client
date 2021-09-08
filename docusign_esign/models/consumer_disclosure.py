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


class ConsumerDisclosure(object):
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
        'account_esign_id': 'str',
        'allow_cd_withdraw': 'str',
        'allow_cd_withdraw_metadata': 'SettingsMetadata',
        'change_email': 'str',
        'change_email_other': 'str',
        'company_name': 'str',
        'company_phone': 'str',
        'copy_cost_per_page': 'str',
        'copy_fee_collection_method': 'str',
        'copy_request_email': 'str',
        'custom': 'str',
        'enable_esign': 'str',
        'esign_agreement': 'str',
        'esign_text': 'str',
        'language_code': 'str',
        'must_agree_to_esign': 'str',
        'pdf_id': 'str',
        'use_brand': 'str',
        'use_consumer_disclosure_within_account': 'str',
        'use_consumer_disclosure_within_account_metadata': 'SettingsMetadata',
        'withdraw_address_line1': 'str',
        'withdraw_address_line2': 'str',
        'withdraw_by_email': 'str',
        'withdraw_by_mail': 'str',
        'withdraw_by_phone': 'str',
        'withdraw_city': 'str',
        'withdraw_consequences': 'str',
        'withdraw_email': 'str',
        'withdraw_other': 'str',
        'withdraw_phone': 'str',
        'withdraw_postal_code': 'str',
        'withdraw_state': 'str'
    }

    attribute_map = {
        'account_esign_id': 'accountEsignId',
        'allow_cd_withdraw': 'allowCDWithdraw',
        'allow_cd_withdraw_metadata': 'allowCDWithdrawMetadata',
        'change_email': 'changeEmail',
        'change_email_other': 'changeEmailOther',
        'company_name': 'companyName',
        'company_phone': 'companyPhone',
        'copy_cost_per_page': 'copyCostPerPage',
        'copy_fee_collection_method': 'copyFeeCollectionMethod',
        'copy_request_email': 'copyRequestEmail',
        'custom': 'custom',
        'enable_esign': 'enableEsign',
        'esign_agreement': 'esignAgreement',
        'esign_text': 'esignText',
        'language_code': 'languageCode',
        'must_agree_to_esign': 'mustAgreeToEsign',
        'pdf_id': 'pdfId',
        'use_brand': 'useBrand',
        'use_consumer_disclosure_within_account': 'useConsumerDisclosureWithinAccount',
        'use_consumer_disclosure_within_account_metadata': 'useConsumerDisclosureWithinAccountMetadata',
        'withdraw_address_line1': 'withdrawAddressLine1',
        'withdraw_address_line2': 'withdrawAddressLine2',
        'withdraw_by_email': 'withdrawByEmail',
        'withdraw_by_mail': 'withdrawByMail',
        'withdraw_by_phone': 'withdrawByPhone',
        'withdraw_city': 'withdrawCity',
        'withdraw_consequences': 'withdrawConsequences',
        'withdraw_email': 'withdrawEmail',
        'withdraw_other': 'withdrawOther',
        'withdraw_phone': 'withdrawPhone',
        'withdraw_postal_code': 'withdrawPostalCode',
        'withdraw_state': 'withdrawState'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ConsumerDisclosure - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_esign_id = None
        self._allow_cd_withdraw = None
        self._allow_cd_withdraw_metadata = None
        self._change_email = None
        self._change_email_other = None
        self._company_name = None
        self._company_phone = None
        self._copy_cost_per_page = None
        self._copy_fee_collection_method = None
        self._copy_request_email = None
        self._custom = None
        self._enable_esign = None
        self._esign_agreement = None
        self._esign_text = None
        self._language_code = None
        self._must_agree_to_esign = None
        self._pdf_id = None
        self._use_brand = None
        self._use_consumer_disclosure_within_account = None
        self._use_consumer_disclosure_within_account_metadata = None
        self._withdraw_address_line1 = None
        self._withdraw_address_line2 = None
        self._withdraw_by_email = None
        self._withdraw_by_mail = None
        self._withdraw_by_phone = None
        self._withdraw_city = None
        self._withdraw_consequences = None
        self._withdraw_email = None
        self._withdraw_other = None
        self._withdraw_phone = None
        self._withdraw_postal_code = None
        self._withdraw_state = None
        self.discriminator = None

        setattr(self, "_{}".format('account_esign_id'), kwargs.get('account_esign_id', None))
        setattr(self, "_{}".format('allow_cd_withdraw'), kwargs.get('allow_cd_withdraw', None))
        setattr(self, "_{}".format('allow_cd_withdraw_metadata'), kwargs.get('allow_cd_withdraw_metadata', None))
        setattr(self, "_{}".format('change_email'), kwargs.get('change_email', None))
        setattr(self, "_{}".format('change_email_other'), kwargs.get('change_email_other', None))
        setattr(self, "_{}".format('company_name'), kwargs.get('company_name', None))
        setattr(self, "_{}".format('company_phone'), kwargs.get('company_phone', None))
        setattr(self, "_{}".format('copy_cost_per_page'), kwargs.get('copy_cost_per_page', None))
        setattr(self, "_{}".format('copy_fee_collection_method'), kwargs.get('copy_fee_collection_method', None))
        setattr(self, "_{}".format('copy_request_email'), kwargs.get('copy_request_email', None))
        setattr(self, "_{}".format('custom'), kwargs.get('custom', None))
        setattr(self, "_{}".format('enable_esign'), kwargs.get('enable_esign', None))
        setattr(self, "_{}".format('esign_agreement'), kwargs.get('esign_agreement', None))
        setattr(self, "_{}".format('esign_text'), kwargs.get('esign_text', None))
        setattr(self, "_{}".format('language_code'), kwargs.get('language_code', None))
        setattr(self, "_{}".format('must_agree_to_esign'), kwargs.get('must_agree_to_esign', None))
        setattr(self, "_{}".format('pdf_id'), kwargs.get('pdf_id', None))
        setattr(self, "_{}".format('use_brand'), kwargs.get('use_brand', None))
        setattr(self, "_{}".format('use_consumer_disclosure_within_account'), kwargs.get('use_consumer_disclosure_within_account', None))
        setattr(self, "_{}".format('use_consumer_disclosure_within_account_metadata'), kwargs.get('use_consumer_disclosure_within_account_metadata', None))
        setattr(self, "_{}".format('withdraw_address_line1'), kwargs.get('withdraw_address_line1', None))
        setattr(self, "_{}".format('withdraw_address_line2'), kwargs.get('withdraw_address_line2', None))
        setattr(self, "_{}".format('withdraw_by_email'), kwargs.get('withdraw_by_email', None))
        setattr(self, "_{}".format('withdraw_by_mail'), kwargs.get('withdraw_by_mail', None))
        setattr(self, "_{}".format('withdraw_by_phone'), kwargs.get('withdraw_by_phone', None))
        setattr(self, "_{}".format('withdraw_city'), kwargs.get('withdraw_city', None))
        setattr(self, "_{}".format('withdraw_consequences'), kwargs.get('withdraw_consequences', None))
        setattr(self, "_{}".format('withdraw_email'), kwargs.get('withdraw_email', None))
        setattr(self, "_{}".format('withdraw_other'), kwargs.get('withdraw_other', None))
        setattr(self, "_{}".format('withdraw_phone'), kwargs.get('withdraw_phone', None))
        setattr(self, "_{}".format('withdraw_postal_code'), kwargs.get('withdraw_postal_code', None))
        setattr(self, "_{}".format('withdraw_state'), kwargs.get('withdraw_state', None))

    @property
    def account_esign_id(self):
        """Gets the account_esign_id of this ConsumerDisclosure.  # noqa: E501

        A GUID identifying the account associated with the consumer disclosure  # noqa: E501

        :return: The account_esign_id of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._account_esign_id

    @account_esign_id.setter
    def account_esign_id(self, account_esign_id):
        """Sets the account_esign_id of this ConsumerDisclosure.

        A GUID identifying the account associated with the consumer disclosure  # noqa: E501

        :param account_esign_id: The account_esign_id of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._account_esign_id = account_esign_id

    @property
    def allow_cd_withdraw(self):
        """Gets the allow_cd_withdraw of this ConsumerDisclosure.  # noqa: E501

        Indicates whether the customer can withdraw their acceptance of the consumer disclosure.  # noqa: E501

        :return: The allow_cd_withdraw of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._allow_cd_withdraw

    @allow_cd_withdraw.setter
    def allow_cd_withdraw(self, allow_cd_withdraw):
        """Sets the allow_cd_withdraw of this ConsumerDisclosure.

        Indicates whether the customer can withdraw their acceptance of the consumer disclosure.  # noqa: E501

        :param allow_cd_withdraw: The allow_cd_withdraw of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._allow_cd_withdraw = allow_cd_withdraw

    @property
    def allow_cd_withdraw_metadata(self):
        """Gets the allow_cd_withdraw_metadata of this ConsumerDisclosure.  # noqa: E501


        :return: The allow_cd_withdraw_metadata of this ConsumerDisclosure.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._allow_cd_withdraw_metadata

    @allow_cd_withdraw_metadata.setter
    def allow_cd_withdraw_metadata(self, allow_cd_withdraw_metadata):
        """Sets the allow_cd_withdraw_metadata of this ConsumerDisclosure.


        :param allow_cd_withdraw_metadata: The allow_cd_withdraw_metadata of this ConsumerDisclosure.  # noqa: E501
        :type: SettingsMetadata
        """

        self._allow_cd_withdraw_metadata = allow_cd_withdraw_metadata

    @property
    def change_email(self):
        """Gets the change_email of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The change_email of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._change_email

    @change_email.setter
    def change_email(self, change_email):
        """Sets the change_email of this ConsumerDisclosure.

          # noqa: E501

        :param change_email: The change_email of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._change_email = change_email

    @property
    def change_email_other(self):
        """Gets the change_email_other of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The change_email_other of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._change_email_other

    @change_email_other.setter
    def change_email_other(self, change_email_other):
        """Sets the change_email_other of this ConsumerDisclosure.

          # noqa: E501

        :param change_email_other: The change_email_other of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._change_email_other = change_email_other

    @property
    def company_name(self):
        """Gets the company_name of this ConsumerDisclosure.  # noqa: E501

        The name of the company associated with the consumer disclosure.  # noqa: E501

        :return: The company_name of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ConsumerDisclosure.

        The name of the company associated with the consumer disclosure.  # noqa: E501

        :param company_name: The company_name of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def company_phone(self):
        """Gets the company_phone of this ConsumerDisclosure.  # noqa: E501

        The phone number of the company associated with the consumer disclosure.  # noqa: E501

        :return: The company_phone of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._company_phone

    @company_phone.setter
    def company_phone(self, company_phone):
        """Sets the company_phone of this ConsumerDisclosure.

        The phone number of the company associated with the consumer disclosure.  # noqa: E501

        :param company_phone: The company_phone of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._company_phone = company_phone

    @property
    def copy_cost_per_page(self):
        """Gets the copy_cost_per_page of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The copy_cost_per_page of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._copy_cost_per_page

    @copy_cost_per_page.setter
    def copy_cost_per_page(self, copy_cost_per_page):
        """Sets the copy_cost_per_page of this ConsumerDisclosure.

          # noqa: E501

        :param copy_cost_per_page: The copy_cost_per_page of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._copy_cost_per_page = copy_cost_per_page

    @property
    def copy_fee_collection_method(self):
        """Gets the copy_fee_collection_method of this ConsumerDisclosure.  # noqa: E501

        Specifies the fee collection method for cases in which the customer requires paper copies of the document.  Maximum Length: 255 characters  # noqa: E501

        :return: The copy_fee_collection_method of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._copy_fee_collection_method

    @copy_fee_collection_method.setter
    def copy_fee_collection_method(self, copy_fee_collection_method):
        """Sets the copy_fee_collection_method of this ConsumerDisclosure.

        Specifies the fee collection method for cases in which the customer requires paper copies of the document.  Maximum Length: 255 characters  # noqa: E501

        :param copy_fee_collection_method: The copy_fee_collection_method of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._copy_fee_collection_method = copy_fee_collection_method

    @property
    def copy_request_email(self):
        """Gets the copy_request_email of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The copy_request_email of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._copy_request_email

    @copy_request_email.setter
    def copy_request_email(self, copy_request_email):
        """Sets the copy_request_email of this ConsumerDisclosure.

          # noqa: E501

        :param copy_request_email: The copy_request_email of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._copy_request_email = copy_request_email

    @property
    def custom(self):
        """Gets the custom of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The custom of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this ConsumerDisclosure.

          # noqa: E501

        :param custom: The custom of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._custom = custom

    @property
    def enable_esign(self):
        """Gets the enable_esign of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The enable_esign of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._enable_esign

    @enable_esign.setter
    def enable_esign(self, enable_esign):
        """Sets the enable_esign of this ConsumerDisclosure.

          # noqa: E501

        :param enable_esign: The enable_esign of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._enable_esign = enable_esign

    @property
    def esign_agreement(self):
        """Gets the esign_agreement of this ConsumerDisclosure.  # noqa: E501

        The Electronic Record and Signature Disclosure text. The disclosure text includes the html formatting.  # noqa: E501

        :return: The esign_agreement of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._esign_agreement

    @esign_agreement.setter
    def esign_agreement(self, esign_agreement):
        """Sets the esign_agreement of this ConsumerDisclosure.

        The Electronic Record and Signature Disclosure text. The disclosure text includes the html formatting.  # noqa: E501

        :param esign_agreement: The esign_agreement of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._esign_agreement = esign_agreement

    @property
    def esign_text(self):
        """Gets the esign_text of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The esign_text of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._esign_text

    @esign_text.setter
    def esign_text(self, esign_text):
        """Sets the esign_text of this ConsumerDisclosure.

          # noqa: E501

        :param esign_text: The esign_text of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._esign_text = esign_text

    @property
    def language_code(self):
        """Gets the language_code of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The language_code of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this ConsumerDisclosure.

          # noqa: E501

        :param language_code: The language_code of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._language_code = language_code

    @property
    def must_agree_to_esign(self):
        """Gets the must_agree_to_esign of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The must_agree_to_esign of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._must_agree_to_esign

    @must_agree_to_esign.setter
    def must_agree_to_esign(self, must_agree_to_esign):
        """Sets the must_agree_to_esign of this ConsumerDisclosure.

          # noqa: E501

        :param must_agree_to_esign: The must_agree_to_esign of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._must_agree_to_esign = must_agree_to_esign

    @property
    def pdf_id(self):
        """Gets the pdf_id of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The pdf_id of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._pdf_id

    @pdf_id.setter
    def pdf_id(self, pdf_id):
        """Sets the pdf_id of this ConsumerDisclosure.

          # noqa: E501

        :param pdf_id: The pdf_id of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._pdf_id = pdf_id

    @property
    def use_brand(self):
        """Gets the use_brand of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The use_brand of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._use_brand

    @use_brand.setter
    def use_brand(self, use_brand):
        """Sets the use_brand of this ConsumerDisclosure.

          # noqa: E501

        :param use_brand: The use_brand of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._use_brand = use_brand

    @property
    def use_consumer_disclosure_within_account(self):
        """Gets the use_consumer_disclosure_within_account of this ConsumerDisclosure.  # noqa: E501

          # noqa: E501

        :return: The use_consumer_disclosure_within_account of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._use_consumer_disclosure_within_account

    @use_consumer_disclosure_within_account.setter
    def use_consumer_disclosure_within_account(self, use_consumer_disclosure_within_account):
        """Sets the use_consumer_disclosure_within_account of this ConsumerDisclosure.

          # noqa: E501

        :param use_consumer_disclosure_within_account: The use_consumer_disclosure_within_account of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._use_consumer_disclosure_within_account = use_consumer_disclosure_within_account

    @property
    def use_consumer_disclosure_within_account_metadata(self):
        """Gets the use_consumer_disclosure_within_account_metadata of this ConsumerDisclosure.  # noqa: E501


        :return: The use_consumer_disclosure_within_account_metadata of this ConsumerDisclosure.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._use_consumer_disclosure_within_account_metadata

    @use_consumer_disclosure_within_account_metadata.setter
    def use_consumer_disclosure_within_account_metadata(self, use_consumer_disclosure_within_account_metadata):
        """Sets the use_consumer_disclosure_within_account_metadata of this ConsumerDisclosure.


        :param use_consumer_disclosure_within_account_metadata: The use_consumer_disclosure_within_account_metadata of this ConsumerDisclosure.  # noqa: E501
        :type: SettingsMetadata
        """

        self._use_consumer_disclosure_within_account_metadata = use_consumer_disclosure_within_account_metadata

    @property
    def withdraw_address_line1(self):
        """Gets the withdraw_address_line1 of this ConsumerDisclosure.  # noqa: E501

        Contains the first address line of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters.   # noqa: E501

        :return: The withdraw_address_line1 of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_address_line1

    @withdraw_address_line1.setter
    def withdraw_address_line1(self, withdraw_address_line1):
        """Sets the withdraw_address_line1 of this ConsumerDisclosure.

        Contains the first address line of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters.   # noqa: E501

        :param withdraw_address_line1: The withdraw_address_line1 of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_address_line1 = withdraw_address_line1

    @property
    def withdraw_address_line2(self):
        """Gets the withdraw_address_line2 of this ConsumerDisclosure.  # noqa: E501

        Contains the second address line of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters.   # noqa: E501

        :return: The withdraw_address_line2 of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_address_line2

    @withdraw_address_line2.setter
    def withdraw_address_line2(self, withdraw_address_line2):
        """Sets the withdraw_address_line2 of this ConsumerDisclosure.

        Contains the second address line of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters.   # noqa: E501

        :param withdraw_address_line2: The withdraw_address_line2 of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_address_line2 = withdraw_address_line2

    @property
    def withdraw_by_email(self):
        """Gets the withdraw_by_email of this ConsumerDisclosure.  # noqa: E501

        Indicates whether the customer can withdraw consent by email.  # noqa: E501

        :return: The withdraw_by_email of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_by_email

    @withdraw_by_email.setter
    def withdraw_by_email(self, withdraw_by_email):
        """Sets the withdraw_by_email of this ConsumerDisclosure.

        Indicates whether the customer can withdraw consent by email.  # noqa: E501

        :param withdraw_by_email: The withdraw_by_email of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_by_email = withdraw_by_email

    @property
    def withdraw_by_mail(self):
        """Gets the withdraw_by_mail of this ConsumerDisclosure.  # noqa: E501

        Indicates whether the customer can withdraw consent by postal mail.  # noqa: E501

        :return: The withdraw_by_mail of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_by_mail

    @withdraw_by_mail.setter
    def withdraw_by_mail(self, withdraw_by_mail):
        """Sets the withdraw_by_mail of this ConsumerDisclosure.

        Indicates whether the customer can withdraw consent by postal mail.  # noqa: E501

        :param withdraw_by_mail: The withdraw_by_mail of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_by_mail = withdraw_by_mail

    @property
    def withdraw_by_phone(self):
        """Gets the withdraw_by_phone of this ConsumerDisclosure.  # noqa: E501

        Indicates whether the customer can withdraw consent by phone.  # noqa: E501

        :return: The withdraw_by_phone of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_by_phone

    @withdraw_by_phone.setter
    def withdraw_by_phone(self, withdraw_by_phone):
        """Sets the withdraw_by_phone of this ConsumerDisclosure.

        Indicates whether the customer can withdraw consent by phone.  # noqa: E501

        :param withdraw_by_phone: The withdraw_by_phone of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_by_phone = withdraw_by_phone

    @property
    def withdraw_city(self):
        """Gets the withdraw_city of this ConsumerDisclosure.  # noqa: E501

        Contains the city of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 50 characters.   # noqa: E501

        :return: The withdraw_city of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_city

    @withdraw_city.setter
    def withdraw_city(self, withdraw_city):
        """Sets the withdraw_city of this ConsumerDisclosure.

        Contains the city of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 50 characters.   # noqa: E501

        :param withdraw_city: The withdraw_city of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_city = withdraw_city

    @property
    def withdraw_consequences(self):
        """Gets the withdraw_consequences of this ConsumerDisclosure.  # noqa: E501

        Indicates the consequences of withdrawing consent.  # noqa: E501

        :return: The withdraw_consequences of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_consequences

    @withdraw_consequences.setter
    def withdraw_consequences(self, withdraw_consequences):
        """Sets the withdraw_consequences of this ConsumerDisclosure.

        Indicates the consequences of withdrawing consent.  # noqa: E501

        :param withdraw_consequences: The withdraw_consequences of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_consequences = withdraw_consequences

    @property
    def withdraw_email(self):
        """Gets the withdraw_email of this ConsumerDisclosure.  # noqa: E501

        Contains the email address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters.   # noqa: E501

        :return: The withdraw_email of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_email

    @withdraw_email.setter
    def withdraw_email(self, withdraw_email):
        """Sets the withdraw_email of this ConsumerDisclosure.

        Contains the email address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters.   # noqa: E501

        :param withdraw_email: The withdraw_email of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_email = withdraw_email

    @property
    def withdraw_other(self):
        """Gets the withdraw_other of this ConsumerDisclosure.  # noqa: E501

        Indicates other information need to withdraw consent.  Maximum length: 255 characters.  # noqa: E501

        :return: The withdraw_other of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_other

    @withdraw_other.setter
    def withdraw_other(self, withdraw_other):
        """Sets the withdraw_other of this ConsumerDisclosure.

        Indicates other information need to withdraw consent.  Maximum length: 255 characters.  # noqa: E501

        :param withdraw_other: The withdraw_other of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_other = withdraw_other

    @property
    def withdraw_phone(self):
        """Gets the withdraw_phone of this ConsumerDisclosure.  # noqa: E501

        Contains the phone number which a customer can call to register consent withdrawal notification.  Maximum length: 20 characters.   # noqa: E501

        :return: The withdraw_phone of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_phone

    @withdraw_phone.setter
    def withdraw_phone(self, withdraw_phone):
        """Sets the withdraw_phone of this ConsumerDisclosure.

        Contains the phone number which a customer can call to register consent withdrawal notification.  Maximum length: 20 characters.   # noqa: E501

        :param withdraw_phone: The withdraw_phone of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_phone = withdraw_phone

    @property
    def withdraw_postal_code(self):
        """Gets the withdraw_postal_code of this ConsumerDisclosure.  # noqa: E501

        Contains the postal code of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 20 characters.   # noqa: E501

        :return: The withdraw_postal_code of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_postal_code

    @withdraw_postal_code.setter
    def withdraw_postal_code(self, withdraw_postal_code):
        """Sets the withdraw_postal_code of this ConsumerDisclosure.

        Contains the postal code of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 20 characters.   # noqa: E501

        :param withdraw_postal_code: The withdraw_postal_code of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_postal_code = withdraw_postal_code

    @property
    def withdraw_state(self):
        """Gets the withdraw_state of this ConsumerDisclosure.  # noqa: E501

        Contains the state of the postal address to which a customer can send a consent withdrawal notification.  # noqa: E501

        :return: The withdraw_state of this ConsumerDisclosure.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_state

    @withdraw_state.setter
    def withdraw_state(self, withdraw_state):
        """Sets the withdraw_state of this ConsumerDisclosure.

        Contains the state of the postal address to which a customer can send a consent withdrawal notification.  # noqa: E501

        :param withdraw_state: The withdraw_state of this ConsumerDisclosure.  # noqa: E501
        :type: str
        """

        self._withdraw_state = withdraw_state

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
        if issubclass(ConsumerDisclosure, dict):
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
        if not isinstance(other, ConsumerDisclosure):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsumerDisclosure):
            return True

        return self.to_dict() != other.to_dict()
