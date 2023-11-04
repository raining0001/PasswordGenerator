import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*',]

print("Welcome to the PyPassword Generator!")
letters_number = int(input("How many letters would you like in your password? \n"))
symbol_number = int(input("How many symbols would you like ? \n"))
number_num = int(input("How many numbers would you like? \n"))


password = ""
for l in range(1,number_num + 1):
  password +=  random.choice(numbers)
for l in range(1,symbol_number + 1):
  password +=random.choice(symbols)
for l in range(1,letters_number+1):
  password += random.choice(letters)

password = ''.join(random.sample(password,len(password)))
print(password)
# print(f"Here is your password : {password}")

 