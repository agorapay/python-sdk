"""
Model
"""

from dataclasses import dataclass
from typing import Any, Literal, Optional, TypedDict

from config import Config

PAYMETHODKEY = Literal["SDD", "SCT", "CARD", "SDD B2B", "PISP", "INT", "SCT INST"]
SEQUENCE = Literal["OOFF", "FRST", "RCUR", "FNAL"]

TRANSACTIONSTATUS = Literal[
    "created",
    "in_progress",
    "accepted",
    "completed",
    "canceled",
    "refused",
    "abandonned",
    "refund",
]
OPERATIONTYPE = Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "11"]
MONTH = Literal["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
DAYOFMONTH = Literal[
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
]
DAYOFWEEK = Literal["0", "1", "2", "3", "4", "5", "6"]
ACCOUNTTYPE = Literal["1", "3", "4", "5", "6", "13", "14", "15", "16"]


class Response(TypedDict):
    """Response Structure"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description


class Amount(TypedDict):
    """Amount Structure"""

    value: str  # The value of the amount in decimal with max 2 digits after separator
    currency: str  # The currency iso code of the amount with 3 characters


class Commission(TypedDict):
    """Commission Structure"""

    amount: str  # Amount of the commission in the currency of the order with two decimal maximum
    account: Optional[str]  # Account number for the commission


class BreakDown(TypedDict):
    """Break Down Structure"""

    amount: Amount  # Amount structure
    sellerAccountNumber: str  # Account number of the merchant
    label: str  # Label for the breakdown
    commission: Optional[Commission]  # Commission information


class PaymentMethodSimple(TypedDict):
    """Payment Method Simple Structure"""

    id: str  # Id of the payment method


class Payer(TypedDict):
    """Payer Structure"""

    IPAddress: Optional[str]  # IP Address of the customer
    reference: str  # Reference of the customer from the marketplace
    userAgent: Optional[str]  # The browser information use to request the payment
    language: Optional[str]  # The default language of the browser.
    # The first two characters are used to identify the language code


class Details(TypedDict):
    """Payment Details Information"""

    firstName: Optional[str]
    lastName: Optional[str]
    address: Optional[str]  # Road name and number
    city: Optional[str]
    postalCode: Optional[str]
    country: Optional[str]  # Country in 3 letters ISO format
    iban: Optional[str]
    email: Optional[str]
    state: Optional[str]
    gender: Optional[str]
    phoneNumber: Optional[str]
    sequence: Optional[SEQUENCE]  # Mandate sequence. Enum: [ OOFF, FRST, RCUR, FNAL ]
    reference: Optional[
        str
    ]  # For payment with mandate, this field is the reference to the mandate for sequence
    # RCUR or LAST. For payment with card, this field is the transactionId of the first
    # authorization transaction
    socialReason: Optional[str]  # Compagny name
    address2: Optional[str]  # Additional address


@dataclass
class Request:
    """Request Structure"""

    method: str
    url: str
    data: Any
    headers: dict
    config: Config
    multipart: Literal[True, False] = False
