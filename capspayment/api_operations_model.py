"""Operations API Model"""

from typing import List, Literal, Optional, TypedDict

from model import ACCOUNTTYPE, OPERATIONTYPE, PAYMETHODKEY, Amount

OPERATIONSIDE = Literal["PAYIN", "PAYOUT", "TRANSFER"]
OPERATIONSTATUS = Literal[
    "registered", "waiting", "cashed", "cancelled", "suspended", "rejected"
]


class BreakDownSimple(TypedDict):
    """Break Down Simple Structure"""

    amount: Amount  # Amount structure
    sellerAccountNumber: str  # Account number of the merchant
    label: str  # Label for the breakdown


class Operation(TypedDict):
    """Operation Structure"""

    amount: Amount  # Amount structure
    date: Optional[str]  # operation Date
    side: OPERATIONSIDE  # Direction of the operation. Enum: [PAYIN, PAYOUT, TRANSFER]
    type: OPERATIONTYPE  # Type of an operation
    # Enum: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    status: OPERATIONSTATUS  # Status of an operation
    # Enum: [registered, waiting, cashed, cancelled, suspended, rejected]
    breakdownList: Optional[List[BreakDownSimple]]  # List of breakdown for this payment
    metaData: Optional[str]  # JSON data for the marketplace
    transactionId: str  # Reference for the operation
    creationDateTime: Optional[str]  # ISO 8601 format (ex: 20210325T082300+01:00)
    accountNumber: Optional[str]  # A string representing the account number
    cachedCumulAmount: Optional[str]
    orderReference: Optional[str]  # Marketplace reference for this order
    accountCurrencyCode: Optional[str]  # Currency code in 3 characters ISO format
    operationLabel: Optional[str]  # Label of the operation
    relatedMsgStatusLabel: Optional[str]  # Status explanation
    thirdPartyName: Optional[str]
    accountType: Optional[ACCOUNTTYPE]  # Type of account
    # 1: principal
    # 3: waiting
    # 4: suspense
    # 5: change
    # 6: commission
    # 13: voucher
    # 14: reliquat
    # 15: autorization
    # 16: pre-autorization
    # Enum: [ 1, 3, 4, 5, 6, 13, 14, 15, 16 ]
    accountCptNumber: Optional[str]  # A string representing the account number
    accountCptTypeLabel: Optional[ACCOUNTTYPE]  # Type of account
    # Enum: [ 1, 3, 4, 5, 6, 13, 14, 15, 16 ]
    accountCptCurrencyCode: Optional[str]  # Currency code in 3 characters ISO format
    thirdPartyCptName: Optional[str]


class OperationsListRequest(TypedDict):
    """Data in input of operations/list request"""

    pagination: Optional[str]  # Numbers of ligne in reporting. Limited to 100
    startDate: Optional[
        str
    ]  # Begin date of operation reporting in YYYYMMDDHHMMSS format
    endDate: Optional[str]  # End Date of operation Reporting in YYYYMMDDHHMMSS format
    maxAmount: Optional[str]
    minAmount: Optional[str]
    offset: Optional[str]
    orderReference: Optional[str]  # Marketplace reference for this order
    currency: Optional[str]  # Currency code in 3 characters ISO format
    transactionId: Optional[str]  # Id of the payment transaction
    paymentMethodKey: Optional[
        PAYMETHODKEY
    ]  # Key identifier of the payment method type id
    sellerAccountNumber: Optional[str]  # Account number of the merchant
    parentAccountNumber: Optional[str]  # A string representing the account number


class OperationsListResponse(TypedDict):
    """Data in output of operations/list request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    operationList: List[Operation]  # List of operation matching the request
    resultCodeMessage: Optional[str]  # The failure description
    lineCount: Optional[str]  # Total number of lines
