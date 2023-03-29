# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=super-init-not-called

from typing import Any, Callable, List, Optional, Tuple
from azure.core.async_paging import AsyncPageIterator
from azure.core.exceptions import HttpResponseError
from .._shared.response_handlers import (
    process_storage_error,
    return_context_and_deserialized)
from .._models import QueueMessage, QueueProperties


class MessagesPaged(AsyncPageIterator):
    """An iterable of Queue Messages.

    :param Callable command: Function to retrieve the next page of items.
    :param int results_per_page: The maximum number of messages to retrieve per
        call.
    :param int max_messages: The maximum number of messages to retrieve from
        the queue.
    """

    command: Callable
    """Function to retrieve the next page of items."""
    results_per_page: int = None
    """A UTC date value representing the time the message expires."""
    max_messages: int = None
    """The maximum number of messages to retrieve from the queue."""

    def __init__(
        self, command: Callable,
        results_per_page: int = None,
        continuation_token: str = None,
        max_messages: int = None
    ) -> None:
        if continuation_token is not None:
            raise ValueError("This operation does not support continuation token")

        super(MessagesPaged, self).__init__(
            self._get_next_cb,
            self._extract_data_cb,
        )
        self._command = command
        self.results_per_page = results_per_page
        self._max_messages = max_messages

    async def _get_next_cb(self, continuation_token: str) -> Any:
        try:
            if self._max_messages is not None:
                if self.results_per_page is None:
                    self.results_per_page = 1
                if self._max_messages < 1:
                    raise StopAsyncIteration("End of paging")
                self.results_per_page = min(self.results_per_page, self._max_messages)
            return await self._command(number_of_messages=self.results_per_page)
        except HttpResponseError as error:
            process_storage_error(error)

    async def _extract_data_cb(self, messages: QueueMessage) -> Tuple[str, List[QueueMessage]]:
        # There is no concept of continuation token, so raising on my own condition
        if not messages:
            raise StopAsyncIteration("End of paging")
        if self._max_messages is not None:
            self._max_messages = self._max_messages - len(messages)
        return "TOKEN_IGNORED", [QueueMessage._from_generated(q) for q in messages]  # pylint: disable=protected-access


class QueuePropertiesPaged(AsyncPageIterator):
    """An iterable of Queue properties.

    :param Callable command: Function to retrieve the next page of items.
    :param str prefix: Filters the results to return only queues whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of queue names to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    """

    service_endpoint: str
    """The service URL."""
    prefix: str
    """A queue name prefix being used to filter the list."""
    marker: str
    """The continuation token of the current page of results."""
    results_per_page: int = None
    """The maximum number of results retrieved per API call."""
    next_marker: str
    """The continuation token to retrieve the next page of results."""
    location_mode: str
    """The location mode being used to list results. The available options include "primary" and "secondary"."""
    command: Callable
    """Function to retrieve the next page of items."""
    prefix: str = None
    """Filters the results to return only queues whose names begin with the specified prefix."""
    results_per_page: int
    """The maximum number of queue names to retrieve per
        call."""
    continuation_token: str = None
    """An opaque continuation token."""

    def __init__(
        self, command: Callable,
        prefix: str = None,
        results_per_page: int = None,
        continuation_token: str = None
    ) -> None:
        super(QueuePropertiesPaged, self).__init__(
            self._get_next_cb,
            self._extract_data_cb,
            continuation_token=continuation_token or ""
        )
        self._command = command
        self.service_endpoint = None
        self.prefix = prefix
        self.marker = None
        self.results_per_page = results_per_page
        self.location_mode = None

    async def _get_next_cb(self, continuation_token: str) -> Any:
        try:
            return await self._command(
                marker=continuation_token or None,
                maxresults=self.results_per_page,
                cls=return_context_and_deserialized,
                use_location=self.location_mode)
        except HttpResponseError as error:
            process_storage_error(error)

    async def _extract_data_cb(self, get_next_return: str) -> Tuple[Optional[str], List[QueueProperties]]:
        self.location_mode, self._response = get_next_return
        self.service_endpoint = self._response.service_endpoint
        self.prefix = self._response.prefix
        self.marker = self._response.marker
        self.results_per_page = self._response.max_results
        props_list = [QueueProperties._from_generated(q) for q in self._response.queue_items] # pylint: disable=protected-access
        return self._response.next_marker or None, props_list
