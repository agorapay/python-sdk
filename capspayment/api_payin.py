"""
Payin API
"""

from dataclasses import dataclass
from typing import Union

from api_payin_model import (
    PayinAdjustPaymentRequest,
    PayinCancelRequest,
    PayinCancelResponse,
    PayinCaptureRequest,
    PayinCaptureResponse,
    PayinMandateRequest,
    PayinMandateResponse,
    PayinOrderDetailsRequest,
    PayinOrderDetailsResponse,
    PayinPaymentDetailsRequest,
    PayinPaymentDetailsResponse,
    PayinPaymentIframeRequest,
    PayinPaymentIframeResponse,
    PayinPaymentMethodsRequest,
    PayinPaymentMethodsResponse,
    PayinPaymentRequest,
    PayinPaymentResponse,
    PayinRefundRequest,
    PayinRefundResponse,
    PayinTicketRequest,
    PayinTicketResponse,
)
from base import BaseRequest
from model import Response


@dataclass
class ApiPayin(BaseRequest):
    """Payin API requests"""

    def payment(
        self, payload: PayinPaymentRequest
    ) -> Union[PayinPaymentResponse, Response]:
        """Submit a payment"""
        return self.request("POST", "/payin/payment", payload)

    def payment_details(
        self, payload: PayinPaymentDetailsRequest
    ) -> Union[PayinPaymentDetailsResponse, Response]:
        """Submit additionnal payment details"""
        return self.request("POST", "/payin/paymentDetails", payload)

    def payment_methods(
        self, payload: PayinPaymentMethodsRequest
    ) -> Union[PayinPaymentMethodsResponse, Response]:
        """Submit an order/get payment methods"""
        return self.request("POST", "/payin/paymentMethods", payload)

    def capture(
        self, payload: PayinCaptureRequest
    ) -> Union[PayinCaptureResponse, Response]:
        """Capture a transaction/order"""
        return self.request("POST", "/payin/capture", payload)

    def cancel(
        self, payload: PayinCancelRequest
    ) -> Union[PayinCancelResponse, Response]:
        """Cancel a transaction/order"""
        return self.request("POST", "/payin/cancel", payload)

    def order_details(
        self, payload: PayinOrderDetailsRequest
    ) -> Union[PayinOrderDetailsResponse, Response]:
        """Get all the order details"""
        return self.request("GET", "/payin/orderDetails", payload)

    def adjust_payment(self, payload: PayinAdjustPaymentRequest) -> Response:
        """Adjust the amount of the payment/change the breakdown of the payment"""
        return self.request("POST", "/payin/adjustPayment", payload)

    def payment_iframe(
        self, payload: PayinPaymentIframeRequest
    ) -> Union[PayinPaymentIframeResponse, Response]:
        """Submit an order/get an authent code"""
        return self.request("POST", "/payin/paymentIframe", payload)

    def refund(
        self, payload: PayinRefundRequest
    ) -> Union[PayinRefundResponse, Response]:
        """Refund a transaction/order"""
        return self.request("POST", "/payin/refund", payload)

    def mandate(
        self, payload: PayinMandateRequest
    ) -> Union[PayinMandateResponse, Response]:
        """Get signed mandate file"""
        return self.request("GET", "/payin/mandate", payload)

    def ticket(
        self, payload: PayinTicketRequest
    ) -> Union[PayinTicketResponse, Response]:
        """Get card payment ticket"""
        return self.request("GET", "/payin/ticket", payload)
