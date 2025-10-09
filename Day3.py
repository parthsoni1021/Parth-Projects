"""print("Criteria to ride")
a = float(input("Enter your height (in cm) "))

if a >= 120:
    print("You can ride")
    b = int(input("Enter your age "))
    if b <= 7:
        d = 7
    elif b in (7,18):
        d = 9
    else:
        d = 10
    print("Ride amount is $",d)
    c = input("are you going to take pictures, write 1 for Yes and 0 for No ")
    if c == 1:
        print("Your total bill is, $",d+3)
    else:
        print(f"Your total bill is {d}")
else:
    print("Can't ride")
"""

"""
#Python Pizza delivers
print("Welcome to python pizza delivery")
size = input("What is the size of the pizza you want? S, M or L "))
pepperoni = input("Do you want pepperoni in the pizza? Y or N ")
cheese = input("Do you want extra cheese in the pizza? Y or N ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if cheese == "Y":
    bill += 1

print("Your final bil is $", bill)

"""

"""
print(not 5)
print(not 0)
print(not 1)
a = 5
b = 7
print(not a)
if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C)
"""
print('''
           ___
  (o|_+_|o) 
   ( . . )   
  _( (Y) )_  
 / /,---.\ \ 
/ / | + | \ \
\_)-"   "-(_/  
  |_______| 
  _)  |  (_ 
 (___,'.___)
      ''')

start = input("Welcome to the Treasure Island. Your mission is to find the treasure.\nType START to play: ")

if start.upper() == "START":
    a = input('You\'re at a crossroad. Which road you choose? "Left" or "Right" ').lower()

    if a == "left":
        b = input("Swim or Wait? ").lower()

        if b == "wait":
            c = input("Which door? Red, Blue, or Yellow? ").lower()

            if c == "red" or c == "blue":
                print("Game Over!")
            elif c == "yellow":
                print("You Win!")
            else:
                print("Invalid input. Bye bye.")
        else:
            print("Game Over.")
    else:
        print("You've lost.")
else:
    print("There is no place for mischief. Type START to play.")
