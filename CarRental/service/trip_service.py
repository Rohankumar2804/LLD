from CarRental.database.cab_manager import CabManager
from CarRental.database.rider_manager import RiderManager
from CarRental.database.trip_manager import TripManger
from CarRental.strategy.default_cab_matching_strategy import DefaultMatchingCab
from CarRental.strategy.default_price_calculation_strategy import DefaultPriceCalculationStrategy


class TripService:
    def __init__(self):
        self.cabs_manager = CabManager()
        self.trip_manager = TripManger(self.cabs_manager,DefaultMatchingCab(),DefaultPriceCalculationStrategy())
        self.rider_manager = RiderManager()

    def register_rider(self,rider):
        self.rider_manager.add_rider(rider)

    def register_cab(self,cab):
        self.cabs_manager.add_cab(cab)

    def book_cab(self, rider, from_location, to_location):
        return self.trip_manager.book_cab(rider,from_location,to_location)

    def end_trip(self,id):
        self.trip_manager.end_trip(id)

    def update_cab_location(self,cab,location):
        self.cabs_manager.update_cab_location(cab.id,location)

    def get_all_trip_by_rider(self,rider):
       return self.trip_manager.get_all_trips_by_rider(rider)