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


class TemplateTabs(object):
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
        'approve_tabs': 'list[Approve]',
        'checkbox_tabs': 'list[Checkbox]',
        'company_tabs': 'list[Company]',
        'date_signed_tabs': 'list[DateSigned]',
        'date_tabs': 'list[Date]',
        'decline_tabs': 'list[Decline]',
        'email_address_tabs': 'list[EmailAddress]',
        'email_tabs': 'list[Email]',
        'envelope_id_tabs': 'list[EnvelopeId]',
        'first_name_tabs': 'list[FirstName]',
        'formula_tabs': 'list[FormulaTab]',
        'full_name_tabs': 'list[FullName]',
        'initial_here_tabs': 'list[InitialHere]',
        'last_name_tabs': 'list[LastName]',
        'list_tabs': 'list[List]',
        'notarize_tabs': 'list[Notarize]',
        'note_tabs': 'list[Note]',
        'number_tabs': 'list[Number]',
        'radio_group_tabs': 'list[RadioGroup]',
        'signer_attachment_tabs': 'list[SignerAttachment]',
        'sign_here_tabs': 'list[SignHere]',
        'smart_section_tabs': 'list[SmartSection]',
        'ssn_tabs': 'list[Ssn]',
        'text_tabs': 'list[Text]',
        'title_tabs': 'list[Title]',
        'view_tabs': 'list[View]',
        'zip_tabs': 'list[Zip]'
    }

    attribute_map = {
        'approve_tabs': 'approveTabs',
        'checkbox_tabs': 'checkboxTabs',
        'company_tabs': 'companyTabs',
        'date_signed_tabs': 'dateSignedTabs',
        'date_tabs': 'dateTabs',
        'decline_tabs': 'declineTabs',
        'email_address_tabs': 'emailAddressTabs',
        'email_tabs': 'emailTabs',
        'envelope_id_tabs': 'envelopeIdTabs',
        'first_name_tabs': 'firstNameTabs',
        'formula_tabs': 'formulaTabs',
        'full_name_tabs': 'fullNameTabs',
        'initial_here_tabs': 'initialHereTabs',
        'last_name_tabs': 'lastNameTabs',
        'list_tabs': 'listTabs',
        'notarize_tabs': 'notarizeTabs',
        'note_tabs': 'noteTabs',
        'number_tabs': 'numberTabs',
        'radio_group_tabs': 'radioGroupTabs',
        'signer_attachment_tabs': 'signerAttachmentTabs',
        'sign_here_tabs': 'signHereTabs',
        'smart_section_tabs': 'smartSectionTabs',
        'ssn_tabs': 'ssnTabs',
        'text_tabs': 'textTabs',
        'title_tabs': 'titleTabs',
        'view_tabs': 'viewTabs',
        'zip_tabs': 'zipTabs'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """TemplateTabs - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._approve_tabs = None
        self._checkbox_tabs = None
        self._company_tabs = None
        self._date_signed_tabs = None
        self._date_tabs = None
        self._decline_tabs = None
        self._email_address_tabs = None
        self._email_tabs = None
        self._envelope_id_tabs = None
        self._first_name_tabs = None
        self._formula_tabs = None
        self._full_name_tabs = None
        self._initial_here_tabs = None
        self._last_name_tabs = None
        self._list_tabs = None
        self._notarize_tabs = None
        self._note_tabs = None
        self._number_tabs = None
        self._radio_group_tabs = None
        self._signer_attachment_tabs = None
        self._sign_here_tabs = None
        self._smart_section_tabs = None
        self._ssn_tabs = None
        self._text_tabs = None
        self._title_tabs = None
        self._view_tabs = None
        self._zip_tabs = None
        self.discriminator = None

        setattr(self, "_{}".format('approve_tabs'), kwargs.get('approve_tabs', None))
        setattr(self, "_{}".format('checkbox_tabs'), kwargs.get('checkbox_tabs', None))
        setattr(self, "_{}".format('company_tabs'), kwargs.get('company_tabs', None))
        setattr(self, "_{}".format('date_signed_tabs'), kwargs.get('date_signed_tabs', None))
        setattr(self, "_{}".format('date_tabs'), kwargs.get('date_tabs', None))
        setattr(self, "_{}".format('decline_tabs'), kwargs.get('decline_tabs', None))
        setattr(self, "_{}".format('email_address_tabs'), kwargs.get('email_address_tabs', None))
        setattr(self, "_{}".format('email_tabs'), kwargs.get('email_tabs', None))
        setattr(self, "_{}".format('envelope_id_tabs'), kwargs.get('envelope_id_tabs', None))
        setattr(self, "_{}".format('first_name_tabs'), kwargs.get('first_name_tabs', None))
        setattr(self, "_{}".format('formula_tabs'), kwargs.get('formula_tabs', None))
        setattr(self, "_{}".format('full_name_tabs'), kwargs.get('full_name_tabs', None))
        setattr(self, "_{}".format('initial_here_tabs'), kwargs.get('initial_here_tabs', None))
        setattr(self, "_{}".format('last_name_tabs'), kwargs.get('last_name_tabs', None))
        setattr(self, "_{}".format('list_tabs'), kwargs.get('list_tabs', None))
        setattr(self, "_{}".format('notarize_tabs'), kwargs.get('notarize_tabs', None))
        setattr(self, "_{}".format('note_tabs'), kwargs.get('note_tabs', None))
        setattr(self, "_{}".format('number_tabs'), kwargs.get('number_tabs', None))
        setattr(self, "_{}".format('radio_group_tabs'), kwargs.get('radio_group_tabs', None))
        setattr(self, "_{}".format('signer_attachment_tabs'), kwargs.get('signer_attachment_tabs', None))
        setattr(self, "_{}".format('sign_here_tabs'), kwargs.get('sign_here_tabs', None))
        setattr(self, "_{}".format('smart_section_tabs'), kwargs.get('smart_section_tabs', None))
        setattr(self, "_{}".format('ssn_tabs'), kwargs.get('ssn_tabs', None))
        setattr(self, "_{}".format('text_tabs'), kwargs.get('text_tabs', None))
        setattr(self, "_{}".format('title_tabs'), kwargs.get('title_tabs', None))
        setattr(self, "_{}".format('view_tabs'), kwargs.get('view_tabs', None))
        setattr(self, "_{}".format('zip_tabs'), kwargs.get('zip_tabs', None))

    @property
    def approve_tabs(self):
        """Gets the approve_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document where you want the recipient to approve documents in an envelope without placing a signature or initials on the document. If the recipient clicks the Approve tag during the signing process, the recipient is considered to have signed the document. No information is shown on the document for the approval, but it is recorded as a signature in the envelope history.  # noqa: E501

        :return: The approve_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Approve]
        """
        return self._approve_tabs

    @approve_tabs.setter
    def approve_tabs(self, approve_tabs):
        """Sets the approve_tabs of this TemplateTabs.

        Specifies a tag on the document where you want the recipient to approve documents in an envelope without placing a signature or initials on the document. If the recipient clicks the Approve tag during the signing process, the recipient is considered to have signed the document. No information is shown on the document for the approval, but it is recorded as a signature in the envelope history.  # noqa: E501

        :param approve_tabs: The approve_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Approve]
        """

        self._approve_tabs = approve_tabs

    @property
    def checkbox_tabs(self):
        """Gets the checkbox_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document in a location where the recipient can select an option.  # noqa: E501

        :return: The checkbox_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Checkbox]
        """
        return self._checkbox_tabs

    @checkbox_tabs.setter
    def checkbox_tabs(self, checkbox_tabs):
        """Sets the checkbox_tabs of this TemplateTabs.

        Specifies a tag on the document in a location where the recipient can select an option.  # noqa: E501

        :param checkbox_tabs: The checkbox_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Checkbox]
        """

        self._checkbox_tabs = checkbox_tabs

    @property
    def company_tabs(self):
        """Gets the company_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document where you want the recipient's company name to appear.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :return: The company_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Company]
        """
        return self._company_tabs

    @company_tabs.setter
    def company_tabs(self, company_tabs):
        """Sets the company_tabs of this TemplateTabs.

        Specifies a tag on the document where you want the recipient's company name to appear.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :param company_tabs: The company_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Company]
        """

        self._company_tabs = company_tabs

    @property
    def date_signed_tabs(self):
        """Gets the date_signed_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tab on the document where the date the document was signed will automatically appear.  # noqa: E501

        :return: The date_signed_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[DateSigned]
        """
        return self._date_signed_tabs

    @date_signed_tabs.setter
    def date_signed_tabs(self, date_signed_tabs):
        """Sets the date_signed_tabs of this TemplateTabs.

        Specifies a tab on the document where the date the document was signed will automatically appear.  # noqa: E501

        :param date_signed_tabs: The date_signed_tabs of this TemplateTabs.  # noqa: E501
        :type: list[DateSigned]
        """

        self._date_signed_tabs = date_signed_tabs

    @property
    def date_tabs(self):
        """Gets the date_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tab on the document where you want the recipient to enter a date. Date tabs are single-line fields that allow date information to be entered in any format. The tooltip for this tab recommends entering the date as MM/DD/YYYY, but this is not enforced. The format entered by the signer is retained.   If you need a particular date format enforced, DocuSign recommends using a Text tab with a Validation Pattern and Validation Message to enforce the format.  # noqa: E501

        :return: The date_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Date]
        """
        return self._date_tabs

    @date_tabs.setter
    def date_tabs(self, date_tabs):
        """Sets the date_tabs of this TemplateTabs.

        Specifies a tab on the document where you want the recipient to enter a date. Date tabs are single-line fields that allow date information to be entered in any format. The tooltip for this tab recommends entering the date as MM/DD/YYYY, but this is not enforced. The format entered by the signer is retained.   If you need a particular date format enforced, DocuSign recommends using a Text tab with a Validation Pattern and Validation Message to enforce the format.  # noqa: E501

        :param date_tabs: The date_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Date]
        """

        self._date_tabs = date_tabs

    @property
    def decline_tabs(self):
        """Gets the decline_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document where you want to give the recipient the option of declining an envelope. If the recipient clicks the Decline tag during the signing process, the envelope is voided.  # noqa: E501

        :return: The decline_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Decline]
        """
        return self._decline_tabs

    @decline_tabs.setter
    def decline_tabs(self, decline_tabs):
        """Sets the decline_tabs of this TemplateTabs.

        Specifies a tag on the document where you want to give the recipient the option of declining an envelope. If the recipient clicks the Decline tag during the signing process, the envelope is voided.  # noqa: E501

        :param decline_tabs: The decline_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Decline]
        """

        self._decline_tabs = decline_tabs

    @property
    def email_address_tabs(self):
        """Gets the email_address_tabs of this TemplateTabs.  # noqa: E501

        Specifies a location on the document where you want where you want the recipient's email, as entered in the recipient information, to display.  # noqa: E501

        :return: The email_address_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[EmailAddress]
        """
        return self._email_address_tabs

    @email_address_tabs.setter
    def email_address_tabs(self, email_address_tabs):
        """Sets the email_address_tabs of this TemplateTabs.

        Specifies a location on the document where you want where you want the recipient's email, as entered in the recipient information, to display.  # noqa: E501

        :param email_address_tabs: The email_address_tabs of this TemplateTabs.  # noqa: E501
        :type: list[EmailAddress]
        """

        self._email_address_tabs = email_address_tabs

    @property
    def email_tabs(self):
        """Gets the email_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document where you want the recipient to enter an email. Email tags are single-line fields that accept any characters. The system checks that a valid email format (i.e. xxx@yyy.zzz) is entered in the tag. It uses the same parameters as a Text tab, with the validation message and pattern set for email information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :return: The email_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Email]
        """
        return self._email_tabs

    @email_tabs.setter
    def email_tabs(self, email_tabs):
        """Sets the email_tabs of this TemplateTabs.

        Specifies a tag on the document where you want the recipient to enter an email. Email tags are single-line fields that accept any characters. The system checks that a valid email format (i.e. xxx@yyy.zzz) is entered in the tag. It uses the same parameters as a Text tab, with the validation message and pattern set for email information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :param email_tabs: The email_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Email]
        """

        self._email_tabs = email_tabs

    @property
    def envelope_id_tabs(self):
        """Gets the envelope_id_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document where you want the envelope ID for to appear. Recipients cannot enter or change the information in this tab, it is for informational purposes only.  # noqa: E501

        :return: The envelope_id_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[EnvelopeId]
        """
        return self._envelope_id_tabs

    @envelope_id_tabs.setter
    def envelope_id_tabs(self, envelope_id_tabs):
        """Sets the envelope_id_tabs of this TemplateTabs.

        Specifies a tag on the document where you want the envelope ID for to appear. Recipients cannot enter or change the information in this tab, it is for informational purposes only.  # noqa: E501

        :param envelope_id_tabs: The envelope_id_tabs of this TemplateTabs.  # noqa: E501
        :type: list[EnvelopeId]
        """

        self._envelope_id_tabs = envelope_id_tabs

    @property
    def first_name_tabs(self):
        """Gets the first_name_tabs of this TemplateTabs.  # noqa: E501

        Specifies tag on a document where you want the recipient's first name to appear. This tag takes the recipient's name, as entered in the recipient information, splits it into sections based on spaces and uses the first section as the first name.  # noqa: E501

        :return: The first_name_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[FirstName]
        """
        return self._first_name_tabs

    @first_name_tabs.setter
    def first_name_tabs(self, first_name_tabs):
        """Sets the first_name_tabs of this TemplateTabs.

        Specifies tag on a document where you want the recipient's first name to appear. This tag takes the recipient's name, as entered in the recipient information, splits it into sections based on spaces and uses the first section as the first name.  # noqa: E501

        :param first_name_tabs: The first_name_tabs of this TemplateTabs.  # noqa: E501
        :type: list[FirstName]
        """

        self._first_name_tabs = first_name_tabs

    @property
    def formula_tabs(self):
        """Gets the formula_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag that is used to add a calculated field to a document. Envelope recipients cannot directly enter information into the tag; the formula tab calculates and displays a new value when changes are made to the reference tag values. The reference tag information and calculation operations are entered in the \"formula\" element. See the [ML:Using the Calculated Fields Feature] quick start guide or [ML:DocuSign Service User Guide] for more information about formulas.  # noqa: E501

        :return: The formula_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[FormulaTab]
        """
        return self._formula_tabs

    @formula_tabs.setter
    def formula_tabs(self, formula_tabs):
        """Sets the formula_tabs of this TemplateTabs.

        Specifies a tag that is used to add a calculated field to a document. Envelope recipients cannot directly enter information into the tag; the formula tab calculates and displays a new value when changes are made to the reference tag values. The reference tag information and calculation operations are entered in the \"formula\" element. See the [ML:Using the Calculated Fields Feature] quick start guide or [ML:DocuSign Service User Guide] for more information about formulas.  # noqa: E501

        :param formula_tabs: The formula_tabs of this TemplateTabs.  # noqa: E501
        :type: list[FormulaTab]
        """

        self._formula_tabs = formula_tabs

    @property
    def full_name_tabs(self):
        """Gets the full_name_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document where you want the recipient's name to appear.  # noqa: E501

        :return: The full_name_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[FullName]
        """
        return self._full_name_tabs

    @full_name_tabs.setter
    def full_name_tabs(self, full_name_tabs):
        """Sets the full_name_tabs of this TemplateTabs.

        Specifies a tag on the document where you want the recipient's name to appear.  # noqa: E501

        :param full_name_tabs: The full_name_tabs of this TemplateTabs.  # noqa: E501
        :type: list[FullName]
        """

        self._full_name_tabs = full_name_tabs

    @property
    def initial_here_tabs(self):
        """Gets the initial_here_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag location in the document at which a recipient will place their initials. The `optional` parameter specifies whether the initials are required or optional.  # noqa: E501

        :return: The initial_here_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[InitialHere]
        """
        return self._initial_here_tabs

    @initial_here_tabs.setter
    def initial_here_tabs(self, initial_here_tabs):
        """Sets the initial_here_tabs of this TemplateTabs.

        Specifies a tag location in the document at which a recipient will place their initials. The `optional` parameter specifies whether the initials are required or optional.  # noqa: E501

        :param initial_here_tabs: The initial_here_tabs of this TemplateTabs.  # noqa: E501
        :type: list[InitialHere]
        """

        self._initial_here_tabs = initial_here_tabs

    @property
    def last_name_tabs(self):
        """Gets the last_name_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on a document where you want the recipient's last name to appear. This tag takes the recipient's name, as entered in the recipient information, splits it into sections based on spaces and uses the last section as the last name.  # noqa: E501

        :return: The last_name_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[LastName]
        """
        return self._last_name_tabs

    @last_name_tabs.setter
    def last_name_tabs(self, last_name_tabs):
        """Sets the last_name_tabs of this TemplateTabs.

        Specifies a tag on a document where you want the recipient's last name to appear. This tag takes the recipient's name, as entered in the recipient information, splits it into sections based on spaces and uses the last section as the last name.  # noqa: E501

        :param last_name_tabs: The last_name_tabs of this TemplateTabs.  # noqa: E501
        :type: list[LastName]
        """

        self._last_name_tabs = last_name_tabs

    @property
    def list_tabs(self):
        """Gets the list_tabs of this TemplateTabs.  # noqa: E501

        Specify this tag to give your recipient a list of options, presented as a drop-down list, from which they can select.  # noqa: E501

        :return: The list_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[List]
        """
        return self._list_tabs

    @list_tabs.setter
    def list_tabs(self, list_tabs):
        """Sets the list_tabs of this TemplateTabs.

        Specify this tag to give your recipient a list of options, presented as a drop-down list, from which they can select.  # noqa: E501

        :param list_tabs: The list_tabs of this TemplateTabs.  # noqa: E501
        :type: list[List]
        """

        self._list_tabs = list_tabs

    @property
    def notarize_tabs(self):
        """Gets the notarize_tabs of this TemplateTabs.  # noqa: E501

          # noqa: E501

        :return: The notarize_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Notarize]
        """
        return self._notarize_tabs

    @notarize_tabs.setter
    def notarize_tabs(self, notarize_tabs):
        """Sets the notarize_tabs of this TemplateTabs.

          # noqa: E501

        :param notarize_tabs: The notarize_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Notarize]
        """

        self._notarize_tabs = notarize_tabs

    @property
    def note_tabs(self):
        """Gets the note_tabs of this TemplateTabs.  # noqa: E501

        Specifies a location on the document where you want to place additional information, in the form of a note, for a recipient.  # noqa: E501

        :return: The note_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Note]
        """
        return self._note_tabs

    @note_tabs.setter
    def note_tabs(self, note_tabs):
        """Sets the note_tabs of this TemplateTabs.

        Specifies a location on the document where you want to place additional information, in the form of a note, for a recipient.  # noqa: E501

        :param note_tabs: The note_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Note]
        """

        self._note_tabs = note_tabs

    @property
    def number_tabs(self):
        """Gets the number_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document where you want the recipient to enter a number. It uses the same parameters as a Text tab, with the validation message and pattern set for number information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.   # noqa: E501

        :return: The number_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Number]
        """
        return self._number_tabs

    @number_tabs.setter
    def number_tabs(self, number_tabs):
        """Sets the number_tabs of this TemplateTabs.

        Specifies a tag on the document where you want the recipient to enter a number. It uses the same parameters as a Text tab, with the validation message and pattern set for number information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.   # noqa: E501

        :param number_tabs: The number_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Number]
        """

        self._number_tabs = number_tabs

    @property
    def radio_group_tabs(self):
        """Gets the radio_group_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document in a location where the recipient can select one option from a group of options using a radio button. The radio buttons do not have to be on the same page in a document.  # noqa: E501

        :return: The radio_group_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[RadioGroup]
        """
        return self._radio_group_tabs

    @radio_group_tabs.setter
    def radio_group_tabs(self, radio_group_tabs):
        """Sets the radio_group_tabs of this TemplateTabs.

        Specifies a tag on the document in a location where the recipient can select one option from a group of options using a radio button. The radio buttons do not have to be on the same page in a document.  # noqa: E501

        :param radio_group_tabs: The radio_group_tabs of this TemplateTabs.  # noqa: E501
        :type: list[RadioGroup]
        """

        self._radio_group_tabs = radio_group_tabs

    @property
    def signer_attachment_tabs(self):
        """Gets the signer_attachment_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document when you want the recipient to add supporting documents to an envelope.  # noqa: E501

        :return: The signer_attachment_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[SignerAttachment]
        """
        return self._signer_attachment_tabs

    @signer_attachment_tabs.setter
    def signer_attachment_tabs(self, signer_attachment_tabs):
        """Sets the signer_attachment_tabs of this TemplateTabs.

        Specifies a tag on the document when you want the recipient to add supporting documents to an envelope.  # noqa: E501

        :param signer_attachment_tabs: The signer_attachment_tabs of this TemplateTabs.  # noqa: E501
        :type: list[SignerAttachment]
        """

        self._signer_attachment_tabs = signer_attachment_tabs

    @property
    def sign_here_tabs(self):
        """Gets the sign_here_tabs of this TemplateTabs.  # noqa: E501

        A complex type the contains information about the tag that specifies where the recipient places their signature in the document. The \"optional\" parameter sets if the signature is required or optional.   # noqa: E501

        :return: The sign_here_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[SignHere]
        """
        return self._sign_here_tabs

    @sign_here_tabs.setter
    def sign_here_tabs(self, sign_here_tabs):
        """Sets the sign_here_tabs of this TemplateTabs.

        A complex type the contains information about the tag that specifies where the recipient places their signature in the document. The \"optional\" parameter sets if the signature is required or optional.   # noqa: E501

        :param sign_here_tabs: The sign_here_tabs of this TemplateTabs.  # noqa: E501
        :type: list[SignHere]
        """

        self._sign_here_tabs = sign_here_tabs

    @property
    def smart_section_tabs(self):
        """Gets the smart_section_tabs of this TemplateTabs.  # noqa: E501

          # noqa: E501

        :return: The smart_section_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[SmartSection]
        """
        return self._smart_section_tabs

    @smart_section_tabs.setter
    def smart_section_tabs(self, smart_section_tabs):
        """Sets the smart_section_tabs of this TemplateTabs.

          # noqa: E501

        :param smart_section_tabs: The smart_section_tabs of this TemplateTabs.  # noqa: E501
        :type: list[SmartSection]
        """

        self._smart_section_tabs = smart_section_tabs

    @property
    def ssn_tabs(self):
        """Gets the ssn_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document where you want the recipient to enter a Social Security Number (SSN). A SSN can be typed with or without dashes. It uses the same parameters as a Text tab, with the validation message and pattern set for SSN information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :return: The ssn_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Ssn]
        """
        return self._ssn_tabs

    @ssn_tabs.setter
    def ssn_tabs(self, ssn_tabs):
        """Sets the ssn_tabs of this TemplateTabs.

        Specifies a tag on the document where you want the recipient to enter a Social Security Number (SSN). A SSN can be typed with or without dashes. It uses the same parameters as a Text tab, with the validation message and pattern set for SSN information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :param ssn_tabs: The ssn_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Ssn]
        """

        self._ssn_tabs = ssn_tabs

    @property
    def text_tabs(self):
        """Gets the text_tabs of this TemplateTabs.  # noqa: E501

        Specifies a that that is an adaptable field that allows the recipient to enter different text information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :return: The text_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Text]
        """
        return self._text_tabs

    @text_tabs.setter
    def text_tabs(self, text_tabs):
        """Sets the text_tabs of this TemplateTabs.

        Specifies a that that is an adaptable field that allows the recipient to enter different text information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :param text_tabs: The text_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Text]
        """

        self._text_tabs = text_tabs

    @property
    def title_tabs(self):
        """Gets the title_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document where you want the recipient's title to appear.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :return: The title_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Title]
        """
        return self._title_tabs

    @title_tabs.setter
    def title_tabs(self, title_tabs):
        """Sets the title_tabs of this TemplateTabs.

        Specifies a tag on the document where you want the recipient's title to appear.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :param title_tabs: The title_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Title]
        """

        self._title_tabs = title_tabs

    @property
    def view_tabs(self):
        """Gets the view_tabs of this TemplateTabs.  # noqa: E501

          # noqa: E501

        :return: The view_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[View]
        """
        return self._view_tabs

    @view_tabs.setter
    def view_tabs(self, view_tabs):
        """Sets the view_tabs of this TemplateTabs.

          # noqa: E501

        :param view_tabs: The view_tabs of this TemplateTabs.  # noqa: E501
        :type: list[View]
        """

        self._view_tabs = view_tabs

    @property
    def zip_tabs(self):
        """Gets the zip_tabs of this TemplateTabs.  # noqa: E501

        Specifies a tag on the document where you want the recipient to enter a ZIP code. The ZIP code can be a five numbers or the ZIP+4 format with nine numbers. The zip code can be typed with or without dashes. It uses the same parameters as a Text tab, with the validation message and pattern set for ZIP code information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :return: The zip_tabs of this TemplateTabs.  # noqa: E501
        :rtype: list[Zip]
        """
        return self._zip_tabs

    @zip_tabs.setter
    def zip_tabs(self, zip_tabs):
        """Sets the zip_tabs of this TemplateTabs.

        Specifies a tag on the document where you want the recipient to enter a ZIP code. The ZIP code can be a five numbers or the ZIP+4 format with nine numbers. The zip code can be typed with or without dashes. It uses the same parameters as a Text tab, with the validation message and pattern set for ZIP code information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :param zip_tabs: The zip_tabs of this TemplateTabs.  # noqa: E501
        :type: list[Zip]
        """

        self._zip_tabs = zip_tabs

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
        if issubclass(TemplateTabs, dict):
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
        if not isinstance(other, TemplateTabs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateTabs):
            return True

        return self.to_dict() != other.to_dict()
