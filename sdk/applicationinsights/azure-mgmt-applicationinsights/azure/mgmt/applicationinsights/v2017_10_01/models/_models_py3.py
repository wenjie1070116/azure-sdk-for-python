# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Optional, TYPE_CHECKING

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Resource(_serialization.Model):
    """An Azure resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
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


class ApplicationInsightsComponentPricingPlan(Resource):
    """An Application Insights component pricing plan.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar plan_type: Pricing Plan Type Name.
    :vartype plan_type: str
    :ivar cap: Daily data volume cap in GB.
    :vartype cap: float
    :ivar reset_hour: Daily data volume cap UTC reset hour.
    :vartype reset_hour: int
    :ivar warning_threshold: Reserved, not used for now.
    :vartype warning_threshold: int
    :ivar stop_send_notification_when_hit_threshold: Reserved, not used for now.
    :vartype stop_send_notification_when_hit_threshold: bool
    :ivar stop_send_notification_when_hit_cap: Do not send a notification email when the daily data
     volume cap is met.
    :vartype stop_send_notification_when_hit_cap: bool
    :ivar max_history_cap: Maximum daily data volume cap that the user can set for this component.
    :vartype max_history_cap: float
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "reset_hour": {"readonly": True},
        "max_history_cap": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "plan_type": {"key": "properties.planType", "type": "str"},
        "cap": {"key": "properties.cap", "type": "float"},
        "reset_hour": {"key": "properties.resetHour", "type": "int"},
        "warning_threshold": {"key": "properties.warningThreshold", "type": "int"},
        "stop_send_notification_when_hit_threshold": {
            "key": "properties.stopSendNotificationWhenHitThreshold",
            "type": "bool",
        },
        "stop_send_notification_when_hit_cap": {"key": "properties.stopSendNotificationWhenHitCap", "type": "bool"},
        "max_history_cap": {"key": "properties.maxHistoryCap", "type": "float"},
    }

    def __init__(
        self,
        *,
        plan_type: Optional[str] = None,
        cap: Optional[float] = None,
        warning_threshold: Optional[int] = None,
        stop_send_notification_when_hit_threshold: Optional[bool] = None,
        stop_send_notification_when_hit_cap: Optional[bool] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword plan_type: Pricing Plan Type Name.
        :paramtype plan_type: str
        :keyword cap: Daily data volume cap in GB.
        :paramtype cap: float
        :keyword warning_threshold: Reserved, not used for now.
        :paramtype warning_threshold: int
        :keyword stop_send_notification_when_hit_threshold: Reserved, not used for now.
        :paramtype stop_send_notification_when_hit_threshold: bool
        :keyword stop_send_notification_when_hit_cap: Do not send a notification email when the daily
         data volume cap is met.
        :paramtype stop_send_notification_when_hit_cap: bool
        """
        super().__init__(**kwargs)
        self.plan_type = plan_type
        self.cap = cap
        self.reset_hour = None
        self.warning_threshold = warning_threshold
        self.stop_send_notification_when_hit_threshold = stop_send_notification_when_hit_threshold
        self.stop_send_notification_when_hit_cap = stop_send_notification_when_hit_cap
        self.max_history_cap = None


class CloudErrorBody(_serialization.Model):
    """An error response from the Batch service.

    :ivar code: An identifier for the error. Codes are invariant and are intended to be consumed
     programmatically.
    :vartype code: str
    :ivar message: A message describing the error, intended to be suitable for display in a user
     interface.
    :vartype message: str
    :ivar target: The target of the particular error. For example, the name of the property in
     error.
    :vartype target: str
    :ivar details: A list of additional details about the error.
    :vartype details: list[~azure.mgmt.applicationinsights.v2017_10_01.models.CloudErrorBody]
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[CloudErrorBody]"},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        details: Optional[List["_models.CloudErrorBody"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword code: An identifier for the error. Codes are invariant and are intended to be consumed
         programmatically.
        :paramtype code: str
        :keyword message: A message describing the error, intended to be suitable for display in a user
         interface.
        :paramtype message: str
        :keyword target: The target of the particular error. For example, the name of the property in
         error.
        :paramtype target: str
        :keyword details: A list of additional details about the error.
        :paramtype details: list[~azure.mgmt.applicationinsights.v2017_10_01.models.CloudErrorBody]
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class EASubscriptionMigrationDate(_serialization.Model):
    """Subscription migrate date information properties.

    :ivar is_grand_fatherable_subscription: Is subscription in the grand fatherable subscription
     list.
    :vartype is_grand_fatherable_subscription: bool
    :ivar opted_in_date: Time to start using new pricing model.
    :vartype opted_in_date: ~datetime.datetime
    """

    _attribute_map = {
        "is_grand_fatherable_subscription": {"key": "isGrandFatherableSubscription", "type": "bool"},
        "opted_in_date": {"key": "optedInDate", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        is_grand_fatherable_subscription: Optional[bool] = None,
        opted_in_date: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword is_grand_fatherable_subscription: Is subscription in the grand fatherable subscription
         list.
        :paramtype is_grand_fatherable_subscription: bool
        :keyword opted_in_date: Time to start using new pricing model.
        :paramtype opted_in_date: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.is_grand_fatherable_subscription = is_grand_fatherable_subscription
        self.opted_in_date = opted_in_date
