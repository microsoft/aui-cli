# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import ArgumentsContext
from knack.commands import CommandGroup
from ._format import (transform_measure_table_output,
                      transform_measures_table_output)


def load_measures_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'measures', 'aui_cli.groups.measures.{}') as group:
        group.command('list', 'commands#list_measures',
                      table_transformer=transform_measures_table_output)
    with CommandGroup(cli_command_loader, 'measures', 'aui_cli.groups.measures.{}') as group:
        group.command('show', 'commands#show_measure',
                      table_transformer=transform_measure_table_output)


def load_measures_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'measures list') as arguments:
        arguments.argument('instance_id', options_list=('--instance-id'))
    with ArgumentsContext(cli_command_loader, 'measures show') as arguments:
        arguments.argument('instance_id', options_list=('--instance-id'))
        arguments.argument('measure_name', options_list=('--measure-name'))
