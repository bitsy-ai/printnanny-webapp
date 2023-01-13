# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.123.2
    Contact: leigh@printnanny.ai
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


class CrashReport(object):
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
        'id': 'str',
        'url': 'str',
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'description': 'str',
        'email': 'str',
        'os_version': 'str',
        'os_logs': 'str',
        'browser_version': 'str',
        'browser_logs': 'str',
        'serial': 'str',
        'posthog_session': 'str',
        'status': 'CrashReportStatusEnum',
        'support_comment': 'str',
        'user': 'int',
        'pi': 'int'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'description': 'description',
        'email': 'email',
        'os_version': 'os_version',
        'os_logs': 'os_logs',
        'browser_version': 'browser_version',
        'browser_logs': 'browser_logs',
        'serial': 'serial',
        'posthog_session': 'posthog_session',
        'status': 'status',
        'support_comment': 'support_comment',
        'user': 'user',
        'pi': 'pi'
    }

    def __init__(self, id=None, url=None, created_dt=None, updated_dt=None, description=None, email=None, os_version=None, os_logs=None, browser_version=None, browser_logs=None, serial=None, posthog_session=None, status=None, support_comment=None, user=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """CrashReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._url = None
        self._created_dt = None
        self._updated_dt = None
        self._description = None
        self._email = None
        self._os_version = None
        self._os_logs = None
        self._browser_version = None
        self._browser_logs = None
        self._serial = None
        self._posthog_session = None
        self._status = None
        self._support_comment = None
        self._user = None
        self._pi = None
        self.discriminator = None

        self.id = id
        self.url = url
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        self.description = description
        self.email = email
        self.os_version = os_version
        self.os_logs = os_logs
        self.browser_version = browser_version
        self.browser_logs = browser_logs
        self.serial = serial
        self.posthog_session = posthog_session
        if status is not None:
            self.status = status
        self.support_comment = support_comment
        self.user = user
        self.pi = pi

    @property
    def id(self):
        """Gets the id of this CrashReport.  # noqa: E501


        :return: The id of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CrashReport.


        :param id: The id of this CrashReport.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def url(self):
        """Gets the url of this CrashReport.  # noqa: E501


        :return: The url of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CrashReport.


        :param url: The url of this CrashReport.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def created_dt(self):
        """Gets the created_dt of this CrashReport.  # noqa: E501


        :return: The created_dt of this CrashReport.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this CrashReport.


        :param created_dt: The created_dt of this CrashReport.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this CrashReport.  # noqa: E501


        :return: The updated_dt of this CrashReport.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this CrashReport.


        :param updated_dt: The updated_dt of this CrashReport.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def description(self):
        """Gets the description of this CrashReport.  # noqa: E501


        :return: The description of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CrashReport.


        :param description: The description of this CrashReport.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def email(self):
        """Gets the email of this CrashReport.  # noqa: E501


        :return: The email of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CrashReport.


        :param email: The email of this CrashReport.  # noqa: E501
        :type email: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501

        self._email = email

    @property
    def os_version(self):
        """Gets the os_version of this CrashReport.  # noqa: E501


        :return: The os_version of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this CrashReport.


        :param os_version: The os_version of this CrashReport.  # noqa: E501
        :type os_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                os_version is not None and len(os_version) > 255):
            raise ValueError("Invalid value for `os_version`, length must be less than or equal to `255`")  # noqa: E501

        self._os_version = os_version

    @property
    def os_logs(self):
        """Gets the os_logs of this CrashReport.  # noqa: E501


        :return: The os_logs of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._os_logs

    @os_logs.setter
    def os_logs(self, os_logs):
        """Sets the os_logs of this CrashReport.


        :param os_logs: The os_logs of this CrashReport.  # noqa: E501
        :type os_logs: str
        """

        self._os_logs = os_logs

    @property
    def browser_version(self):
        """Gets the browser_version of this CrashReport.  # noqa: E501


        :return: The browser_version of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._browser_version

    @browser_version.setter
    def browser_version(self, browser_version):
        """Sets the browser_version of this CrashReport.


        :param browser_version: The browser_version of this CrashReport.  # noqa: E501
        :type browser_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                browser_version is not None and len(browser_version) > 255):
            raise ValueError("Invalid value for `browser_version`, length must be less than or equal to `255`")  # noqa: E501

        self._browser_version = browser_version

    @property
    def browser_logs(self):
        """Gets the browser_logs of this CrashReport.  # noqa: E501


        :return: The browser_logs of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._browser_logs

    @browser_logs.setter
    def browser_logs(self, browser_logs):
        """Sets the browser_logs of this CrashReport.


        :param browser_logs: The browser_logs of this CrashReport.  # noqa: E501
        :type browser_logs: str
        """

        self._browser_logs = browser_logs

    @property
    def serial(self):
        """Gets the serial of this CrashReport.  # noqa: E501


        :return: The serial of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this CrashReport.


        :param serial: The serial of this CrashReport.  # noqa: E501
        :type serial: str
        """
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) > 255):
            raise ValueError("Invalid value for `serial`, length must be less than or equal to `255`")  # noqa: E501

        self._serial = serial

    @property
    def posthog_session(self):
        """Gets the posthog_session of this CrashReport.  # noqa: E501


        :return: The posthog_session of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._posthog_session

    @posthog_session.setter
    def posthog_session(self, posthog_session):
        """Sets the posthog_session of this CrashReport.


        :param posthog_session: The posthog_session of this CrashReport.  # noqa: E501
        :type posthog_session: str
        """
        if (self.local_vars_configuration.client_side_validation and
                posthog_session is not None and len(posthog_session) > 255):
            raise ValueError("Invalid value for `posthog_session`, length must be less than or equal to `255`")  # noqa: E501

        self._posthog_session = posthog_session

    @property
    def status(self):
        """Gets the status of this CrashReport.  # noqa: E501


        :return: The status of this CrashReport.  # noqa: E501
        :rtype: CrashReportStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CrashReport.


        :param status: The status of this CrashReport.  # noqa: E501
        :type status: CrashReportStatusEnum
        """

        self._status = status

    @property
    def support_comment(self):
        """Gets the support_comment of this CrashReport.  # noqa: E501


        :return: The support_comment of this CrashReport.  # noqa: E501
        :rtype: str
        """
        return self._support_comment

    @support_comment.setter
    def support_comment(self, support_comment):
        """Sets the support_comment of this CrashReport.


        :param support_comment: The support_comment of this CrashReport.  # noqa: E501
        :type support_comment: str
        """

        self._support_comment = support_comment

    @property
    def user(self):
        """Gets the user of this CrashReport.  # noqa: E501


        :return: The user of this CrashReport.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CrashReport.


        :param user: The user of this CrashReport.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def pi(self):
        """Gets the pi of this CrashReport.  # noqa: E501


        :return: The pi of this CrashReport.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this CrashReport.


        :param pi: The pi of this CrashReport.  # noqa: E501
        :type pi: int
        """

        self._pi = pi

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
        if not isinstance(other, CrashReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrashReport):
            return True

        return self.to_dict() != other.to_dict()
