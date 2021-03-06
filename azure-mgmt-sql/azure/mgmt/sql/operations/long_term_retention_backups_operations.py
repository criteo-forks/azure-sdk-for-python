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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class LongTermRetentionBackupsOperations(object):
    """LongTermRetentionBackupsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for the request. Constant value: "2017-03-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2017-03-01-preview"

        self.config = config

    def get(
            self, location_name, long_term_retention_server_name, long_term_retention_database_name, backup_name, custom_headers=None, raw=False, **operation_config):
        """Gets a long term retention backup.

        :param location_name: The location of the database.
        :type location_name: str
        :param long_term_retention_server_name:
        :type long_term_retention_server_name: str
        :param long_term_retention_database_name:
        :type long_term_retention_database_name: str
        :param backup_name: The backup name.
        :type backup_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LongTermRetentionBackup or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.sql.models.LongTermRetentionBackup or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'locationName': self._serialize.url("location_name", location_name, 'str'),
            'longTermRetentionServerName': self._serialize.url("long_term_retention_server_name", long_term_retention_server_name, 'str'),
            'longTermRetentionDatabaseName': self._serialize.url("long_term_retention_database_name", long_term_retention_database_name, 'str'),
            'backupName': self._serialize.url("backup_name", backup_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LongTermRetentionBackup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups/{backupName}'}


    def _delete_initial(
            self, location_name, long_term_retention_server_name, long_term_retention_database_name, backup_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'locationName': self._serialize.url("location_name", location_name, 'str'),
            'longTermRetentionServerName': self._serialize.url("long_term_retention_server_name", long_term_retention_server_name, 'str'),
            'longTermRetentionDatabaseName': self._serialize.url("long_term_retention_database_name", long_term_retention_database_name, 'str'),
            'backupName': self._serialize.url("backup_name", backup_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def delete(
            self, location_name, long_term_retention_server_name, long_term_retention_database_name, backup_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Deletes a long term retention backup.

        :param location_name: The location of the database
        :type location_name: str
        :param long_term_retention_server_name:
        :type long_term_retention_server_name: str
        :param long_term_retention_database_name:
        :type long_term_retention_database_name: str
        :param backup_name: The backup name.
        :type backup_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None or
         ClientRawResponse<None> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[None]]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = self._delete_initial(
            location_name=location_name,
            long_term_retention_server_name=long_term_retention_server_name,
            long_term_retention_database_name=long_term_retention_database_name,
            backup_name=backup_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups/{backupName}'}

    def list_by_database(
            self, location_name, long_term_retention_server_name, long_term_retention_database_name, only_latest_per_database=None, database_state=None, custom_headers=None, raw=False, **operation_config):
        """Lists all long term retention backups for a database.

        :param location_name: The location of the database
        :type location_name: str
        :param long_term_retention_server_name:
        :type long_term_retention_server_name: str
        :param long_term_retention_database_name:
        :type long_term_retention_database_name: str
        :param only_latest_per_database: Whether or not to only get the latest
         backup for each database.
        :type only_latest_per_database: bool
        :param database_state: Whether to query against just live databases,
         just deleted databases, or all databases. Possible values include:
         'All', 'Live', 'Deleted'
        :type database_state: str or
         ~azure.mgmt.sql.models.LongTermRetentionDatabaseState
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of LongTermRetentionBackup
        :rtype:
         ~azure.mgmt.sql.models.LongTermRetentionBackupPaged[~azure.mgmt.sql.models.LongTermRetentionBackup]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_database.metadata['url']
                path_format_arguments = {
                    'locationName': self._serialize.url("location_name", location_name, 'str'),
                    'longTermRetentionServerName': self._serialize.url("long_term_retention_server_name", long_term_retention_server_name, 'str'),
                    'longTermRetentionDatabaseName': self._serialize.url("long_term_retention_database_name", long_term_retention_database_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if only_latest_per_database is not None:
                    query_parameters['onlyLatestPerDatabase'] = self._serialize.query("only_latest_per_database", only_latest_per_database, 'bool')
                if database_state is not None:
                    query_parameters['databaseState'] = self._serialize.query("database_state", database_state, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.LongTermRetentionBackupPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.LongTermRetentionBackupPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_database.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups'}

    def list_by_location(
            self, location_name, only_latest_per_database=None, database_state=None, custom_headers=None, raw=False, **operation_config):
        """Lists the long term retention backups for a given location.

        :param location_name: The location of the database
        :type location_name: str
        :param only_latest_per_database: Whether or not to only get the latest
         backup for each database.
        :type only_latest_per_database: bool
        :param database_state: Whether to query against just live databases,
         just deleted databases, or all databases. Possible values include:
         'All', 'Live', 'Deleted'
        :type database_state: str or
         ~azure.mgmt.sql.models.LongTermRetentionDatabaseState
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of LongTermRetentionBackup
        :rtype:
         ~azure.mgmt.sql.models.LongTermRetentionBackupPaged[~azure.mgmt.sql.models.LongTermRetentionBackup]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_location.metadata['url']
                path_format_arguments = {
                    'locationName': self._serialize.url("location_name", location_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if only_latest_per_database is not None:
                    query_parameters['onlyLatestPerDatabase'] = self._serialize.query("only_latest_per_database", only_latest_per_database, 'bool')
                if database_state is not None:
                    query_parameters['databaseState'] = self._serialize.query("database_state", database_state, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.LongTermRetentionBackupPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.LongTermRetentionBackupPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_location.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionBackups'}

    def list_by_server(
            self, location_name, long_term_retention_server_name, only_latest_per_database=None, database_state=None, custom_headers=None, raw=False, **operation_config):
        """Lists the long term retention backups for a given server.

        :param location_name: The location of the database
        :type location_name: str
        :param long_term_retention_server_name:
        :type long_term_retention_server_name: str
        :param only_latest_per_database: Whether or not to only get the latest
         backup for each database.
        :type only_latest_per_database: bool
        :param database_state: Whether to query against just live databases,
         just deleted databases, or all databases. Possible values include:
         'All', 'Live', 'Deleted'
        :type database_state: str or
         ~azure.mgmt.sql.models.LongTermRetentionDatabaseState
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of LongTermRetentionBackup
        :rtype:
         ~azure.mgmt.sql.models.LongTermRetentionBackupPaged[~azure.mgmt.sql.models.LongTermRetentionBackup]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_server.metadata['url']
                path_format_arguments = {
                    'locationName': self._serialize.url("location_name", location_name, 'str'),
                    'longTermRetentionServerName': self._serialize.url("long_term_retention_server_name", long_term_retention_server_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if only_latest_per_database is not None:
                    query_parameters['onlyLatestPerDatabase'] = self._serialize.query("only_latest_per_database", only_latest_per_database, 'bool')
                if database_state is not None:
                    query_parameters['databaseState'] = self._serialize.query("database_state", database_state, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.LongTermRetentionBackupPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.LongTermRetentionBackupPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_server.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionBackups'}
