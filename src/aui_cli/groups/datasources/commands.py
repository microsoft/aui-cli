# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from aui_cli.common.services import get_client, get_custom_headers


def list_datasources(instance_id):
    """
    Lists all data sources.

    :param instance_id: ID of the instance
    """

    client = get_client()

    return client.get_all_entity_metadata(instance_id=instance_id,
                                          custom_headers=get_custom_headers())


def show_datasource(instance_id, data_source_id):
    """
    Show a data source

    :param instance_id: ID of the instance
    :param data_source_id: ID of the data source
    """

    client = get_client()

    return client.get_data_source(instance_id=instance_id,
                                  data_source_id=data_source_id,
                                  custom_headers=get_custom_headers())
