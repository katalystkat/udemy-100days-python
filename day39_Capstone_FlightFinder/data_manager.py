import requests
sheety_endpoint = "https://api.sheety.co/eddca771378f3e3e1c27faca1f8e2c85/flightDeals/flightDeals"
BEARER = "Bearer ASEDFSDGTHSRDVDFGDRS"
headers = {"Authorization": BEARER}

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        results = requests.get(sheety_endpoint, headers=headers)
        data = results.json()
        print(data)
        #length = len(data["flightDeals"])
        #for n in range(0, length):
        # self.destination_data = data['flightDeals']
        # return self.destination_data

    def update_destination_codes(self):
       for city in self.destination_data:
            new_data = {
                "flightDeal": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json= new_data
            )
            print(response.text)

