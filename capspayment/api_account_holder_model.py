"""Account Holder API Model"""

from typing import List, Literal, Optional, TypedDict

DOCUMENTSTATUS = Literal["MISSING", "PARTIAL", "TOVALIDATE", "VALIDATED", "REFUSED"]
ROLE = Literal["BE", "D", "MD", "AP", "CP"]
GENDER = Literal["M", "F"]
REGULATEDSOCIETY = Literal["Y", "N"]
FILEEXT = Literal["JPEG", "JPG", "PNG", "PDF", "DOC"]
MANDATORY = Literal["Y", "N"]


class Owner(TypedDict):
    """Account Owner Information"""

    firstName: Optional[str]  # Mandatory if socialReason not present
    lastName: Optional[str]  # Mandatory if socialReson not present
    socialReason: Optional[str]  # Mandatory if firstName or lastName not present
    address: str  # Number and road name
    city: str
    postalCode: str
    country: str  # The ISO country code in 3 characters format
    gender: Optional[GENDER]  # M or F. Mandatory if socialReason not present


class RequirementRequest(TypedDict):
    """Requirement Request Structure"""

    id: str  # Requirement identification number
    mandatory: MANDATORY  # -Y if document must be provided -N if document is not mandatory
    label: str  # Requirement description
    fileExt: Optional[FILEEXT]  # Type of file provided in fileContent (PDF)
    fileContent: Optional[str]  # Content of the document base64 encoded
    status: Optional[
        DOCUMENTSTATUS
    ]  # Document status. Enum: [MISSING, PARTIAL, TOVALIDATE, VALIDATED, REFUSED]
    receiptDate: Optional[str]  # Date of document reception in ISO8601 format
    validationDate: Optional[
        str
    ]  # Date of validation of the document in ISO8601 format


class RequirementResponse(TypedDict):
    """Requirement Response Structure"""

    id: str  # Requirement identification number
    label: Optional[str]  # Requirement description
    fileExt: Optional[FILEEXT]  # Type of file provided (JPEG, JPG, PNG, PDF, DOC)
    fileContent: Optional[str]  # Content of the document base64 encoded
    fileType: str  # Type of docuemnt (National card identity, KBIS, ...)
    mandatory: Optional[MANDATORY]  # Y or N. May be absent if N


class RequirementUploadRequest(TypedDict):
    """Requirement Upload Request Structure"""

    id: str  # Requirement identification number
    fileExt: FILEEXT  # Type of file provided (JPEG, JPG, PNG, PDF, DOC)
    fileContent: str  # Content of the document base64 encoded
    fileType: str  # Type of docuemnt (National card identity, KBIS, ...)


class RegisterAccount(TypedDict):
    """Register Account Structure"""

    country: str  # The ISO country code in 3 characters format
    currency: str  # Currency code in 3 characters ISO format
    iban: str  # International Bank Account Number
    floorLimit: str  # Floor limit in currency unit


class RegisterAddress(TypedDict):
    """Register Address Structure"""

    address: str  # Number and road name
    city: str
    postalCode: str
    country: str  # The ISO country code in 3 characters format


class RegisterPersonRequest(TypedDict):
    """Register Person Request Structure"""

    gender: GENDER  # Person gender M or F. Enum: [M, F]
    firstName: str
    lastName: str
    email: Optional[str]
    phoneNumber: Optional[str]
    roles: List[ROLE]  # Role of a physical person. Enum: [BE, D, MD, AP, CP]
    # BE : Beneficial owner, D : Manager, MD : Mandatary, AP : Protal admin
    # CP : Legal representative
    birthDate: Optional[str]  # Date of birth in YYYYMMAA format


class RegisterPersonResponse(TypedDict):
    """Register Person Response Structure"""

    firstName: str
    lastName: str
    id: str  # Registration identification number
    requirements: List[RequirementResponse]  # List of document to provide or provided


