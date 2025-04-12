from parkinglot.models.car import Car
from parkinglot.models.parkingslot import ParkingLot
from parkinglot.strategy.natural_order_strategy import NaturalOrderStrategy
from parkinglot.strategy.parking_strategy import ParkingStrategy


class ParkingLotService:
    parking_lot = None
    def create_parking_lot(self,capacity,strategy:ParkingStrategy):
        self.parking_lot = ParkingLot(capacity,strategy)

    def park_car(self,car):
        self.parking_lot.park(car)

    def leave(self,slot_num):
        self.parking_lot.leave(slot_num)

    def status(self):
        return self.parking_lot.getStatus()

    def get_slot_by_reg(self, reg_number):
        return self.parking_lot.get_slot_by_reg(reg_number)

    def get_slots_by_color(self, color):
        return self.parking_lot.get_slots_by_color(color)

    def get_regs_by_color(self, color):
        return self.parking_lot.get_regs_by_color(color)



if __name__  == "__main__":
    service = ParkingLotService()
    service.create_parking_lot(6,NaturalOrderStrategy())

    service.park_car(Car("KA-01-HH-1234","White"))
    service.park_car(Car("KA-01-HH-9999", "White"))
    service.park_car(Car("KA-01-BB-0001", "Black"))
    service.park_car(Car("KA-01-HH-7777", "Red"))
    service.park_car(Car("KA-01-HH-2701", "Blue"))
    service.park_car(Car("KA-01-HH-3141", "Black"))

    service.leave(3)

    print(service.status())
    service.park_car(Car("KA-01-P-333", "White"))
    service.park_car(Car("DL-12-AA-9999", "White"))

    print(service.status())

    print(service.get_slots_by_color("White"))

    print(service.get_slot_by_reg("KA-01-HH-3141"))






