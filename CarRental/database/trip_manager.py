from CarRental.exception.exception import TripAlreadyExists, NoCabsAvailable, RecordNotFound
from CarRental.models.trip import Trip
from CarRental.strategy.cab_matching_strategy import CabMatchingStrategy
from CarRental.strategy.price_calculation_strategy import PriceCalculationStrategy


class TripManger:
    trips: dict[str, Trip]

    def __init__(self, cabs_manager, strategy: CabMatchingStrategy,price_strategy: PriceCalculationStrategy):
        self.cabs_manager = cabs_manager
        self.strategy = strategy
        self.price_strategy = price_strategy
        self.trips = {}

    def add_trip(self, trip):
        if trip.id in self.trips:
            raise TripAlreadyExists("Cab already exists")
        self.trips[trip.id] = trip

    def get_all_trips_by_rider(self,rider):
        return [trip for trip in self.trips.values() if trip.rider == rider]


    def book_cab(self, rider, from_location, to_location):
        available_cabs = self.cabs_manager.get_all_available_cabs()
        cab = self.strategy.find_cabs(available_cabs,from_location)
        if not cab:
            raise NoCabsAvailable("No cabs available")
        cab.update_availability_status(False)
        trip = Trip(id=f"trip_{len(self.trips) + 1}",
                    rider=rider,
                    cab=cab,
                    from_location=from_location,
                    to_location=to_location,
                    price=self.price_strategy.calculate_price(from_location,to_location))  # Dummy pricing logic
        self.add_trip(trip)
        return trip


    def get_trip(self, id):
        if self.trips.get(id):
            return self.trips[id]
        raise RecordNotFound("Record not found")
    def end_trip(self,id):
        trip = self.get_trip(id)
        trip.end_trip()

