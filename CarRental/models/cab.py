from CarRental.models.location import Location


class Cab:
    id: str
    driverName : str
    available : bool
    location :  Location

    def __init__(self,id,driver_name,available = True,location =None):
        self.id = id
        self.driverName = driver_name
        self.available = available
        self.location=location
        self.available = True

    def updateLocation(self,location : Location):
        self.location = location

    def update_availability_status(self,available):
        self.available = available

    def is_available(self):
        return self.available
