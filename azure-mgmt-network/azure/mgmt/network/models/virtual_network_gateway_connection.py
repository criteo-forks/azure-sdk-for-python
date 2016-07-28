# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class VirtualNetworkGatewayConnection(Resource):
    """A common class for general resource information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource Id
    :type id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param authorization_key: The authorizationKey.
    :type authorization_key: str
    :param virtual_network_gateway1:
    :type virtual_network_gateway1: :class:`VirtualNetworkGateway
     <azure.mgmt.network.models.VirtualNetworkGateway>`
    :param virtual_network_gateway2:
    :type virtual_network_gateway2: :class:`VirtualNetworkGateway
     <azure.mgmt.network.models.VirtualNetworkGateway>`
    :param local_network_gateway2:
    :type local_network_gateway2: :class:`LocalNetworkGateway
     <azure.mgmt.network.models.LocalNetworkGateway>`
    :param connection_type: Gateway connection type
     -Ipsec/Dedicated/VpnClient/Vnet2Vnet. Possible values include: 'IPsec',
     'Vnet2Vnet', 'ExpressRoute', 'VPNClient'
    :type connection_type: str or :class:`VirtualNetworkGatewayConnectionType
     <azure.mgmt.network.models.VirtualNetworkGatewayConnectionType>`
    :param routing_weight: The Routing weight.
    :type routing_weight: int
    :param shared_key: The Ipsec share key.
    :type shared_key: str
    :param connection_status: Virtual network Gateway connection status.
     Possible values include: 'Unknown', 'Connecting', 'Connected',
     'NotConnected'
    :type connection_status: str or
     :class:`VirtualNetworkGatewayConnectionStatus
     <azure.mgmt.network.models.VirtualNetworkGatewayConnectionStatus>`
    :param egress_bytes_transferred: The Egress Bytes Transferred in this
     connection
    :type egress_bytes_transferred: long
    :param ingress_bytes_transferred: The Ingress Bytes Transferred in this
     connection
    :type ingress_bytes_transferred: long
    :param peer: The reference to peerings resource.
    :type peer: :class:`SubResource <azure.mgmt.network.models.SubResource>`
    :param enable_bgp: EnableBgp Flag
    :type enable_bgp: bool
    :param resource_guid: Gets or sets resource guid property of the
     VirtualNetworkGatewayConnection resource
    :type resource_guid: str
    :param provisioning_state: Gets provisioning state of the
     VirtualNetworkGatewayConnection resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param etag: Gets a unique read-only string that changes whenever the
     resource is updated
    :type etag: str
    """ 

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'authorization_key': {'key': 'properties.authorizationKey', 'type': 'str'},
        'virtual_network_gateway1': {'key': 'properties.virtualNetworkGateway1', 'type': 'VirtualNetworkGateway'},
        'virtual_network_gateway2': {'key': 'properties.virtualNetworkGateway2', 'type': 'VirtualNetworkGateway'},
        'local_network_gateway2': {'key': 'properties.localNetworkGateway2', 'type': 'LocalNetworkGateway'},
        'connection_type': {'key': 'properties.connectionType', 'type': 'str'},
        'routing_weight': {'key': 'properties.routingWeight', 'type': 'int'},
        'shared_key': {'key': 'properties.sharedKey', 'type': 'str'},
        'connection_status': {'key': 'properties.connectionStatus', 'type': 'str'},
        'egress_bytes_transferred': {'key': 'properties.egressBytesTransferred', 'type': 'long'},
        'ingress_bytes_transferred': {'key': 'properties.ingressBytesTransferred', 'type': 'long'},
        'peer': {'key': 'properties.peer', 'type': 'SubResource'},
        'enable_bgp': {'key': 'properties.enableBgp', 'type': 'bool'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, location=None, tags=None, authorization_key=None, virtual_network_gateway1=None, virtual_network_gateway2=None, local_network_gateway2=None, connection_type=None, routing_weight=None, shared_key=None, connection_status=None, egress_bytes_transferred=None, ingress_bytes_transferred=None, peer=None, enable_bgp=None, resource_guid=None, provisioning_state=None, etag=None):
        super(VirtualNetworkGatewayConnection, self).__init__(id=id, location=location, tags=tags)
        self.authorization_key = authorization_key
        self.virtual_network_gateway1 = virtual_network_gateway1
        self.virtual_network_gateway2 = virtual_network_gateway2
        self.local_network_gateway2 = local_network_gateway2
        self.connection_type = connection_type
        self.routing_weight = routing_weight
        self.shared_key = shared_key
        self.connection_status = connection_status
        self.egress_bytes_transferred = egress_bytes_transferred
        self.ingress_bytes_transferred = ingress_bytes_transferred
        self.peer = peer
        self.enable_bgp = enable_bgp
        self.resource_guid = resource_guid
        self.provisioning_state = provisioning_state
        self.etag = etag