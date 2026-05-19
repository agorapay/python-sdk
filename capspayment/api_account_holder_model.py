"""Account Holder API Model"""

from typing import List, Literal, Optional, TypedDict

ROLE = Literal["BE", "D", "MD", "CP", "PR"]
GENDER = Literal["M", "F"]
REGULATEDSOCIETY = Literal["Y", "N"]
USPERSON = Literal["Y", "N"]
FILEEXT = Literal["JPEG", "JPG", "PNG", "PDF", "DOC"]
FILEEXTUPLOAD = Literal["JPEG", "PNG", "PDF", "DOC", "XLS", "XLSX"]
FILEEXTDETAIL = Literal["PDF"]
MANDATORY = Literal["Y", "N"]
RESIDENT = Literal["R", "N"]
VALUE = Literal["Y", "N", "NC"]
VALIDATED = Literal["Y", "N"]
CHANNEL = Literal["EPI"]
REQUESTSTATUS = Literal[
    "To validate",
    "Confirmed",
    "Pending",
    "Validated",
    "Rejected",
    "Canceled",
    "Expired",
    "Completed",
    "Forced",
    "To check",
    "Created",
    "Analysis",
    "To read",
    "To score",
    "To control",
    "To screen",
]
REQUIREMENTSTATUS = Literal[
    "Missing",
    "Incomplete",
    "To validate",
    "Validated",
    "To sign",
    "Forced",
    "To read",
    "To screen",
    "Supervised"
]
DOCSTATUS = Literal[
    "Missing",
    "Partial",
    "To validate",
    "Validated",
    "Refused"
]
FILETYPE = Literal[
    "PASSPORT",
    "IDCARD_FRONT_BACK",
    "COMPANY_REG",
    "BANK_ID",
    "COMPANY_REG_WORLD",
    "OTHER_DOC",
    "ACCOUNT_AGR",
    "QUESTIONNAIRE",
    "IDCARD_FRONT",
    "IDCARD_BACK",
    "NONPROFIT_REG",
    "NONPROFIT_OJ",
    "COMPANY_ART",
    "REPORT_GEN_ASS",
    "PERMANENT_RES",
    "UBO_REG",
    "SIRENE_REG",
    "RECEIPT_APP",
    "SIRENE_NOT",
    "INDIVIDUAL_REG",
    "PROPERTY_TAX",
    "HOUSING_TAX",
    "INVOICE",
    "COOP_APP",
    "PROOF_REG",
    "COMPANY_CER_WORLD",
    "COMPANY_ART_WORLD",
    "UBO_REG_WORLD",
    "SYND_ID",
    "REPORT_GEN_SYND",
    "CPS_CARD",
    "RPPS_CARD",
    "DEGREE_CARD",
    "CPP_CARD",
    "CERTIFIED_STATUS",
    "PROCURATION",
    "MGR_MANDATE"
]


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


class Role(TypedDict):
    """Role Information"""

    role: Optional[ROLE]  # Physical person role


class RequirementResponse(TypedDict):
    """Requirement Response Structure"""

    id: str  # Requirement identification number
    label: Optional[str]  # Requirement description
    code: Optional[str]  # Requirement code identification
    fileExt: Optional[FILEEXT]  # Type of file provided (JPEG, JPG, PNG, PDF, DOC)
    fileContent: Optional[str]  # Content of the document base64 encoded
    fileType: Optional[str]  # Type of docuemnt (National card identity, KBIS, ...)
    mandatory: Optional[MANDATORY]  # Y or N. May be absent if N


class RequirementResponseDetailDocument(TypedDict):
    """Requirement Response Detail Document Structure"""

    fileExt: Optional[FILEEXTDETAIL]  # Type of file provided in fileContent (PDF)
    fileContent: Optional[str]  # Content of the document base64 encoded
    status: DOCSTATUS  # Document status
    receiptDate: Optional[str]  # Date of document reception in ISO8601 format
    validated: Optional[VALIDATED]  # Y or N
    fileType: Optional[str]  # Type of docuemnt (National card identity, KBIS, ...)
    validateDate: Optional[str]  # Date of document validation in ISO8601 format
    reason: Optional[str]  # Operation label transmitted in payment system.


class RequirementResponseDetail(TypedDict):
    """Requirement Response Detail Structure"""

    id: str  # Requirement identification number
    mandatory: MANDATORY  # Y or N. May be absent if N
    label: str  # Requirement description
    code: Optional[str]  # Requirement code identification
    status: Optional[REQUIREMENTSTATUS]  # Requirement status
    fileExt: Optional[FILEEXTDETAIL]  # Type of file provided in fileContent (PDF)
    fileContent: Optional[str]  # Content of the document base64 encoded
    documents: Optional[List[RequirementResponseDetailDocument]]  # List of documents


