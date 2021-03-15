from InsufficientFundsException import InsufficientFundsException
    
class Accounts:
    def __init__(self, name, balance = 0):
        self.name = name.title()
        self.balance = float(balance)
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException (f"You do not have sufficient funds to make this withdrawal. The maximum you can withdraw is {self.balance}")
        else:
            self.balance -= amount
            return self.balance

    def getbalance(self):
        return self.balance



#     # def __str__(self): ???
#     #     return 'account {} current balance is £{}'.format(self.name, self._balance)

        



