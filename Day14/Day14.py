#!C:/Users/HD176PR/AppData/Local/Microsoft/WindowsApps/python3.12.exe

# C:\Users\HD176PR\AppData\Local\anaconda3\python.exe - This is the local env which was troubling

# A shebang (also called a hashbang) is a special line at the very top of a script file that tells the operating system which interpreter to use to run the file.

import pyfiglet 
import random
from Day14.game_data import data

logo = "Higher Lower"
print(pyfiglet.figlet_format(logo))
art = "v / s"
versus = pyfiglet.figlet_format(art)

# Tip: Always try to be as structured as possible

def format_data(account):
    """Takes the account data and returns it into printable format"""
    account_name = account['name']
    account_desc = account["description"]
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(user_guess, a_follower, b_follower):
    """Takes a user guess, check which has more followers and if the user guess is correct"""
    # Either write 4 if else conditions, or as follows
    if a_follower > b_follower:
        return user_guess == 'a'
    else:
        return user_guess == 'b'
    

# Display Art
print(logo)
score = 0

# Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

# Format the account data into printable format
print(f"Compare A: {format_data(account_a)}")
print(versus)
print(f"Against B: {format_data(account_b)}")

# Ask the user for a guess
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct
## Get follower count of each account and check using if statement
a_follower_count = account_a['follower_count']
b_follower_count = account_b['follower_count']

is_correct = check_answer(guess, a_follower_count, b_follower_count)

# Give user feedback on their guess.
if is_correct:
    print(f"You're right!, Current Score {score}")
    score += 1
else:
    print(f"Sorry, that's wrong. Final Score {score}")

# Score keeping

# Make the game repeatable

# Make the account at B become the account at A


