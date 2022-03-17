#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests
sheety_endpoint = "https://api.sheety.co/eddca771378f3e3e1c27faca1f8e2c85/flightDeals/flightDeals"
BEARER = "bearer ASEDFSDGTHSRDVDFGDRS"
headers = {"Authorization": BEARER}

results = requests.get(sheety_endpoint, headers = headers)
results_json = results.json()

#sheet_data = [lowestPrice for (lowestPrice, data) in results_json["flightDeals"]]
#pprint(sheet_data)
pprint(results.json())
