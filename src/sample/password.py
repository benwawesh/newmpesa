import important
import base64
from date import format_date
def password_generator():
    data_to_encode = important.business_short_code + important.pass_key + format_date()
    encoded_string= base64.b64encode(data_to_encode.encode())
    decoded_password= encoded_string.decode('utf-8')
    
    return decoded_password
