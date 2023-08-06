import os
import time
from datetime import datetime
import pytz
from twilio.rest import Client
from dotenv import load_dotenv, dotenv_values

def sendMessage(info):
    load_dotenv()
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")

    auth_token  = os.getenv("TWILIO_AUTH_TOKEN")
    to_number = os.getenv("TO_NUMBER")
    from_number = os.getenv("FROM_NUMBER")

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=to_number, 
        from_=from_number,
        body=info)
    print(message.sid)

def send_time_message(message):
    est_tz = pytz.timezone('US/Eastern')
    while True:
        # Get current time in Eastern Standard Time
        current_time = datetime.now(est_tz)
        if current_time.hour == 9 and current_time.minute == 30:
            sendMessage(message)
            time.sleep(30)
        time.sleep(10)