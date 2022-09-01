import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "IFTwjei_wWGL4k2lTIcsv1ZcW7DxvJc6"

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search_flight(self):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": "LON",
            "fly_to": "",
            "date_from": "",
            "date_to": "",
            "return_from": "",
            "return_to": "",
        }