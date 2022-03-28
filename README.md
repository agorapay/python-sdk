CAPSPAYMENT PYTHON SDK
=================================================

CAPSPayment SDK is a Python client library to work with CAPSPAYMENT REST API.
&nbsp;

Requirements
-------------------------------------------------
To use this SDK, you will need (as a minimum):
* Python >= v3.8
* Modules => requirements.txt
&nbsp;

Install
-------------------------------------------------
```python
python setup.py install  
```

or 
```python
pip install -r requirements.txt  
```
&nbsp;

Quick Start
-------------------------------------------------

* 1 - Init Api  
    ex: Payment Account API  

    ```python
    from api import CAPSPaymentAPI  
    api_request = CAPSPaymentAPI(
        api_url,
        token_url,
        token_user,
        token_password,
    ).payment_account_api()
    ```
    or

    ```python
    from api import CAPSPaymentAPI  
    api_main = CAPSPaymentAPI(
        api_url,
        token_url,
        token_user,
        token_password,
    )
    api_request = api_main.payment_account_api()
    ```

* 2 - Call API method  
    ex: call payment_account  
    ```python
    payload = {'accountNumber': '1300600000EUR01004110'}  
    response = api_request.payment_account(payload)  
    ```
&nbsp;

API links:
-------------------------------------------------

| API | Method
| ----------- | ----------- |
| Account Holder | account_holder_api
| Operations | operations_api
| Payin | payin_api
| Payment Account | payment_account_api
| Payout | payout_api
| Transfer | transfer_api

&nbsp;

List SDK functions to use for API AccountHolder
-------------------------------------------------

You will find in this table which function to use for each API "AccountHolder" endpoint :

| AccountHolder Endpoint      | SDK Functions | Method
| ----------- | ----------- | ----------- |
| /accountHolder/register      | ApiAccountHolder.register(payload)       | POST
| /accountHolder/unregister      | ApiAccountHolder.unregister(payload)       | POST
| /accountHolder/update      | ApiAccountHolder.update(payload)       | POST
| /accountHolder/uploadDocument      | ApiAccountHolder.upload_document(payload)       | POST
| /accountHolder/registrationDetails      | ApiAccountHolder.registration_details(payload)       | GET

&nbsp;

List SDK functions to use for API Operation
-------------------------------------------------

You will find in this table which function to use for each API "Operation" endpoint :

| Operation Endpoint      | SDK Functions | Method
| ----------- | ----------- |----------- |
| /operations/list     | ApiOperations.operation_list(payload)       | POST

&nbsp;

List SDK functions to use for API Payin
-------------------------------------------------

You will find in this table which function to use for each API "Payin" endpoint :

| Payin Endpoint      | SDK Functions | Method |
| ----------- | ----------- |----------- |
| /payin/payment      | ApiPayin.payment(payload)       | POST
| /payin/paymentDetails   | ApiPayin.payment_details(payload)        | POST
| /payin/paymentMethods   | ApiPayin.payment_methods(payload)        | POST
| /payin/capture   | ApiPayin.capture(payload)        | POST
| /payin/cancel   | ApiPayin.cancel(payload)        | POST
| /payin/orderDetails   | ApiPayin.order_details(payload)        | GET
| /payin/adjustPayment   | ApiPayin.adjust_payment(payload)        | POST
| /payin/paymentIframe   | ApiPayin.payment_iframe(payload)        | POST
| /payin/refund   | ApiPayin.refund(payload)        | POST
| /payin/mandate   | ApiPayin.mandate(payload)        | GET
| /payin/ticket   | ApiPayin.ticket(payload)        | GET

&nbsp;

List SDK functions to use for API PaymentAccount
-------------------------------------------------

You will find in this table which function to use for each API "PaymentAccount" endpoint :

| PaymentAccount Endpoint      | SDK Functions | Method
| ----------- | ----------- |----------- |
| /paymentAccount/setFloorLimit      | ApiPaymentAccount.set_floor_limit(payload) | POST
| /paymentAccount/setIBAN   | ApiPaymentAccount.set_iban(payload)        | POST
| /paymentAccount/disableIBAN   | ApiPaymentAccount.disable_iban(payload)        | POST
| /paymentAccount/List   | ApiPaymentAccount.payment_account_list(payload)        | POST
| /paymentAccount/recharge   | ApiPaymentAccount.recharge(payload)        | POST
| /paymentAccount   | ApiPaymentAccount.payment_account(payload)       | GET
| /paymentAccount/payoutAuto   | ApiPaymentAccount.payout_auto(payload)       | POST
| /paymentAccount/credit   | ApiPaymentAccount.credit(payload)       | POST
| /paymentAccount/create   | ApiPaymentAccount.create(payload)       | POST

&nbsp;

List SDK functions to use for API Payout
-------------------------------------------------

You will find in this table which function to use for each API "Payout" endpoint :

| Payout Endpoint      | SDK Functions | Method
| ----------- | ----------- |----------- |
| /payout/create      | ApiPayout.create(payload)       | POST

&nbsp;

List SDK functions to use for API Transfer
-------------------------------------------------

You will find in this table which function to use for each API "Transfert" endpoint :

| Transfer Endpoint      | SDK Functions | Method
| ----------- | ----------- | ----------- |
| /transfer/create      | ApiTransfer.create(payload)       | POST

&nbsp;

&nbsp;
