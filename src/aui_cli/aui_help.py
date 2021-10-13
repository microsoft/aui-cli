# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help import CLIHelp
from .common.version import VERSION

# pylint: disable=anomalous-backslash-in-string
# pylint: disable=import-outside-toplevel
# pylint: disable=unused-import


class AuiHelp(CLIHelp):
    """
    Specific help class for the AuI modules.
    """

    def __init__(self, cli_ctx=None):
        # import command group help
        import aui_cli.groups.instances._help
        super(AuiHelp, self).__init__(cli_ctx=cli_ctx,
                                      welcome_message=WELCOME_MESSAGE)


# Logo generation http://patorjk.com/software/taag/#p=display&h=2&v=3&f=Doom&t=aui%20cli
WELCOME_MESSAGE = f"""AuI CLI {VERSION}

             _         _ _
            (_)       | (_)
  __ _ _   _ _     ___| |_
 / _` | | | | |   / __| | |
| (_| | |_| | |  | (__| | |
 \__,_|\__,_|_|   \___|_|_|

Use `aui_cli -h` to see available commands.

Available commands:"""

# pylint: enable=anomalous-backslash-in-string
# pylint: enable=import-outside-toplevel
# pylint: enable=unused-import
