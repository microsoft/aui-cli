# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from aui_cli.common.services import get_client, get_custom_headers


def list_roles(instance_id):
    """
    Lists all roles.

    :param instance_id: ID of the instance
    """
    client = get_client()

    return client.getallroledefinitions(instance_id=instance_id,
                                        custom_headers=get_custom_headers())


def list_role_assignments(instance_id):
    """
    Lists all role assignments.

    :param instance_id: ID of the instance
    """
    client = get_client()

    return client.getallroleassignments(instance_id=instance_id,
                                        custom_headers=get_custom_headers())


def show_user_role(instance_id):
    """
    Show current user role

    :param instance_id: ID of the instance
    """
    client = get_client()

    return client.getcurrentuserrole(instance_id=instance_id,
                                     custom_headers=get_custom_headers())
