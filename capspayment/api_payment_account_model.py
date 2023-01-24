"""Payment Account API Model"""

from typing import List, Literal, Optional, TypedDict

from model import DAYOFMONTH, DAYOFWEEK, MONTH, Amount

FILETYPE = Literal["JPEG", "PNG", "PDF", "DOC", "XLS", "XLSX"]
FREQUENCY = Literal["0", "1", "2", "3"]
STATUS = Literal["A", "D", "R", "S"]
STATUSLABEL = Literal["activated", "deactivated", "registered", "suspended"]
PAYMETHODKEY = Literal["SCT"]
PAYMETHODKEYIBAN = Literal["SCT", "SCT INST"]
REPORTTYPE = Literal["ACCOUNT_STATEMENT", "INVOICE", "IC_FEE_REPORT"]
REPORTFORMAT = Literal["P", "C"]


class Account(TypedDict):
    """Account Structure"""

    number: Optional[str]  # Number of the account
    name: Optional[str]  # Thirdparty name
    status: Optional[
        STATUSLABEL
    ]  # The status of the account. Enum: [ activated, deactivated, registered, suspended ]
    currency: Optional[str]  # Currency code in 3 characters ISO format
    type: Optional[str]  # Account type
    payoutAuto: Optional[str]  # 1 if payout auto activated
    floorLimit: Optional[str]  # Minimum amount for payout auto
    balance: Optional[str]
    availableBalance: Optional[str]


class PaymentAccount(TypedDict):
    """Payment Account Structure"""

    number: Optional[str]  # Number of the account
    name: Optional[str]  # Thirdparty name
    status: Optional[
        STATUS
    ]  # Account status code in one char length. Enum: [ A, D, R, S ]
    # A: Activated D: Deactivated R: Registered S: Suspended
    currency: Optional[str]  # Currency code in 3 characters ISO format
    type: Optional[str]  # Account type
    payoutAuto: Optional[str]  # 1 if payout auto activated
    floorLimit: Optional[str]  # Minimum amount for payout auto
    reference: Optional[str]  # Account reference


class PaymentAccountRequest(TypedDict):
    """Data in input of paymentAccount request"""

    accountNumber: str  # Identifier of the account to get details


class PaymentAccountResponse(TypedDict):
    """Data in output of paymentAccount request"""

    account: Optional[Account]
    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description


class PaymentAccountListRequest(TypedDict):
    """Data in input of paymentAccount/list request"""

    accountNumber: Optional[str]  # A string representing the account number
    currency: Optional[str]  # Currency code in 3 characters ISO format
    accountStatus: Optional[
        STATUS
    ]  # Account status code in one char length. Enum: [ A, D, R, S ]
    # A: Activated D: Deactivated R: Registered S: Suspended
    sellerReference: Optional[str]  # Account reference
    pagination: Optional[
        str
    ]  # Numbers of ligne in reporting. Limited to 100. Default value 50.
    offset: Optional[str]  # Start response line. Set to 0 when not indicated


class PaymentAccountListResponse(TypedDict):
    """Data in output of paymentAccount/list request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    lineCount: Optional[str]  # Total number of lines
    accountList: Optional[List[PaymentAccount]]  # List of accounts


class PaymentAccountCreditRequest(TypedDict):
    """Data in input of paymentAccount/credit request"""

    accountNumber: str  # A string representing the account number
    amount: str  # Recharge amount
    currency: str  # Currency code in 3 characters ISO format
    paymentMethodKey: PAYMETHODKEY  # Key identifier of the payment method type id


class PaymentAccountCreditResponse(TypedDict):
    """Data in output of paymentAccount/credit request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    transactionId: Optional[str]  # Id of the payment transaction
    virtualIban: Optional[str]  # Iban to make payment to for SCT or SWIFT method


class PaymentAccountPayoutAutoRequest(TypedDict):
    """Data in input of paymentAccount/payoutAuto request"""

    accountNumber: Optional[str]  # A string representing the account number
    amount: str  # Recharge amount
    frequency: FREQUENCY  # Enum: [0, 1, 2, 3]
    # 0: deactivate 1: once a day 2: once a week 3: once a month 10: Automatic on threshold
    dayOfWeek: Optional[DAYOFWEEK]  # Between 0 and 6
    dayOfMonth: Optional[DAYOFMONTH]  # Between 1 et 31
    paymentMethodAlias: Optional[str]  # Alias for the payment method


class PaymentAccountSetIBANRequest(TypedDict):
    """Data in input of paymentAccount/setIBAN request"""

    accountNumber: Optional[str]  # A string representing the account number
    lastName: Optional[str]  # The last name of the IBAN account's owner
    firstName: Optional[str]  # The first name of the IBAN account's owner
    address: str  # The road name and number of the IBAN account's owner
    city: str  # The city of the IBAN account's owner
    country: str  # The country code (in 3 letter format) of the IBAN account's owner
    postalCode: str  # The postal code of the IBAN account's owner
    socialReason: Optional[str]  # The name of the IBAN account's owner if compagny
    fileType: Optional[FILETYPE]  # Type of the file contening the proof document
    fileContent: Optional[
        str
    ]  # The content of the file contening the proof in base64 encoding format
    iban: str  # The new IBAN
    currency: str  # Currency code in 3 characters ISO format
    paymentMethodAlias: Optional[
        str
    ]  # Current payment method alias to update. If not provided a new payment method is added
    paymentMethodKey: Optional[
        PAYMETHODKEYIBAN
    ]  # Key identifier of the payment method type id


class PaymentAccountSetIBANResponse(TypedDict):
    """Data in output of paymentAccount/setIBAN request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    requestId: Optional[str]  # ID to identify processing request
    paymentMethodAlias: Optional[
        str
    ]  # Current payment method alias to update. If not provided a new payment method is added


class PaymentAccountDisableIBANRequest(TypedDict):
    """Data in input of paymentAccount/disableIBAN request"""

    requestId: Optional[str]  # Current payment method, or pending payment method
    paymentMethodAlias: Optional[str]  # Current payment method alias to update.
    # If not provided a new payment method is added


class PaymentAccountSetFloorLimitRequest(TypedDict):
    """Data in input of paymentAccount/setFloorLimit request"""

    accountNumber: str  # A string representing the account number
    amount: Amount  # Amount structure


class PaymentAccountReportRequest(TypedDict):
    """Data in input of paymentAccount/report request"""

    accountNumber: Optional[str]  # A string representing the account number
    type: REPORTTYPE  # Type of report. Available values : ACCOUNT_STATEMENT, INVOICE, IC_FEE_REPORT
    format: REPORTFORMAT  # Format of the report. Available values : P, C
    year: str  # Year of the report in AAAA format. Must be less or equal to the current year.
    month: Optional[
        MONTH
    ]  # Month of the report in MM format. Must be less or equal to the current month.


class PaymentAccountReportResponse(TypedDict):
    """Data in output of paymentAccount/report request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    type: Optional[
        REPORTTYPE
    ]  # Type of report. Available values : ACCOUNT_STATEMENT, INVOICE, IC_FEE_REPORT
    accountNumber: Optional[str]  # A string representing the account number
    year: Optional[
        str
    ]  # Year of the report in AAAA format. Must be less or equal to the current year.
    month: Optional[
        MONTH
    ]  # Month of the report in MM format. Must be less or equal to the current month.
    fileContent: Optional[
        str
    ]  # The content of the file contening the proof in base64 encoding format
