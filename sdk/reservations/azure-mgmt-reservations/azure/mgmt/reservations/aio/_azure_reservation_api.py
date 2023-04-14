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
from ._configuration import AzureReservationAPIConfiguration
from .operations import (
    AzureReservationAPIOperationsMixin,
    CalculateExchangeOperations,
    CalculateRefundOperations,
    ExchangeOperations,
    OperationOperations,
    QuotaOperations,
    QuotaRequestStatusOperations,
    ReservationOperations,
    ReservationOrderOperations,
    ReturnOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class AzureReservationAPI(
    AzureReservationAPIOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """This API describe Azure Reservation.

    :ivar reservation: ReservationOperations operations
    :vartype reservation: azure.mgmt.reservations.aio.operations.ReservationOperations
    :ivar reservation_order: ReservationOrderOperations operations
    :vartype reservation_order: azure.mgmt.reservations.aio.operations.ReservationOrderOperations
    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.reservations.aio.operations.OperationOperations
    :ivar calculate_refund: CalculateRefundOperations operations
    :vartype calculate_refund: azure.mgmt.reservations.aio.operations.CalculateRefundOperations
    :ivar return_operations: ReturnOperations operations
    :vartype return_operations: azure.mgmt.reservations.aio.operations.ReturnOperations
    :ivar calculate_exchange: CalculateExchangeOperations operations
    :vartype calculate_exchange: azure.mgmt.reservations.aio.operations.CalculateExchangeOperations
    :ivar exchange: ExchangeOperations operations
    :vartype exchange: azure.mgmt.reservations.aio.operations.ExchangeOperations
    :ivar quota: QuotaOperations operations
    :vartype quota: azure.mgmt.reservations.aio.operations.QuotaOperations
    :ivar quota_request_status: QuotaRequestStatusOperations operations
    :vartype quota_request_status:
     azure.mgmt.reservations.aio.operations.QuotaRequestStatusOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self, credential: "AsyncTokenCredential", base_url: str = "https://management.azure.com", **kwargs: Any
    ) -> None:
        self._config = AzureReservationAPIConfiguration(credential=credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.reservation = ReservationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.reservation_order = ReservationOrderOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operation = OperationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.calculate_refund = CalculateRefundOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.return_operations = ReturnOperations(self._client, self._config, self._serialize, self._deserialize)
        self.calculate_exchange = CalculateExchangeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.exchange = ExchangeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.quota = QuotaOperations(self._client, self._config, self._serialize, self._deserialize)
        self.quota_request_status = QuotaRequestStatusOperations(
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

    async def __aenter__(self) -> "AzureReservationAPI":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
