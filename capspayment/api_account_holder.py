"""
Account Holder API
"""

from dataclasses import dataclass
from typing import Union

from api_account_holder_model import (
    AccountHolderRegisterRequest,
    AccountHolderRegisterResponse,
    AccountHolderRegistrationDetailsRequest,
    AccountHolderRegistrationDetailsResponse,
    AccountHolderUnregisterRequest,
    AccountHolderUpdateRequest,
    AccountHolderUpdateResponse,
    AccountHolderUploadDocumentRequest,
    AccountHolderUploadDocumentResponse,
)
from base import BaseRequest
from model import Response


@dataclass
class ApiAccountHolder(BaseRequest):
    """Account Holder API requests"""

    def register(
        self, payload: AccountHolderRegisterRequest
    ) -> Union[AccountHolderRegisterResponse, Response]:
        """Start registering new account holder"""
        return self.request("POST", "/accountHolder/register", payload)

    def unregister(self, payload: AccountHolderUnregisterRequest) -> Response:
        """Unregister pending account holder registration"""
        return self.request("POST", "/accountHolder/unregister", payload)

    def update(
        self, payload: AccountHolderUpdateRequest
    ) -> Union[AccountHolderUpdateResponse, Response]:
        """Update"""
        return self.request("POST", "/accountHolder/update", payload)

    def upload_document(
        self, payload: AccountHolderUploadDocumentRequest
    ) -> Union[AccountHolderUploadDocumentResponse, Response]:
        """Upload Document"""
        return self.request("POST", "/accountHolder/uploadDocument", payload)

    def registration_details(
        self, payload: AccountHolderRegistrationDetailsRequest
    ) -> Union[AccountHolderRegistrationDetailsResponse, Response]:
        """Get Registration Details"""
        return self.request("GET", "/accountHolder/registrationDetails", payload)
