# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
from knack.config import CLIConfig

CLI_ENV_VARIABLE_PREFIX = 'AUI_CLI_'


def _get_config_dir():
    config_dir = os.getenv('AUI_CLI_CONFIG_DIR', None) or \
        os.path.expanduser(os.path.join('~', '.aui_cli'))
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    return config_dir


GLOBAL_CONFIG_DIR = _get_config_dir()
GLOBAL_CONFIG = CLIConfig(config_dir=GLOBAL_CONFIG_DIR)
