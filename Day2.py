"""
print(len(str(123456)))  #Typecasting
print('Hello'[0])   #Subscripting
print(123+345)
print(148_256_843)  #large number
print(type(123))

print(6/3)  #implicitly typecasted to float
print(6//3)  #int - Quotient

name = "Parth"
Age = 21
print(int(52.81))

print(f"Your name is {name}, age is {Age}")
"""


print("Welcome to the tip calculator")
a = float(input("What was your total bill? $"))
b = int(input("What percentage of the amount you want to give tip? "))
c = int(input("How many people will have the split divided into? "))
d = (a/c)*(1+b/100)
e = round(d,2)
print(f"Amount per person: ${e}")
