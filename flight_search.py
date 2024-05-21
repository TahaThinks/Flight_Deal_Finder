from api_data import AMADEUS_KEY, AMADEUS_SECRET, AMADEUS_URL
import requests
class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def write_iataCode(self, flight_available):
        city = flight_available["city"]
        amadeus_endpoint = f"{AMADEUS_URL}/reference-data/locations"
        amadeus_params = {
            "subType": "CITY",
            "keyword": city,
        }
        amadeus_header = {
            "Authorization": f"Bearer {AMADEUS_SECRET}"
        }
        amadeus_response = requests.get(url=amadeus_endpoint, params=amadeus_params, headers=amadeus_header)
        print(amadeus_response.json())

        flight_available["iataCode"] = "TESTING"
        return flight_available
