"""
Payout API
"""

from dataclasses import dataclass
from typing import Union

from api_payout_model import PayoutRequest, PayoutResponse
from base import BaseRequest
from model import Response


@dataclass
class ApiPayout(BaseRequest):
    """Payout API requests"""

    def create(self, payload: PayoutRequest) -> Union[PayoutResponse, Response]:
        """Ask for a payout"""
        return self.request("POST", "/payout/create", payload)
