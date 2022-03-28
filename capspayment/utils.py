"""
Utils
"""

import logging
import sys
from typing import Any

import httpx
from config import Config

LOG = logging.getLogger(__name__)


def dic_fields_tostring(dic: dict) -> None:
    """Convert dict to string"""
    for key, value in dic.items():
        if isinstance(value, dict):
            dic_fields_tostring(dic[key])
        elif isinstance(value, list):
            lst_fields_tostring(dic[key])
        else:
            dic[key] = str(value)


def lst_fields_tostring(lst: list) -> None:
    """Convert list to string"""
    for index, value in enumerate(lst):
        if isinstance(value, dict):
            dic_fields_tostring(lst[index])
        elif isinstance(value, list):
            lst_fields_tostring(lst[index])
        else:
            lst[index] = str(value)


def json_fields_tostring(json: dict) -> None:
    """Convert json to string"""
    dic_fields_tostring(json)


def custom_request(method: str, url: str, data: Any, config: Config) -> Any:
    """Create a custom request"""

    if not config or (config and config.check_config() != ""):
        return None

    token_value = ""
    token_id = ""
    if config.token:
        token_value = str(config.token.token_value)
        token_id = str(config.token.token_id)

    headers = {
        "Authorization": "Bearer " + token_value,
        "Content-Type": "application/json",
        "id_token": token_id,
    }

    response = simple_request(method, url, data, headers, config)

    if response:
        return response.text
    return None


def simple_request(
    method: str, url: str, data: Any, headers: dict, config: Config
) -> Any:
    """Send simple request"""

    if not config or (config and config.check_config() != ""):
        return None

    response = None
    try:
        if method == "GET":
            if data:
                response = httpx.get(
                    url, params=data, headers=headers, timeout=config.timeout
                )
            else:
                response = httpx.get(url, headers=headers, timeout=config.timeout)
        elif method == "POST":
            if data:
                json_fields_tostring(data)
                response = httpx.post(
                    url, headers=headers, json=data, timeout=config.timeout
                )
            else:
                response = httpx.post(url, headers=headers, timeout=config.timeout)
        else:
            response = None
            LOG.error("Token Method is not valid - %s", method)
            raise Exception("Token Method is not valid")
        response.raise_for_status()
    except httpx.ConnectError as err:
        # eg, no internet
        LOG.error(err)
        sys.exit(err)
    except httpx.TimeoutException as err:
        # eg, url, server and other errors
        LOG.error(err)
        raise
    except httpx.HTTPError as err:
        # eg, url, server and other errors
        LOG.error(err)
        raise err
    except Exception as error:
        LOG.error("custom_request error: Can not send request - %s", error)
        raise error

    return response
