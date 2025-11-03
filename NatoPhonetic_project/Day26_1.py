student_dict = {
    'student': ['Angela','James',"Lily"],
    "score": [56,76,98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)
    
for (key, value) in student_dict.items():
    print(key, value)

import pandas 

student_df = pandas.DataFrame(student_dict)
print(student_df)

# Looping through a dataframe
for (key, value) in student_df.items():
    print(key)
    print(value)
    
# for (key, value) in student_df:  ->    ValueError: too many values to unpack (expected 2)
    # print(key)
    # print(value)
    
# Inbuilt - Loop through rows of a dataframe
for (index, row) in student_df.iterrows():
    print(index)
    print(row)   # A pandas series object, i.e. we can call using the dot notation
    print(row.student, row.score)
    if row.student == 'Angela':
        print(row.score)