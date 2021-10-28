# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.6.6, generator: @autorest/python@5.6.4)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ArtifactArchitecture(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    I386 = "386"
    AMD64 = "amd64"
    ARM = "arm"
    ARM64 = "arm64"
    MIPS = "mips"
    MIPS_LE = "mipsle"
    MIPS64 = "mips64"
    MIPS64_LE = "mips64le"
    PPC64 = "ppc64"
    PPC64_LE = "ppc64le"
    RISC_V64 = "riscv64"
    S390_X = "s390x"
    WASM = "wasm"

class ArtifactManifestOrderBy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Sort options for ordering manifests in a collection.
    """

    #: Do not provide an orderby value in the request.
    NONE = "none"
    #: Order manifests by LastUpdatedOn field, from most recently updated to least recently updated.
    LAST_UPDATED_ON_DESCENDING = "timedesc"
    #: Order manifest by LastUpdatedOn field, from least recently updated to most recently updated.
    LAST_UPDATED_ON_ASCENDING = "timeasc"

class ArtifactOperatingSystem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AIX = "aix"
    ANDROID = "android"
    DARWIN = "darwin"
    DRAGONFLY = "dragonfly"
    FREE_BSD = "freebsd"
    ILLUMOS = "illumos"
    I_OS = "ios"
    JS = "js"
    LINUX = "linux"
    NET_BSD = "netbsd"
    OPEN_BSD = "openbsd"
    PLAN9 = "plan9"
    SOLARIS = "solaris"
    WINDOWS = "windows"

class ArtifactTagOrderBy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    #: Do not provide an orderby value in the request.
    NONE = "none"
    #: Order tags by LastUpdatedOn field, from most recently updated to least recently updated.
    LAST_UPDATED_ON_DESCENDING = "timedesc"
    #: Order tags by LastUpdatedOn field, from least recently updated to most recently updated.
    LAST_UPDATED_ON_ASCENDING = "timeasc"

class TokenGrantType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Grant type is expected to be refresh_token
    """

    REFRESH_TOKEN = "refresh_token"
    PASSWORD = "password"
