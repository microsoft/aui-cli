# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from aui_cli.common.exceptions import check_exception
from aui_cli.common.services import get_client, get_custom_headers


def list_segments(instance_id):
    """
    Lists all segments.

    :param instance_id: ID of the instance
    """

    client = get_client()

    response = client.get_all_segments(instance_id=instance_id,
                                       custom_headers=get_custom_headers())
    return check_exception(response)


def activate_segment(instance_id, segment_name):
    """
    Activate a segment.

    :param instance_id: ID of the instance
    :param segment_name: name of the segment
    """

    client = get_client()

    response = client.activate_segment(instance_id=instance_id,
                                       segment_name=segment_name,
                                       custom_headers=get_custom_headers())
    return check_exception(response)


def deactivate_segment(instance_id, segment_name):
    """
    Deactivate a segment.

    :param instance_id: ID of the instance
    :param segment_name: name of the segment
    """

    client = get_client()

    response = client.deactivate_segment(instance_id=instance_id,
                                         segment_name=segment_name,
                                         custom_headers=get_custom_headers())
    return check_exception(response)
