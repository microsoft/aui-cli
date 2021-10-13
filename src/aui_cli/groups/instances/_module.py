# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# --------------------------------------------------------------------------------------------

from knack.arguments import ArgumentsContext
from knack.commands import CommandGroup


def load_instances_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'instances', 'aui_cli.groups.instances.{}') as group:
        group.command('list', 'commands#list_instances')


def load_instances_arguments(cli_command_loader):
    None
