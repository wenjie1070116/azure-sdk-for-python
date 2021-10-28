# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ContainersOperations:
    """ContainersOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.containerinstance.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def list_logs(
        self,
        resource_group_name: str,
        container_group_name: str,
        container_name: str,
        tail: Optional[int] = None,
        timestamps: Optional[bool] = None,
        **kwargs: Any
    ) -> "_models.Logs":
        """Get the logs for a specified container instance.

        Get the logs for a specified container instance in a specified resource group and container
        group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param container_group_name: The name of the container group.
        :type container_group_name: str
        :param container_name: The name of the container instance.
        :type container_name: str
        :param tail: The number of lines to show from the tail of the container instance log. If not
         provided, all available logs are shown up to 4mb.
        :type tail: int
        :param timestamps: If true, adds a timestamp at the beginning of every line of log output. If
         not provided, defaults to false.
        :type timestamps: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Logs, or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.Logs
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Logs"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01"
        accept = "application/json"

        # Construct URL
        url = self.list_logs.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'containerGroupName': self._serialize.url("container_group_name", container_group_name, 'str'),
            'containerName': self._serialize.url("container_name", container_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if tail is not None:
            query_parameters['tail'] = self._serialize.query("tail", tail, 'int')
        if timestamps is not None:
            query_parameters['timestamps'] = self._serialize.query("timestamps", timestamps, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Logs', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_logs.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/logs'}  # type: ignore

    async def execute_command(
        self,
        resource_group_name: str,
        container_group_name: str,
        container_name: str,
        container_exec_request: "_models.ContainerExecRequest",
        **kwargs: Any
    ) -> "_models.ContainerExecResponse":
        """Executes a command in a specific container instance.

        Executes a command for a specific container instance in a specified resource group and
        container group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param container_group_name: The name of the container group.
        :type container_group_name: str
        :param container_name: The name of the container instance.
        :type container_name: str
        :param container_exec_request: The request for the exec command.
        :type container_exec_request: ~azure.mgmt.containerinstance.models.ContainerExecRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContainerExecResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.ContainerExecResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ContainerExecResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.execute_command.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'containerGroupName': self._serialize.url("container_group_name", container_group_name, 'str'),
            'containerName': self._serialize.url("container_name", container_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(container_exec_request, 'ContainerExecRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ContainerExecResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    execute_command.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/exec'}  # type: ignore

    async def attach(
        self,
        resource_group_name: str,
        container_group_name: str,
        container_name: str,
        **kwargs: Any
    ) -> "_models.ContainerAttachResponse":
        """Attach to the output of a specific container instance.

        Attach to the output stream of a specific container instance in a specified resource group and
        container group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param container_group_name: The name of the container group.
        :type container_group_name: str
        :param container_name: The name of the container instance.
        :type container_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContainerAttachResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.ContainerAttachResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ContainerAttachResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01"
        accept = "application/json"

        # Construct URL
        url = self.attach.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'containerGroupName': self._serialize.url("container_group_name", container_group_name, 'str'),
            'containerName': self._serialize.url("container_name", container_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ContainerAttachResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    attach.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/attach'}  # type: ignore
