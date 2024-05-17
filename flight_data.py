from api_data import SHEETY_AUTH, SHEETY_URL
import requests
import datetime as dt


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = 0
        self.departure_airport_code = ""
        self.departure_city = ""


