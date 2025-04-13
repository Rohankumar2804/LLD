from math import sqrt


class Location:
    x : float
    y : float

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_location(self):
        return self.x,self.y

    def get_distance(self,location):
        return sqrt((location.x-self.x)*(location.x-self.x) + (location.y-self.y)*(location.y-self.y))



if __name__ == "__main__":
    p1 = Location(float(4.9),float(2))
    p2 = Location(float(10.9),float(20))

    print(p1.get_distance(p2))
    print(p1.get_location())