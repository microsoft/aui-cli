# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CLICommandsLoader
from aui_cli.groups.datasources._module import load_datasources_commands, load_datasources_arguments
from aui_cli.groups.instances._module import load_instances_commands, load_instances_arguments
from aui_cli.groups.measures._module import load_measures_commands, load_measures_arguments
from aui_cli.groups.roles._module import load_roles_commands, load_roles_arguments
from aui_cli.groups.search._module import load_search_commands, load_search_arguments
from aui_cli.groups.segments._module import load_segments_commands, load_segments_arguments


class AuiCommandsLoader(CLICommandsLoader):
    """
    Specific command class loader for the AuI modules
    """

    def load_command_table(self, args):
        load_datasources_commands(self)
        load_instances_commands(self)
        load_measures_commands(self)
        load_roles_commands(self)
        load_search_commands(self)
        load_segments_commands(self)
        return super(AuiCommandsLoader, self).load_command_table(args)

    def load_arguments(self, command):
        load_datasources_arguments(self)
        load_instances_arguments(self)
        load_measures_arguments(self)
        load_roles_arguments(self)
        load_search_arguments(self)
        load_segments_arguments(self)
        super(AuiCommandsLoader, self).load_arguments(command)
