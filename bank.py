# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.




class Account:
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0
        self.deposits=[]
        self.withdrawals=[]
    def deposit (self, amount):

       self.balance= amount

       return f"you have deposited this amount{amount} and this is your balance {self.balance}"

    def deposit (self, amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            self.deposits.append(amount)
            print(self.deposits)
            return f"You have deposited {amount}. Your new balance is {self.balance}"

 

    def withdraw (self, amount):
        self.transaction=100
        if amount>self.balance:
            return f"Your balance is {self.balance}. You cannot withdraw the {amount}"
        elif amount<0:
            return f"Withdrawal must be positive"

        else:
            self.balance-=amount+self.transaction
            self.withdrawals.append(amount)
            return f"You have withdrawn {amount}. Your balance is {self.balance}", self.withdrawals

    def deposits_statements(self):
        for c in self.deposits:
            print(c,end="/n")

 

    def withdrawals_statements(self):
        for a in self.withdrawals:
            print(a,end="/n")

    def current_balance(self):
        return f"{self.balance}"




    


    

           