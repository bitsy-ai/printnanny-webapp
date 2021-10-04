"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Window(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WINDOW_START_FIELD_NUMBER: builtins.int
    WINDOW_END_FIELD_NUMBER: builtins.int
    window_start: builtins.float = ...
    window_end: builtins.float = ...
    def __init__(self,
        *,
        window_start : builtins.float = ...,
        window_end : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"window_end",b"window_end",u"window_start",b"window_start"]) -> None: ...
global___Window = Window

class OctoprintEnvironment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_VERSION_FIELD_NUMBER: builtins.int
    PLUGIN_VERSION_FIELD_NUMBER: builtins.int
    PYTHON_VERSION_FIELD_NUMBER: builtins.int
    PIP_VERSION_FIELD_NUMBER: builtins.int
    OCTOPI_VERSION_FIELD_NUMBER: builtins.int
    OCTOPRINT_VERSION_FIELD_NUMBER: builtins.int
    VIRTUALENV_FIELD_NUMBER: builtins.int
    PLATFORM_FIELD_NUMBER: builtins.int
    BITS_FIELD_NUMBER: builtins.int
    CORES_FIELD_NUMBER: builtins.int
    FREQ_FIELD_NUMBER: builtins.int
    RAM_FIELD_NUMBER: builtins.int
    PI_MODEL_FIELD_NUMBER: builtins.int
    PI_THROTTLE_STATE_FIELD_NUMBER: builtins.int
    client_version: typing.Text = ...
    plugin_version: typing.Text = ...
    python_version: typing.Text = ...
    pip_version: typing.Text = ...
    octopi_version: typing.Text = ...
    octoprint_version: typing.Text = ...
    virtualenv: typing.Text = ...
    platform: typing.Text = ...
    bits: builtins.int = ...
    cores: builtins.int = ...
    freq: builtins.float = ...
    ram: builtins.int = ...
    pi_model: typing.Text = ...
    pi_throttle_state: typing.Text = ...
    def __init__(self,
        *,
        client_version : typing.Text = ...,
        plugin_version : typing.Text = ...,
        python_version : typing.Text = ...,
        pip_version : typing.Text = ...,
        octopi_version : typing.Text = ...,
        octoprint_version : typing.Text = ...,
        virtualenv : typing.Text = ...,
        platform : typing.Text = ...,
        bits : builtins.int = ...,
        cores : builtins.int = ...,
        freq : builtins.float = ...,
        ram : builtins.int = ...,
        pi_model : typing.Text = ...,
        pi_throttle_state : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bits",b"bits",u"client_version",b"client_version",u"cores",b"cores",u"freq",b"freq",u"octopi_version",b"octopi_version",u"octoprint_version",b"octoprint_version",u"pi_model",b"pi_model",u"pi_throttle_state",b"pi_throttle_state",u"pip_version",b"pip_version",u"platform",b"platform",u"plugin_version",b"plugin_version",u"python_version",b"python_version",u"ram",b"ram",u"virtualenv",b"virtualenv"]) -> None: ...
global___OctoprintEnvironment = OctoprintEnvironment

class PrintSession(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SESSION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    CREATED_TS_FIELD_NUMBER: builtins.int
    DATESEGMENT_FIELD_NUMBER: builtins.int
    session: typing.Text = ...
    id: builtins.int = ...
    created_ts: builtins.float = ...
    datesegment: typing.Text = ...
    def __init__(self,
        *,
        session : typing.Text = ...,
        id : builtins.int = ...,
        created_ts : builtins.float = ...,
        datesegment : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"created_ts",b"created_ts",u"datesegment",b"datesegment",u"id",b"id",u"session",b"session"]) -> None: ...
global___PrintSession = PrintSession

class Metadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TS_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    OCTOPRINT_DEVICE_ID_FIELD_NUMBER: builtins.int
    CLOUDIOT_DEVICE_ID_FIELD_NUMBER: builtins.int
    OCTOPRINT_ENVIRONMENT_FIELD_NUMBER: builtins.int
    PRINT_SESSION_FIELD_NUMBER: builtins.int
    ts: builtins.float = ...
    user_id: builtins.int = ...
    octoprint_device_id: builtins.int = ...
    cloudiot_device_id: builtins.int = ...
    @property
    def octoprint_environment(self) -> global___OctoprintEnvironment: ...
    @property
    def print_session(self) -> global___PrintSession: ...
    def __init__(self,
        *,
        ts : builtins.float = ...,
        user_id : builtins.int = ...,
        octoprint_device_id : builtins.int = ...,
        cloudiot_device_id : builtins.int = ...,
        octoprint_environment : typing.Optional[global___OctoprintEnvironment] = ...,
        print_session : typing.Optional[global___PrintSession] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"octoprint_environment",b"octoprint_environment",u"print_session",b"print_session"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cloudiot_device_id",b"cloudiot_device_id",u"octoprint_device_id",b"octoprint_device_id",u"octoprint_environment",b"octoprint_environment",u"print_session",b"print_session",u"ts",b"ts",u"user_id",b"user_id"]) -> None: ...
global___Metadata = Metadata
