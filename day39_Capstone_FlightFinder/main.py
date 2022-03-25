#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)
if sheet_data[0]["iataCode"] == "":
       from flight_search import FlightSearch
       flight_search = FlightSearch()
       print("hello")
       print(sheet_data)
       print(len(sheet_data))
       for n in range(0,len(sheet_data)):              # sheet_data[n]['iataCode'] = flight_search.get_destination_code(sheet_data[n]['city'])
              print(flight_search.get_destination_code(sheet_data[n]['city']))
              sheet_data[n]["iataCode"] = flight_search.get_destination_code(sheet_data[n]["city"])
       data_manager.destination_data = sheet_data
       data_manager.update_destination_codes()

flight_search = FlightSearch()
x = datetime.now()
y = timedelta(days = 60)
z = datetime.now() + timedelta(days=180)
for n in range(0, len(sheet_data)):
       flight_search.check_flights(origin_city_code = "LAX", destination_city_code = sheet_data[n]["iataCode"], from_time=x, to_time=z)
#def check_flights(self, origin_city_code, destination_city_code, from_time, to_time): dd/mm/YYYY, e.g. 29/05/2021
