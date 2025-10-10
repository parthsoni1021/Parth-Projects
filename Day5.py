# Loops

# fruits = ["apple", "banana", "mango", "orange", "grapes", "pineapple", "strawberry"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
    

numbers = [3, 7, 12, 5, 9, 20, 15, 8, 1, 14]
total = sum(numbers)
print(total)

added = 0
for i in numbers:
    added += i

print(added)

max = 0
for i in numbers:
    if i > max:
        max = i

print(max)


for number in range(1,10,2):   #10 not included
    print(number)

#This is a sample change

def project():
    import random

    print("This is a password generator")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 

    a = int(input("What is the letters of letters you want in your password? "))
    b = int(input("How many numbers you want in your password? "))
    c = int(input("How many symbols you want in your password? "))

    d = random.choices(letters, k=a)  #returns a list
    e = random.choices(numbers, k=b)
    f = random.choices(symbols, k=c)

    concat = d+e+f
    # shuffled = random.shuffle(concat)
    # print(type(shuffled))  #type none
    random.shuffle(concat)
    password = "".join(concat)

    print("Your password is", password)

if __name__ == "__main__":
    project()























