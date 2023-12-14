import random
from data import letters , numbers , symbols
class Main:
    def __init__(self,letters_num,symbol_num,number_num):
        self.letters_num = letters_num
        self.symbol_num = symbol_num
        self.number_num = number_num
        self.password = ""
        
    def user_input(self):
        print("Welcome to the PyPassword Generator!")
        self.letters_num = int(input("How many letters would you like in your password? \n"))
        self.symbol_num = int(input("How many symbols would you like ? \n"))
        self.number_num = int(input("How many numbers would you like? \n"))
        

    def create(self):
        for i in range (1,self.letters_num +1):
            self.password += random.choice(letters)
        for i in range(1,self.symbol_num + 1):
            self.password += random.choice(symbols)
        for i in range (1,self.number_num +1):
            self.password += random.choice(numbers)

        self.password = ''.join(random.sample(self.password,len(self.password)))
        print(self.password)

        
        



