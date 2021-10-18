# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import ArgumentsContext
from knack.commands import CommandGroup
from ._format import (transform_segments_table_output)


def load_segments_commands(cli_command_loader):
    """
    Registers the module's commands.

    :param cli_command_loader: knack command loader
    """

    with CommandGroup(cli_command_loader, 'segments', 'aui_cli.groups.segments.{}') as group:
        group.command('list', 'commands#list_segments',
                      table_transformer=transform_segments_table_output)
    with CommandGroup(cli_command_loader, 'segments', 'aui_cli.groups.segments.{}') as group:
        group.command('activate', 'commands#activate_segment')
    with CommandGroup(cli_command_loader, 'segments', 'aui_cli.groups.segments.{}') as group:
        group.command('deactivate', 'commands#deactivate_segment')


def load_segments_arguments(cli_command_loader):
    """
    Registers the commands' arguments.

    :param cli_command_loader: knack command loader
    """

    with ArgumentsContext(cli_command_loader, 'segments') as arguments:
        arguments.argument('instance_id', options_list=('--instance-id'))
    with ArgumentsContext(cli_command_loader, 'segments activate') as arguments:
        arguments.argument('segment_name', options_list=('--segment-name'))
    with ArgumentsContext(cli_command_loader, 'segments deactivate') as arguments:
        arguments.argument('segment_name', options_list=('--segment-name'))
