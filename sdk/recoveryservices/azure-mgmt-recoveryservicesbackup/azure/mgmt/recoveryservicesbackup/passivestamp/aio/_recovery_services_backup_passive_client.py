# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import RecoveryServicesBackupPassiveClientConfiguration
from .operations import (
    AadPropertiesOperations,
    BackupCrrJobDetailsOperations,
    BackupCrrJobsOperations,
    BackupProtectedItemsCrrOperations,
    BackupResourceStorageConfigsOperations,
    BackupUsageSummariesCRROperations,
    CrossRegionRestoreOperations,
    CrrOperationResultsOperations,
    CrrOperationStatusOperations,
    RecoveryPointsCrrOperations,
    RecoveryPointsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class RecoveryServicesBackupPassiveClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Open API 2.0 Specs for Azure RecoveryServices Backup service.

    :ivar backup_usage_summaries_crr: BackupUsageSummariesCRROperations operations
    :vartype backup_usage_summaries_crr:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.BackupUsageSummariesCRROperations
    :ivar aad_properties: AadPropertiesOperations operations
    :vartype aad_properties:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.AadPropertiesOperations
    :ivar cross_region_restore: CrossRegionRestoreOperations operations
    :vartype cross_region_restore:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.CrossRegionRestoreOperations
    :ivar backup_crr_job_details: BackupCrrJobDetailsOperations operations
    :vartype backup_crr_job_details:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.BackupCrrJobDetailsOperations
    :ivar backup_crr_jobs: BackupCrrJobsOperations operations
    :vartype backup_crr_jobs:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.BackupCrrJobsOperations
    :ivar crr_operation_results: CrrOperationResultsOperations operations
    :vartype crr_operation_results:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.CrrOperationResultsOperations
    :ivar crr_operation_status: CrrOperationStatusOperations operations
    :vartype crr_operation_status:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.CrrOperationStatusOperations
    :ivar recovery_points: RecoveryPointsOperations operations
    :vartype recovery_points:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.RecoveryPointsOperations
    :ivar backup_resource_storage_configs: BackupResourceStorageConfigsOperations operations
    :vartype backup_resource_storage_configs:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.BackupResourceStorageConfigsOperations
    :ivar recovery_points_crr: RecoveryPointsCrrOperations operations
    :vartype recovery_points_crr:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.RecoveryPointsCrrOperations
    :ivar backup_protected_items_crr: BackupProtectedItemsCrrOperations operations
    :vartype backup_protected_items_crr:
     azure.mgmt.recoveryservicesbackup.passivestamp.aio.operations.BackupProtectedItemsCrrOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription Id. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2021-11-15". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = RecoveryServicesBackupPassiveClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.backup_usage_summaries_crr = BackupUsageSummariesCRROperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.aad_properties = AadPropertiesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.cross_region_restore = CrossRegionRestoreOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.backup_crr_job_details = BackupCrrJobDetailsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.backup_crr_jobs = BackupCrrJobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.crr_operation_results = CrrOperationResultsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.crr_operation_status = CrrOperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.recovery_points = RecoveryPointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_resource_storage_configs = BackupResourceStorageConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.recovery_points_crr = RecoveryPointsCrrOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.backup_protected_items_crr = BackupProtectedItemsCrrOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "RecoveryServicesBackupPassiveClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
