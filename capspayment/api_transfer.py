"""
Transfert API
"""

from dataclasses import dataclass
from typing import Union

from api_transfer_model import TransferRequest, TransferResponse
from base import BaseRequest
from model import Response


@dataclass
class ApiTransfer(BaseRequest):
    """Transfer API requests"""

    def create(self, payload: TransferRequest) -> Union[TransferResponse, Response]:
        """Ask for a transfer between two accounts"""
        return self.request("POST", "/transfer/create", payload)
