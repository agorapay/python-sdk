"""Payin API Model"""

from typing import List, Literal, Optional, TypedDict

from model import OPERATIONTYPE, SEQUENCE, TRANSACTIONSTATUS, Amount, BreakDown

ORDERSTATUS = Literal[
    "created", "pending_payment", "partial_complete", "complete", "canceled"
]
PAYMENTMETHODTYPEID = Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

CBCHALLENGE = Literal["01", "02", "03", "04"]

CAPTURE = Literal["1", "0", "Y", "N"]

ALIAS = Literal["1", "0", "Y", "N"]

RECURRENT = Literal["1", "0", "Y", "N"]

PAGE = Literal["full", "iframe"]

PAYMENTOPTIONS = Literal["cardOnFile", "withoutCardOnFile"]


class Alias(TypedDict):
    """Alias Structure"""

    id: str  # Identifier for the alias
    expirationDate: Optional[str]  # format MMYY
    maskedPan: Optional[
        str
    ]  # First 6 and last 4 digits of the PAN for card or Masqued IABN for SDD
    label: Optional[str]  # Label of the alias
    brand: Optional[str]  # Card brand (CB, VISA, MASTERCARD) or bank code for IBAN
    bankCode: Optional[str]


class AliasSimple(TypedDict):
    """Alias Simple Structure"""

    id: str  # Identifier for the alias


class Cart(TypedDict):
    """Cart Structure"""

    totalQuantity: str  # number of article in cart


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


class PaymentMethodSimple(TypedDict):
    """Payment Method Simple Structure"""

    id: str  # Id of the payment method


class PaymentMethod(TypedDict):
    """Payment Method Structure"""

    aliasList: Optional[List[Alias]]
    id: str  # Id of the payment method
    label: Optional[str]  # Label of the payment Method
    type: Optional[
        PAYMENTMETHODTYPEID
    ]  # Id of the type of payment method. Enum: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # 1: Sepa Direct Debit 2: Sepa Credit Transfer 3: Transfer 4: Card 5: SWIFT
    # 6: Sepa Direct Debit B2B 7: Letter of credit 8: Voucher 9: Remainder
    # 10: SCT instant 11: PISP


class PayerSimple(TypedDict):
    """Payer Simple Structure"""

    reference: str  # Reference of the customer from the marketplace
    language: Optional[str]  # The default language of the browser.


class Transaction(TypedDict):
    """Transaction Structure"""

    paymentMethodId: Optional[str]  # Id of the payment Method used for the transaction
    id: str  # Id of the payment transaction
    status: TRANSACTIONSTATUS  # Status of a transaction
    amount: Amount  # Amount structure
    type: Optional[OPERATIONTYPE]  # Type of the operation
    # 1: Purchase 2: Refund 3: Manual
    # 4: Transfer 5: Payment 6: Reload/Payout
    # 7: Authorization 8: Pre-authorization 9: Unpaid 11: Fees


class PayinPaymentRequest(TypedDict):
    """Data in input of payin/payment request"""

    transPaymentMethod: Optional[PaymentMethodSimple]
    orderId: Optional[
        str
    ]  # Order id obtained in order creation and to provide in each next request
    orderReference: Optional[str]  # Marketplace reference for this order
    orderCountryCode: Optional[str]  # The ISO country code in 3 characters format
    breakdownList: Optional[List[BreakDown]]  # List of breakdown for this payment
    alias: Optional[AliasSimple]
    metaData: Optional[str]  # JSON data for the marketplace
    payer: Optional[Payer]
    details: Optional[Details]
    capture: Optional[CAPTURE]  # Capture indicator. Set to "0" for authorization only
    transactionAmount: Amount  # Amount structure
    urlRedirect: str  # Url where the client must be redirected at the end of the payment
    # with the partner
    registerAlias: Optional[
        ALIAS
    ]  # When set to "1", an alias will be registered when the payment will be completed,
    # if possible
    reason: Optional[str]  # Operation label transmited in payment system
    endToEndId: Optional[str]  # Use to identify transaction in SEPA transfer
    cart: Optional[Cart]
    operationDate: Optional[str]  # Date of the operation. The format must be YYYYMMDD
    cbChallenge: Optional[CBCHALLENGE]  # Challenge negotiation for card payment.
    # 01: No preference, 02: No challenge required, 03: Desired challenge
    # 04: Required challenge
    paymentOptions: Optional[PAYMENTOPTIONS]


