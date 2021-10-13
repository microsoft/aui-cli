# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CLICommandsLoader
from aui_cli.groups.instances._module import load_instances_commands, load_instances_arguments


class AuiCommandsLoader(CLICommandsLoader):
    """
    Specific command class loader for the AuI modules
    """

    def load_command_table(self, args):
        load_instances_commands(self)
        return super(AuiCommandsLoader, self).load_command_table(args)

    def load_arguments(self, command):
        load_instances_arguments(self)
        super(AuiCommandsLoader, self).load_arguments(command)
