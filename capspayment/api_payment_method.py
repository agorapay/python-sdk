"""
Payment Method API
"""

from dataclasses import dataclass
from typing import Union

from api_payment_method_model import (
    PaymentMethodGetAliasRequest,
    PaymentMethodGetAliasResponse,
    PaymentMethodGetIBANRequest,
    PaymentMethodGetIBANResponse,
    PaymentMethodListRequest,
    PaymentMethodListResponse,
    PaymentMethodRemoveAliasRequest,
)
from base import BaseRequest
from model import Response


@dataclass
class ApiPaymentMethod(BaseRequest):
    """Payment Method API requests"""

    def remove_alias(self, payload: PaymentMethodRemoveAliasRequest) -> Response:
        """Remove a given payment method alias id"""
        return self.request("POST", "/paymentMethod/removeAlias", payload)

    def get_alias(
        self, payload: PaymentMethodGetAliasRequest
    ) -> Union[PaymentMethodGetAliasResponse, Response]:
        """Get a list of the available payment method aliases according to the
        payer reference and eventually for a specific payment method"""
        return self.request("POST", "/paymentMethod/getAlias", payload)

    def payment_method_list(
        self, payload: PaymentMethodListRequest
    ) -> Union[PaymentMethodListResponse, Response]:
        """List payment methods and eventually aliases, according to the
        transaction amount and the country of the payer"""
        return self.request("POST", "/paymentMethod/list", payload)

    def get_iban(
        self, payload: PaymentMethodGetIBANRequest
    ) -> Union[PaymentMethodGetIBANResponse, Response]:
        """Get IBAN from a given payment method alias, as saved during an instant payment SCT"""
        return self.request("POST", "/paymentMethod/getIBAN", payload)
