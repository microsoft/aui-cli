# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import ArgumentsContext
from knack.commands import CommandGroup
from ._format import (transform_datasource_table_output,
                      transform_datasources_table_output)


def load_datasources_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'datasources', 'aui_cli.groups.datasources.{}') as group:
        group.command('list', 'commands#list_datasources',
                      table_transformer=transform_datasources_table_output)
    with CommandGroup(cli_command_loader, 'datasources', 'aui_cli.groups.datasources.{}') as group:
        group.command('show', 'commands#show_datasource',
                      table_transformer=transform_datasource_table_output)


def load_datasources_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'datasources list') as arguments:
        arguments.argument('instance_id', options_list=('--instance-id'))
    with ArgumentsContext(cli_command_loader, 'datasources show') as arguments:
        arguments.argument('instance_id', options_list=('--instance-id'))
        arguments.argument('data_source_id', options_list=('--datasource-id'))
