# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.cosmosdb import CosmosDBManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cosmosdb
# USAGE
    python cosmos_db_restorable_database_account_get.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CosmosDBManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.restorable_database_accounts.get_by_location(
        location="West US",
        instance_id="d9b26648-2f53-4541-b3d8-3044f4f9810d",
    )
    print(response)


# x-ms-original-file: specification/cosmos-db/resource-manager/Microsoft.DocumentDB/preview/2022-11-15-preview/examples/CosmosDBRestorableDatabaseAccountGet.json
if __name__ == "__main__":
    main()
