
from datetime import datetime
from time import strftime

from yaml import load
class Account:
    def __init__(self,account_name,account_number):
     self.account_name=account_name
     self.account_number=account_number
     self.balance=0
     self.deposits=[]
     self.withdrawals=[]
     self.transaction={}
    def deposit(self,ammount):
        time=strftime("%c")
        naration="You have deposited"
        self.transaction={naration,ammount,time,}
        if ammount<=0:
            return f"Deposit must be positive ammount"
        else:
            self.balance+=ammount
            self.deposits.append(ammount)
            return f"{self.transaction} your balance is {self.balance}"


    def withdrawal(self,ammount):
        self.transaction=100
        if ammount<=0:
            return f"Ammount should be  positive number"
        elif ammount>self.balance:
             return f"Your ammount is greater than your balance"
        elif ammount+self.transaction>self.balance:
            return f"you have less money in your account"
        else:
            time=strftime("%c")
            naration="you have withdrawn"
            transactions={naration,ammount,time}
            self.balance-=ammount+self.transaction
            self.withdrawals.append(ammount)
            return f"{transactions} and your balance is {self.balance}"

    def deposits_statement(self):
        for x in self.deposits:
            print(len(x))

    def withdrawals_statement(self):
        for y in self.withdrawals:
            print(len(y))

    def balance(self):
        return self.balance

    def full_statement(self):
        self.loan_balance=0
        now=datetime.now()
        for y,z in zip(len(self.deposits,self.withdrawals)):
            return(f"{now},{y},{z}")

    def transfer(self,receiver,amount):
        self.receiver=receiver
        self.amount=amount
        current_balance=self.balance-amount
        if amount<=0:
            print( f"You don't have enough balane")
        elif amount>self.balance:
            print(f"Your cannot transfer {amount}.You balance is currently {self.balance}")
        elif amount<self.balance:
            print(f"You have transfered {amount} to {self.receiver} your balane is currently {current_balance}")
    def  loan(self,loan):
        self.loan=loan
        self.interest=0.03*self.loan
        self.total_loan=self.loan+self.interest
        if len(self.deposits)>10 and loan<=sum(self.deposits)//3 and loan>100 and self.balance<0:
            print(f"You got a loan of {loan} and your balance is {self.amount}")
        else:
            print("loan is not eligable")
    def paymentloan(self,loanPaid):
        self.loanPaid=loanPaid
        self.interest=0.03*self.loan
        total_topay=loanPaid+self.interest
        loan_remaining=self.loan-loanPaid
        new_balance=self.loan_amount-total_topay
        if total_topay>0:
            print(f"You have deposited {loanPaid} a loan of {self.loan}Ksh.Your new loan balance is {new_balance}Ksh")
        elif total_topay>loan_remaining:
            print(f"Congratulations!! You have cleared your loan of {self.amount}.Your new balance is{new_balance}")
        else:
            print(f"You have a loan balance of {self.total_loan}")
    def current_balance(self):
        print(f"Your current balance {self.balance}Ksh" )











   

    

  

 




