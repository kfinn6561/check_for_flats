from config import SMS_TO_NUMBERS
import os
from twilio.rest import Client
from threading import Thread


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure



def send_sms(message):
    Thread(target=send_async_sms, args=(message,)).start()

def send_async_sms(message):
    try:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        for to_number in SMS_TO_NUMBERS:
            client.messages.create(body=message,from_='+447360542923',to=to_number)
    except:
        print('Error sending sms')
    return 0
