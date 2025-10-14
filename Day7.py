"""Hangman Game"""
import random


#pip install random-word
# from random_word import RandomWords
# word = RandomWords().get_random_word()
# print(word)                                      #giving difficult words



with open(r"C:\Users\HD176PR\OneDrive - EY\Documents\Python_sessions\common_english_words.txt") as f:
    words = f.read().splitlines()
chosen_word = random.choice(words)
print(chosen_word)


#1 - Creating a blank placeholder
placeholder = "".join("_") * len(chosen_word)
print(placeholder)
""" initializing empty string and running a loop over chosen word and concatenating is ineffective"""

#2 Asking user to guess the word

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    #3 Create a display that fills the right guess in the placeholder
    display = ""
    correct_letters = []

    for letter in chosen_word:    # iterates over the letters in chosen_word
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win")


























# #pip install random-word
# # from random_word import RandomWords
# # word = RandomWords().get_random_word()
# # print(word)                                      #giving difficult words

# with open(r"C:\Users\Parth Soni\OneDrive - IIT Delhi\Documents\Python\common_english_words.txt") as f:
#     words = f.read().splitlines()
# word = random.choice(words)
# print(word)

# blanks = ""
# for i in range(0,len(word)):
#     blanks += "-"
# print(blanks)

# def find_indexes(letter, word):
#     word_list = []
#     for i in range(0,len(word)):
#         word_list.append(word[i])
#     print(word_list)
#     indexes = []
#     for i in range(len(word_list)):
#         if word_list[i] == letter:
#             indexes.append(i)  #Index
#     return indexes
#     # print(indexes)

# def guessed_correct(letter, word):
#     if letter in word:
#         return True
#     else:
#         return False

# def replace_blank(index_list, letter, blank_str):
#     blank_list = []
#     for _ in range(len(blank_str)):                       # 0 included
#         # blank_list = [].append('-')                       # append returns none, so blank_list is NoneType
#                                                         # print(type(blank_list))
#                                                         # print(type(index_list))
#         blank_list.append('-')   
#     for i in range(len(index_list)):
#         blank_list[index_list[i]] = letter

#     blank_new = ""
#     for i in range(len(blank_list)):
#         blank_new = blank_new + blank_list[i]
#     #print(blank_new)
#     return blank_new

# def word_found(blank_new):
#     if blank_new == word:
#         word_found = True
#     else:
#         word_found = False
#     return word_found

# # print(find_indexes("p", "apple"))
# print(replace_blank([1, 2],"p", "-----"))
# print(type(replace_blank([1, 2],"p", "-----")))
# print(guessed_correct('p', 'apple'))

# def artmaker():

#     stages = [
#     ""
#     _______
#     |/      
#     |      
#     |      
#     |      
#     |      
#     |
#     |___
#     "",
#     ""
#     _______
#     |/      |
#     |      (_)
#     |      
#     |      
#     |      
#     |
#     |___
#     "",
#     ""
#     _______
#     |/      |
#     |      (_)
#     |       |
#     |       |
#     |      
#     |
#     |___
#     "",
#     ""
#     _______
#     |/      |
#     |      (_)
#     |      \\|/
#     |       |
#     |      
#     |
#     |___
#     "",
#     ""
#     _______
#     |/      |
#     |      (_)
#     |      \\|/
#     |       |
#     |      /
#     |
#     |___
#     "",
#     ""
#     _______
#     |/      |
#     |      (_)
#     |      \\|/
#     |       |
#     |      / \\
#     |
#     |___
#     ""
# ]

#     return stages[no_of_wrong_guesses]

[{()}]

# #Start integration

# no_of_wrong_guesses = 0

# while no_of_wrong_guesses < 5:
#     inp = input("Guess the letter: ")
#     if guessed_correct(inp, word) == True:
#         ind = find_indexes(inp, word)
#         print(replace_blank(ind, inp, blanks))
#     else:
#         no_of_wrong_guesses += 1
#     print(artmaker())
# print(artmaker(), "Game over! You chose the wrong word")




























