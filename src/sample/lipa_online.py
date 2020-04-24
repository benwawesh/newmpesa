import requests
import base64
import important
from access_token import generate_access_token
from date import format_date
from password import password_generator
from requests.auth import HTTPBasicAuth
data=format_date()
password= password_generator()

 
def lipa_na_mpesa():

    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": important.business_short_code ,
    "Password": password,
    "Timestamp": data ,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "5",
    "PartyA":  important.phone_no,
    "PartyB": important.business_short_code  ,
    "PhoneNumber": important.phone_no ,
    "CallBackURL": "https://ben.com/callback",
    "AccountReference": "12345678",
    "TransactionDesc": "school fees "
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)
lipa_na_mpesa()
