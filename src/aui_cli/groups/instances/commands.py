# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from aui_cli.common.exceptions import check_exception
from aui_cli.common.services import get_client, get_custom_headers


def list_instances():
    """
    Lists all instances.
    """

    client = get_client()

    response = client.get_all_instances(custom_headers=get_custom_headers())
    return check_exception(response)


def show_instance(instance_id):
    """
    Show an instance

    :param instance_id: ID of the instance
    """

    client = get_client()

    response = client.get_instance_metadata(instance_id, custom_headers=get_custom_headers())
    return check_exception(response)
