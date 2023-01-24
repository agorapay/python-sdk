"""
Utils
"""

import json
import logging
import mimetypes
import sys
from io import BytesIO
from typing import Any, Literal

import httpx
from config import Config
from model import Request

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


def json_fields_tostring(data: dict) -> None:
    """Convert json to string"""
    dic_fields_tostring(data)


def json_tobytes(data: dict) -> BytesIO:
    """Convert json dict to BytesIO"""
    json_content = json.dumps(data)
    return BytesIO(bytes(json_content, "utf-8"))


def file_tobytes(data: str) -> BytesIO:
    """Convert file content to BytesIO"""
    return BytesIO(bytes(data, "utf-8"))


def get_file_content_type(file_name: str) -> str:
    """Get content-type from filename"""
    ctype, encoding = mimetypes.guess_type(file_name)
    if ctype is None or encoding is not None:
        return "application/octet-stream"
    return ctype


def get_file_multipart(file_name: str, file_content: str) -> tuple:
    """Get multipart file data"""
    return (
        "file",
        (file_name, file_tobytes(file_content), get_file_content_type(file_name)),
    )


def get_json_multipart(data: dict) -> tuple:
    """Get multipart json data"""
    return ("json", (None, json_tobytes(data), "application/json"))


def custom_request(
    method: str,
    url: str,
    data: Any,
    config: Config,
    multipart: Literal[True, False] = False,
) -> Any:
    """Create a custom request"""

    if not config or (config and config.check_config() != ""):
        return None

    token_value = ""
    token_id = ""
    if config.token:
        token_value = str(config.token.token_value)
        token_id = str(config.token.token_id)

    if multipart:
        headers = {
            "Authorization": "Bearer " + token_value,
            "id_token": token_id,
        }
    else:
        headers = {
            "Authorization": "Bearer " + token_value,
            "Content-Type": "application/json",
            "id_token": token_id,
        }
    req = Request(method, url, data, headers, config, multipart)
    response = simple_request(req)

    if response:
        return response.text
    return None


def simple_request_get(request: Request) -> Any:
    """Send simple request GET"""

    if request.data:
        return httpx.get(
            request.url,
            params=request.data,
            headers=request.headers,
            timeout=request.config.timeout,
        )

    return httpx.get(
        request.url, headers=request.headers, timeout=request.config.timeout
    )


def simple_request_post(request: Request) -> Any:
    """Send simple request POST"""

    if request.data:
        if request.multipart:
            return httpx.post(
                request.url,
                headers=request.headers,
                files=request.data.get("files", []),
                timeout=request.config.timeout,
            )

        json_fields_tostring(request.data)
        return httpx.post(
            request.url,
            headers=request.headers,
            json=request.data,
            timeout=request.config.timeout,
        )

    return httpx.post(
        request.url, headers=request.headers, timeout=request.config.timeout
    )


def simple_request(request: Request) -> Any:
    """Send simple request"""

    if not request.config or (request.config and request.config.check_config() != ""):
        return None

    response = None
    try:
        if request.method == "GET":
            response = simple_request_get(request)
        elif request.method == "POST":
            response = simple_request_post(request)
        else:
            response = None
            LOG.error("Token Method is not valid - %s", request.method)
            raise Exception("Token Method is not valid")
        response.raise_for_status()
    except httpx.ConnectError as err:
        # eg, no internet
        LOG.error(err)
        sys.exit(err)
    except httpx.TimeoutException as err:
        # eg, url, server and other errors
        LOG.error(err)
        raise err
    except httpx.HTTPError as err:
        # eg, url, server and other errors
        LOG.error(err)
        raise err
    except Exception as error:
        LOG.error("custom_request error: Can not send request - %s", error)
        raise error

    return response
