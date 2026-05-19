"""Virtual IBAN API Model"""

from typing import List, Literal, Optional, TypedDict

STATUSVIBAN = Literal["0", "1"]
MODEVIBAN = Literal["0", "1", "2"]

class VirtualIbanDetails(TypedDict):
    """Virtual Iban Details Structure"""

    accountNumber: Optional[str]  # A string representing the account number
    virtualIban: Optional[str]  # Iban to make payment to for SCT or SWIFT method
    status: Optional[STATUSVIBAN]  # Virtual IBAN status (0: inactif, 1: actif)
    mode: Optional[MODEVIBAN]  # Virtual IBAN mode
    # (0: single use, 1: multiple uses (recurring), 2: unlimited)
    payerRef: Optional[str]  # Payer reference associated to the virtual IBAN


class PayerVIban(TypedDict):
    """Payer Virtual Iban Structure"""

    reference: str  # Reference of the customer from the marketplace


class VIbanCreateRequest(TypedDict):
    """Data in input of vIban/create request"""

    accountNumber: str  # A string representing the account number
    payer: Optional[PayerVIban]  # Payer information


class VIbanCreateResponse(TypedDict):
    """Data in output of vIban/create request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    virtualIban: Optional[str]  # Iban to make payment to for SCT or SWIFT method


class VIbanDeleteRequest(TypedDict):
    """Data in input of vIban/delete request"""

    virtualIban: str  # Iban to make payment to for SCT or SWIFT method


class VIbanListRequest(TypedDict):
    """Data in input of vIban/list request"""

    accountNumber: Optional[str]  # A string representing the account number
    payer: Optional[PayerVIban]  # Payer information
    virtualIban: Optional[str]  # Iban to make payment to for SCT or SWIFT method


class VIbanListResponse(TypedDict):
    """Data in output of vIban/list request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    lineCount: Optional[str]  # Total number of lines
    virtualIBANList: Optional[List[VirtualIbanDetails]]
