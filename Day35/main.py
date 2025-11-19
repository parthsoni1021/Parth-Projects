# API Authentication

# endpoints and parameters 

import requests, truststore
from twilio.rest import Client
from dotenv import load_dotenv
import os           # using export keyword to export the keys values 

truststore.inject_into_ssl()

# OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = '599a4012f5e0b25509dfd91f4d33161a'
load_dotenv()
# print(os.environ)

ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")

# print(ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER)

weather_params = {
    'lat': 57.6263877,
    'lon': 39.8933705 ,
    'appid': api_key,
    'cnt' : 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)

print(response.status_code)
# response.raise_for_status()  

weather_data = response.json()

# print(weather_data)

print(weather_data['list'])

weather_list = []
for i in weather_data['list']:   # i is a dict
    weather = i['weather']       #weather is a list which can contain multiple dict. We go through the dictionary and check id
    
    for j in range(0,len(weather)):
        check = weather[j]['id']    # type dict

        weather_list.append(check)
# print(weather_list)

def send_message():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body='It might rain Today. Take an Umbrella ☂️',
        from_= TWILIO_NUMBER,
        to = '+919116535915',    # The number used to make account.
    )

    print(message.status)

def send_whatsapp():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    wp_message = client.messages.create(
        body='It might rain Today. Take an Umbrella ☂️',
        from_='whatsapp:+14155238886',
        to='whatsapp:+919116535915'
        )
    print(wp_message.sid)

# www.ventusky.com
will_rain = None
for i in weather_list:
    if i < 700:
        will_rain = True

if will_rain:
    # print('Bring an Umbrella')
    # send_message()
    send_whatsapp()

## apilist.fun - for more fun projects
