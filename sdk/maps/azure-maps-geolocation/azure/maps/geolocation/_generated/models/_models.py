# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional, TYPE_CHECKING

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class CountryRegion(_serialization.Model):
    """The object containing the country/region information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar iso_code: The IP Address's 2-character code `(ISO 3166-1)
     <https://www.iso.org/iso-3166-country-codes.html>`_ of the country or region. Please note, IP
     address in ranges reserved for special purpose will return Null for country/region.
    :vartype iso_code: str
    """

    _validation = {
        'iso_code': {'readonly': True},
    }

    _attribute_map = {
        "iso_code": {"key": "isoCode", "type": "str"},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super().__init__(**kwargs)
        self.iso_code = None


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.maps.geolocation.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.maps.geolocation.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorDetail]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~azure.maps.geolocation.models.ErrorDetail
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorDetail"},
    }

    def __init__(
        self,
        *,
        error: Optional["_models.ErrorDetail"] = None,
        **kwargs
    ):
        """
        :keyword error: The error object.
        :paramtype error: ~azure.maps.geolocation.models.ErrorDetail
        """
        super().__init__(**kwargs)
        self.error = error


class IpAddressToLocationResult(_serialization.Model):
    """This object is returned from a successful call to IP Address to country/region API.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar country_region: The object containing the country/region information.
    :vartype country_region: ~azure.maps.geolocation.models.CountryRegion
    :ivar ip_address: The IP Address of the request.
    :vartype ip_address: str
    """

    _validation = {
        'country_region': {'readonly': True},
        'ip_address': {'readonly': True},
    }

    _attribute_map = {
        "country_region": {"key": "countryRegion", "type": "CountryRegion"},
        "ip_address": {"key": "ipAddress", "type": "str"},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super().__init__(**kwargs)
        self.country_region = None
        self.ip_address = None
