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

from msrest.serialization import Model


class ClassicAdministrator(Model):
    """Classic Administrators.

    :param id: The ID of the administrator.
    :type id: str
    :param name: The name of the administrator.
    :type name: str
    :param type: The type of the administrator.
    :type type: str
    :param email_address: The email address of the administrator.
    :type email_address: str
    :param role: The role of the administrator.
    :type role: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'email_address': {'key': 'properties.emailAddress', 'type': 'str'},
        'role': {'key': 'properties.role', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, name: str=None, type: str=None, email_address: str=None, role: str=None, **kwargs) -> None:
        super(ClassicAdministrator, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type
        self.email_address = email_address
        self.role = role
