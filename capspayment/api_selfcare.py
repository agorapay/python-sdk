"""
SelfCare API
"""

from dataclasses import dataclass
from typing import Union

from api_selfcare_model import SelfCareInitRequest, SelfCareInitResponse
from base import BaseRequest
from model import Response


@dataclass
class ApiSelfCare(BaseRequest):
    """SelfCare API requests"""

    def init(
        self, payload: SelfCareInitRequest
    ) -> Union[SelfCareInitResponse, Response]:
        """Init Selfcare seller enrollment by creating a new request,
        identified by requestId value"""
        return self.request("POST", "/selfcare/init", payload)
