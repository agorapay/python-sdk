"""
CAPSPayment API
"""

import logging
import sys

from api_account_holder import ApiAccountHolder
from api_operations import ApiOperations
from api_payin import ApiPayin
from api_payment_account import ApiPaymentAccount
from api_payout import ApiPayout
from api_transfer import ApiTransfer
from config import Config


def init_logger() -> None:
    """Init logger file"""
    log = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level=logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    log.addHandler(handler)


class CAPSPaymentAPI:
    """CAPSPayment API class"""

    def __init__(
        self,
        api_url: str = "",
        token_url: str = "",
        token_user: str = "",
        token_password: str = "",
    ) -> None:
        self.config = Config(api_url, token_url, token_user, token_password)
        init_logger()

    def account_holder_api(self) -> ApiAccountHolder:
        """Get Account Holder API"""
        return ApiAccountHolder(self.config)

    def operations_api(self) -> ApiOperations:
        """Get Operations API"""
        return ApiOperations(self.config)

    def payin_api(self) -> ApiPayin:
        """Get Payin API"""
        return ApiPayin(self.config)

    def payment_account_api(self) -> ApiPaymentAccount:
        """Get Payment Account API"""
        return ApiPaymentAccount(self.config)

    def payout_api(self) -> ApiPayout:
        """Get Payout API"""
        return ApiPayout(self.config)

    def transfer_api(self) -> ApiTransfer:
        """Get Transfer API"""
        return ApiTransfer(self.config)
