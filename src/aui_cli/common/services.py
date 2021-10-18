# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from dynamics.customerinsights.api import CustomerInsightsAPIAPIMPublic
from msrest.authentication import BasicTokenAuthentication
from .config import GLOBAL_CONFIG


def get_client():
    """
    Returns an authenticated CustomerInsights client.
    """

    auth_token = GLOBAL_CONFIG.get("authentication", "token")
    auth = BasicTokenAuthentication({'access_token': auth_token})
    return CustomerInsightsAPIAPIMPublic(credentials=auth)


def get_custom_headers():
    """
    Returns the additional headers containing the API key information.
    """

    api_key = GLOBAL_CONFIG.get("authentication", "api_key")
    return {
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': api_key
    }
