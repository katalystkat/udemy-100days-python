import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "A87YOXJgKncswStzrxxtaYOMvAFoHeeC"
endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

class FlightSearch:

    def get_destination_code(self, city_name):
        query = {
            "term" : city_name,
            "location_types": "city",
        }
        headers = {"apikey": TEQUILA_API_KEY}
        data = requests.get(url=endpoint,headers = headers, params = query)
        data_json = data.json()
        data = data_json['locations']
        return data[0]['code']

    def check_flights(self,origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey":TEQUILA_API_KEY
        }
        query ={
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        try:
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers = headers, params = query,)
            response_json = response.json()
            data = response_json['data'][0]
            price = data['price']
            print(price)
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None
        flight_data = FlightData(
            price = data["price"],
            origin_city = data["cityFrom"],
            origin_airport = data["flyFrom"],
            destination_city = data["cityTo"],
            destination_airport = data["flyTo"],
            out_date = data["route"][0]["local_departure"].split("T")[0],
            return_date = data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city} has cheapest prices at {flight_data.price} available on {flight_data.out_date}")
        return flight_data
