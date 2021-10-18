# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


def transform_segments_table_output(result):
    """
    Formats a list of segments.

    :param result: list of segments JSON object
    """

    table_output = []
    for item in result:
        table_output.append(_transform_segment_row(item))

    return table_output


def transform_segment_table_output(result):
    """
    Formats a segment.

    :param result: segment JSON object
    """

    table_output = [_transform_segment_row(result)]

    return table_output


def _transform_segment_row(row):
    table_row = OrderedDict()
    table_row['Name'] = row['name']
    table_row['Friendly name'] = row['friendlyName']
    table_row['State'] = row['state']

    return table_row
