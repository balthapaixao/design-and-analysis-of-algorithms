class Flight:
    def __init__(self, name, id, origin, destination):
        self.name = name
        self.id = id
        self.origin = origin
        self.destination = destination

    def __str__(self):
        return self.name


class FlightController:
    def __init__(self):
        self.queue = []

    def list_waiting_flights(self):
        print("Waiting flights:")
        for flight in self.queue:
            print(flight)

    def list_waiting_flights_details(self):
        print("Waiting flights details:")
        for flight in self.queue:
            print(
                f"Flight: {flight.name}, ID: {flight.id}, Origin: {flight.origin}, Destination: {flight.destination}"
            )

    def add_flight(self, flight):
        self.queue.append(flight)

    def authorize_takeoff(self):
        if len(self.queue) > 0:
            flight = self.queue.pop(0)
            print(f"Flight {flight.name} authorized to takeoff")
        else:
            print("No flight waiting for takeoff")

    def list_first_flight(self):
        if len(self.queue) > 0:
            print(f"First flight: {self.queue[0]}")
        else:
            print("No flight waiting for takeoff")

    def list_waiting_flights_size(self):
        print(f"Waiting flights size: {len(self.queue)}")


def test_flight_controller() -> None:
    flight_controller = FlightController()
    flight_controller.list_waiting_flights_size()
    flight_controller.list_waiting_flights()
    flight_controller.list_first_flight()
    flight_controller.authorize_takeoff()

    flight_one = Flight("LATAM 7246", 1, "Rio de Janeiro", "São Paulo")
    flight_two = Flight("GOL 1234", 2, "São Paulo", "Rio de Janeiro")
    flight_three = Flight("AZUL 5678", 3, "São Paulo", "Rio de Janeiro")
    flight_controller.add_flight(flight_one)
    flight_controller.add_flight(flight_two)
    flight_controller.add_flight(flight_three)

    flight_controller.list_waiting_flights_size()
    flight_controller.list_waiting_flights()
    flight_controller.list_first_flight()
    flight_controller.authorize_takeoff()

    flight_controller.list_waiting_flights_size()
    flight_controller.list_waiting_flights()
    flight_controller.list_first_flight()
    flight_controller.authorize_takeoff()

    flight_controller.list_waiting_flights_size()
    flight_controller.list_waiting_flights()
    flight_controller.list_first_flight()
    flight_controller.authorize_takeoff()

    flight_controller.list_waiting_flights_size()
    flight_controller.list_waiting_flights()


if __name__ == "__main__":
    test_flight_controller()
