# Todo - Replace the name placeholder with the actual name
# Save the letters in the folder 'ReadyToSend'

# readlines(), replace() and strip() method

f = open(r'Output\ReadyToSend\example.txt', 'r')
letter_list = f.readlines()


line1_string = letter_list[0]

with open(r'Input\Letters\names.txt', 'r') as names: 
    name_list = names.readlines()
    for name in name_list:
        cleaned_name = name.strip()

        named_str = line1_string.replace('name', cleaned_name)
        letter_list[0] = named_str

        output_file = f'letter_{cleaned_name}.txt'
        
        # with open(r'Output\ReadyToSend\{output_file}', 'w') as f:     This will throw error due to 'r' or raw string
        
        with open(f'Output\\ReadyToSend\\{output_file}', 'w') as f:        # use forward slashes or \\
            for line in letter_list:
                f.write(line)

    
        










