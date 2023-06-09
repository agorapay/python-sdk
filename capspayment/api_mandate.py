"""
Mandate API
"""

from dataclasses import dataclass
from typing import Union

from api_mandate_model import MandateCreateRequest, MandateCreateResponse
from base import BaseRequest
from model import Response


@dataclass
class ApiMandate(BaseRequest):
    """Mandate API requests"""

    def create(
        self, payload: MandateCreateRequest
    ) -> Union[MandateCreateResponse, Response]:
        """Generate a SEPA Direct debit mandate B2C or B2B, do not generate any transactions"""
        return self.request("POST", "/mandate/create", payload)
