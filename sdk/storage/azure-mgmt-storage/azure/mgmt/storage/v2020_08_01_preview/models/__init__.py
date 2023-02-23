# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccountSasParameters
from ._models_py3 import ActiveDirectoryProperties
from ._models_py3 import AzureEntityResource
from ._models_py3 import AzureFilesIdentityBasedAuthentication
from ._models_py3 import BlobContainer
from ._models_py3 import BlobInventoryPolicy
from ._models_py3 import BlobInventoryPolicyDefinition
from ._models_py3 import BlobInventoryPolicyFilter
from ._models_py3 import BlobInventoryPolicyRule
from ._models_py3 import BlobInventoryPolicySchema
from ._models_py3 import BlobRestoreParameters
from ._models_py3 import BlobRestoreRange
from ._models_py3 import BlobRestoreStatus
from ._models_py3 import BlobServiceItems
from ._models_py3 import BlobServiceProperties
from ._models_py3 import ChangeFeed
from ._models_py3 import CheckNameAvailabilityResult
from ._models_py3 import CloudErrorBody
from ._models_py3 import CorsRule
from ._models_py3 import CorsRules
from ._models_py3 import CustomDomain
from ._models_py3 import DateAfterCreation
from ._models_py3 import DateAfterModification
from ._models_py3 import DeleteRetentionPolicy
from ._models_py3 import DeletedAccount
from ._models_py3 import DeletedAccountListResult
from ._models_py3 import DeletedShare
from ._models_py3 import Dimension
from ._models_py3 import Encryption
from ._models_py3 import EncryptionScope
from ._models_py3 import EncryptionScopeKeyVaultProperties
from ._models_py3 import EncryptionScopeListResult
from ._models_py3 import EncryptionService
from ._models_py3 import EncryptionServices
from ._models_py3 import Endpoints
from ._models_py3 import ErrorResponse
from ._models_py3 import ErrorResponseBody
from ._models_py3 import ExtendedLocation
from ._models_py3 import FileServiceItems
from ._models_py3 import FileServiceProperties
from ._models_py3 import FileShare
from ._models_py3 import FileShareItem
from ._models_py3 import FileShareItems
from ._models_py3 import GeoReplicationStats
from ._models_py3 import IPRule
from ._models_py3 import Identity
from ._models_py3 import ImmutabilityPolicy
from ._models_py3 import ImmutabilityPolicyProperties
from ._models_py3 import KeyVaultProperties
from ._models_py3 import LastAccessTimeTrackingPolicy
from ._models_py3 import LeaseContainerRequest
from ._models_py3 import LeaseContainerResponse
from ._models_py3 import LegalHold
from ._models_py3 import LegalHoldProperties
from ._models_py3 import ListAccountSasResponse
from ._models_py3 import ListBlobInventoryPolicy
from ._models_py3 import ListContainerItem
from ._models_py3 import ListContainerItems
from ._models_py3 import ListQueue
from ._models_py3 import ListQueueResource
from ._models_py3 import ListQueueServices
from ._models_py3 import ListServiceSasResponse
from ._models_py3 import ListTableResource
from ._models_py3 import ListTableServices
from ._models_py3 import ManagementPolicy
from ._models_py3 import ManagementPolicyAction
from ._models_py3 import ManagementPolicyBaseBlob
from ._models_py3 import ManagementPolicyDefinition
from ._models_py3 import ManagementPolicyFilter
from ._models_py3 import ManagementPolicyRule
from ._models_py3 import ManagementPolicySchema
from ._models_py3 import ManagementPolicySnapShot
from ._models_py3 import ManagementPolicyVersion
from ._models_py3 import MetricSpecification
from ._models_py3 import Multichannel
from ._models_py3 import NetworkRuleSet
from ._models_py3 import ObjectReplicationPolicies
from ._models_py3 import ObjectReplicationPolicy
from ._models_py3 import ObjectReplicationPolicyFilter
from ._models_py3 import ObjectReplicationPolicyRule
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProtocolSettings
from ._models_py3 import ProxyResource
from ._models_py3 import QueueServiceProperties
from ._models_py3 import Resource
from ._models_py3 import ResourceAccessRule
from ._models_py3 import RestorePolicyProperties
from ._models_py3 import Restriction
from ._models_py3 import RoutingPreference
from ._models_py3 import SKUCapability
from ._models_py3 import ServiceSasParameters
from ._models_py3 import ServiceSpecification
from ._models_py3 import Sku
from ._models_py3 import SkuInformation
from ._models_py3 import SmbSetting
from ._models_py3 import StorageAccount
from ._models_py3 import StorageAccountCheckNameAvailabilityParameters
from ._models_py3 import StorageAccountCreateParameters
from ._models_py3 import StorageAccountInternetEndpoints
from ._models_py3 import StorageAccountKey
from ._models_py3 import StorageAccountListKeysResult
from ._models_py3 import StorageAccountListResult
from ._models_py3 import StorageAccountMicrosoftEndpoints
from ._models_py3 import StorageAccountRegenerateKeyParameters
from ._models_py3 import StorageAccountUpdateParameters
from ._models_py3 import StorageQueue
from ._models_py3 import StorageSkuListResult
from ._models_py3 import SystemData
from ._models_py3 import Table
from ._models_py3 import TableServiceProperties
from ._models_py3 import TagFilter
from ._models_py3 import TagProperty
from ._models_py3 import TrackedResource
from ._models_py3 import UpdateHistoryProperty
from ._models_py3 import Usage
from ._models_py3 import UsageListResult
from ._models_py3 import UsageName
from ._models_py3 import VirtualNetworkRule

