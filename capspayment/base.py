"""
Base
"""

from dataclasses import dataclass
from typing import Any

import httpx
from authentication import token_request
from config import Config, Token
from utils import custom_request


@dataclass
class BaseRequest:
    """Base Request Class"""

    config: Config

    def request(self, method: str, endpoint: str, data: Any) -> Any:
        """Call rest api method"""
        if not self.config or (self.config and self.config.check_config() != ""):
            return None

        url = self.config.api_url.rstrip("/") + endpoint
        try:
            token = token_request(self.config)

            self.config.token = Token(
                token_value=token[0], token_expiry=token[1], token_id=token[2]
            )

            response = custom_request(method, url, data, self.config)
        except httpx.HTTPStatusError as err:
            if err.response.status_code == 400:
                return err.response.text
            if err.response.status_code != 401:
                return {
                    "resultCode": str(err.response.status_code),
                    "resultMessage": "",
                }
            token = token_request(self.config)

            self.config.token = Token(
                token_value=token[0], token_expiry=token[1], token_id=token[2]
            )

            try:
                response = custom_request(method, url, data, self.config)
            except httpx.HTTPStatusError as err:
                return {
                    "resultCode": str(err.response.status_code),
                    "resultMessage": "",
                }
        return response
