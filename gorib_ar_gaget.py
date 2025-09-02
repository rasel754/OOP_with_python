class Laptop:
    def __init__(self , brand, price, color , memory):
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory
    
    def run(self):
        return f"Running Laptop {self.brand}"
    
    def coding(self):
        return f"learning pythond ans solve problem"
         

class Phone:
    def __init__(self , brand, price, color , is_dual):
        self.brand=brand
        self.price=price
        self.color=color
        self.is_dual=is_dual


    def run(self):
        return f"kom kore tip"

    def call(self, number , text):
        return f"send message on {number} , text {text}"
    
class Camera:
    def __init__(self , brand, price, color , pixel):
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel

    def picTul(self):
        pass
    def changeLens(self):
        pass
