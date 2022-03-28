"""Payout API Model"""

from typing import Optional, TypedDict

from model import TRANSACTIONSTATUS, Amount, Commission


class PayoutRequest(TypedDict):
    """Data in input of payout/create request"""

    endToEndId: Optional[str]  # End to end identifier
    payoutAmount: Amount  # Amount structure
    paymentMethodAlias: str  # Alias for the payment method
    accountNumber: str  # A string representing the account number
    commission: Optional[Commission]  # Commission information
    metaData: Optional[str]  # JSON data for the marketplace
    reason: Optional[str]  # Operation label transmited in payment system


class PayoutResponse(TypedDict):
    """Data in output of payout/create request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    transactionId: Optional[str]  # Id of the payment transaction
    transactionStatus: Optional[TRANSACTIONSTATUS]  # Status of a transaction
