# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, List, Optional, TYPE_CHECKING

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ActionGroupPatchBody(_serialization.Model):
    """A tenant action group object for the body of patch operations.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar enabled: Indicates whether this tenant action group is enabled. If a tenant action group
     is not enabled, then none of its actions will be activated.
    :vartype enabled: bool
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "enabled": {"key": "properties.enabled", "type": "bool"},
    }

    def __init__(self, *, tags: Optional[Dict[str, str]] = None, enabled: bool = True, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword enabled: Indicates whether this tenant action group is enabled. If a tenant action
         group is not enabled, then none of its actions will be activated.
        :paramtype enabled: bool
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.enabled = enabled


class AzureAppPushReceiver(_serialization.Model):
    """The Azure mobile App push notification receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar name: The name of the Azure mobile app push receiver. Names must be unique across all
     receivers within a tenant action group. Required.
    :vartype name: str
    :ivar email_address: The email address registered for the Azure mobile app. Required.
    :vartype email_address: str
    """

    _validation = {
        "name": {"required": True},
        "email_address": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "email_address": {"key": "emailAddress", "type": "str"},
    }

    def __init__(self, *, name: str, email_address: str, **kwargs: Any) -> None:
        """
        :keyword name: The name of the Azure mobile app push receiver. Names must be unique across all
         receivers within a tenant action group. Required.
        :paramtype name: str
        :keyword email_address: The email address registered for the Azure mobile app. Required.
        :paramtype email_address: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.email_address = email_address