from ._storage_management_client_enums import AccessTier
from ._storage_management_client_enums import AccountStatus
from ._storage_management_client_enums import BlobInventoryPolicyName
from ._storage_management_client_enums import BlobRestoreProgressStatus
from ._storage_management_client_enums import Bypass
from ._storage_management_client_enums import CorsRuleAllowedMethodsItem
from ._storage_management_client_enums import CreatedByType
from ._storage_management_client_enums import DefaultAction
from ._storage_management_client_enums import DirectoryServiceOptions
from ._storage_management_client_enums import EnabledProtocols
from ._storage_management_client_enums import EncryptionScopeSource
from ._storage_management_client_enums import EncryptionScopeState
from ._storage_management_client_enums import Enum28
from ._storage_management_client_enums import ExtendedLocationTypes
from ._storage_management_client_enums import GeoReplicationStatus
from ._storage_management_client_enums import HttpProtocol
from ._storage_management_client_enums import ImmutabilityPolicyState
from ._storage_management_client_enums import ImmutabilityPolicyUpdateType
from ._storage_management_client_enums import InventoryRuleType
from ._storage_management_client_enums import KeyPermission
from ._storage_management_client_enums import KeySource
from ._storage_management_client_enums import KeyType
from ._storage_management_client_enums import Kind
from ._storage_management_client_enums import LargeFileSharesState
from ._storage_management_client_enums import LeaseContainerRequestAction
from ._storage_management_client_enums import LeaseDuration
from ._storage_management_client_enums import LeaseState
from ._storage_management_client_enums import LeaseStatus
from ._storage_management_client_enums import ListContainersInclude
from ._storage_management_client_enums import ListSharesExpand
from ._storage_management_client_enums import ManagementPolicyName
from ._storage_management_client_enums import MinimumTlsVersion
from ._storage_management_client_enums import Name
from ._storage_management_client_enums import Permissions
from ._storage_management_client_enums import PrivateEndpointConnectionProvisioningState
from ._storage_management_client_enums import PrivateEndpointServiceConnectionStatus
from ._storage_management_client_enums import ProvisioningState
from ._storage_management_client_enums import PublicAccess
from ._storage_management_client_enums import Reason
from ._storage_management_client_enums import ReasonCode
from ._storage_management_client_enums import RootSquashType
from ._storage_management_client_enums import RoutingChoice
from ._storage_management_client_enums import RuleType
from ._storage_management_client_enums import Services
from ._storage_management_client_enums import ShareAccessTier
from ._storage_management_client_enums import SignedResource
from ._storage_management_client_enums import SignedResourceTypes
from ._storage_management_client_enums import SkuName
from ._storage_management_client_enums import SkuTier
from ._storage_management_client_enums import State
from ._storage_management_client_enums import StorageAccountExpand
from ._storage_management_client_enums import UsageUnit
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccountSasParameters",
    "ActiveDirectoryProperties",
    "AzureEntityResource",
    "AzureFilesIdentityBasedAuthentication",
    "BlobContainer",
    "BlobInventoryPolicy",
    "BlobInventoryPolicyDefinition",
    "BlobInventoryPolicyFilter",
    "BlobInventoryPolicyRule",
    "BlobInventoryPolicySchema",
    "BlobRestoreParameters",
    "BlobRestoreRange",
    "BlobRestoreStatus",
    "BlobServiceItems",
    "BlobServiceProperties",
    "ChangeFeed",
    "CheckNameAvailabilityResult",
    "CloudErrorBody",
    "CorsRule",
    "CorsRules",
    "CustomDomain",
    "DateAfterCreation",
    "DateAfterModification",
    "DeleteRetentionPolicy",
    "DeletedAccount",
    "DeletedAccountListResult",
    "DeletedShare",
    "Dimension",
    "Encryption",
    "EncryptionScope",
    "EncryptionScopeKeyVaultProperties",
    "EncryptionScopeListResult",
    "EncryptionService",
    "EncryptionServices",
    "Endpoints",
    "ErrorResponse",
    "ErrorResponseBody",
    "ExtendedLocation",
    "FileServiceItems",
    "FileServiceProperties",
    "FileShare",
    "FileShareItem",
    "FileShareItems",
    "GeoReplicationStats",
    "IPRule",
    "Identity",
    "ImmutabilityPolicy",
    "ImmutabilityPolicyProperties",
    "KeyVaultProperties",
    "LastAccessTimeTrackingPolicy",
    "LeaseContainerRequest",
    "LeaseContainerResponse",
    "LegalHold",
    "LegalHoldProperties",
    "ListAccountSasResponse",
    "ListBlobInventoryPolicy",
    "ListContainerItem",
    "ListContainerItems",
    "ListQueue",
    "ListQueueResource",
    "ListQueueServices",
    "ListServiceSasResponse",
    "ListTableResource",
    "ListTableServices",
    "ManagementPolicy",
    "ManagementPolicyAction",
    "ManagementPolicyBaseBlob",
    "ManagementPolicyDefinition",
    "ManagementPolicyFilter",
    "ManagementPolicyRule",
    "ManagementPolicySchema",
    "ManagementPolicySnapShot",
    "ManagementPolicyVersion",
    "MetricSpecification",
    "Multichannel",
    "NetworkRuleSet",
    "ObjectReplicationPolicies",
    "ObjectReplicationPolicy",
    "ObjectReplicationPolicyFilter",
    "ObjectReplicationPolicyRule",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "ProtocolSettings",
    "ProxyResource",
    "QueueServiceProperties",
    "Resource",
    "ResourceAccessRule",
    "RestorePolicyProperties",
    "Restriction",
    "RoutingPreference",
    "SKUCapability",
    "ServiceSasParameters",
    "ServiceSpecification",
    "Sku",
    "SkuInformation",
    "SmbSetting",
    "StorageAccount",
    "StorageAccountCheckNameAvailabilityParameters",
    "StorageAccountCreateParameters",
    "StorageAccountInternetEndpoints",
    "StorageAccountKey",
    "StorageAccountListKeysResult",
    "StorageAccountListResult",
    "StorageAccountMicrosoftEndpoints",
    "StorageAccountRegenerateKeyParameters",
    "StorageAccountUpdateParameters",
    "StorageQueue",
    "StorageSkuListResult",
    "SystemData",
    "Table",
    "TableServiceProperties",
    "TagFilter",
    "TagProperty",
    "TrackedResource",
    "UpdateHistoryProperty",
    "Usage",
    "UsageListResult",
    "UsageName",
    "VirtualNetworkRule",
    "AccessTier",
    "AccountStatus",
    "BlobInventoryPolicyName",
    "BlobRestoreProgressStatus",
    "Bypass",
    "CorsRuleAllowedMethodsItem",
    "CreatedByType",
    "DefaultAction",
    "DirectoryServiceOptions",
    "EnabledProtocols",
    "EncryptionScopeSource",
    "EncryptionScopeState",
    "Enum28",
    "ExtendedLocationTypes",
    "GeoReplicationStatus",
    "HttpProtocol",
    "ImmutabilityPolicyState",
    "ImmutabilityPolicyUpdateType",
    "InventoryRuleType",
    "KeyPermission",
    "KeySource",
    "KeyType",
    "Kind",
    "LargeFileSharesState",
    "LeaseContainerRequestAction",
    "LeaseDuration",
    "LeaseState",
    "LeaseStatus",
    "ListContainersInclude",
    "ListSharesExpand",
    "ManagementPolicyName",
    "MinimumTlsVersion",
    "Name",
    "Permissions",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "PublicAccess",
    "Reason",
    "ReasonCode",
    "RootSquashType",
    "RoutingChoice",
    "RuleType",
    "Services",
    "ShareAccessTier",
    "SignedResource",
    "SignedResourceTypes",
    "SkuName",
    "SkuTier",
    "State",
    "StorageAccountExpand",
    "UsageUnit",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
