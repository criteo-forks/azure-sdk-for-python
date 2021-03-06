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


class TaskContainerExecutionInformation(Model):
    """Contains information about the container which a task is executing.

    :param container_id: The ID of the container.
    :type container_id: str
    :param state: The state of the container. This is the state of the
     container according to the Docker service. It is equivalent to the status
     field returned by "docker inspect".
    :type state: str
    :param error: Detailed error information about the container. This is the
     detailed error string from the Docker service, if available. It is
     equivalent to the error field returned by "docker inspect".
    :type error: str
    """

    _attribute_map = {
        'container_id': {'key': 'containerId', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'error': {'key': 'error', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TaskContainerExecutionInformation, self).__init__(**kwargs)
        self.container_id = kwargs.get('container_id', None)
        self.state = kwargs.get('state', None)
        self.error = kwargs.get('error', None)
