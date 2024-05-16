#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_data import FlightData

flight_details = FlightData()
sheet_data = flight_details.read_data()
print(sheet_data['prices'])

flights_available = sheet_data['prices']

for flight_available in flights_available:
    if not flight_available["iataCode"]:
        print(f"No Code for {flight_available["city"]}, Adding..")
        flight_details.write_data(flight_available)
