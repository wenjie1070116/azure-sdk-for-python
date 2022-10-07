# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
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
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._advanced_threat_protection_operations import build_create_request, build_get_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AdvancedThreatProtectionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2019_01_01.aio.SecurityCenter`'s
        :attr:`advanced_threat_protection` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, resource_id: str, **kwargs: Any) -> _models.AdvancedThreatProtectionSetting:
        """Gets the Advanced Threat Protection settings for the specified resource.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :keyword setting_name: Advanced Threat Protection setting name. Default value is "current".
         Note that overriding this default value may result in unsupported behavior.
        :paramtype setting_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdvancedThreatProtectionSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-01-01"))  # type: str
        setting_name = kwargs.pop("setting_name", "current")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AdvancedThreatProtectionSetting]

        request = build_get_request(
            resource_id=resource_id,
            api_version=api_version,
            setting_name=setting_name,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AdvancedThreatProtectionSetting", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{resourceId}/providers/Microsoft.Security/advancedThreatProtectionSettings/{settingName}"}  # type: ignore

    @overload
    async def create(
        self,
        resource_id: str,
        advanced_threat_protection_setting: _models.AdvancedThreatProtectionSetting,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AdvancedThreatProtectionSetting:
        """Creates or updates the Advanced Threat Protection settings on a specified resource.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param advanced_threat_protection_setting: Advanced Threat Protection Settings. Required.
        :type advanced_threat_protection_setting:
         ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword setting_name: Advanced Threat Protection setting name. Default value is "current".
         Note that overriding this default value may result in unsupported behavior.
        :paramtype setting_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdvancedThreatProtectionSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        resource_id: str,
        advanced_threat_protection_setting: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AdvancedThreatProtectionSetting:
        """Creates or updates the Advanced Threat Protection settings on a specified resource.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param advanced_threat_protection_setting: Advanced Threat Protection Settings. Required.
        :type advanced_threat_protection_setting: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword setting_name: Advanced Threat Protection setting name. Default value is "current".
         Note that overriding this default value may result in unsupported behavior.
        :paramtype setting_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdvancedThreatProtectionSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        resource_id: str,
        advanced_threat_protection_setting: Union[_models.AdvancedThreatProtectionSetting, IO],
        **kwargs: Any
    ) -> _models.AdvancedThreatProtectionSetting:
        """Creates or updates the Advanced Threat Protection settings on a specified resource.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param advanced_threat_protection_setting: Advanced Threat Protection Settings. Is either a
         model type or a IO type. Required.
        :type advanced_threat_protection_setting:
         ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting or IO
        :keyword setting_name: Advanced Threat Protection setting name. Default value is "current".
         Note that overriding this default value may result in unsupported behavior.
        :paramtype setting_name: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdvancedThreatProtectionSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-01-01"))  # type: str
        setting_name = kwargs.pop("setting_name", "current")  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AdvancedThreatProtectionSetting]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(advanced_threat_protection_setting, (IO, bytes)):
            _content = advanced_threat_protection_setting
        else:
            _json = self._serialize.body(advanced_threat_protection_setting, "AdvancedThreatProtectionSetting")

        request = build_create_request(
            resource_id=resource_id,
            api_version=api_version,
            setting_name=setting_name,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AdvancedThreatProtectionSetting", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {"url": "/{resourceId}/providers/Microsoft.Security/advancedThreatProtectionSettings/{settingName}"}  # type: ignore
