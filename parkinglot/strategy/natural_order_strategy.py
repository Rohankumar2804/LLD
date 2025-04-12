import heapq

from parkinglot.models.car import Car
from parkinglot.models.slot import Slot
from parkinglot.strategy.parking_strategy import ParkingStrategy


class NaturalOrderStrategy(ParkingStrategy):

    def __init__(self):
        self.slots = []

    def add_slots(self,slots):
        for slot in slots:
            heapq.heappush(self.slots,(slot.get_number(),slot))

    def get_next_available_slot(self):
        while len(self.slots) > 0:
            _,slot = heapq.heappop(self.slots)
            if slot.is_free():
                return slot
        return None

    def add_slot(self,slot):
        heapq.heappush(self.slots,(slot.get_number(),slot))


if __name__ == '__main__':
    strategy = NaturalOrderStrategy()
    slots = [Slot(1),Slot(2),Slot(5),Slot(4)]
    strategy.add_slots(slots)

    free_slot : Slot = strategy.get_next_available_slot()
    print(free_slot.get_number())

    car = Car(1,"123")
    free_slot.park_car(car)

    free_slot: Slot = strategy.get_next_available_slot()
    print(free_slot.get_number())
    free_slot.park_car(car)
    free_slot.leave()
    strategy.add_slot(slots[1])

    free_slot: Slot = strategy.get_next_available_slot()
    print(free_slot.get_number())
    free_slot.park_car(car)
    free_slot: Slot = strategy.get_next_available_slot()
    print(free_slot.get_number())





