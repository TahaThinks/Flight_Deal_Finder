#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager

flight_details = DataManager()

sheet_data = flight_details.read_data()
print(sheet_data['prices'])
flights_available = sheet_data['prices']

flight_details_update = FlightSearch()
for flight_available in flights_available:
    if not flight_available["iataCode"]:
        flight_details_update.write_data(flight_available)
        flight_details.write_data()

print(flights_available)