class PayinPaymentResponse(TypedDict):
    """Data in output of payin/payment request"""

    orderId: Optional[
        str
    ]  # Order id obtained in order creation and to provide in each next request
    orderStatus: Optional[
        ORDERSTATUS
    ]  # Status of an order. Enum: [created, pending_payment, partial_complete, complete, canceled]
    transactionId: Optional[str]  # Id of the payment transaction
    transactionStatus: Optional[TRANSACTIONSTATUS]  # Status of a transaction
    resultCode: str  # API operation result. This code is 0 in case of success
    virtualIban: Optional[str]  # Iban to make payment to for SCT or SWIFT method
    redirectUrl: Optional[
        str
    ]  # Url to redirect the client to to continue the payment with an external partner
    # The marketplace must redirect his/her client to this url to continue payment process
    reference: Optional[str]  # Mandate referernce
    resultCodeMessage: Optional[str]  # The failure description
    redirectInd: Optional[str]  # 1 if user must be redirect to the redirectUrl site


class PayinPaymentDetailsRequest(TypedDict):
    """Data in input of payin/paymentDetails request"""

    metaData: Optional[str]  # JSON data for the marketplace
    orderId: str  # Order id obtained in order creation and to provide in each next request
    paymentData: Optional[str]  # Specific data for a payment method


class PayinPaymentDetailsResponse(TypedDict):
    """Data in output of payin/paymentDetails request"""

    orderId: Optional[
        str
    ]  # Order id obtained in order creation and to provide in each next request
    orderStatus: Optional[
        ORDERSTATUS
    ]  # Status of an order. Enum: [created, pending_payment, partial_complete, complete, canceled]
    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    transactionId: Optional[str]  # Id of the payment transaction
    transactionStatus: Optional[TRANSACTIONSTATUS]  # Status of a transaction
    reference: Optional[str]  # Mandate referernce


class PayinPaymentMethodsRequest(TypedDict):
    """Data in input of payin/paymentMethods request"""

    orderReference: str  # Marketplace reference for this order
    orderCountryCode: str  # The ISO country code in 3 characters format
    amount: Amount  # Amount structure
    payer: Payer
    metaData: Optional[str]  # JSON data for the marketplace


class PayinPaymentMethodsResponse(TypedDict):
    """Data in output of payin/paymentMethods request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    paymentMethodList: Optional[List[PaymentMethod]]
    orderId: Optional[
        str
    ]  # Order id obtained in order creation and to provide in each next request
    resultCodeMessage: Optional[str]  # The failure description


class PayinCaptureRequest(TypedDict):
    """Data in input of payin/capture request"""

    orderId: str  # Order id obtained in order creation and to provide in each next request
    transactionAmount: Amount  # Amount structure
    metaData: Optional[str]  # JSON data for the marketplace
    breakdownList: Optional[List[BreakDown]]  # List of breakdown for this payment
    transactionId: Optional[str]  # Id of the payment transaction


class PayinCaptureResponse(TypedDict):
    """Data in output of payin/capture request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    orderStatus: ORDERSTATUS  # Status of an order
    # Enum: [created, pending_payment, partial_complete, complete, canceled]
    transactionList: List[Transaction]  # List of the order transactions
    resultCodeMessage: Optional[str]  # The failure description
    orderId: str  # Order id obtained in order creation and to provide in each next request


class PayinCancelRequest(TypedDict):
    """Data in input of payin/cancel request"""

    orderId: str  # Order id obtained in order creation and to provide in each next request
    transactionId: Optional[str]  # Id of the payment transaction
    metaData: Optional[str]  # JSON data for the marketplace


