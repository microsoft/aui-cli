# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


def transform_roles_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_role_row(item))

    return table_output


def transform_role_table_output(result):
    table_output = [_transform_role_row(result)]

    return table_output


def _transform_role_row(row):
    table_row = OrderedDict()
    table_row['Name'] = row['roleName']
    table_row['Description'] = row['description']

    return table_row
