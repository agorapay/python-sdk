"""
Virtual IBAN API
"""

from dataclasses import dataclass
from typing import Union

from api_v_iban_model import (
    VIbanCreateRequest,
    VIbanCreateResponse,
    VIbanDeleteRequest,
    VIbanListRequest,
    VIbanListResponse,
)
from base import BaseRequest
from model import Response


@dataclass
class ApiVIban(BaseRequest):
    """Virtual IBAN API requests"""

    def create(
        self, payload: VIbanCreateRequest
    ) -> Union[VIbanCreateResponse, Response]:
        """
        Generate a virtual IBAN for an internal account
        without initiating a payment transaction
        """
        return self.request("POST", "/vIban/create", payload)

    def delete(self, payload: VIbanDeleteRequest) -> Response:
        """Remove a virtual IBAN associated with an account"""
        return self.request("POST", "/vIban/delete", payload)

    def v_iban_list(
        self, payload: VIbanListRequest
    ) -> Union[VIbanListResponse, Response]:
        """IBAN virtual List"""
        return self.request("GET", "/vIban/list", payload)
