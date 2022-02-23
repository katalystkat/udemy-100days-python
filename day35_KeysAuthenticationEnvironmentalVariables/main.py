import requests
from twilio.rest import Client

account_sid = ------
auth_token = -----
phone_number = "+18607757217"

api_key = ------
latitude = 24.163490
longitude = 120.646744
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters={
    "lat": latitude,
    "lon": longitude,
     "appid": api_key,
    "exclude": "current,minutely,daily",
    "units": "imperial",
}
data = requests.get(OMW_Endpoint, params=parameters)
data.raise_for_status()
data_json = data.json()
hourly = data_json["hourly"]
will_rain = False
for hour in range(0,12):
    weather = hourly[hour]["weather"]
    if int(weather[0]["id"])<700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's apparently umbrella weather today, bring your silly umbrella",
        from_='+#######,
        to='+########'
    )



