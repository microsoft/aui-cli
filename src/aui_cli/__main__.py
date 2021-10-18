# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys

from .aui_cli import AuiCLI


def main():
    """
    Entry point for the AuI CLI
    """

    try:
        aui_cli = AuiCLI()
        exit_code = aui_cli.invoke(sys.argv[1:])
        sys.exit(exit_code)
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()
