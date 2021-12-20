class machine: 
    def __init__(self,name,amount):
            self.name = name
            self.amount = amount
            self.price = 0
            self.total = 0
    
    def __Pricelist(self): 
        if self.name.lower() == "chocolate":
            self.price = 100
        elif self.name.lower() == "chips":
            self.price = 50
        elif self.name.lower() == "soda":
            self.price = 125
        elif self.name.lower() == "juice":
            self.price = 75
        else:
            self.price = 0
    
    def total_price(self):
        self.__Pricelist() 
        self.total=self.price*self.amount/100
        return self.total 

    def total_change(self):
        self.__Pricelist()
        self.total = self.price*self.amount
        return self.total

    def __str__(self):
        self.__Pricelist()
        return f"Name: {self.name}\n Amount: {self.amount}\n Price: {self.price}\n Total: {self.total}"

    def get_price(self):
        self.__Pricelist()
        return self.price