# Dynamics 365 Audience Insights CLI

The AuI CLI is a command line tool for [Dynamics 365 Audience Insights](https://dynamics.microsoft.com/ai/customer-insights/audience-insights-capability).

It is based on the [customerinsights](https://pypi.org/project/customerinsights) Python library and exposes some of the [Audience Insights APIs](https://docs.microsoft.com/dynamics365/customer-insights/audience-insights/apis)

## Installation

1. Install Python 3.9 or later from [python.org](https://www.python.org/downloads), apt-get, or some other installer.

1. Install the [poetry](https://python-poetry.org) package

1. Start a shell:

    ```bash
    poetry shell
    ```

1. Install the packages:

    ```bash
    poetry install
    ```

1. Build `aui-cli`:

    ```bash
    poetry build
    ```

1. Verify the correct installation:

    ```bash
    > aui-cli --help

    Group
        aui-cli

    Subgroups:
        datasources : Commands to manage data sources.
        instances   : Commands to manage instances.
        measures    : Commands to manage measures.
        roles       : Commands to manage access roles.
        search      : Commands to manage search.
        segments    : Commands to manage segments.
    ```

1. Get help on any command with `--help`:

    ```bash
    > aui-cli instances list --help

    Command
        aui-cli instances list : Lists all instances.

    Arguments

    Global Arguments
        --debug            : Increase logging verbosity to show all debug logs.
        --help -h          : Show this help message and exit.
        --only-show-errors : Only show errors, suppressing warnings.
        --output -o        : Output format.  Allowed values: json, jsonc, none, table, tsv, yaml, yamlc.
                            Default: json.
        --query            : JMESPath query string. See http://jmespath.org/ for more information and
                            examples.
        --verbose          : Increase logging verbosity. Use --debug for full debug logs.
    ```

## Configuration

All configuration values are stored in the file `~/.aui-cli/config`, automatically created the first time the application is run.

In the `[autentication]` section, add your `api_key` and OAuth token:

```text
[authentication]
api_key = REDACTED
token = REDACTED
```

An alternate base url (default is `https://api.ci.ai.dynamics.com/v1`) can be defined in the `[endpoint]` section:

```text
[endpoint]
base_url = https://api.ci.ai.dynamics-alternate.com/v1
```

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit [https://cla.microsoft.com](https://cla.microsoft.com).

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

### Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
