# Debugging

# describe the problem
# Fix the underlined errors
# print is your friend
# Run the code often. After each small step, so that you can fix one bug at a time, not when all got compiled.
# Debugger
#  breakpoint, step over, step into, step into my code, step out

# Final tip: Take a break if the code is not running after a time. 
# Still if the code isn't working after a lot of hardwork, is to ask a friend.


import random 
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])