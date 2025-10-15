import random

# Generating a random Python dictionary
dict = {f'key_{i}': random.randint(1, 100) for i in range(5)}
print(dict)

for things in dict:
    print(things)

dict['key_0'] = 99
print(dict)

new_dict = {}  #empty list
new_dict['key_10'] = 10
print(new_dict)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def criteria(x):
    if 91 <= x <= 100:
        grade = "Outstanding" 
    elif 81 <= x <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= x <= 80:
        grade = "Acceptable" 
    elif x <= 70:
        grade = "Fail"
    print(grade) 
    return grade
    

# for key in student_scores:
    # student_grades = {
    #     key: criteria(student_scores[key]),
    # }                This won't work, we need to make a different empty dict 

student_grades = {}
for key in student_scores:
    student_grades[key] = criteria(student_scores[key])

print(student_grades)


database = {
    'student': {
        'name': 'Alice',
        'age': 22,
        'courses': ['Mathematics', 'Physics', 'Computer Science'],
        'grades': {
            'Mathematics': 90,
            'Physics': 85,
            'Computer Science': 95
        }
    },
    'university': {
        'name': 'XYZ University',
        'location': 'City Center',
        'departments': [
            {
                'name': 'Engineering',
                'head': 'Dr. Smith',
                'courses_offered': ['Mechanical Engineering', 'Electrical Engineering']
            },
            {
                'name': 'Arts',
                'head': 'Prof. Johnson',
                'courses_offered': ['History', 'Literature']
            }
        ]
    }
}

print(database['student']['courses'][2])
print(database['university']['departments'][0]['courses_offered'][1])

import os

def project():
    def clear_console():
        # For Windows
        if os.name == 'nt':
            os.system('cls')
        else:                     #posix
            os.system('clear')

    bid_list = []
    bid_dict = {}

    inp = "True"
    while inp.lower() == "true":
        clear_console()
        a = input("What is the name? ")
        b = float(input("What is your bid value? $"))
        bid_dict[a] = b
        bid_list.append(b)
        inp = input("Are there any other players, True or False? ")

    clear_console()
    if bid_list:
        d = max(bid_list)
        for i in bid_dict:
            if bid_dict[i] == d:
                print(f"Winner is {i} with a bid of ${d}")
    else:
        print("No bids were placed.")

if __name__ == "__main__":
    project()