from abc import ABC, abstractmethod

class ParkingStrategy(ABC):

    @abstractmethod
    def add_slots(self,slots):
        pass

    @abstractmethod
    def get_next_available_slot(self):
        pass

    @abstractmethod
    def add_slot(self,slot):
        pass