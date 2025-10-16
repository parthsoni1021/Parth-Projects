# title function in strings
# def function1(text):
#     return text + " " + text

# def function2(text):
#     return text.title()

# op = function2(function1("helLo")) 
# print(op)

# # Multiple return values
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))


# # Checking for leap year
# # Step 1: Checking if a particular year is divisible by 100
# # Step 2: If yes, it is leap only if it is divisible by 400
# # Step 4: For all the non century years, leap is divisible by 4

# def is_leap(year):
#     if year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         else:
#             return False
#     else:
#         if year % 4 == 0:
#             return True
#         else:
#             return False
        
    
# #Calculator
# art = """
#  _____________________
# |  _________________  |
# | | JO           0. | |
# | |_________________| |
# |  ___ ___ ___   ___  |
# | | 7 | 8 | 9 | | + | |
# | |___|___|___| |___| |
# | | 4 | 5 | 6 | | - | |
# | |___|___|___| |___| |
# | | 1 | 2 | 3 | | x | |
# | |___|___|___| |___| |
# | | . | 0 | = | | / | |
# | |___|___|___| |___| |
# |_____________________|
# """
# print(art, "\nWelcome to the calculator")

# a = float(input("First number "))
# is_continue = True

# i = 0
# result_list = [a]                  # list of the first operand
# while is_continue == True:
#     op_list = ['+', '-', '*', '/']
#     for o in op_list:
#         print(o)
#     op = input("choose an operation")
#     b = float(input("second number "))
    
#     if op == '+':
#         result = result_list[i]+b
#     elif op == '-':
#         result = result_list[i]-b
#     elif op == '*':
#         result = result_list[i]*b
#     elif op == "/":
#         result = result_list[i]/b
#     else:
#         print("Invalid_input")
    
#     result_list.append(result)
#     i += 1
#     print(f"result: {result}")

#     calc_again = input("You want to continue? True or False? ")
#     if calc_again == 'True':         # not True but 'True'
#         is_continue = True
#         continue
#     else:
#         is_continue = False



#using functions

# storing functions into another name
def add(a,b):
    return a+b

# my_fav_operation = add
# print(my_fav_operation(4,5))

# TODO1: Write the other three functions
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

# TODO2: Add these 4 functions into dictionary as values. 
operations = {
    "+": add,         #don't trigger the functions as we are storing it, not calling it
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#TODO3: Use the dictionary operations to perform the calculations.
a = 4
b = 8
operation = '*'
func = operations[operation] 
print(func(a,b))                   #equivalent to print(operations[*](4,8))

should_accumulate = True
num1 = float(input("What is the first number: "))

def calculator():
    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation")
        num2 = float(input("What is the second number: "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type y to continue calculating with {answer} or type 'n' to start a new calculation")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()                            #recursion

calculator()