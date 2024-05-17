import datetime

from api_data import SHEETY_AUTH, SHEETY_URL
import requests
import datetime as dt

tomorrow = dt.datetime.now() + datetime.timedelta(days=1)
six_months = dt.datetime.now() + datetime.timedelta(weeks=6*4)
print(tomorrow.strftime("%Y-%m-%d"))
print(six_months.strftime("%Y-%m-%d"))

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = 0
        self.departure_airport_code = ""
        self.departure_city = ""


