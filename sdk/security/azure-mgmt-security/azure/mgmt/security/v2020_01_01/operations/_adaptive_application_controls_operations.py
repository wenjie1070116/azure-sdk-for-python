# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    subscription_id: str,
    *,
    include_path_recommendations: Optional[bool] = None,
    summary: Optional[bool] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Security/applicationWhitelistings"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if include_path_recommendations is not None:
        _params["includePathRecommendations"] = _SERIALIZER.query(
            "include_path_recommendations", include_path_recommendations, "bool"
        )
    if summary is not None:
        _params["summary"] = _SERIALIZER.query("summary", summary, "bool")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(asc_location: str, group_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/applicationWhitelistings/{groupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "ascLocation": _SERIALIZER.url("asc_location", asc_location, "str"),
        "groupName": _SERIALIZER.url("group_name", group_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_put_request(asc_location: str, group_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/applicationWhitelistings/{groupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "ascLocation": _SERIALIZER.url("asc_location", asc_location, "str"),
        "groupName": _SERIALIZER.url("group_name", group_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(asc_location: str, group_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/applicationWhitelistings/{groupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "ascLocation": _SERIALIZER.url("asc_location", asc_location, "str"),
        "groupName": _SERIALIZER.url("group_name", group_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


class AdaptiveApplicationControlsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2020_01_01.SecurityCenter`'s
        :attr:`adaptive_application_controls` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self, include_path_recommendations: Optional[bool] = None, summary: Optional[bool] = None, **kwargs: Any
    ) -> _models.AdaptiveApplicationControlGroups:
        """Gets a list of application control machine groups for the subscription.

        :param include_path_recommendations: Include the policy rules. Default value is None.
        :type include_path_recommendations: bool
        :param summary: Return output in a summarized form. Default value is None.
        :type summary: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdaptiveApplicationControlGroups or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.AdaptiveApplicationControlGroups
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
        cls: ClsType[_models.AdaptiveApplicationControlGroups] = kwargs.pop("cls", None)

        request = build_list_request(
            subscription_id=self._config.subscription_id,
            include_path_recommendations=include_path_recommendations,
            summary=summary,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AdaptiveApplicationControlGroups", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/applicationWhitelistings"}

    @distributed_trace
    def get(self, asc_location: str, group_name: str, **kwargs: Any) -> _models.AdaptiveApplicationControlGroup:
        """Gets an application control VM/server group.

        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param group_name: Name of an application control machine group. Required.
        :type group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdaptiveApplicationControlGroup or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.AdaptiveApplicationControlGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
        cls: ClsType[_models.AdaptiveApplicationControlGroup] = kwargs.pop("cls", None)

        request = build_get_request(
            asc_location=asc_location,
            group_name=group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AdaptiveApplicationControlGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/applicationWhitelistings/{groupName}"
    }

    @overload
    def put(
        self,
        asc_location: str,
        group_name: str,
        body: _models.AdaptiveApplicationControlGroup,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AdaptiveApplicationControlGroup:
        """Update an application control machine group.

        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param group_name: Name of an application control machine group. Required.
        :type group_name: str
        :param body: Required.
        :type body: ~azure.mgmt.security.v2020_01_01.models.AdaptiveApplicationControlGroup
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdaptiveApplicationControlGroup or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.AdaptiveApplicationControlGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put(
        self, asc_location: str, group_name: str, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.AdaptiveApplicationControlGroup:
        """Update an application control machine group.

        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param group_name: Name of an application control machine group. Required.
        :type group_name: str
        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdaptiveApplicationControlGroup or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.AdaptiveApplicationControlGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put(
        self,
        asc_location: str,
        group_name: str,
        body: Union[_models.AdaptiveApplicationControlGroup, IO],
        **kwargs: Any
    ) -> _models.AdaptiveApplicationControlGroup:
        """Update an application control machine group.

        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param group_name: Name of an application control machine group. Required.
        :type group_name: str
        :param body: Is either a AdaptiveApplicationControlGroup type or a IO type. Required.
        :type body: ~azure.mgmt.security.v2020_01_01.models.AdaptiveApplicationControlGroup or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdaptiveApplicationControlGroup or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.AdaptiveApplicationControlGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AdaptiveApplicationControlGroup] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "AdaptiveApplicationControlGroup")

        request = build_put_request(
            asc_location=asc_location,
            group_name=group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.put.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AdaptiveApplicationControlGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/applicationWhitelistings/{groupName}"
    }

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, asc_location: str, group_name: str, **kwargs: Any
    ) -> None:
        """Delete an application control machine group.

        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param group_name: Name of an application control machine group. Required.
        :type group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            asc_location=asc_location,
            group_name=group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/applicationWhitelistings/{groupName}"
    }
