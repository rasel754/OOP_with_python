# bus company 
class Company:
    def __init__(self, name, address):
        self.name=name
        self.bus=[]
        self.counter=[]
        self.drivers=[]
        self.routes=[]
        self.counter=[]
        self.supervisor=[] 
        self.fare=[]


class Driver:
    def __init__(self, name , age, license):
        self.license=license
        self.name=name
        self.age=age

class Counter :
    def __init__(self):
        pass
    def purchase_a_ticket(self , start, destination):
        pass


class Passenger:
    pass

class Supervisor:
    pass