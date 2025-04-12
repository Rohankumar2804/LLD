from .car import Car

class Slot:
    number : int
    parkedCar : Car | None

    def __init__(self,number):
        self.number = number
        self.parkedCar = None

    def park_car(self,car):
        self.parkedCar = car

    def leave(self):
        self.parkedCar = None

    def get_number(self):
        return self.number

    def get_parked_car(self):
        return self.parkedCar

    def is_free(self):
        return self.parkedCar == None



if __name__ == '__main__':
    car = Car("white","123")
    print(car.get_color())
    print(car.get_registration_number())

    slot = Slot(1)
    print(slot.__dict__)

    slot.park_car(car)
    print(slot.get_parked_car())
    print(slot.__dict__)

    slot.leave()
    print(slot.__dict__)

