# # Namespaces: Local vs global

# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")  #2

# increase_enemies()
# print(f"enemies outside function: {enemies}")    #1



# # Local Scope
# # def drink_potion():
# #     potion_strength = 2
# #     print(potion_strength)

# drink_potion()
# # print(potion_strength)     Gives error

# #Global scope
# player_health = 10

# def drink_potion():
#     potion_strength = 2   # local variable
#     print(player_health)  # global variable
    
# drink_potion()    

# # Any thing we name, a variable, function, datastructure, etc has a namespace. It can be global or local
# # Creating a variable inside a function makes it local, but not the case for if/else/for/while loop etc

# game_level = 5
# ememies = ['a', 'b', 'c']

# def create_enemy():
#     # new enemy = ""  # to avoid the linter caution
#     if game_level <= 5:
#         new_enemy = enemies[0]

#     print(new_enemy) 

# # Modifying something within the global scope

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")  #2

# increase_enemies()
# print(f"enemies outside function: {enemies}")    #1

# # In this example, both enemies are completely different objects. The first one is the global variable, while the other is local

# def increase_enemies2():
#     enemies += 1    #this will show an error
#     print(enemies)

# increase_enemies2()

# # pip show pylint flake8 ruff # pip install ruff


# def increase_enemies2():
#     global enemies     # This is often not preferred. Maybe we can read it, but modifying isn't recommended
#     enemies += 1    #this will show an error
#     print(enemies)

# # Global Constants

# PI = 3.12159
# GOOGLE_URL = "https://www.google.com"  
# # A general convention while using global scope to remind that we shouldn't modify this

import random

print("Welcome to the Number Guessing name\n I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty, 'easy' or 'hard': ")
if level == 'easy':
    attempts = 10
else:                              #elif can be introduced
    attempts = 5

num = random.randint(1,100)  #both included
print(num)

while attempts > 0:
    print(f"Your have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > num:
        print("Too high")
        attempts -= 1
    elif guess == num:
        print("You've made a correct guess")
        break
    else:
        print("Too low")
        attempts -= 1











