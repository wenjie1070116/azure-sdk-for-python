# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.msi import ManagedServiceIdentityClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-msi
# USAGE
    python federated_identity_credential_delete.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ManagedServiceIdentityClient(
        credential=DefaultAzureCredential(),
        subscription_id="c267c0e7-0a73-4789-9e17-d26aeb0904e5",
    )

    response = client.federated_identity_credentials.delete(
        resource_group_name="rgName",
        resource_name="resourceName",
        federated_identity_credential_resource_name="ficResourceName",
    )
    print(response)


# x-ms-original-file: specification/msi/resource-manager/Microsoft.ManagedIdentity/stable/2023-01-31/examples/FederatedIdentityCredentialDelete.json
if __name__ == "__main__":
    main()
