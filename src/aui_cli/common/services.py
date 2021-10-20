# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from dynamics.customerinsights.api import CustomerInsights
from knack.log import get_logger
from .config import GLOBAL_CONFIG

logger = get_logger(__name__)


def get_client():
    """
    Returns an authenticated CustomerInsights client.
    """

    base_url = GLOBAL_CONFIG.get("endpoint", "base_url", None)
    if base_url:
        logger.info(f'Using base url: {base_url}')
    return CustomerInsights(base_url)


def get_custom_headers():
    """
    Returns the additional headers containing the API key information.
    """

    api_key = GLOBAL_CONFIG.get("authentication", "api_key")
    auth_token = GLOBAL_CONFIG.get("authentication", "token")
    return {
        'Cache-Control': 'no-cache',
        'Authorization': f'Bearer {auth_token}',
        'Ocp-Apim-Subscription-Key': api_key
    }
