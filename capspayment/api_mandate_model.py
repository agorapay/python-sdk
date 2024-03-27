"""Mandate API Model"""

from typing import Literal, Optional, TypedDict

from model import Details, Payer, PaymentMethodSimple

OTP = Literal["1", "Y"]


class MandateCreateRequest(TypedDict):
    """Data in input of mandate/create request"""

    transPaymentMethod: PaymentMethodSimple
    payer: Payer
    details: Details
    urlRedirect: Optional[
        str
    ]  # Url where the client must be redirected at the end of the payment
    # with the partner
    otp: Optional[OTP]  # Force signature by OTP. Enum: [ 1, Y ]


class MandateCreateResponse(TypedDict):
    """Data in output of mandate/create request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    reference: Optional[str]  # Mandate reference
    redirectUrl: Optional[
        str
    ]  # Url to redirect the client to to continue the payment with an external partner
    redirectInd: Optional[str]  # 1 if user must be redirect to the redirectUrl site
    mandateId: Optional[str]  # Mandate identifier


class MandateUpdateRequest(TypedDict):
    """Data in input of mandate/update request"""

    reference: str  # Mandate reference
    mandateId: str  # Identifier for the mandate to update
