"""Payment Method API Model"""

from typing import List, Optional, TypedDict

from model import (
    AliasSimple,
    Amount,
    Payer,
    PayerSimple,
    PaymentMethod,
    PaymentMethodSimple,
)


class PaymentMethodRemoveAliasRequest(TypedDict):
    """Data in input of paymentMethod/removeAlias request"""

    transPaymentMethod: PaymentMethodSimple
    payer: PayerSimple
    alias: AliasSimple


class PaymentMethodGetAliasRequest(TypedDict):
    """Data in input of paymentMethod/getAlias request"""

    transPaymentMethod: Optional[PaymentMethodSimple]
    payer: PayerSimple


class PaymentMethodGetAliasResponse(TypedDict):
    """Data in output of paymentMethod/getAlias request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    paymentMethodList: Optional[List[PaymentMethod]]


class PaymentMethodListRequest(TypedDict):
    """Data in input of paymentMethod/list request"""

    countryCode: str  # The ISO country code in 3 characters format
    amount: Amount  # Amount structure
    payer: Optional[Payer]


class PaymentMethodListResponse(TypedDict):
    """Data in output of paymentMethod/list request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    paymentMethodList: Optional[List[PaymentMethod]]


class PaymentMethodGetIBANRequest(TypedDict):
    """Data in input of paymentMethod/getIBAN request"""

    paymentMethodAlias: str  # Alias for the payment method


class PaymentMethodGetIBANResponse(TypedDict):
    """Data in output of paymentMethod/getIBAN request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    holder: Optional[str]  # Thirdparty name
    bic: Optional[str]  # Business Identifier Code allocated to a financial institution
    # by the ISO 9362 Registration Authority
    iban: Optional[str]  # International Bank Account Number
