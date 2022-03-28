"""Operations API"""

from dataclasses import dataclass
from typing import Union

from api_operations_model import OperationsListRequest, OperationsListResponse
from base import BaseRequest
from model import Response


@dataclass
class ApiOperations(BaseRequest):
    """Operation API requests"""

    def operation_list(
        self, payload: OperationsListRequest
    ) -> Union[OperationsListResponse, Response]:
        """Get operations matching a set of criterias"""
        return self.request("POST", "/operations/list", payload)
