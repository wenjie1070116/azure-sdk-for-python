# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Optional, TYPE_CHECKING

from ... import _serialization

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class CloudErrorBody(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.security.v2021_01_15_preview.models.CloudErrorBody]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.security.v2021_01_15_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[CloudErrorBody]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ConnectionStrings(_serialization.Model):
    """Connection string for ingesting security data and logs.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Connection strings. Required.
    :vartype value: list[~azure.mgmt.security.v2021_01_15_preview.models.IngestionConnectionString]
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[IngestionConnectionString]"},
    }

    def __init__(self, *, value: List["_models.IngestionConnectionString"], **kwargs: Any) -> None:
        """
        :keyword value: Connection strings. Required.
        :paramtype value:
         list[~azure.mgmt.security.v2021_01_15_preview.models.IngestionConnectionString]
        """
        super().__init__(**kwargs)
        self.value = value


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class IngestionConnectionString(_serialization.Model):
    """Connection string for ingesting security data and logs.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar location: The region where ingested logs and data resides.
    :vartype location: str
    :ivar value: Connection string value.
    :vartype value: str
    """

    _validation = {
        "location": {"readonly": True},
        "value": {"readonly": True},
    }

    _attribute_map = {
        "location": {"key": "location", "type": "str"},
        "value": {"key": "value", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.location = None
        self.value = None


class Resource(_serialization.Model):
    """Describes an Azure resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class IngestionSetting(Resource):
    """Configures how to correlate scan data and logs with resources associated with the subscription.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar properties: Ingestion setting data.
    :vartype properties: JSON
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "properties": {"key": "properties", "type": "object"},
    }

    def __init__(self, *, properties: Optional[JSON] = None, **kwargs: Any) -> None:
        """
        :keyword properties: Ingestion setting data.
        :paramtype properties: JSON
        """
        super().__init__(**kwargs)
        self.properties = properties


class IngestionSettingList(_serialization.Model):
    """List of ingestion settings.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of ingestion settings.
    :vartype value: list[~azure.mgmt.security.v2021_01_15_preview.models.IngestionSetting]
    :ivar next_link: The URI to fetch the next page.
    :vartype next_link: str
    """

    _validation = {
        "value": {"readonly": True},
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[IngestionSetting]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.value = None
        self.next_link = None


class IngestionSettingToken(_serialization.Model):
    """Configures how to correlate scan data and logs with resources associated with the subscription.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar token: The token is used for correlating security data and logs with the resources in the
     subscription.
    :vartype token: str
    """

    _validation = {
        "token": {"readonly": True},
    }

    _attribute_map = {
        "token": {"key": "token", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.token = None
