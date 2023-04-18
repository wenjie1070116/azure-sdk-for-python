# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=protected-access

from typing import Dict, Optional

from marshmallow.exceptions import ValidationError as SchemaValidationError

from azure.ai.ml._exception_helper import log_and_raise_error
from azure.ai.ml._restclient.v2023_02_01_preview.models import ListViewType, FeaturestoreEntityVersion
from azure.ai.ml._restclient.v2023_02_01_preview import AzureMachineLearningWorkspaces as ServiceClient022023Preview
from azure.ai.ml._scope_dependent_operations import OperationConfig, OperationScope, _ScopeDependentOperations
from azure.ai.ml.exceptions import ValidationException


# from azure.ai.ml._telemetry import ActivityType, monitor_with_activity
from azure.ai.ml._utils._feature_store_utils import (
    _archive_or_restore,
)
from azure.ai.ml._utils._logger_utils import OpsLogger
from azure.ai.ml._utils._experimental import experimental
from azure.ai.ml.entities._feature_store_entity.feature_store_entity import FeatureStoreEntity
from azure.core.polling import LROPoller
from azure.core.paging import ItemPaged

ops_logger = OpsLogger(__name__)
module_logger = ops_logger.module_logger


@experimental
class FeatureStoreEntityOperations(_ScopeDependentOperations):
    """FeatureStoreEntityOperations.

    You should not instantiate this class directly. Instead, you should
    create an MLClient instance that instantiates it for you and
    attaches it as an attribute.
    """

    def __init__(
        self,
        operation_scope: OperationScope,
        operation_config: OperationConfig,
        service_client: ServiceClient022023Preview,
        **kwargs: Dict,
    ):
        super(FeatureStoreEntityOperations, self).__init__(operation_scope, operation_config)
        ops_logger.update_info(kwargs)
        self._operation = service_client.featurestore_entity_versions
        self._container_operation = service_client.featurestore_entity_containers
        self._service_client = service_client
        self._init_kwargs = kwargs

    # @monitor_with_activity(logger, "FeatureStoreEntity.List", ActivityType.PUBLICAPI)
    def list(
        self,
        *,
        name: Optional[str] = None,
        list_view_type: ListViewType = ListViewType.ACTIVE_ONLY,
    ) -> ItemPaged[FeatureStoreEntity]:
        """List the FeatureStoreEntity assets of the workspace.

        :param name: Name of a specific FeatureStoreEntity asset, optional.
        :type name: Optional[str]
        :param list_view_type: View type for including/excluding (for example) archived FeatureStoreEntity assets.
        Default: ACTIVE_ONLY.
        :type list_view_type: Optional[ListViewType]
        :return: An iterator like instance of FeatureStoreEntity objects
        :rtype: ~azure.core.paging.ItemPaged[FeatureStoreEntity]
        """
        if name:
            return self._operation.list(
                workspace_name=self._workspace_name,
                name=name,
                cls=lambda objs: [FeatureStoreEntity._from_rest_object(obj) for obj in objs],
                list_view_type=list_view_type,
                **self._scope_kwargs,
            )
        return self._container_operation.list(
            workspace_name=self._workspace_name,
            cls=lambda objs: [FeatureStoreEntity._from_container_rest_object(obj) for obj in objs],
            list_view_type=list_view_type,
            **self._scope_kwargs,
        )

    def _get(self, name: str, version: str = None) -> FeaturestoreEntityVersion:
        return self._operation.get(
            resource_group_name=self._resource_group_name,
            workspace_name=self._workspace_name,
            name=name,
            version=version,
            **self._init_kwargs,
        )

    # @monitor_with_activity(logger, "FeatureStoreEntity.Get", ActivityType.PUBLICAPI)
    def get(self, name: str, version: str) -> FeatureStoreEntity:
        """Get the specified FeatureStoreEntity asset.

        :param name: Name of FeatureStoreEntity asset.
        :type name: str
        :param version: Version of FeatureStoreEntity asset.
        :type version: str
        :raises ~azure.ai.ml.exceptions.ValidationException: Raised if FeatureStoreEntity cannot be successfully
            identified and retrieved. Details will be provided in the error message.
        :return: FeatureStoreEntity asset object.
        :rtype: ~azure.ai.ml.entities.FeatureStoreEntity
        """
        try:
            feature_store_entity_version_resource = self._get(name, version)
            return FeatureStoreEntity._from_rest_object(feature_store_entity_version_resource)
        except (ValidationException, SchemaValidationError) as ex:
            log_and_raise_error(ex)

    # @monitor_with_activity(logger, "FeatureStoreEntity.BeginCreateOrUpdate", ActivityType.PUBLICAPI)
    def begin_create_or_update(self, feature_store_entity: FeatureStoreEntity) -> LROPoller[FeatureStoreEntity]:
        """Create or update FeatureStoreEntity

        :param feature_store_entity: FeatureStoreEntity definition.
        :type feature_store_entity: FeatureStoreEntity
        :return: An instance of LROPoller that returns a FeatureStoreEntity.
        :rtype: ~azure.core.polling.LROPoller[~azure.ai.ml.entities.FeatureStoreEntity]
        """
        feature_store_entity_resource = FeatureStoreEntity._to_rest_object(feature_store_entity)

        return self._operation.begin_create_or_update(
            resource_group_name=self._resource_group_name,
            workspace_name=self._workspace_name,
            name=feature_store_entity.name,
            version=feature_store_entity.version,
            body=feature_store_entity_resource,
            cls=lambda response, deserialized, headers: FeatureStoreEntity._from_rest_object(deserialized),
        )

    # @monitor_with_activity(logger, "FeatureStoreEntity.Archive", ActivityType.PUBLICAPI)
    def archive(
        self,
        *,
        name: str,
        version: str,
        **kwargs,  # pylint:disable=unused-argument
    ) -> None:
        """Archive a FeatureStoreEntity asset.

        :param name: Name of FeatureStoreEntity asset.
        :type name: str
        :param version: Version of FeatureStoreEntity asset.
        :type version: str
        :return: None
        """

        _archive_or_restore(
            asset_operations=self,
            version_operation=self._operation,
            is_archived=True,
            name=name,
            version=version,
        )

    # @monitor_with_activity(logger, "FeatureStoreEntity.Restore", ActivityType.PUBLICAPI)
    def restore(
        self,
        *,
        name: str,
        version: str,
        **kwargs,  # pylint:disable=unused-argument
    ) -> None:
        """Restore an archived FeatureStoreEntity asset.

        :param name: Name of FeatureStoreEntity asset.
        :type name: str
        :param version: Version of FeatureStoreEntity asset.
        :type version: str
        :return: None
        """

        _archive_or_restore(
            asset_operations=self,
            version_operation=self._operation,
            is_archived=False,
            name=name,
            version=version,
        )
