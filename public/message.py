import os
import time
from datetime import datetime
import pytz
from twilio.rest import Client
from dotenv import load_dotenv, dotenv_values

def sendMessage(info): #send message using twilio api
    load_dotenv() #loads environment variables
    account_sid = os.getenv("TWILIO_ACCOUNT_SID") #uses environment variables to get twilio account sid

    auth_token  = os.getenv("TWILIO_AUTH_TOKEN") #uses enviornment variables to get twilio authenticaition token
    to_number = os.getenv("TO_NUMBER") #uses enviornment variables to retireve phone number
    from_number = os.getenv("FROM_NUMBER") #uses enviornment variables to retrieve Twilio phone number

    client = Client(account_sid, auth_token) #sends message
    message = client.messages.create(
        to=to_number, 
        from_=from_number,
        body=info)
    print(message.sid) #prints message id

def send_time_message(message): #sends message at 9:30am EST
    est_tz = pytz.timezone('US/Eastern')
    while True:
        current_time = datetime.now(est_tz)
        if current_time.hour == 9 and current_time.minute == 30:
            sendMessage(message)
            time.sleep(30)
        time.sleep(10)
