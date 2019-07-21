#balance = 100

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
    else:
        print('not enough money')
        
#print(balance)
#withdraw(25)


def new_withdraw(balance = 100):
    
    def draw(balance, amount):
        if balance >= amount:
            balance -= amount
            return balance
        else:
            return 'not enough money'
            
    return lambda amount: draw(balance, amount)

class AccountBalance:
    
    def __init__(self, amount):
        self.balance = amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('not enough money')
            
    def deposit(self, amount):
        self.balance += amount
        
    def __str__(self):
        return str(self.balance)
        
def make_account(amount):
    return AccountBalance(amount)

John = make_account(100)
print(John)
John.withdraw(25)
print(John)
John.withdraw(25)
print(John)