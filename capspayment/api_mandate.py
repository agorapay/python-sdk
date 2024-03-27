"""
Mandate API
"""

from dataclasses import dataclass
from typing import Union

from api_mandate_model import (
    MandateCreateRequest,
    MandateCreateResponse,
    MandateUpdateRequest,
)
from base import BaseRequest
from model import Response


@dataclass
class ApiMandate(BaseRequest):
    """Mandate API requests"""

    def create(
        self, payload: MandateCreateRequest
    ) -> Union[MandateCreateResponse, Response]:
        """Generate a new direct debit mandate without payment"""
        return self.request("POST", "/mandate/create", payload)

    def update(self, payload: MandateUpdateRequest) -> Response:
        """Update information for an existing mandate"""
        return self.request("POST", "/mandate/update", payload)