class AzureResource(_serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class EmailReceiver(_serialization.Model):
    """An email receiver.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: The name of the email receiver. Names must be unique across all receivers within a
     tenant action group. Required.
    :vartype name: str
    :ivar email_address: The email address of this receiver. Required.
    :vartype email_address: str
    :ivar use_common_alert_schema: Indicates whether to use common alert schema.
    :vartype use_common_alert_schema: bool
    :ivar status: The receiver status of the e-mail. Known values are: "NotSpecified", "Enabled",
     and "Disabled".
    :vartype status: str or ~$(python-base-namespace).v2023_03_01_preview.models.ReceiverStatus
    """

    _validation = {
        "name": {"required": True},
        "email_address": {"required": True},
        "status": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "email_address": {"key": "emailAddress", "type": "str"},
        "use_common_alert_schema": {"key": "useCommonAlertSchema", "type": "bool"},
        "status": {"key": "status", "type": "str"},
    }

    def __init__(self, *, name: str, email_address: str, use_common_alert_schema: bool = False, **kwargs: Any) -> None:
        """
        :keyword name: The name of the email receiver. Names must be unique across all receivers within
         a tenant action group. Required.
        :paramtype name: str
        :keyword email_address: The email address of this receiver. Required.
        :paramtype email_address: str
        :keyword use_common_alert_schema: Indicates whether to use common alert schema.
        :paramtype use_common_alert_schema: bool
        """
        super().__init__(**kwargs)
        self.name = name
        self.email_address = email_address
        self.use_common_alert_schema = use_common_alert_schema
        self.status = None


class ErrorResponse(_serialization.Model):
    """Describes the format of Error response.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, code: Optional[str] = None, message: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword code: Error code.
        :paramtype code: str
        :keyword message: Error message indicating why the operation failed.
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message


class SmsReceiver(_serialization.Model):
    """An SMS receiver.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: The name of the SMS receiver. Names must be unique across all receivers within a
     tenant action group. Required.
    :vartype name: str
    :ivar country_code: The country code of the SMS receiver. Required.
    :vartype country_code: str
    :ivar phone_number: The phone number of the SMS receiver. Required.
    :vartype phone_number: str
    :ivar status: The status of the receiver. Known values are: "NotSpecified", "Enabled", and
     "Disabled".
    :vartype status: str or ~$(python-base-namespace).v2023_03_01_preview.models.ReceiverStatus
    """

    _validation = {
        "name": {"required": True},
        "country_code": {"required": True},
        "phone_number": {"required": True},
        "status": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "country_code": {"key": "countryCode", "type": "str"},
        "phone_number": {"key": "phoneNumber", "type": "str"},
        "status": {"key": "status", "type": "str"},
    }

    def __init__(self, *, name: str, country_code: str, phone_number: str, **kwargs: Any) -> None:
        """
        :keyword name: The name of the SMS receiver. Names must be unique across all receivers within a
         tenant action group. Required.
        :paramtype name: str
        :keyword country_code: The country code of the SMS receiver. Required.
        :paramtype country_code: str
        :keyword phone_number: The phone number of the SMS receiver. Required.
        :paramtype phone_number: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.country_code = country_code
        self.phone_number = phone_number
        self.status = None


class TenantActionGroupList(_serialization.Model):
    """A list of tenant action groups.

    :ivar value: The list of tenant action groups.
    :vartype value:
     list[~$(python-base-namespace).v2023_03_01_preview.models.TenantActionGroupResource]
    :ivar next_link: Provides the link to retrieve the next set of elements.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[TenantActionGroupResource]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.TenantActionGroupResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword value: The list of tenant action groups.
        :paramtype value:
         list[~$(python-base-namespace).v2023_03_01_preview.models.TenantActionGroupResource]
        :keyword next_link: Provides the link to retrieve the next set of elements.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class TenantActionGroupResource(AzureResource):  # pylint: disable=too-many-instance-attributes
    """A tenant action group resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar group_short_name: The short name of the action group. This will be used in SMS messages.
    :vartype group_short_name: str
    :ivar enabled: Indicates whether this tenant action group is enabled. If a tenant action group
     is not enabled, then none of its receivers will receive communications.
    :vartype enabled: bool
    :ivar email_receivers: The list of email receivers that are part of this tenant action group.
    :vartype email_receivers:
     list[~$(python-base-namespace).v2023_03_01_preview.models.EmailReceiver]
    :ivar sms_receivers: The list of SMS receivers that are part of this tenant action group.
    :vartype sms_receivers: list[~$(python-base-namespace).v2023_03_01_preview.models.SmsReceiver]
    :ivar webhook_receivers: The list of webhook receivers that are part of this tenant action
     group.
    :vartype webhook_receivers:
     list[~$(python-base-namespace).v2023_03_01_preview.models.WebhookReceiver]
    :ivar azure_app_push_receivers: The list of AzureAppPush receivers that are part of this tenant
     action group.
    :vartype azure_app_push_receivers:
     list[~$(python-base-namespace).v2023_03_01_preview.models.AzureAppPushReceiver]
    :ivar voice_receivers: The list of voice receivers that are part of this tenant action group.
    :vartype voice_receivers:
     list[~$(python-base-namespace).v2023_03_01_preview.models.VoiceReceiver]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
        "group_short_name": {"max_length": 12},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "group_short_name": {"key": "properties.groupShortName", "type": "str"},
        "enabled": {"key": "properties.enabled", "type": "bool"},
        "email_receivers": {"key": "properties.emailReceivers", "type": "[EmailReceiver]"},
        "sms_receivers": {"key": "properties.smsReceivers", "type": "[SmsReceiver]"},
        "webhook_receivers": {"key": "properties.webhookReceivers", "type": "[WebhookReceiver]"},
        "azure_app_push_receivers": {"key": "properties.azureAppPushReceivers", "type": "[AzureAppPushReceiver]"},
        "voice_receivers": {"key": "properties.voiceReceivers", "type": "[VoiceReceiver]"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        group_short_name: Optional[str] = None,
        enabled: bool = True,
        email_receivers: Optional[List["_models.EmailReceiver"]] = None,
        sms_receivers: Optional[List["_models.SmsReceiver"]] = None,
        webhook_receivers: Optional[List["_models.WebhookReceiver"]] = None,
        azure_app_push_receivers: Optional[List["_models.AzureAppPushReceiver"]] = None,
        voice_receivers: Optional[List["_models.VoiceReceiver"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword group_short_name: The short name of the action group. This will be used in SMS
         messages.
        :paramtype group_short_name: str
        :keyword enabled: Indicates whether this tenant action group is enabled. If a tenant action
         group is not enabled, then none of its receivers will receive communications.
        :paramtype enabled: bool
        :keyword email_receivers: The list of email receivers that are part of this tenant action
         group.
        :paramtype email_receivers:
         list[~$(python-base-namespace).v2023_03_01_preview.models.EmailReceiver]
        :keyword sms_receivers: The list of SMS receivers that are part of this tenant action group.
        :paramtype sms_receivers:
         list[~$(python-base-namespace).v2023_03_01_preview.models.SmsReceiver]
        :keyword webhook_receivers: The list of webhook receivers that are part of this tenant action
         group.
        :paramtype webhook_receivers:
         list[~$(python-base-namespace).v2023_03_01_preview.models.WebhookReceiver]
        :keyword azure_app_push_receivers: The list of AzureAppPush receivers that are part of this
         tenant action group.
        :paramtype azure_app_push_receivers:
         list[~$(python-base-namespace).v2023_03_01_preview.models.AzureAppPushReceiver]
        :keyword voice_receivers: The list of voice receivers that are part of this tenant action
         group.
        :paramtype voice_receivers:
         list[~$(python-base-namespace).v2023_03_01_preview.models.VoiceReceiver]
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.group_short_name = group_short_name
        self.enabled = enabled
        self.email_receivers = email_receivers
        self.sms_receivers = sms_receivers
        self.webhook_receivers = webhook_receivers
        self.azure_app_push_receivers = azure_app_push_receivers
        self.voice_receivers = voice_receivers


class VoiceReceiver(_serialization.Model):
    """A voice receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar name: The name of the voice receiver. Names must be unique across all receivers within a
     tenant action group. Required.
    :vartype name: str
    :ivar country_code: The country code of the voice receiver. Required.
    :vartype country_code: str
    :ivar phone_number: The phone number of the voice receiver. Required.
    :vartype phone_number: str
    """

    _validation = {
        "name": {"required": True},
        "country_code": {"required": True},
        "phone_number": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "country_code": {"key": "countryCode", "type": "str"},
        "phone_number": {"key": "phoneNumber", "type": "str"},
    }

    def __init__(self, *, name: str, country_code: str, phone_number: str, **kwargs: Any) -> None:
        """
        :keyword name: The name of the voice receiver. Names must be unique across all receivers within
         a tenant action group. Required.
        :paramtype name: str
        :keyword country_code: The country code of the voice receiver. Required.
        :paramtype country_code: str
        :keyword phone_number: The phone number of the voice receiver. Required.
        :paramtype phone_number: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.country_code = country_code
        self.phone_number = phone_number


class WebhookReceiver(_serialization.Model):
    """A webhook receiver.

    All required parameters must be populated in order to send to Azure.

    :ivar name: The name of the webhook receiver. Names must be unique across all receivers within
     a tenant action group. Required.
    :vartype name: str
    :ivar service_uri: The URI where webhooks should be sent. Required.
    :vartype service_uri: str
    :ivar use_common_alert_schema: Indicates whether to use common alert schema.
    :vartype use_common_alert_schema: bool
    :ivar use_aad_auth: Indicates whether or not use AAD authentication.
    :vartype use_aad_auth: bool
    :ivar object_id: Indicates the webhook app object Id for aad auth.
    :vartype object_id: str
    :ivar identifier_uri: Indicates the identifier uri for aad auth.
    :vartype identifier_uri: str
    :ivar tenant_id: Indicates the tenant id for aad auth.
    :vartype tenant_id: str
    """

    _validation = {
        "name": {"required": True},
        "service_uri": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "service_uri": {"key": "serviceUri", "type": "str"},
        "use_common_alert_schema": {"key": "useCommonAlertSchema", "type": "bool"},
        "use_aad_auth": {"key": "useAadAuth", "type": "bool"},
        "object_id": {"key": "objectId", "type": "str"},
        "identifier_uri": {"key": "identifierUri", "type": "str"},
        "tenant_id": {"key": "tenantId", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: str,
        service_uri: str,
        use_common_alert_schema: bool = False,
        use_aad_auth: bool = False,
        object_id: Optional[str] = None,
        identifier_uri: Optional[str] = None,
        tenant_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: The name of the webhook receiver. Names must be unique across all receivers
         within a tenant action group. Required.
        :paramtype name: str
        :keyword service_uri: The URI where webhooks should be sent. Required.
        :paramtype service_uri: str
        :keyword use_common_alert_schema: Indicates whether to use common alert schema.
        :paramtype use_common_alert_schema: bool
        :keyword use_aad_auth: Indicates whether or not use AAD authentication.
        :paramtype use_aad_auth: bool
        :keyword object_id: Indicates the webhook app object Id for aad auth.
        :paramtype object_id: str
        :keyword identifier_uri: Indicates the identifier uri for aad auth.
        :paramtype identifier_uri: str
        :keyword tenant_id: Indicates the tenant id for aad auth.
        :paramtype tenant_id: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.service_uri = service_uri
        self.use_common_alert_schema = use_common_alert_schema
        self.use_aad_auth = use_aad_auth
        self.object_id = object_id
        self.identifier_uri = identifier_uri
        self.tenant_id = tenant_id
