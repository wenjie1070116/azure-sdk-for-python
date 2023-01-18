# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CallConnectionStateModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the call connection."""

    UNKNOWN = "unknown"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    TRANSFERRING = "transferring"
    TRANSFER_ACCEPTED = "transferAccepted"
    DISCONNECTING = "disconnecting"
    DISCONNECTED = "disconnected"


class CallLocatorKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The call locator kind."""

    GROUP_CALL_LOCATOR = "groupCallLocator"
    SERVER_CALL_LOCATOR = "serverCallLocator"


class CallRejectReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The rejection reason."""

    NONE = "none"
    BUSY = "busy"
    FORBIDDEN = "forbidden"


class CommunicationCloudEnvironmentModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CommunicationCloudEnvironmentModel."""

    PUBLIC = "public"
    DOD = "dod"
    GCCH = "gcch"


class CommunicationIdentifierModelKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of CommunicationIdentifierModel."""

    UNKNOWN = "unknown"
    COMMUNICATION_USER = "communicationUser"
    PHONE_NUMBER = "phoneNumber"
    MICROSOFT_TEAMS_USER = "microsoftTeamsUser"


class Gender(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Voice gender type."""

    MALE = "male"
    FEMALE = "female"


class MediaStreamingAudioChannelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Audio channel type to stream, eg. unmixed audio, mixed audio."""

    MIXED = "mixed"
    UNMIXED = "unmixed"


class MediaStreamingContentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Content type to stream, eg. audio, audio/video."""

    AUDIO = "audio"


class MediaStreamingTransportType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of transport to be used for media streaming, eg. Websocket."""

    WEBSOCKET = "websocket"


class PlaySourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the type of the play source."""

    FILE = "file"
    TEXT = "text"


class RecognitionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines the sub-type of the recognize operation.
    In case of cancel operation the this field is not set and is returned empty.
    """

    DTMF = "dtmf"
    CHOICES = "choices"


class RecognizeInputType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines the type of the recognition."""

    DTMF = "dtmf"
    CHOICES = "choices"


class RecordingChannelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The channel type of call recording."""

    MIXED = "mixed"
    UNMIXED = "unmixed"


class RecordingContentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The content type of call recording."""

    AUDIO = "audio"
    AUDIO_VIDEO = "audioVideo"


class RecordingFormatType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The format type of call recording."""

    WAV = "wav"
    MP3 = "mp3"
    MP4 = "mp4"


class RecordingState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """RecordingState."""

    ACTIVE = "active"
    INACTIVE = "inactive"


class RecordingStorageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Recording storage mode. ``External`` enables bring your own storage."""

    ACS = "acs"
    AZURE_BLOB = "azureBlob"


class Tone(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tone."""

    ZERO = "zero"
    ONE = "one"
    TWO = "two"
    THREE = "three"
    FOUR = "four"
    FIVE = "five"
    SIX = "six"
    SEVEN = "seven"
    EIGHT = "eight"
    NINE = "nine"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    POUND = "pound"
    ASTERISK = "asterisk"
