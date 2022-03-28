"""
Authentication
"""

import base64
import datetime
import json

import utils
from config import Config


def token_request(config: Config) -> tuple:
    """Create authorization request"""

    if not config or (config and config.check_config() != ""):
        return (None, None, None)

    headers = {
        "Authorization": "Basic "
        + base64.b64encode(
            (config.token_user + ":" + config.token_password).encode("utf-8")
        ).decode("utf-8")
    }

    response = utils.simple_request(
        config.token_method, config.token_url, None, headers, config
    )

    if response:
        now = datetime.datetime.utcnow().replace(microsecond=0)
        data = json.loads(response.text)
        return (
            data["access_token"],
            now + datetime.timedelta(seconds=data["expires_in"]),
            data["id_token"],
        )
    return (None, None, None)
