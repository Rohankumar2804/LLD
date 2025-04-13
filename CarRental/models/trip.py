from CarRental.models.cab import Cab
from CarRental.models.location import Location
from CarRental.models.rider import Rider
from CarRental.models.tripstatus import TripStatus


class Trip:
    id : str
    from_location: Location
    to_location: Location
    rider: Rider
    cab: Cab
    status : TripStatus
    price : float

    def __init__(self,id,from_location,to_location,rider,cab,price):
        self.id = id
        self.rider = rider
        self.cab = cab
        self.from_location = from_location
        self.to_location = to_location
        self.price = price
        self.status = TripStatus.IN_PROGRESS


    def end_trip(self):
        self.status = TripStatus.COMPLETED
        self.cab.update_availability_status(True)