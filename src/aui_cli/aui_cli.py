# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

from knack import CLI
from .common.config import CLI_ENV_VARIABLE_PREFIX, GLOBAL_CONFIG_DIR
from .aui_commands import AuiCommandsLoader
from .aui_help import AuiHelp

CLI_NAME = "aui-cli"


class AuiCLI(CLI):
    """
    Main class for the AuI Exports CLI.
    """

    def __init__(self):
        super(AuiCLI, self).__init__(cli_name=CLI_NAME,
                                     config_dir=GLOBAL_CONFIG_DIR,
                                     config_env_var_prefix=CLI_ENV_VARIABLE_PREFIX,
                                     commands_loader_cls=AuiCommandsLoader,
                                     help_cls=AuiHelp)
        self.args = None
