# Simpler code for main.py

PLACEHOLDER = 'name'

with open(r'Input\Letters\names.txt', 'r') as names_file:
    names = names_file.readlines()

with open(r'Input\Letters\example.txt', 'r') as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f'Output/ReadyToSend/letter_for_{stripped_name}', 'w') as completed_letter:
            completed_letter.write(new_letter)



"""# file = open('my_file.txt')
# contents = file.read()
# print(contents)

# file.close()        # otherwise memory will be consumed 

with open('my_file.txt') as file:
    contents = file.read()
    print(contents)
    # No need to close it now. 

with open('my_file.txt', mode='w') as file:   #by default mode is 'r'
    file.write('New text.')  #prev text will be deleter

with open('my_file.txt', mode='a') as file:   # append mode
    file.write('Text appended.')    # Will be appended in same line unless \n is writte

# with open('new_file.txt', 'w') as file2:       #in write mode, automaticallyc creates a file if not there
#     file.write('Text written.')              

# Root folder is generally C drive in windows and Macintosh.HD in Mac (Represented by just a \ or C:\)

# Absolute Path - Always relative to the root
# Relative Path - Relative to the folder we are in (or the working directory)  .\working_directory\relativepath.extension 
# or working_directory\relativepath.extension 

# when we write ..\parentfolder.ourdesiredfile.extension   .. is to go to the parent folder

# Note: In windows and Macs, backward and forward are used respectively. But in python, it doesn't matter



with open('../../../../../Downloads/new_file.txt') as file:
    contents = file.read()
    print(contents)

"""