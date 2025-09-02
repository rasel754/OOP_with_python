class vehicle:
    def __init__(self,name, price):
        self.name=name
        self.price=price

    def move(self):
        pass

class Bus(vehicle):
    def __init__(self, name, price,seat):
        self.seat=seat
        super().__init__(name, price)

class Truck(vehicle):
    def __init__(self, name, price,weight):
        self.weight=weight
        super().__init__(name, price)
# etai multi level inheritance
class PickUpTruck(Truck):
    def __init__(self, name, price, weight , shortDestination):
        self.shortDes=shortDestination
        super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat ,tempture):
        self.tempture=tempture
        super().__init__(name, price, seat)