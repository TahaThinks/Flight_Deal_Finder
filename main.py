#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_data import FlightData

flight_details = FlightData()
sheet_data = flight_details.read_data()
print(sheet_data['prices'])

flights_details = sheet_data['prices']

for flight_details in flights_details:
    if flight_details["iataCode"] == "":
        print(f"No Code, adding one now for {flight_details["city"]}")

# is_iataCode = sheet_data['prices']