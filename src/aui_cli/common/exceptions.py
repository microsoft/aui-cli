# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from dynamics.customerinsights.api.models.api_error_result_py3 import ApiErrorResult


class AuIApiError(Exception):
    """
    Exception occuring while calling the AuI endpoint.
    """

    def __init__(self, message):
        super(AuIApiError, self).__init__(message)
        self.message = message


def check_exception(response):
    """
    Check if the response is an AuI API error and raise the AuIApiError exception.
    """

    if ApiErrorResult == type(response):
        raise AuIApiError(response.message)

    return response
