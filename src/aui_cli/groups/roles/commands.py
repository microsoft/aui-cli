# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from aui_cli.common.exceptions import check_exception
from aui_cli.common.services import get_client, get_custom_headers


def list_roles(instance_id):
    """
    Lists all roles.

    :param instance_id: ID of the instance
    """
    client = get_client()

    response = client.get_all_role_definitions(instance_id=instance_id,
                                               custom_headers=get_custom_headers())
    return check_exception(response)


def list_role_assignments(instance_id):
    """
    Lists all role assignments.

    :param instance_id: ID of the instance
    """
    client = get_client()

    response = client.get_all_role_assignments(instance_id=instance_id,
                                               custom_headers=get_custom_headers())
    return check_exception(response)


def show_user_role(instance_id):
    """
    Show current user role

    :param instance_id: ID of the instance
    """
    client = get_client()

    response = client.get_current_user_role(instance_id=instance_id,
                                            custom_headers=get_custom_headers())
    return check_exception(response)
