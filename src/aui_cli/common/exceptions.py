# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from dynamics.customerinsights.api.models.api_error_result_py3 import ApiErrorResult


class AuIApiError(Exception):
    """
    Exception occuring while calling the AuI endpoint.
    """

    def __init__(self, error: ApiErrorResult):
        super(AuIApiError, self).__init__(error.message)
        self.http_status_code = error.http_status_code
        self.exception_culprit = error.exception_culprit
        self.error_code = error.error_code
        self.result_severity = error.result_severity
        self.message = error.message

    def to_string(self):
        """
        Returns the string representation of the exception
        """
        return f'({self.error_code}) {self.message}'


def check_exception(response):
    """
    Check if the response is an AuI API error and raise the AuIApiError exception.

    :param response: HTTP response
    """
    if ApiErrorResult == type(response):
        raise AuIApiError(response)

    return response
