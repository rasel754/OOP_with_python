class Bank:
    def __init__(self , holderName, deposite):
        self.holderName=holderName #public
        self._branchName="chandpur 21" #protected
        self.__deposite =deposite #pirvate

    def deposit(self,ammount):
        self.__deposite+=ammount
    
    def getBlance(self):
        return self.__deposite
    

rasel=Bank("rasel bro" , 4000)
print(rasel.holderName)
rasel.holderName="shoel bor"
rasel.deposit(2000)
print(rasel.getBlance())
print(rasel.holderName)

# print(dir(rasel))#access private keyword
print(rasel._Bank__deposite)
