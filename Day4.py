import random
import os
os.system("cls")
"""
# https://docs.python.org/3/library/random.html

# random_integer = random.randint(1,10)  # 1 and 10 included
# print(random_integer)

# random_numbner_0_to_1 = random.random() * 10
# print(random_numbner_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

num = random.randint(1,10)
if num > 5:
    print("Heads")
else:
    print("Tails")

print(random.randint(0,1))
"""


#List Data structure - Ordered

indian_states = ["Delhi", "Raj", "UP","Uttarakhand", "Bihar"]
print([indian_states[i] for i in range(0,5)])


indian_states[2] = "Uttar Pradesh"
indian_states.append("Gujarat")

print(indian_states)

#https://docs.python.org/3/tutorial/datastructures.html

print(random.choice(indian_states))
i = random.randint(0, len(indian_states)-1)
print(indian_states[i])


fruits = ["apple", "banana", "mango", "orange", "grapes", "pineapple", "strawberry"]
vegetables = ["carrot", "broccoli", "spinach", "tomato", "potato", "cucumber", "bell pepper"]
eatables = [fruits, vegetables]
print(eatables[1][1])

def project():
    print(
        '''
██████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███
██─▄─▄█─██─█─███▀██─▄▀████
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
█████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
██████████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
█▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀

Welcome to the Rock Paper Scissors Game !!'''
    )
    rock = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """
    paper = """
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """
    scissor = """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """

    list = ['r','p','s']
    user = input("What do you choose, write 'r' for Rock, 'p' for Paper and 's' for scissor ")
    computer = random.choice(list)

    if user == 'r':
        print(rock)
        if computer == 'r':
            print("computer       ",rock)
            print("Draw")
        elif computer == 'p':
            print("computer       ",paper)
            print("you lost")
        else:
            print("computer       ",scissor)
            print("You won!")

    elif user == 'p':
        print(paper)
        if computer == 'r':
            print("computer       ",rock)
            print("You Won!")
        elif computer == 'p':
            print("computer       ",paper)
            print("Draw")
        else:
            print("computer       ",scissor)
            print("You lost!")

    elif user == 's':
        print(scissor)
        if computer == 'r':
            print("computer       ",rock)
            print("You Lost!")
        elif computer == 'p':
            print("computer       ",paper)
            print("You Won!")
        else:
            print("computer       ",scissor)
            print("Draw")

    else:
        print("Invalid Input")

if __name__ == "__main__":
    project()