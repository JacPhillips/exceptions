from bankbaseclass import Accounts
from InsufficientFundsException import InsufficientFundsException

john = Accounts("john", 1000)
print(john.name,john.balance)

try:
    john.withdraw(100)
except InsufficientFundsException as err:
    print(err)
else: 
    print(f"Your new balance is", john.balance)