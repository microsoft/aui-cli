# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import ArgumentsContext
from knack.commands import CommandGroup


def load_search_commands(cli_command_loader):
    """
    Registers the module's commands.

    :param cli_command_loader: knack command loader
    """

    with CommandGroup(cli_command_loader, 'search', 'aui_cli.groups.search.{}') as group:
        group.command('show', 'commands#show_configuration')


def load_search_arguments(cli_command_loader):
    """
    Registers the commands' arguments.

    :param cli_command_loader: knack command loader
    """

    with ArgumentsContext(cli_command_loader, 'search') as arguments:
        arguments.argument('instance_id', options_list=('--instance-id'))
