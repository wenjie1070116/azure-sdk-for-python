# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AliasPathAttributes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The attributes of the token that the alias path is referring to."""

    NONE = "None"
    """The token that the alias path is referring to has no attributes."""
    MODIFIABLE = "Modifiable"
    """The token that the alias path is referring to is modifiable by policies with 'modify' effect."""


class AliasPathTokenType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the token that the alias path is referring to."""

    NOT_SPECIFIED = "NotSpecified"
    """The token type is not specified."""
    ANY = "Any"
    """The token type can be anything."""
    STRING = "String"
    """The token type is string."""
    OBJECT = "Object"
    """The token type is object."""
    ARRAY = "Array"
    """The token type is array."""
    INTEGER = "Integer"
    """The token type is integer."""
    NUMBER = "Number"
    """The token type is number."""
    BOOLEAN = "Boolean"
    """The token type is boolean."""


class AliasPatternType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of alias pattern."""

    NOT_SPECIFIED = "NotSpecified"
    """NotSpecified is not allowed."""
    EXTRACT = "Extract"
    """Extract is the only allowed value."""


class AliasType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the alias."""

    NOT_SPECIFIED = "NotSpecified"
    """Alias type is unknown (same as not providing alias type)."""
    PLAIN_TEXT = "PlainText"
    """Alias value is not secret."""
    MASK = "Mask"
    """Alias value is secret."""


class ChangeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of change that will be made to the resource when the deployment is executed."""

    CREATE = "Create"
    """The resource does not exist in the current state but is present in the desired state. The
    #: resource will be created when the deployment is executed."""
    DELETE = "Delete"
    """The resource exists in the current state and is missing from the desired state. The resource
    #: will be deleted when the deployment is executed."""
    IGNORE = "Ignore"
    """The resource exists in the current state and is missing from the desired state. The resource
    #: will not be deployed or modified when the deployment is executed."""
    DEPLOY = "Deploy"
    """The resource exists in the current state and the desired state and will be redeployed when the
    #: deployment is executed. The properties of the resource may or may not change."""
    NO_CHANGE = "NoChange"
    """The resource exists in the current state and the desired state and will be redeployed when the
    #: deployment is executed. The properties of the resource will not change."""
    MODIFY = "Modify"
    """The resource exists in the current state and the desired state and will be redeployed when the
    #: deployment is executed. The properties of the resource will change."""
    UNSUPPORTED = "Unsupported"
    """The resource is not supported by What-If."""


class DeploymentMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The mode that is used to deploy resources. This value can be either Incremental or Complete. In
    Incremental mode, resources are deployed without deleting existing resources that are not
    included in the template. In Complete mode, resources are deployed and existing resources in
    the resource group that are not included in the template are deleted. Be careful when using
    Complete mode as you may unintentionally delete resources.
    """

    INCREMENTAL = "Incremental"
    COMPLETE = "Complete"


class ExpressionEvaluationOptionsScopeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The scope to be used for evaluation of parameters, variables and functions in a nested
    template.
    """

    NOT_SPECIFIED = "NotSpecified"
    OUTER = "Outer"
    INNER = "Inner"


class ExtendedLocationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The extended location type."""

    EDGE_ZONE = "EdgeZone"


class OnErrorDeploymentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The deployment on error behavior type. Possible values are LastSuccessful and
    SpecificDeployment.
    """

    LAST_SUCCESSFUL = "LastSuccessful"
    SPECIFIC_DEPLOYMENT = "SpecificDeployment"


class PropertyChangeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of property change."""

    CREATE = "Create"
    """The property does not exist in the current state but is present in the desired state. The
    #: property will be created when the deployment is executed."""
    DELETE = "Delete"
    """The property exists in the current state and is missing from the desired state. It will be
    #: deleted when the deployment is executed."""
    MODIFY = "Modify"
    """The property exists in both current and desired state and is different. The value of the
    #: property will change when the deployment is executed."""
    ARRAY = "Array"
    """The property is an array and contains nested changes."""
    NO_EFFECT = "NoEffect"
    """The property will not be set or updated."""


class ProviderAuthorizationConsentState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provider authorization consent state."""

    NOT_SPECIFIED = "NotSpecified"
    REQUIRED = "Required"
    NOT_REQUIRED = "NotRequired"
    CONSENTED = "Consented"


class ProvisioningOperation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of the current provisioning operation."""

    NOT_SPECIFIED = "NotSpecified"
    """The provisioning operation is not specified."""
    CREATE = "Create"
    """The provisioning operation is create."""
    DELETE = "Delete"
    """The provisioning operation is delete."""
    WAITING = "Waiting"
    """The provisioning operation is waiting."""
    AZURE_ASYNC_OPERATION_WAITING = "AzureAsyncOperationWaiting"
    """The provisioning operation is waiting Azure async operation."""
    RESOURCE_CACHE_WAITING = "ResourceCacheWaiting"
    """The provisioning operation is waiting for resource cache."""
    ACTION = "Action"
    """The provisioning operation is action."""
    READ = "Read"
    """The provisioning operation is read."""
    EVALUATE_DEPLOYMENT_OUTPUT = "EvaluateDeploymentOutput"
    """The provisioning operation is evaluate output."""
    DEPLOYMENT_CLEANUP = "DeploymentCleanup"
    """The provisioning operation is cleanup. This operation is part of the 'complete' mode
    #: deployment."""


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Denotes the state of provisioning."""

    NOT_SPECIFIED = "NotSpecified"
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    READY = "Ready"
    CREATING = "Creating"
    CREATED = "Created"
    DELETING = "Deleting"
    DELETED = "Deleted"
    CANCELED = "Canceled"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type."""

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class TagsPatchOperation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operation type for the patch API."""

    REPLACE = "Replace"
    """The 'replace' option replaces the entire set of existing tags with a new set."""
    MERGE = "Merge"
    """The 'merge' option allows adding tags with new names and updating the values of tags with
    #: existing names."""
    DELETE = "Delete"
    """The 'delete' option allows selectively deleting tags based on given names or name/value pairs."""


class WhatIfResultFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The format of the What-If results."""

    RESOURCE_ID_ONLY = "ResourceIdOnly"
    FULL_RESOURCE_PAYLOADS = "FullResourcePayloads"
