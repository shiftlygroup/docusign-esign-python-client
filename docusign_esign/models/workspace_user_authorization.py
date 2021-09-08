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


class WorkspaceUserAuthorization(object):
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
        'can_delete': 'str',
        'can_move': 'str',
        'can_transact': 'str',
        'can_view': 'str',
        'created': 'str',
        'created_by_id': 'str',
        'error_details': 'ErrorDetails',
        'modified': 'str',
        'modified_by_id': 'str',
        'workspace_user_id': 'str',
        'workspace_user_information': 'WorkspaceUser'
    }

    attribute_map = {
        'can_delete': 'canDelete',
        'can_move': 'canMove',
        'can_transact': 'canTransact',
        'can_view': 'canView',
        'created': 'created',
        'created_by_id': 'createdById',
        'error_details': 'errorDetails',
        'modified': 'modified',
        'modified_by_id': 'modifiedById',
        'workspace_user_id': 'workspaceUserId',
        'workspace_user_information': 'workspaceUserInformation'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """WorkspaceUserAuthorization - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._can_delete = None
        self._can_move = None
        self._can_transact = None
        self._can_view = None
        self._created = None
        self._created_by_id = None
        self._error_details = None
        self._modified = None
        self._modified_by_id = None
        self._workspace_user_id = None
        self._workspace_user_information = None
        self.discriminator = None

        setattr(self, "_{}".format('can_delete'), kwargs.get('can_delete', None))
        setattr(self, "_{}".format('can_move'), kwargs.get('can_move', None))
        setattr(self, "_{}".format('can_transact'), kwargs.get('can_transact', None))
        setattr(self, "_{}".format('can_view'), kwargs.get('can_view', None))
        setattr(self, "_{}".format('created'), kwargs.get('created', None))
        setattr(self, "_{}".format('created_by_id'), kwargs.get('created_by_id', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('modified'), kwargs.get('modified', None))
        setattr(self, "_{}".format('modified_by_id'), kwargs.get('modified_by_id', None))
        setattr(self, "_{}".format('workspace_user_id'), kwargs.get('workspace_user_id', None))
        setattr(self, "_{}".format('workspace_user_information'), kwargs.get('workspace_user_information', None))

    @property
    def can_delete(self):
        """Gets the can_delete of this WorkspaceUserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The can_delete of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this WorkspaceUserAuthorization.

          # noqa: E501

        :param can_delete: The can_delete of this WorkspaceUserAuthorization.  # noqa: E501
        :type: str
        """

        self._can_delete = can_delete

    @property
    def can_move(self):
        """Gets the can_move of this WorkspaceUserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The can_move of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._can_move

    @can_move.setter
    def can_move(self, can_move):
        """Sets the can_move of this WorkspaceUserAuthorization.

          # noqa: E501

        :param can_move: The can_move of this WorkspaceUserAuthorization.  # noqa: E501
        :type: str
        """

        self._can_move = can_move

    @property
    def can_transact(self):
        """Gets the can_transact of this WorkspaceUserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The can_transact of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._can_transact

    @can_transact.setter
    def can_transact(self, can_transact):
        """Sets the can_transact of this WorkspaceUserAuthorization.

          # noqa: E501

        :param can_transact: The can_transact of this WorkspaceUserAuthorization.  # noqa: E501
        :type: str
        """

        self._can_transact = can_transact

    @property
    def can_view(self):
        """Gets the can_view of this WorkspaceUserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The can_view of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        """Sets the can_view of this WorkspaceUserAuthorization.

          # noqa: E501

        :param can_view: The can_view of this WorkspaceUserAuthorization.  # noqa: E501
        :type: str
        """

        self._can_view = can_view

    @property
    def created(self):
        """Gets the created of this WorkspaceUserAuthorization.  # noqa: E501

        The UTC DateTime when the workspace user authorization was created.  # noqa: E501

        :return: The created of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WorkspaceUserAuthorization.

        The UTC DateTime when the workspace user authorization was created.  # noqa: E501

        :param created: The created of this WorkspaceUserAuthorization.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def created_by_id(self):
        """Gets the created_by_id of this WorkspaceUserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The created_by_id of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this WorkspaceUserAuthorization.

          # noqa: E501

        :param created_by_id: The created_by_id of this WorkspaceUserAuthorization.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def error_details(self):
        """Gets the error_details of this WorkspaceUserAuthorization.  # noqa: E501


        :return: The error_details of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this WorkspaceUserAuthorization.


        :param error_details: The error_details of this WorkspaceUserAuthorization.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def modified(self):
        """Gets the modified of this WorkspaceUserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The modified of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this WorkspaceUserAuthorization.

          # noqa: E501

        :param modified: The modified of this WorkspaceUserAuthorization.  # noqa: E501
        :type: str
        """

        self._modified = modified

    @property
    def modified_by_id(self):
        """Gets the modified_by_id of this WorkspaceUserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The modified_by_id of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._modified_by_id

    @modified_by_id.setter
    def modified_by_id(self, modified_by_id):
        """Sets the modified_by_id of this WorkspaceUserAuthorization.

          # noqa: E501

        :param modified_by_id: The modified_by_id of this WorkspaceUserAuthorization.  # noqa: E501
        :type: str
        """

        self._modified_by_id = modified_by_id

    @property
    def workspace_user_id(self):
        """Gets the workspace_user_id of this WorkspaceUserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The workspace_user_id of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._workspace_user_id

    @workspace_user_id.setter
    def workspace_user_id(self, workspace_user_id):
        """Sets the workspace_user_id of this WorkspaceUserAuthorization.

          # noqa: E501

        :param workspace_user_id: The workspace_user_id of this WorkspaceUserAuthorization.  # noqa: E501
        :type: str
        """

        self._workspace_user_id = workspace_user_id

    @property
    def workspace_user_information(self):
        """Gets the workspace_user_information of this WorkspaceUserAuthorization.  # noqa: E501


        :return: The workspace_user_information of this WorkspaceUserAuthorization.  # noqa: E501
        :rtype: WorkspaceUser
        """
        return self._workspace_user_information

    @workspace_user_information.setter
    def workspace_user_information(self, workspace_user_information):
        """Sets the workspace_user_information of this WorkspaceUserAuthorization.


        :param workspace_user_information: The workspace_user_information of this WorkspaceUserAuthorization.  # noqa: E501
        :type: WorkspaceUser
        """

        self._workspace_user_information = workspace_user_information

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
        if issubclass(WorkspaceUserAuthorization, dict):
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
        if not isinstance(other, WorkspaceUserAuthorization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspaceUserAuthorization):
            return True

        return self.to_dict() != other.to_dict()
