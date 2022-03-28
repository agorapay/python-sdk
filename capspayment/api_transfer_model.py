"""Transfer API Model"""

from typing import Optional, TypedDict

from model import Amount


class TransferRequest(TypedDict):
    """Data in input of transfer/create request"""

    accountCptNumber: str  # A string representing the account number
    transferAmount: Amount  # Amount structure
    accountNumber: str  # A string representing the account number
    orderRef: Optional[str]  # Marketplace reference for this order
    metaData: Optional[
        str
    ]  # JSON data for the marketplace. This data is not used by payment system
    reason: str  # Operation label transmited in payment system


class TransferResponse(TypedDict):
    """Data in output of transfer/create request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    transactionId: Optional[str]  # Id of the payment transaction
