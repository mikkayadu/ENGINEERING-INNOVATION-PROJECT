import os
from twilio.rest import Client
import requests

api_key = "2d159eeae300c091fd195a2dfe26f975"

account_sid = "AC2f8c041aa9c97da2767c111b3e113675"
auth_token = "44a33606129ddde751e8791d3ea58f9b"

weather_params = {"lat": -5.087930,
                  "lon": -42.800980,
                  "appid": api_key,
                  "exclude": "current,minutely,daily"
                  }

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_params)

response.raise_for_status()

weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(
        to="+233558278035",
        from_="+17273356641",
        body="It's going to rain today. Remember to take your umbrella.☂️")
    print(message.status)
# print(data)

