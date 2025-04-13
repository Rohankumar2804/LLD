from CarRental.exception.exception import RiderAlreadyExists, RecordNotFound
from CarRental.models.rider import Rider


class RiderManager:
    riders: dict[str, Rider]

    def __init__(self):
        self.riders = {}

    def add_rider(self, rider):
        if rider.id in self.riders:
            raise RiderAlreadyExists("rider already exists")
        self.riders[rider.id] = rider

    def get_rider(self, id):
        if self.riders.get(id):
            return self.riders[id]
        raise RecordNotFound("Record not found")
