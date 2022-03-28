"""
Config Module
"""

import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

LOG = logging.getLogger(__name__)


@dataclass
class Token:
    """Token class"""

    token_value: Optional[str] = None
    token_expiry: Optional[datetime] = None
    token_id: Optional[str] = None


@dataclass
class Config:
    """Config class"""

    api_url: str
    token_url: str
    token_user: str
    token_password: str
    token_method: str = "POST"
    timeout: int = 30
    token: Optional[Token] = None

    def check_config(self) -> str:
        """Check config params"""
        error_label = ""

        if not isinstance(self.api_url, str) or not self.api_url:
            error_label = "API Url is not valid"

        if not isinstance(self.token_method, str) or not self.token_method:
            error_label = "Token Method is not valid"

        if not isinstance(self.token_url, str) or not self.token_url:
            error_label = "Token Url is not valid"

        if not isinstance(self.token_user, str) or not self.token_user:
            error_label = "Token User is not valid"

        if not isinstance(self.token_password, str) or not self.token_password:
            error_label = "Token Password is not valid"

        if error_label != "":
            LOG.error(error_label)

        return error_label
