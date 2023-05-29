# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.1
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


class DemoSubmission(object):
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
        'created_dt': 'datetime',
        'email': 'str',
        'submission': 'str',
        'result': 'str',
        'feedback_nozzle': 'DemoFeedbackEnum',
        'feedback_adhesion': 'DemoFeedbackEnum',
        'feedback_spaghetti': 'DemoFeedbackEnum',
        'feedback_print': 'DemoFeedbackEnum',
        'feedback_raft': 'DemoFeedbackEnum'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'email': 'email',
        'submission': 'submission',
        'result': 'result',
        'feedback_nozzle': 'feedback_nozzle',
        'feedback_adhesion': 'feedback_adhesion',
        'feedback_spaghetti': 'feedback_spaghetti',
        'feedback_print': 'feedback_print',
        'feedback_raft': 'feedback_raft'
    }

    def __init__(self, id=None, created_dt=None, email=None, submission=None, result=None, feedback_nozzle=None, feedback_adhesion=None, feedback_spaghetti=None, feedback_print=None, feedback_raft=None, local_vars_configuration=None):  # noqa: E501
        """DemoSubmission - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._email = None
        self._submission = None
        self._result = None
        self._feedback_nozzle = None
        self._feedback_adhesion = None
        self._feedback_spaghetti = None
        self._feedback_print = None
        self._feedback_raft = None
        self.discriminator = None

        self.id = id
        self.created_dt = created_dt
        self.email = email
        self.submission = submission
        self.result = result
        self.feedback_nozzle = feedback_nozzle
        self.feedback_adhesion = feedback_adhesion
        self.feedback_spaghetti = feedback_spaghetti
        self.feedback_print = feedback_print
        self.feedback_raft = feedback_raft

    @property
    def id(self):
        """Gets the id of this DemoSubmission.  # noqa: E501


        :return: The id of this DemoSubmission.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DemoSubmission.


        :param id: The id of this DemoSubmission.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this DemoSubmission.  # noqa: E501


        :return: The created_dt of this DemoSubmission.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this DemoSubmission.


        :param created_dt: The created_dt of this DemoSubmission.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def email(self):
        """Gets the email of this DemoSubmission.  # noqa: E501


        :return: The email of this DemoSubmission.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DemoSubmission.


        :param email: The email of this DemoSubmission.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501

        self._email = email

    @property
    def submission(self):
        """Gets the submission of this DemoSubmission.  # noqa: E501


        :return: The submission of this DemoSubmission.  # noqa: E501
        :rtype: str
        """
        return self._submission

    @submission.setter
    def submission(self, submission):
        """Sets the submission of this DemoSubmission.


        :param submission: The submission of this DemoSubmission.  # noqa: E501
        :type submission: str
        """
        if self.local_vars_configuration.client_side_validation and submission is None:  # noqa: E501
            raise ValueError("Invalid value for `submission`, must not be `None`")  # noqa: E501

        self._submission = submission

    @property
    def result(self):
        """Gets the result of this DemoSubmission.  # noqa: E501


        :return: The result of this DemoSubmission.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DemoSubmission.


        :param result: The result of this DemoSubmission.  # noqa: E501
        :type result: str
        """
        if self.local_vars_configuration.client_side_validation and result is None:  # noqa: E501
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def feedback_nozzle(self):
        """Gets the feedback_nozzle of this DemoSubmission.  # noqa: E501


        :return: The feedback_nozzle of this DemoSubmission.  # noqa: E501
        :rtype: DemoFeedbackEnum
        """
        return self._feedback_nozzle

    @feedback_nozzle.setter
    def feedback_nozzle(self, feedback_nozzle):
        """Sets the feedback_nozzle of this DemoSubmission.


        :param feedback_nozzle: The feedback_nozzle of this DemoSubmission.  # noqa: E501
        :type feedback_nozzle: DemoFeedbackEnum
        """

        self._feedback_nozzle = feedback_nozzle

    @property
    def feedback_adhesion(self):
        """Gets the feedback_adhesion of this DemoSubmission.  # noqa: E501


        :return: The feedback_adhesion of this DemoSubmission.  # noqa: E501
        :rtype: DemoFeedbackEnum
        """
        return self._feedback_adhesion

    @feedback_adhesion.setter
    def feedback_adhesion(self, feedback_adhesion):
        """Sets the feedback_adhesion of this DemoSubmission.


        :param feedback_adhesion: The feedback_adhesion of this DemoSubmission.  # noqa: E501
        :type feedback_adhesion: DemoFeedbackEnum
        """

        self._feedback_adhesion = feedback_adhesion

    @property
    def feedback_spaghetti(self):
        """Gets the feedback_spaghetti of this DemoSubmission.  # noqa: E501


        :return: The feedback_spaghetti of this DemoSubmission.  # noqa: E501
        :rtype: DemoFeedbackEnum
        """
        return self._feedback_spaghetti

    @feedback_spaghetti.setter
    def feedback_spaghetti(self, feedback_spaghetti):
        """Sets the feedback_spaghetti of this DemoSubmission.


        :param feedback_spaghetti: The feedback_spaghetti of this DemoSubmission.  # noqa: E501
        :type feedback_spaghetti: DemoFeedbackEnum
        """

        self._feedback_spaghetti = feedback_spaghetti

    @property
    def feedback_print(self):
        """Gets the feedback_print of this DemoSubmission.  # noqa: E501


        :return: The feedback_print of this DemoSubmission.  # noqa: E501
        :rtype: DemoFeedbackEnum
        """
        return self._feedback_print

    @feedback_print.setter
    def feedback_print(self, feedback_print):
        """Sets the feedback_print of this DemoSubmission.


        :param feedback_print: The feedback_print of this DemoSubmission.  # noqa: E501
        :type feedback_print: DemoFeedbackEnum
        """

        self._feedback_print = feedback_print

    @property
    def feedback_raft(self):
        """Gets the feedback_raft of this DemoSubmission.  # noqa: E501


        :return: The feedback_raft of this DemoSubmission.  # noqa: E501
        :rtype: DemoFeedbackEnum
        """
        return self._feedback_raft

    @feedback_raft.setter
    def feedback_raft(self, feedback_raft):
        """Sets the feedback_raft of this DemoSubmission.


        :param feedback_raft: The feedback_raft of this DemoSubmission.  # noqa: E501
        :type feedback_raft: DemoFeedbackEnum
        """

        self._feedback_raft = feedback_raft

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
        if not isinstance(other, DemoSubmission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DemoSubmission):
            return True

        return self.to_dict() != other.to_dict()
