class Shopping:
    cart=[] #class attribute or static attribute
    orgin="bd"

    def __init__(self , name, location):
        self.name=" jamu na city" # instance attribute
        self.location=location

    def purchase(self , item , price, amount):
        remaining=amount-price
        print(f"buying {item} for {price} taka and i have know {remaining} taka")

    @staticmethod
    def multi(a,b):
        print(a*b)

    @classmethod
    def hudai_dekhi(self,item):
        print("hudai dekhi eta ",item)

# bashundara=Shopping("mall","not a popular ")
# bashundara.purchase("lungi" , 100,300)
# print(bashundara)


# Shopping.purchase("lungi",23 ,234   )

Shopping.hudai_dekhi("shart")
Shopping.multi(4,8)