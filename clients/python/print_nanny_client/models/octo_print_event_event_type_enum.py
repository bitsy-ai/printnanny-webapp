# coding: utf-8

"""
    print-nanny-client

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

from print_nanny_client.configuration import Configuration


class OctoPrintEventEventTypeEnum(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CLIENTAUTHED = "ClientAuthed"
    CLIENTCLOSED = "ClientClosed"
    CLIENTDEAUTHED = "ClientDeauthed"
    CLIENTOPENED = "ClientOpened"
    SETTINGSUPDATED = "SettingsUpdated"
    USERLOGGEDIN = "UserLoggedIn"
    USERLOGGEDOUT = "UserLoggedOut"
    FILEADDED = "FileAdded"
    FILEREMOVED = "FileRemoved"
    FOLDERADDED = "FolderAdded"
    FOLDERREMOVED = "FolderRemoved"
    TRANSFERDONE = "TransferDone"
    TRANSFERFAILED = "TransferFailed"
    TRANSFERSTARTED = "TransferStarted"
    UPDATEDFILES = "UpdatedFiles"
    UPLOAD = "Upload"
    CAPTUREDONE = "CaptureDone"
    CAPTUREFAILED = "CaptureFailed"
    CAPTURESTART = "CaptureStart"
    MOVIEDONE = "MovieDone"
    MOVIEFAILED = "MovieFailed"
    MOVIERENDERING = "MovieRendering"
    POSTROLLEND = "PostRollEnd"
    POSTROLLSTART = "PostRollStart"
    SLICINGCANCELLED = "SlicingCancelled"
    SLICINGDONE = "SlicingDone"
    SLICINGFAILED = "SlicingFailed"
    SLICINGPROFILEADDED = "SlicingProfileAdded"
    SLICINGPROFILEDELETED = "SlicingProfileDeleted"
    SLICINGPROFILEMODIFIED = "SlicingProfileModified"
    SLICINGSTARTED = "SlicingStarted"
    PRINTERPROFILEADDED = "PrinterProfileAdded"
    PRINTERPROFILEDELETED = "PrinterProfileDeleted"
    PRINTERPROFILEMODIFIED = "PrinterProfileModified"
    PRINTPROGRESS = "PrintProgress"
    PLUGIN_PI_SUPPORT_THROTTLE_STATE = "plugin_pi_support_throttle_state"
    SHUTDOWN = "Shutdown"
    STARTUP = "Startup"

    allowable_values = [CLIENTAUTHED, CLIENTCLOSED, CLIENTDEAUTHED, CLIENTOPENED, SETTINGSUPDATED, USERLOGGEDIN, USERLOGGEDOUT, FILEADDED, FILEREMOVED, FOLDERADDED, FOLDERREMOVED, TRANSFERDONE, TRANSFERFAILED, TRANSFERSTARTED, UPDATEDFILES, UPLOAD, CAPTUREDONE, CAPTUREFAILED, CAPTURESTART, MOVIEDONE, MOVIEFAILED, MOVIERENDERING, POSTROLLEND, POSTROLLSTART, SLICINGCANCELLED, SLICINGDONE, SLICINGFAILED, SLICINGPROFILEADDED, SLICINGPROFILEDELETED, SLICINGPROFILEMODIFIED, SLICINGSTARTED, PRINTERPROFILEADDED, PRINTERPROFILEDELETED, PRINTERPROFILEMODIFIED, PRINTPROGRESS, PLUGIN_PI_SUPPORT_THROTTLE_STATE, SHUTDOWN, STARTUP]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """OctoPrintEventEventTypeEnum - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, OctoPrintEventEventTypeEnum):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoPrintEventEventTypeEnum):
            return True

        return self.to_dict() != other.to_dict()
