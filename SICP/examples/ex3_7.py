class Account:
    
    mistake_counter = 0
    
    def __init__(self, money, password):
        self.money = money
        self.password = password
        
    def call_cops(self):
        print("Cops called")
        
    def check_pass(self, input_pass):
        return self.password == input_pass
        
    def withdraw(self, draw, inputed_password):
        if self.mistake_counter > 5:
            self.call_cops()
        elif self.check_pass(inputed_password):
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
    
class JointAccount(Account):
    
    def __init__(self, acc_obj, acc_pass, new_pass):
        self.acc_obj = acc_obj
        self.acc_pass = acc_pass
        self.password = new_pass
        
    def withdraw(self, amount, input_password):
        if self.mistake_counter > 5:
            self.call_cops()        
        if self.check_pass(input_password):
            self.acc_obj.withdraw(amount, self.acc_pass)
        else:
            self.mistake_counter += 1
            
    def __str__(self):
        return "Joint Account have " + str(self.acc_obj.money) + " coins"
    
def make_joint(acc_obj, acc_pass, new_pass):
    if acc_obj.check_pass(acc_pass):
        return JointAccount(acc_obj, acc_pass, new_pass)
    else:
        print("Wrong password")
        return acc_obj
    
Vasya = Account(100, "123")
Vasya.withdraw(25, "123")
Petya = make_joint(Vasya, "123", "321")
Petya.withdraw(30, "321")
Vasya.withdraw(25, "123")
Petya.withdraw(30, "321")
print(Vasya)
print(Petya)
