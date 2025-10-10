# Loops
import os
os.system("cls")


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

















