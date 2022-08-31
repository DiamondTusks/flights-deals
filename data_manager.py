import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/225f0ec4563dbb435c97abff230d4e64/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    # Use the Sheety API to GET all the data in that sheet and print it out.
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # Importing pretty print and printing the data out to see it formatted.
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)