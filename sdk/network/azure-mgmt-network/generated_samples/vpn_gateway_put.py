# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python vpn_gateway_put.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.vpn_gateways.begin_create_or_update(
        resource_group_name="rg1",
        gateway_name="gateway1",
        vpn_gateway_parameters={
            "location": "westcentralus",
            "properties": {
                "bgpSettings": {
                    "asn": 65515,
                    "bgpPeeringAddresses": [
                        {"customBgpIpAddresses": ["169.254.21.5"], "ipconfigurationId": "Instance0"},
                        {"customBgpIpAddresses": ["169.254.21.10"], "ipconfigurationId": "Instance1"},
                    ],
                    "peerWeight": 0,
                },
                "connections": [
                    {
                        "name": "vpnConnection1",
                        "properties": {
                            "remoteVpnSite": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/vpnSites/vpnSite1"
                            },
                            "vpnLinkConnections": [
                                {
                                    "name": "Connection-Link1",
                                    "properties": {
                                        "connectionBandwidth": 200,
                                        "egressNatRules": [
                                            {
                                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/vpnGateways/gateway1/natRules/nat03"
                                            }
                                        ],
                                        "sharedKey": "key",
                                        "vpnConnectionProtocolType": "IKEv2",
                                        "vpnSiteLink": {
                                            "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/vpnSites/vpnSite1/vpnSiteLinks/siteLink1"
                                        },
                                    },
                                }
                            ],
                        },
                    }
                ],
                "enableBgpRouteTranslationForNat": False,
                "isRoutingPreferenceInternet": False,
                "natRules": [
                    {
                        "name": "nat03",
                        "properties": {
                            "externalMappings": [{"addressSpace": "192.168.0.0/26"}],
                            "internalMappings": [{"addressSpace": "0.0.0.0/26"}],
                            "ipConfigurationId": "",
                            "mode": "EgressSnat",
                            "type": "Static",
                        },
                    }
                ],
                "virtualHub": {
                    "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualHubs/virtualHub1"
                },
            },
            "tags": {"key1": "value1"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2022-09-01/examples/VpnGatewayPut.json
if __name__ == "__main__":
    main()
