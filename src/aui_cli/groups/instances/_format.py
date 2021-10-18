# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


def transform_instances_table_output(result):
    """
    Formats a list of instances.

    :param result: list of instances JSON object
    """

    table_output = []
    for item in result:
        table_output.append(_transform_instance_row(item))

    return table_output


def transform_instance_table_output(result):
    """
    Formats an instance.

    :param result: instance JSON object
    """

    table_output = [_transform_instance_row(result)]

    return table_output


def _transform_instance_row(row):
    table_row = OrderedDict()
    table_row['Instance ID'] = row['instanceId']
    table_row['Name'] = row['name']
    table_row['Azure Region'] = row['azureRegion']

    return table_row
