# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import ArgumentsContext
from knack.commands import CommandGroup
from ._format import (transform_instance_table_output,
                      transform_instances_table_output)


def load_instances_commands(cli_command_loader):
    """
    Registers the module's commands.

    :param cli_command_loader: knack command loader
    """

    with CommandGroup(cli_command_loader, 'instances', 'aui_cli.groups.instances.{}') as group:
        group.command('list', 'commands#list_instances',
                      table_transformer=transform_instances_table_output)
    with CommandGroup(cli_command_loader, 'instances', 'aui_cli.groups.instances.{}') as group:
        group.command('show', 'commands#show_instance',
                      table_transformer=transform_instance_table_output)


def load_instances_arguments(cli_command_loader):
    """
    Registers the commands' arguments.

    :param cli_command_loader: knack command loader
    """

    with ArgumentsContext(cli_command_loader, 'instances show') as arguments:
        arguments.argument('instance_id', options_list=('--instance-id'))
