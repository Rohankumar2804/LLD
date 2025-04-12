
class Car:
    registrationNumber: str
    colour: str

    def __init__(self,registration_number,color):
        self.registrationNumber = registration_number
        self.colour = color

    def get_color(self):
        return self.colour

    def get_registration_number(self):
        return self.registrationNumber






if __name__ == '__main__':
    car = Car("white","123")
    print(car.get_color())
    print(car.get_registration_number())