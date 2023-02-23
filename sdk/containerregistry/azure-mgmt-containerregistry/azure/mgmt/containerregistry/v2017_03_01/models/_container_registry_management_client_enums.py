# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class PasswordName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The password name."""

    PASSWORD = "password"
    PASSWORD2 = "password2"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the container registry at the time the operation was called."""

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"


class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The SKU tier based on the SKU name."""

    BASIC = "Basic"
