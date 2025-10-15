# Calculator

# title function in strings
def function1(text):
    return text + " " + text

def function2(text):
    return text.title()

op = function2(function1("helLo")) 
print(op)

# Multiple return values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))


# Checking for leap year
# Step 1: Checking if a particular year is divisible by 100
# Step 2: If yes, it is leap only if it is divisible by 400
# Step 4: For all the non century years, leap is divisible by 4

def is_leap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False