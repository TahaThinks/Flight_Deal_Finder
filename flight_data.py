from api_data import SHEETY_AUTH, SHEETY_URL
import requests
data = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.auth = SHEETY_AUTH
        self.url = SHEETY_URL

    def read_data(self):
        # response = requests.get(url=self.url, headers=self.auth)
        # return response.json()
        return data

    def write_data(self, flight_available):
        flight_available["iataCode"] = "TESTING"
