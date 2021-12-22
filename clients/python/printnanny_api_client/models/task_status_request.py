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


class TaskStatusRequest(object):
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
        'detail': 'str',
        'wiki_url': 'str',
        'status': 'TaskStatusType',
        'status_display': 'str',
        'css_class': 'str',
        'task': 'int'
    }

    attribute_map = {
        'detail': 'detail',
        'wiki_url': 'wiki_url',
        'status': 'status',
        'status_display': 'status_display',
        'css_class': 'css_class',
        'task': 'task'
    }

    def __init__(self, detail=None, wiki_url=None, status=None, status_display=None, css_class=None, task=None, local_vars_configuration=None):  # noqa: E501
        """TaskStatusRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._detail = None
        self._wiki_url = None
        self._status = None
        self._status_display = None
        self._css_class = None
        self._task = None
        self.discriminator = None

        self.detail = detail
        self.wiki_url = wiki_url
        self.status = status
        self.status_display = status_display
        self.css_class = css_class
        self.task = task

    @property
    def detail(self):
        """Gets the detail of this TaskStatusRequest.  # noqa: E501


        :return: The detail of this TaskStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this TaskStatusRequest.


        :param detail: The detail of this TaskStatusRequest.  # noqa: E501
        :type detail: str
        """
        if (self.local_vars_configuration.client_side_validation and
                detail is not None and len(detail) < 1):
            raise ValueError("Invalid value for `detail`, length must be greater than or equal to `1`")  # noqa: E501

        self._detail = detail

    @property
    def wiki_url(self):
        """Gets the wiki_url of this TaskStatusRequest.  # noqa: E501


        :return: The wiki_url of this TaskStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._wiki_url

    @wiki_url.setter
    def wiki_url(self, wiki_url):
        """Sets the wiki_url of this TaskStatusRequest.


        :param wiki_url: The wiki_url of this TaskStatusRequest.  # noqa: E501
        :type wiki_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                wiki_url is not None and len(wiki_url) < 1):
            raise ValueError("Invalid value for `wiki_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._wiki_url = wiki_url

    @property
    def status(self):
        """Gets the status of this TaskStatusRequest.  # noqa: E501


        :return: The status of this TaskStatusRequest.  # noqa: E501
        :rtype: TaskStatusType
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskStatusRequest.


        :param status: The status of this TaskStatusRequest.  # noqa: E501
        :type status: TaskStatusType
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_display(self):
        """Gets the status_display of this TaskStatusRequest.  # noqa: E501


        :return: The status_display of this TaskStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._status_display

    @status_display.setter
    def status_display(self, status_display):
        """Sets the status_display of this TaskStatusRequest.


        :param status_display: The status_display of this TaskStatusRequest.  # noqa: E501
        :type status_display: str
        """
        if self.local_vars_configuration.client_side_validation and status_display is None:  # noqa: E501
            raise ValueError("Invalid value for `status_display`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status_display is not None and len(status_display) < 1):
            raise ValueError("Invalid value for `status_display`, length must be greater than or equal to `1`")  # noqa: E501

        self._status_display = status_display

    @property
    def css_class(self):
        """Gets the css_class of this TaskStatusRequest.  # noqa: E501


        :return: The css_class of this TaskStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._css_class

    @css_class.setter
    def css_class(self, css_class):
        """Sets the css_class of this TaskStatusRequest.


        :param css_class: The css_class of this TaskStatusRequest.  # noqa: E501
        :type css_class: str
        """
        if self.local_vars_configuration.client_side_validation and css_class is None:  # noqa: E501
            raise ValueError("Invalid value for `css_class`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                css_class is not None and len(css_class) < 1):
            raise ValueError("Invalid value for `css_class`, length must be greater than or equal to `1`")  # noqa: E501

        self._css_class = css_class

    @property
    def task(self):
        """Gets the task of this TaskStatusRequest.  # noqa: E501


        :return: The task of this TaskStatusRequest.  # noqa: E501
        :rtype: int
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this TaskStatusRequest.


        :param task: The task of this TaskStatusRequest.  # noqa: E501
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
        if not isinstance(other, TaskStatusRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskStatusRequest):
            return True

        return self.to_dict() != other.to_dict()
