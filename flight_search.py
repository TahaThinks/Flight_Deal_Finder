class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def write_iataCode(self, flight_available):
        flight_available["iataCode"] = "TESTING"
        return flight_available
