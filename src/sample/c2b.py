import requests
import important
from access_token import generate_access_token


def registration_url():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode": important.shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "http://benwawesh.com/confirmation",
        "ValidationURL": "http://benwawesh.com/validation_url"}

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)
registration_url()

import requests

access_token = generate_access_token()
api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
headers = {"Authorization": "Bearer %s" % access_token}
request = { "ShortCode":important.shortcode,
"CommandID":"CustomerPayBillOnline",
"Amount":"5",
"Msisdn":important.msisdna,
"BillRefNumber":"1234556" }

response = requests.post(api_url, json = request, headers=headers)

print (response.text)
