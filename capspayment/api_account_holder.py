"""
Account Holder API
"""

from dataclasses import dataclass
from typing import Literal, Union

import utils
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
        self,
        payload: AccountHolderUploadDocumentRequest,
        multipart: Literal[True, False] = True,
    ) -> Union[AccountHolderUploadDocumentResponse, Response]:
        """Upload Document"""

        if multipart:
            requirements = payload.get("requirements", [])

            files = []
            if requirements:
                for requirement in requirements:
                    id_val = requirement.get("id", "")
                    file_ext = requirement.get("fileExt", "")
                    file_content = requirement.get("fileContent", "")
                    file_name = f"{id_val}.{file_ext}"

                    if "fileContent" in requirement:
                        del requirement["fileContent"]

                    if "fileExt" in requirement:
                        del requirement["fileExt"]

                    files.append(utils.get_file_multipart(file_name, file_content))

            files.insert(0, utils.get_json_multipart(payload))

            multipart_payload = {"files": files}

            return self.request(
                "POST", "/accountHolder/uploadDocument", multipart_payload, multipart
            )

        return self.request("POST", "/accountHolder/uploadDocument", payload, multipart)

    def registration_details(
        self, payload: AccountHolderRegistrationDetailsRequest
    ) -> Union[AccountHolderRegistrationDetailsResponse, Response]:
        """Get Registration Details"""
        return self.request("GET", "/accountHolder/registrationDetails", payload)