class RegisterPersonUpdateRequest(TypedDict):
    """Register Person Update Request Structure"""

    gender: GENDER  # Person gender M or F. Enum: [M, F]
    firstName: str
    lastName: str
    email: str
    phoneNumber: str
    roles: List[ROLE]  # Role of a physical person. Enum: [BE, D, MD, AP, CP]
    # BE : Beneficial owner, D : Manager, MD : Mandatary, AP : Protal admin
    # CP : Legal representative
    id: Optional[str]  # Id of previous registered person
    birthDate: Optional[str]  # Date of birth in YYYYMMAA format


class AccountHolderRegisterRequest(TypedDict):
    """Data in input of accountHolder/register request"""

    socialReason: str  # Holder name
    compagnyName: Optional[str]  # Commercial name
    country: str  # The ISO country code in 3 characters format
    legalForm: str
    registrationNumber: str  # SIRET for France
    masterAddress: RegisterAddress
    billingAddress: Optional[RegisterAddress]
    turnover: str  # Current or last year turnover in account currency code unit
    regulatedSociety: REGULATEDSOCIETY  # Y or N
    physicalPersons: List[
        RegisterPersonRequest
    ]  # At least one person must be provided with CP role
    account: RegisterAccount
    currency: str  # Currency code in 3 characters ISO format
    owner: Owner


class AccountHolderRegisterResponse(TypedDict):
    """Data in output of accountHolder/register request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    requestId: Optional[str]  # Id used for futher update function call
    accountNumber: Optional[str]  # A string representing the account number
    paymentMethodAlias: Optional[str]  # Alias for the payment method
    requirements: Optional[List[RequirementResponse]]
    physicalPersons: Optional[List[RegisterPersonResponse]]


class AccountHolderUnregisterRequest(TypedDict):
    """Data in input of accountHolder/unregister request"""

    accountNumber: Optional[str]  # A string representing the account number
    requestId: str  # Id to identify processing request


class AccountHolderUpdateRequest(TypedDict):
    """Data in input of accountHolder/update request"""

    socialReason: Optional[str]  # Holder name
    compagnyName: Optional[str]  # Commercial name
    country: Optional[str]  # The ISO country code in 3 characters format
    registrationNumber: Optional[str]  # SIRET for France
    masterAddress: Optional[RegisterAddress]
    billingAddress: Optional[RegisterAddress]
    turnover: Optional[
        str
    ]  # Current or last year turnover in account currency code unit
    regulatedSociety: Optional[REGULATEDSOCIETY]  # Y or N
    physicalPersons: Optional[
        List[RegisterPersonUpdateRequest]
    ]  # At least one person must be provided with CP role
    account: RegisterAccount
    currency: Optional[str]  # Currency code in 3 characters ISO format
    requestId: str  # Id to identify processing request
    owner: Optional[Owner]


class AccountHolderUpdateResponse(TypedDict):
    """Data in output of accountHolder/update request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    requestId: Optional[str]  # Id used for futher update function call
    accountNumber: Optional[str]  # A string representing the account number
    paymentMethodAlias: Optional[str]  # Alias for the payment method
    requirements: Optional[List[RequirementResponse]]
    physicalPersons: Optional[List[RegisterPersonResponse]]


class AccountHolderUploadDocumentRequest(TypedDict):
    """Data in input of accountHolder/uploadDocument request"""

    requirements: List[
        RequirementUploadRequest
    ]  # Document requirement for registration
    requestId: str  # Id to identify processing request


class AccountHolderUploadDocumentResponse(TypedDict):
    """Data in output of accountHolder/uploadDocument request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    requestId: Optional[str]  # Id used for futher update function call
    requirements: Optional[List[RequirementResponse]]
    physicalPersons: Optional[List[RegisterPersonResponse]]


class AccountHolderRegistrationDetailsRequest(TypedDict):
    """Data in input of accountHolder/registrationDetails request"""

    requestId: str  # Registration request identifier


class AccountHolderRegistrationDetailsResponse(TypedDict):
    """Data in output of accountHolder/registrationDetails request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    requestId: Optional[str]  # Id used for futher update function call
    accountNumber: Optional[str]  # A string representing the account number
    paymentMethodAlias: Optional[str]  # Alias for the payment method
    requirements: Optional[List[RequirementResponse]]
    physicalPersons: Optional[List[RegisterPersonResponse]]
