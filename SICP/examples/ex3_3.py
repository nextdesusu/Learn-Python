class Account:
    mistake_counter = 0
    
    def __init__(self, money, password):
        self.money = money
        self.password = password
        
    def call_cops(self):
        print("Cops called")
        
    def withdraw(self, draw, inputed_password):
        if self.mistake_counter > 5:
            self.call_cops()
        elif inputed_password == self.password:
            self.mistake_counter = 0
            if self.money >= draw:
                self.money -= draw
                print("now your account have " + str(self.money))
            else:
                print('You tried to draw more money than account have')
        else:
            print("wrong password")
            self.mistake_counter += 1
            print("you fail " + str(self.mistake_counter) + " times")
            
    def __str__(self):
        return "Account have " + str(self.money) + " coins"
            
A = Account(100, 'pass')
print(A)
A.withdraw(50, '34')
A.withdraw(50, '34')
A.withdraw(50, '34')
A.withdraw(50, '34')
A.withdraw(50, '34')
A.withdraw(125, 'pass')
A.withdraw(50, '34')

def make_account(money, password):
    
    def turn(key):
        if key == "draw":
            return dispatch
        if key == "look":
            return money
    
    def dispatch(draw, input_password):
        if password == input_password:
            if money >= draw:
                return make_account(money - draw, password)
            return "not enough money"
        else:
            return "wrong pass"
        
    return turn


A = make_account(100, "pass")
A = A("draw")(25, "pass")
print(A("look"))