# Namespaces: Local vs global

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")  #2

increase_enemies()
print(f"enemies outside function: {enemies}")    #1

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)     Gives error

#Global scope
player_health = 10

def drink_potion():
    potion_strength = 2   # local variable
    print(player_health)  # global variable
    
drink_potion()    

# Any thing we name, a variable, function, datastructure, etc has a namespace. It can be global or local
# Creating a variable inside a function makes it local, but not the case for if/else/for/while loop etc

game_level = 5
ememies = ['a', 'b', 'c']

def create_enemy():
    # new_enemy = ""
    if game_level <= 5:
        new_enemy = enemies[0]

print(new_enemy)