class PayinCancelResponse(TypedDict):
    """Data in output of payin/cancel request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    orderStatus: Optional[
        ORDERSTATUS
    ]  # Status of an order. Enum: [created, pending_payment, partial_complete, complete, canceled]
    transactionList: Optional[List[Transaction]]  # List of the order transactions
    resultCodeMessage: Optional[str]  # The failure description


class PayinOrderDetailsRequest(TypedDict):
    """Data in input of payin/orderDetails request"""

    orderId: str  # Id of the order


class PayinOrderDetailsResponse(TypedDict):
    """Data in output of payin/orderDetails request"""

    orderAmount: Optional[Amount]  # Amount structure
    orderRemainingAmount: Optional[Amount]  # Amount structure
    orderId: Optional[
        str
    ]  # Order id obtained in order creation and to provide in each next request
    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    orderStatus: Optional[
        ORDERSTATUS
    ]  # Status of an order. Enum: [created, pending_payment, partial_complete, complete, canceled]
    transactionList: Optional[List[Transaction]]  # List of the order transactions


class PayinAdjustPaymentRequest(TypedDict):
    """Data in input of payin/adjustPayment request"""

    breakdownList: Optional[List[BreakDown]]  # List of breakdown for this payment
    metaData: Optional[str]  # JSON data for the marketplace
    adjustAmount: Optional[Amount]
    orderId: Optional[
        str
    ]  # Order id obtained in order creation and to provide in each next request
    transactionId: Optional[str]  # Id of the payment transaction


class PayinPaymentIframeRequest(TypedDict):
    """Data in input of payin/paymentIframe request"""

    orderReference: str  # Marketplace reference for this order
    orderCountryCode: str  # The ISO country code in 3 characters format
    amount: Amount  # Amount structure
    breakdownList: Optional[List[BreakDown]]  # List of breakdown for this payment
    payer: PayerSimple
    capture: Optional[CAPTURE]  # Capture indicator. Set to "0" for authorization only
    metaData: Optional[str]  # JSON data for the marketplace
    recurrent: Optional[
        RECURRENT
    ]  # "1" for recurrent payment "0" or absent if not a recurrent payment
    endToEndId: Optional[str]  # Use to identify transaction in SEPA transfer
    paymentMethodId: Optional[str]  # Identifier of tjhe payment method
    urlRedirect: Optional[
        str
    ]  # Url where the client must be redirected at the end of the payment with the partner
    cart: Optional[Cart]
    paymentAccount: Optional[str]  # Account number of the marketplace
    cbChallenge: Optional[CBCHALLENGE]  # Challenge negotiation for card payment.
    # 01: No preference, 02: No challenge required, 03: Desired challenge
    # 04: Required challenge
    details: Optional[Details]
    page: Optional[PAGE]
    paymentOptions: Optional[PAYMENTOPTIONS]
    reason: Optional[str]  # Operation label transmited in payment system


class PayinPaymentIframeResponse(TypedDict):
    """Data in output of payin/paymentIframe request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    orderId: Optional[
        str
    ]  # Order id obtained in order creation and to provide in each next request
    resultCodeMessage: Optional[str]  # The failure description
    authenticationCode: Optional[
        str
    ]  # Authentification Code to use to open user iframe
    site: Optional[str]  # Site name or number
    url: Optional[str]  # Url to connect iframe to


class PayinRefundRequest(TypedDict):
    """Data in input of payin/refund request"""

    orderId: str  # Order id obtained in order creation and to provide in each next request
    transactionAmount: Amount  # Amount structure
    transactionId: Optional[str]  # Id of the payment transaction
    metaData: Optional[str]  # JSON data for the marketplace
    reason: Optional[str]  # Operation label transmited in payment system
    breakdownList: Optional[List[BreakDown]]  # List of breakdown for this payment
    orderReference: str  # Marketplace reference for this order
    payer: PayerSimple


class PayinRefundResponse(TypedDict):
    """Data in output of payin/refund request"""

    orderStatus: Optional[
        ORDERSTATUS
    ]  # Status of an order. Enum: [created, pending_payment, partial_complete, complete, canceled]
    transactionList: Optional[List[Transaction]]  # List of the order transactions
    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    orderId: Optional[
        str
    ]  # Order id obtained in order creation and to provide in each next request


class PayinMandateRequest(TypedDict):
    """Data in input of payin/mandate request"""

    transactionId: Optional[str]  # Id of the payment transaction
    reference: Optional[str]  # Mandate referernce


class PayinMandateResponse(TypedDict):
    """Data in output of payin/mandate request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    transactionId: Optional[str]  # Id of the payment transaction
    reference: Optional[str]  # Mandate referernce
    signedFileContent: Optional[str]  # PDF file base64 encoded


class PayinTicketRequest(TypedDict):
    """Data in input of payin/ticket request"""

    transactionId: str  # Id of the card transaction
    format: str  # Ticket format : J JSON, P : PDF
    type: str  # Ticket type : C client, M : merchant
    message: Optional[str]  # Message to set in the bottom of the ticket


class PayinTicketResponse(TypedDict):
    """Data in output of payin/ticket request"""

    resultCode: str  # API operation result. This code is 0 in case of success
    resultCodeMessage: Optional[str]  # The failure description
    transactionId: Optional[str]  # Id of the payment transaction
    name: Optional[str]
    brand: Optional[str]
    maskedPan: Optional[str]
    transactionStatus: Optional[TRANSACTIONSTATUS]  # Status of a transaction
    operationDate: Optional[
        str
    ]  # Date of the requested operation. The format must be YYYYMMDD
    operationTime: Optional[str]  # Operation time in HH:MM:SS format
    safe: Optional[str]  # Y if 3DS is verified
    type: Optional[str]  # 1: DEBIT, 2: CREDIT
    authNumber: Optional[str]
    transNumber: Optional[str]
    amount: Optional[Amount]  # Amount structure
    mode: Optional[str]  # PROD or TEST
    fileContent: Optional[str]  # PDF file content base64 encoded, if format is P
    contract: Optional[str]  # Payment partner contract number
