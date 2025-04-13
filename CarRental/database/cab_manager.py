from CarRental.exception.exception import CabAlreadyExists, RecordNotFound
from CarRental.models.cab import Cab


class CabManager:
    cabs: dict[str, Cab]

    def __init__(self):
        self.cabs = {}

    def add_cab(self, cab):
        if cab.id in self.cabs:
            raise CabAlreadyExists("Cab already exists")
        self.cabs[cab.id] = cab

    def get_all_available_cabs(self):
        return [cab for cab in self.cabs.values() if cab.is_available()]

    def get_cab(self,id):
        if self.cabs.get(id):
            return self.cabs[id]
        raise RecordNotFound("Record not found")

    def update_cab_location(self,id,location):
        cab = self.get_cab(id)
        cab.updateLocation(location)

    def update_availability_status(self,id,status):
        cab = self.get_cab(id)
        cab.update_availability_status(status)