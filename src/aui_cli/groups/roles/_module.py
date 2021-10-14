# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import ArgumentsContext
from knack.commands import CommandGroup
from ._format import (transform_roles_table_output)


def load_roles_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'roles', 'aui_cli.groups.roles.{}') as group:
        group.command('list', 'commands#list_roles',
                      table_transformer=transform_roles_table_output)
    with CommandGroup(cli_command_loader, 'roles', 'aui_cli.groups.roles.{}') as group:
        group.command('list-assignments', 'commands#list_role_assignments')
    with CommandGroup(cli_command_loader, 'roles', 'aui_cli.groups.roles.{}') as group:
        group.command('show-user-role', 'commands#show_user_role')


def load_roles_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'roles') as arguments:
        arguments.argument('instance_id', options_list=('--instance-id'))
