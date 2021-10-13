# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from aui_cli.common.services import get_client, get_custom_headers


def list_instances():
    """
    Lists all instances.
    """
    client = get_client()

    instances = client.getallinstances(custom_headers=get_custom_headers())
    return instances


def show_instance(instance_id):
    """
    Show an instance
    """

    client = get_client()

    instance = client.getinstancemetadata(instance_id, custom_headers=get_custom_headers())
    return instance
