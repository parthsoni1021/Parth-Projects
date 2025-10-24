# Make a digital coffee machine

# print report of all coffee machine resources
# check resources sufficient?
# process coins
# check transaction sucessful?
# make coffee using resources


# https://emojipedia.org/hot-beverage
#https://replit.com/@appbrewery/coffee-machine-start#main.py 

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

""" # dict = {1:'a',2:'b',3:'c',4:'d',{5:'e',6:'f'},}  #this will give an error
dict = {1:'a',2:'b',3:'c',4:'d', 5: {6:'e',7:'f'},} # dictionaries keys must be immutable, and dictionary itself if mutable, so it will show error

print(dict[1])  # need to put key, can't call by index. eg. print(dict[0]) will throw error
print(dict[5][7]) """

""" grocery = {
    'sugar': 100,
    'salt': 50,
    'rice': 200}

    Print each item with 'g' unit
    for item, quantity in grocery.items():                            # .items() method
    item_print = f"{item.capitalize()}: {quantity}g"
    print(item_print) """


def printable_dict(unitless_dict):
    units = {
        'water': 'ml',
        'milk': 'ml',
        'coffee': 'g',
        'money': '$'
    }
    for item, value in unitless_dict.items():
        unit = units.get(item, '')     # get() method is used to retrieve the value for a given key
        if unit == '$':
            print(f"{item.capitalize()}: {unit}{value}")
        else:
            print(f"{item.capitalize()}: {value}{unit}")
    
# printable_dict(current_report)


def is_resources_sufficient(coffee_name):
    ans = (current_report['water'] >= MENU[coffee_name]['ingredients']['water']) and \
            (current_report['coffee'] >= MENU[coffee_name]['ingredients']['coffee']) and \
            (current_report['milk'] >= MENU[coffee_name]['ingredients']['milk'])
    return ans
# print(is_resources_sufficient('espresso'))


current_report = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0,
}

def update_report(coffee_choice, current_report):
    updated_report = {}
    updated_report['water'] = current_report['water'] - MENU[coffee_choice]['ingredients']['water']
    updated_report['milk'] = current_report['milk'] - MENU[coffee_choice]['ingredients']['milk']
    updated_report['coffee'] = current_report['coffee'] - MENU[coffee_choice]['ingredients']['coffee']
    updated_report['money'] = current_report['money'] + MENU[coffee_choice]['cost']
    return updated_report

def which_resource_lacks(coffee_name, current_report):
    list_lack_resources = []
    if current_report['water'] < MENU[coffee_name]['ingredients']['water']:
        list_lack_resources.append('water')
    if current_report['coffee'] < MENU[coffee_name]['ingredients']['coffee']:
        list_lack_resources.append('coffee')
    if current_report['milk'] < MENU[coffee_name]['ingredients']['milk']:
        list_lack_resources.append('milk')

    if len(list_lack_resources) == 1:
        return f"{list_lack_resources[0]}."
    elif len(list_lack_resources) == 2:
        return f"{list_lack_resources[0]} and {list_lack_resources[1]}."
    elif len(list_lack_resources) == 3:
        return f"{list_lack_resources[0]}, {list_lack_resources[1]} and {list_lack_resources[2]}."
# which_resource_lacks('espresso', current_report)

running_condition = True
while running_condition:
    # Ask the user for coffee input. This should repeat itself until user inputs 'off'
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice == 'off':
        running_condition = False
    elif coffee_choice == 'report':
        printable_dict(current_report)
    else:
        if is_resources_sufficient(coffee_choice) == True:
            print("Please insert coins")
            quarters = float(input("How many quarters: "))
            dimes = float(input("How many dimes: "))
            nickles = float(input("How many nickles: "))
            pennies = float(input("How many pennies: "))

            total_dollars = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
            if total_dollars < MENU[coffee_choice]['cost']:
                print('Sorry that\'s not enough money. Money refunded')
                continue
            else:
                change = round((total_dollars - MENU[coffee_choice]['cost']),2)
                print(f"Here is ${change} in change")

                print(f'Here\'s your {coffee_choice}☕ Enjoy!')

                current_report = update_report(coffee_choice,current_report)
        else:
            print(f'Sorry there is not enough {which_resource_lacks(coffee_choice, current_report)}')
            continue




# Learnings: 
# If-else blocks should be written together to avoid indentation issues
# Always check the code time to time, especially after inserting a new functionality. Resolve the issue that time only
# Make suitable functions always. This makes code neat and tidy