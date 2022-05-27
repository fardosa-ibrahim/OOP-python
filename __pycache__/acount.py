class Account:
    def __init__(self,name,password,cardnumber,serialnumber,deposit,former_balance,):
        self.name=name
        self.password=password
        self.cardnumber=cardnumber
        self.serialnumber=serialnumber
        self.deposit=deposit
        self.former_balance=former_balance

    def amount(self):
        self.deposit+=self.former_balance
        return f"Hello {self.name} you have  {self.deposit} deposited"

    def withdraw(self):
        self.former_balance-=self.amount
        return f"Hello {self.name} your have withdrawn {self.former_balance} "



    

        


    