"""
Payment Account API
"""

from dataclasses import dataclass
from typing import Literal, Union

import utils
from api_payment_account_model import (PaymentAccountCreditRequest,
                                       PaymentAccountCreditResponse,
                                       PaymentAccountDisableIBANRequest,
                                       PaymentAccountListRequest,
                                       PaymentAccountListResponse,
                                       PaymentAccountPayoutAutoRequest,
                                       PaymentAccountReportRequest,
                                       PaymentAccountReportResponse,
                                       PaymentAccountRequest,
                                       PaymentAccountResponse,
                                       PaymentAccountSetFloorLimitRequest,
                                       PaymentAccountSetIBANRequest,
                                       PaymentAccountSetIBANResponse)
from base import BaseRequest
from model import Response


@dataclass
class ApiPaymentAccount(BaseRequest):
    """Payment Account API requests"""

    def payment_account(
        self, payload: PaymentAccountRequest
    ) -> Union[PaymentAccountResponse, Response]:
        """Get account details"""
        return self.request("GET", "/paymentAccount", payload)

    def payment_account_list(
        self, payload: PaymentAccountListRequest
    ) -> Union[PaymentAccountListResponse, Response]:
        """Get account list"""
        return self.request("POST", "/paymentAccount/List", payload)

    def credit(
        self, payload: PaymentAccountCreditRequest
    ) -> Union[PaymentAccountCreditResponse, Response]:
        """Credit an account"""
        return self.request("POST", "/paymentAccount/credit", payload)

    def payout_auto(self, payload: PaymentAccountPayoutAutoRequest) -> Response:
        """Schedule a payout"""
        return self.request("POST", "/paymentAccount/payoutAuto", payload)

    def set_floor_limit(self, payload: PaymentAccountSetFloorLimitRequest) -> Response:
        """Set Account Floor Limit"""
        return self.request("POST", "/paymentAccount/setFloorLimit", payload)

    def set_iban(
        self,
        payload: PaymentAccountSetIBANRequest,
        multipart: Literal[True, False] = True,
    ) -> Union[PaymentAccountSetIBANResponse, Response]:
        """Start change IBAN process"""

        if multipart:
            file_content = payload.get("fileContent", "")
            file_type = payload.get("fileType", "")
            file_name = f"iban.{file_type}"

            if payload and "fileContent" in payload:
                del payload["fileContent"]

            if payload and "fileType" in payload:
                del payload["fileType"]

            multipart_payload = {
                "files": [
                    utils.get_json_multipart(payload),
                    utils.get_file_multipart(file_name, file_content),
                ]
            }

            return self.request(
                "POST", "/paymentAccount/setIBAN", multipart_payload, multipart
            )

        return self.request("POST", "/paymentAccount/setIBAN", payload, multipart)

    def disable_iban(self, payload: PaymentAccountDisableIBANRequest) -> Response:
        """Disable Account IBAN"""
        return self.request("POST", "/paymentAccount/disableIBAN", payload)

    def recharge(self, payload: dict) -> dict:
        """Recharge"""
        return self.request("POST", "/paymentAccount/recharge", payload)

    def create(self, payload: dict) -> dict:
        """Create Payment Account"""
        return self.request("POST", "/paymentAccount/create", payload)

    def report(
        self, payload: PaymentAccountReportRequest
    ) -> Union[PaymentAccountReportResponse, Response]:
        """Get account report"""
        return self.request("GET", "/paymentAccount/report", payload)
