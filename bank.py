

class Account:
    def __init__(self,account_name,account_number):
     self.account_name=account_name
     self.account_number=account_number
     self.balance=0
     self.deposits=[]
     self.withdrawals=[]
    def deposit(self,ammount):
        if ammount<=0:
            return f"Deposit must be positive ammount"
        else:
            self.balance+=ammount
            self.deposits.append(ammount)
            return self.balance


    def withdrawal(self,amount):
        self.tansaction=100
        
        if amount<=0:
            return f"Ammount should be  positive number"
        elif amount>self.balance:
             return f"Your ammount is greater than your balance"
        else:
            self.balance-=amount+self.tansaction
            self.withdrawals.append(amount)
            return f"{self.account_name} you have withdrawn {amount}. Your new balance is {self.balance}"

    def deposits_statement(self):
        for x in self.deposits:
            print(x ,end="\n")

    def withdrawals_statement(self):
        for y in self.withdrawals:
            print(y, end="\n")

    def balance(self):
        return self.balance


  

 




