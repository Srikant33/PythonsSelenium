import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv('.env')

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def message():
    call = client.calls.create(
                            twiml='<Response><Say>Ahoy, World!</Say></Response>',
                            to= '+13528883629',
                            from_= '+18106424928'
                        )

    print(call.sid)