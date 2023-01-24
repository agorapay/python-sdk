"""SelfCare API Model"""

from typing import Optional, TypedDict


class SelfCareInitRequest(TypedDict):
    """Data in input of selfcare/init request"""

    firstName: str  # Seller first name
    lastName: str  # Seller last name
    email: str  # Email
    phone: str  # Seller phone number
    socialReason: str  # Seller social reason
    accountFloorLimit: str  # Seller floor limit amount.
    # The value of the amount in decimal with max 2 digits after separator.
    # Only digits and dot are authorized.
    language: str  # The first two characters are used to identify the language code.
    # Must be in upper case. Only french is supported at this time.


class SelfCareInitResponse(TypedDict):
    """Data in output of selfcare/init request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    requestId: Optional[str]  # ID to identify processing request
    statusLabel: Optional[str]  # Request status label
