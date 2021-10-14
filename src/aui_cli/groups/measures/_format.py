# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


def transform_measures_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_measure_row(item))

    return table_output


def transform_measure_table_output(result):
    table_output = [_transform_measure_row(result)]

    return table_output


def _transform_measure_row(row):
    table_row = OrderedDict()
    table_row['Name'] = row['name']
    table_row['Display name'] = row['displayName']

    return table_row
