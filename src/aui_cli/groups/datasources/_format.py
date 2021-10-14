# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


def transform_datasources_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_datasource_row(item))

    return table_output


def transform_datasource_table_output(result):
    table_output = [_transform_datasource_row(result)]

    return table_output


def _transform_datasource_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['dataSourceMetadata']['dataSourceId']
    table_row['Name'] = row['dataSourceMetadata']['name']
    table_row['Active'] = row['dataSourceMetadata']['isActive']
    table_row['Last Refresh'] = row['dataSourceMetadata']['lastRefresh']

    return table_row
