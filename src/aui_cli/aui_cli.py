# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

from knack import CLI
from knack.log import get_logger
from .common.config import CLI_ENV_VARIABLE_PREFIX, GLOBAL_CONFIG_DIR
from .common.exceptions import AuIApiError
from .aui_commands import AuiCommandsLoader
from .aui_help import AuiHelp

CLI_NAME = "aui-cli"

logger = get_logger(__name__)


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

    def exception_handler(self, ex):
        if isinstance(ex, AuIApiError):
            logger.error(ex.to_string())
            return 1

        return super(AuiCLI, self).exception_handler(ex)
