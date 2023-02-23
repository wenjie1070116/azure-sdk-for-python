# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
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


def build_list_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2017-08-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2017-08-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(workspace_setting_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2017-08-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2017-08-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "workspaceSettingName": _SERIALIZER.url("workspace_setting_name", workspace_setting_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_request(workspace_setting_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2017-08-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2017-08-01-preview")
    )
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "workspaceSettingName": _SERIALIZER.url("workspace_setting_name", workspace_setting_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_request(workspace_setting_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2017-08-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2017-08-01-preview")
    )
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "workspaceSettingName": _SERIALIZER.url("workspace_setting_name", workspace_setting_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(workspace_setting_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2017-08-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2017-08-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "workspaceSettingName": _SERIALIZER.url("workspace_setting_name", workspace_setting_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


class WorkspaceSettingsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2017_08_01_preview.SecurityCenter`'s
        :attr:`workspace_settings` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(self, **kwargs: Any) -> Iterable["_models.WorkspaceSetting"]:
        """Settings about where we should store your security data and logs. If the result is empty, it
        means that no custom-workspace configuration was set.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either WorkspaceSetting or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2017-08-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2017-08-01-preview")
        )
        cls: ClsType[_models.WorkspaceSettingList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("WorkspaceSettingList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings"}

    @distributed_trace
    def get(self, workspace_setting_name: str, **kwargs: Any) -> _models.WorkspaceSetting:
        """Settings about where we should store your security data and logs. If the result is empty, it
        means that no custom-workspace configuration was set.

        :param workspace_setting_name: Name of the security setting. Required.
        :type workspace_setting_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspaceSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting
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

        api_version: Literal["2017-08-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2017-08-01-preview")
        )
        cls: ClsType[_models.WorkspaceSetting] = kwargs.pop("cls", None)

        request = build_get_request(
            workspace_setting_name=workspace_setting_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("WorkspaceSetting", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName}"
    }

    @overload
    def create(
        self,
        workspace_setting_name: str,
        workspace_setting: _models.WorkspaceSetting,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WorkspaceSetting:
        """creating settings about where we should store your security data and logs.

        :param workspace_setting_name: Name of the security setting. Required.
        :type workspace_setting_name: str
        :param workspace_setting: Security data setting object. Required.
        :type workspace_setting: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspaceSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self,
        workspace_setting_name: str,
        workspace_setting: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WorkspaceSetting:
        """creating settings about where we should store your security data and logs.

        :param workspace_setting_name: Name of the security setting. Required.
        :type workspace_setting_name: str
        :param workspace_setting: Security data setting object. Required.
        :type workspace_setting: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspaceSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create(
        self, workspace_setting_name: str, workspace_setting: Union[_models.WorkspaceSetting, IO], **kwargs: Any
    ) -> _models.WorkspaceSetting:
        """creating settings about where we should store your security data and logs.

        :param workspace_setting_name: Name of the security setting. Required.
        :type workspace_setting_name: str
        :param workspace_setting: Security data setting object. Is either a WorkspaceSetting type or a
         IO type. Required.
        :type workspace_setting: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspaceSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting
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

        api_version: Literal["2017-08-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2017-08-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.WorkspaceSetting] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(workspace_setting, (IO, bytes)):
            _content = workspace_setting
        else:
            _json = self._serialize.body(workspace_setting, "WorkspaceSetting")

        request = build_create_request(
            workspace_setting_name=workspace_setting_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("WorkspaceSetting", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName}"
    }

    @overload
    def update(
        self,
        workspace_setting_name: str,
        workspace_setting: _models.WorkspaceSetting,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WorkspaceSetting:
        """Settings about where we should store your security data and logs.

        :param workspace_setting_name: Name of the security setting. Required.
        :type workspace_setting_name: str
        :param workspace_setting: Security data setting object. Required.
        :type workspace_setting: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspaceSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        workspace_setting_name: str,
        workspace_setting: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WorkspaceSetting:
        """Settings about where we should store your security data and logs.

        :param workspace_setting_name: Name of the security setting. Required.
        :type workspace_setting_name: str
        :param workspace_setting: Security data setting object. Required.
        :type workspace_setting: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspaceSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(
        self, workspace_setting_name: str, workspace_setting: Union[_models.WorkspaceSetting, IO], **kwargs: Any
    ) -> _models.WorkspaceSetting:
        """Settings about where we should store your security data and logs.

        :param workspace_setting_name: Name of the security setting. Required.
        :type workspace_setting_name: str
        :param workspace_setting: Security data setting object. Is either a WorkspaceSetting type or a
         IO type. Required.
        :type workspace_setting: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspaceSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.WorkspaceSetting
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

        api_version: Literal["2017-08-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2017-08-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.WorkspaceSetting] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(workspace_setting, (IO, bytes)):
            _content = workspace_setting
        else:
            _json = self._serialize.body(workspace_setting, "WorkspaceSetting")

        request = build_update_request(
            workspace_setting_name=workspace_setting_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("WorkspaceSetting", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName}"
    }

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, workspace_setting_name: str, **kwargs: Any
    ) -> None:
        """Deletes the custom workspace settings for this subscription. new VMs will report to the default
        workspace.

        :param workspace_setting_name: Name of the security setting. Required.
        :type workspace_setting_name: str
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

        api_version: Literal["2017-08-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2017-08-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            workspace_setting_name=workspace_setting_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName}"
    }