class RequirementUploadRequest(TypedDict):
    """Requirement Upload Request Structure"""

    id: str  # Requirement identification number
    fileExt: Optional[FILEEXTUPLOAD]  # Type of file provided (JPEG, JPG, PNG, PDF, DOC)
    fileType: FILETYPE  # Type of document


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
    country: str  # The ISO country code


class RegisterPersonRequest(TypedDict):
    """Register Person Request Structure"""

    resident: Optional[RESIDENT]  # Flag to indicate whether
    # the physical person is a resident (R) or a non-resident (N)
    gender: GENDER  # Person gender M or F. Enum: [M, F]
    firstName: str
    lastName: str
    email: Optional[str]
    phoneNumber: Optional[str]
    roles: List[Role]  # Role of a physical person. Enum: [BE, D, MD, CP, PR]
    # BE : Beneficial owner, D : Manager, MD : Mandatary, AP : Protal admin
    # CP : Legal representative, PR : Regulated Profession
    birthDate: Optional[str]  # Date of birth in YYYYMMAA format
    physicalAddress: Optional[RegisterAddress]


class OnlineRegisterPersonRequest(TypedDict):
    """Online Register Person Request Structure"""

    gender: GENDER  # Person gender M or F. Enum: [M, F]
    firstName: str
    lastName: str
    email: Optional[str]
    phoneNumber: Optional[str]
    roles: List[Role]  # Role of a physical person. Enum: [BE, D, MD, CP, PR]
    # BE : Beneficial owner, D : Manager, MD : Mandatary, AP : Protal admin
    # CP : Legal representative, PR : Regulated Profession
    resident: Optional[RESIDENT]  # Flag to indicate whether
    # the physical person is a resident (R) or a non-resident (N)
    citizenShip: str  # The ISO country code in 2 characters format
    birthDate: str  # Date of birth in YYYYMMAA format
    birthCountryCode: str  # The ISO country code in 2 characters format
    birthPlaceTown: Optional[str]
    birthPlaceZipCode: Optional[str]
    physicalAddress: Optional[RegisterAddress]
    percentageHeld: Optional[str]
    usPerson: USPERSON


class RegisterPersonResponse(TypedDict):
    """Register Person Response Structure"""

    firstName: str
    lastName: str
    id: str  # Registration identification number
    requirements: List[RequirementResponse]  # List of document to provide or provided


class RegisterPersonResponseDetail(TypedDict):
    """Register Person Response Detail Structure"""

    firstName: str
    lastName: str
    id: str  # Registration identification number
    requirements: List[RequirementResponseDetail]  # List of document to provide or provided


class RegisterPersonUpdateRequest(TypedDict):
    """Register Person Update Request Structure"""

    id: Optional[str]  # Id of previous registered person
    gender: GENDER  # Person gender M or F. Enum: [M, F]
    firstName: str
    lastName: str
    email: Optional[str]
    phoneNumber: Optional[str]
    roles: List[Role]  # Role of a physical person. Enum: [BE, D, MD, CP]
    # BE : Beneficial owner, D : Manager, MD : Mandatary, AP : Protal admin
    # CP : Legal representative
    birthDate: Optional[str]  # Date of birth in YYYYMMAA format
    physicalAddress: Optional[RegisterAddress]


class RiskCountry(TypedDict):
    """Risk Country Information"""

    country: str  # The ISO country code in 2 characters format
    percentage: str  # Percentage of net turnover (excluding VAT) in the country


class Country(TypedDict):
    """Country Information"""

    country: str


class Authority(TypedDict):
    """Authority Information"""

    authorityName: str


class SpecificOperation(TypedDict):
    """Specific Operation Information"""

    value: VALUE  # Existence of a country questionnaire for specific operation
    countryList: Optional[List[Country]]


class LicensedOperation(TypedDict):
    """Licensed Operation Information"""

    value: VALUE  # Existence of a country questionnaire for specific operation
    authorityList: Optional[List[Authority]]


class AccountHolderRegisterRequest(TypedDict):
    """Data in input of accountHolder/register request"""

    productCode: Optional[str]  # Product Code to subscribe to
    NAFCode: Optional[str] # NAF Code
    socialReason: str  # Holder name
    companyName: Optional[str]  # Commercial name
    country: str  # The ISO country code in 3 characters format
    legalForm: str
    registrationNumber: str  # SIRET for France
    masterAddress: RegisterAddress
    commercialAddress: Optional[RegisterAddress]
    turnover: str  # Current or last year turnover in account currency code unit
    regulatedSociety: REGULATEDSOCIETY  # Y or N
    physicalPersons: List[
        RegisterPersonRequest
    ]  # At least one person must be provided with CP role
    account: RegisterAccount
    currency: str  # Currency code in 3 characters ISO format
    owner: Owner
    authorizedOverdraft: Optional[str]  # Maximal amount of Short-Term Credit Facilities


