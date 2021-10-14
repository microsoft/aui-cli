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

## Configuration

Add the `api_key` and OAuth token in the file `~/.aui-cli/config`

```text
[authentication]
api_key = REDACTED
token = REDACTED
```

## Contributing

### Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
