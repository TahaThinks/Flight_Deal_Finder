from api_data import SHEETY_AUTH, SHEETY_URL
import requests

data = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
                   {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
                   {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
                   {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
                   {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
                   {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
                   {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
                   {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
                   {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.auth = SHEETY_AUTH
        self.url = SHEETY_URL

    def download_data(self):
        # response = requests.get(url=self.url, headers=self.auth)
        # return response.json()
        return data

    def upload_data(self, flight_detail):
        put_endpoint = f"{self.url}/{flight_detail["id"]}"
        print(put_endpoint)