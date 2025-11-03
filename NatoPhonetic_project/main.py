import pandas as pd
# dict comprehension using dictionaries - {new_key:new_value for (key,value) in dict.items()}
# dict comprehension using dataframes - {new_key:new_value for (index, row) in df.iterrows()}

# Todo 1 - Create a dict in this format: {'A': 'alfa, 'B': 'Bravo'}
# df_dict = df.to_dict()
# print(df_dict.items())
df = pd.read_csv("nato_phonetic_alphabet.csv")
print(df)

phonetic_dict = {}
for (index, row) in df.iterrows():        #index and row are df series objects
    phonetic_dict[row.letter] = row.code
print(phonetic_dict)

# OR Using dict comprehension
phonetic_dict2 = {row.letter:row.code for (index,row) in df.iterrows()}       #2 lines saved !
print(phonetic_dict2)

# Todo2 - Create a list of phonetic words from the word user inputs
user_input = input('Enter the word: ').upper()
print([phonetic_dict[i] for i in user_input])


