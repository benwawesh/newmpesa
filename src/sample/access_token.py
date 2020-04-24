from requests.auth import HTTPBasicAuth
import requests
import important


def generate_access_token():
    consumer_key = important.consumer_key
    print(consumer_key)
    consumer_secret = important.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_format= r.json()
    my_access_token= json_format['access_token']
    print(json_format)
    return my_access_token
print(generate_access_token())