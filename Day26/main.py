# List comprehension

nums = [1,2,3,4,5,6]
new_list = []
for n in nums:
    add_1 = n + 1
    new_list.append(add_1)

new_list2 = [(n + 1) for n in nums]      #new_list = [new_item for item in list]

# List comprehension is not limited to lists only
name = 'Anglea'
new_list3 = [letter for letter in name]

# List, string, range, tuple etc are all called sequences, which we can iterate through
range_list = [x*2 for x in range(2,6)]

# Conditional list comprehension - new_list = [new_item for item in list if test]
multiple_of_3 = [n for n in nums if n%3==0]

names = ['Parth', 'Arsh', 'Neelam', 'Anil']
caps_greater_5 = [n.upper() for n in names if len(n)>4] 


# Dictionary Comprehension
# dew_dict = {new_key:new_value for item in iterable}  iterable can be list, tuple etc
# dew_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
student_score = {student:random.randint(1,100) for student in names }
# print(student_score)
passed_students = {name:marks for (name, marks) in student_score.items() if marks>=60 }
# print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_words = sentence.split()
# print(list_words)
result = {name.strip('?'):len(name) for name in list_words} 
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {name:c*9/5 + 32 for (name,c) in weather_c.items()}
# print(weather_f)
# If you iterate directly over weather_c,you'd only get the keys ("Monday", "Tuesday", etc.), not the temperatures.

# print(weather_c.items())  <dict_items([('Monday', 12), ('Tuesday', 14)])

student_dict = {
    'student': ["Angela", "James"]
}