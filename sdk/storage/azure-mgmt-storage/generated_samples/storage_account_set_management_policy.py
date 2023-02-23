# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storage
# USAGE
    python storage_account_set_management_policy.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.management_policies.create_or_update(
        resource_group_name="res7687",
        account_name="sto9699",
        management_policy_name="default",
        properties={
            "properties": {
                "policy": {
                    "rules": [
                        {
                            "definition": {
                                "actions": {
                                    "baseBlob": {
                                        "delete": {"daysAfterModificationGreaterThan": 1000},
                                        "tierToArchive": {"daysAfterModificationGreaterThan": 90},
                                        "tierToCool": {"daysAfterModificationGreaterThan": 30},
                                    },
                                    "snapshot": {"delete": {"daysAfterCreationGreaterThan": 30}},
                                },
                                "filters": {"blobTypes": ["blockBlob"], "prefixMatch": ["olcmtestcontainer1"]},
                            },
                            "enabled": True,
                            "name": "olcmtest1",
                            "type": "Lifecycle",
                        },
                        {
                            "definition": {
                                "actions": {
                                    "baseBlob": {
                                        "delete": {"daysAfterModificationGreaterThan": 1000},
                                        "tierToArchive": {"daysAfterModificationGreaterThan": 90},
                                        "tierToCool": {"daysAfterModificationGreaterThan": 30},
                                    }
                                },
                                "filters": {
                                    "blobIndexMatch": [
                                        {"name": "tag1", "op": "==", "value": "val1"},
                                        {"name": "tag2", "op": "==", "value": "val2"},
                                    ],
                                    "blobTypes": ["blockBlob"],
                                    "prefixMatch": ["olcmtestcontainer2"],
                                },
                            },
                            "enabled": True,
                            "name": "olcmtest2",
                            "type": "Lifecycle",
                        },
                    ]
                }
            }
        },
    )
    print(response)


# x-ms-original-file: specification/storage/resource-manager/Microsoft.Storage/stable/2022-09-01/examples/StorageAccountSetManagementPolicy.json
if __name__ == "__main__":
    main()
