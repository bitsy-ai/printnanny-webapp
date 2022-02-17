# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from printnanny_api_client.configuration import Configuration


class TaskStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'status': 'TaskStatusType',
        'deleted': 'datetime',
        'created_dt': 'datetime',
        'task': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'deleted': 'deleted',
        'created_dt': 'created_dt',
        'task': 'task'
    }

    def __init__(self, id=None, status=None, deleted=None, created_dt=None, task=None, local_vars_configuration=None):  # noqa: E501
        """TaskStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._status = None
        self._deleted = None
        self._created_dt = None
        self._task = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.deleted = deleted
        self.created_dt = created_dt
        self.task = task

    @property
    def id(self):
        """Gets the id of this TaskStatus.  # noqa: E501


        :return: The id of this TaskStatus.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskStatus.


        :param id: The id of this TaskStatus.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this TaskStatus.  # noqa: E501


        :return: The status of this TaskStatus.  # noqa: E501
        :rtype: TaskStatusType
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskStatus.


        :param status: The status of this TaskStatus.  # noqa: E501
        :type status: TaskStatusType
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def deleted(self):
        """Gets the deleted of this TaskStatus.  # noqa: E501


        :return: The deleted of this TaskStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this TaskStatus.


        :param deleted: The deleted of this TaskStatus.  # noqa: E501
        :type deleted: datetime
        """
        if self.local_vars_configuration.client_side_validation and deleted is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

    @property
    def created_dt(self):
        """Gets the created_dt of this TaskStatus.  # noqa: E501


        :return: The created_dt of this TaskStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this TaskStatus.


        :param created_dt: The created_dt of this TaskStatus.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def task(self):
        """Gets the task of this TaskStatus.  # noqa: E501


        :return: The task of this TaskStatus.  # noqa: E501
        :rtype: int
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this TaskStatus.


        :param task: The task of this TaskStatus.  # noqa: E501
        :type task: int
        """
        if self.local_vars_configuration.client_side_validation and task is None:  # noqa: E501
            raise ValueError("Invalid value for `task`, must not be `None`")  # noqa: E501

        self._task = task

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskStatus):
            return True

        return self.to_dict() != other.to_dict()
