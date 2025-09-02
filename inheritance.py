class Gadget:
    def __init__(self , brand, price, color ,orgin ):
        self.brand=brand
        self.price=price
        self.color=color
        self.orgin=orgin
    
    def run(self):
        return f"Running Device is {self.brand}"

class Laptop:
    def __init__(self  , memory ,ssd):
        self.memory=memory
        self.ssd=ssd
    
    def coding(self):
        return f"learning pythond ans solve problem"
         

class Phone(Gadget):
    def __init__(self  ,brand, price, color ,orgin, is_dual):
        self.is_dual=is_dual
        super().__init__(brand, price, color ,orgin)

    def call(self, number , text):
        return f"send message on {number} , text {text}"
    
    def __repr__(self):
        return f"phone name: {self.brand} , color: {self.color} , it's come from {self.orgin},price: {self.price} , is it dual :{self.is_dual}"
    
class Camera:
    def __init__(self, pixel):
        self.pixel=pixel

    def changeLens(self):
        pass


#inheritance
myPhone =Phone("iphone",12000,"black","china",True)
print(myPhone)