class AccountHolderRegisterResponse(TypedDict):
    """Data in output of accountHolder/register request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    requestId: Optional[str]  # Id used for futher update function call
    accountNumber: Optional[str]  # A string representing the account number
    paymentMethodAlias: Optional[str]  # Alias for the payment method
    requirements: Optional[List[RequirementResponse]]
    physicalPersons: Optional[List[RegisterPersonResponse]]
    status: Optional[REQUESTSTATUS]  # Request status


class AccountHolderOnlineRegisterRequest(TypedDict):
    """Data in input of accountHolder/onlineRegister request"""

    productCode: str  # Product Code to subscribe to
    sellerReference: Optional[str]  # Agorapay holder reference
    externalReference: str  # External holder reference
    NAFCode: str # NAF Code
    VATCode: str # VAT Code
    socialReason: str  # Holder name
    companyName: Optional[str]  # Commercial name
    currency: str  # Currency code in 3 characters ISO format
    country: str  # The ISO country code in 3 characters format
    legalForm: str
    registrationNumber: str  # SIRET for France
    masterAddress: RegisterAddress
    commercialAddress: Optional[RegisterAddress]
    turnover: str  # Current or last year turnover in account currency code unit
    regulatedSociety: REGULATEDSOCIETY  # Y or N
    usPerson: USPERSON  # Y or N
    physicalPersons: List[
        OnlineRegisterPersonRequest
    ]  # At least one person must be provided with CP role
    account: RegisterAccount
    owner: Owner
    introducerRiskLevel: str  # Vigilance level
    introducerRiskScore: Optional[str]  # Scoring
    taxAddress: Optional[RegisterAddress]  # Tax address for a legal entity
    riskCountry: Optional[List[RiskCountry]]  # For all countries considered high-risk
    # where the client operates and carries out activities
    countryPurchase: Optional[List[Country]]
    specificOperation: Optional[SpecificOperation]
    licensedOperation: Optional[LicensedOperation]
    introducerLastKYCReview: Optional[str]  # Introducer last KYC review in YYYYMMDD format
    channel: Optional[CHANNEL]  # Registration channel


class AccountHolderOnlineRegisterResponse(TypedDict):
    """Data in output of accountHolder/onlineRegister request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    sellerReference: Optional[str]  # Agorapay holder reference
    requestId: Optional[str]  # Request identifier for the enrollment
    tokenId: Optional[str]  # Id used for futher update function call
    externalReference: Optional[str]  # External holder reference
    accountNumber: Optional[str]  # A string representing the account number


class AccountHolderUnregisterRequest(TypedDict):
    """Data in input of accountHolder/unregister request"""

    requestId: str  # Id to identify processing request


class AccountHolderUpdateRequest(TypedDict):
    """Data in input of accountHolder/update request"""

    socialReason: Optional[str]  # Holder name
    companyName: Optional[str]  # Commercial name
    country: Optional[str]  # The ISO country code in 3 characters format
    masterAddress: Optional[RegisterAddress]
    commercialAddress: Optional[RegisterAddress]
    turnover: Optional[
        str
    ]  # Current or last year turnover in account currency code unit
    regulatedSociety: Optional[REGULATEDSOCIETY]  # Y or N
    physicalPersons: Optional[
        List[RegisterPersonUpdateRequest]
    ]  # At least one person must be provided with CP role
    account: Optional[RegisterAccount]
    owner: Optional[Owner]
    currency: Optional[str]  # Currency code in 3 characters ISO format
    requestId: str  # Id to identify processing request

class AccountHolderUpdateResponse(TypedDict):
    """Data in output of accountHolder/update request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    requestId: Optional[str]  # Id used for futher update function call
    accountNumber: Optional[str]  # A string representing the account number
    paymentMethodAlias: Optional[str]  # Alias for the payment method
    requirements: Optional[List[RequirementResponseDetail]]
    physicalPersons: Optional[List[RegisterPersonResponseDetail]]
    status: Optional[str]  # Request status


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
    accountNumber: Optional[str]  # A string representing the account number
    paymentMethodAlias: Optional[str]  # Alias for the payment method
    status: Optional[str]  # Request status
    requirements: Optional[List[RequirementResponseDetail]]
    physicalPersons: Optional[List[RegisterPersonResponseDetail]]


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
    requirements: Optional[List[RequirementResponseDetail]]
    physicalPersons: Optional[List[RegisterPersonResponseDetail]]
    status: Optional[REQUESTSTATUS]  # Request status
