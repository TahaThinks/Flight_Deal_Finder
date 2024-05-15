from api_data import SHEETY_AUTH, SHEETY_URL
import requests
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.auth = SHEETY_AUTH
        self.url = SHEETY_URL

    def getdata(self):
        response = requests.get(url=self.url, headers=self.auth)
        print(response.json())

