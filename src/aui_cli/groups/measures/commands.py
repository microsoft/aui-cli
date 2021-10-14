# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from aui_cli.common.services import get_client, get_custom_headers


def list_measures(instance_id):
    """
    Lists all measures.

    :param instance_id: ID of the instance
    """

    client = get_client()

    return client.getalistofmeasuresmetadata(instance_id=instance_id,
                                             custom_headers=get_custom_headers())


def show_measure(instance_id, measure_name):
    """
    Show a measure

    :param instance_id: ID of the instance
    :param measure_name: name of the measure
    """

    client = get_client()

    return client.getmetadataforameasure(instance_id=instance_id,
                                         measure_name=measure_name,
                                         custom_headers=get_custom_headers())
