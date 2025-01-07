from menu import MENU, resources


def coin_processing(quarter, dime, nickle, penny):
    """ Calculates the money input by the user """
    return 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny


def usable_check(user_coffe, choice, available, cost):
    """
    return the list of remaining resources after making removing the ingredient for te coffee
    """
    ingredient_name = []
    user_choice = choice[user_coffe]['ingredients']

    for key in user_choice:
        ingredient_name.append(key)

    if 'water' in ingredient_name:
        water_usage = available.get('water') - user_choice.get('water')
    else:
        water_usage = available.get('water')

    if 'milk' in ingredient_name:
        milk_usage = available.get('milk') - user_choice.get('milk')
    else:
        milk_usage = available.get('milk')

    if 'coffe' in ingredient_name:
        coffee_usage = available.get('coffee') - user_choice.get('coffee')
    else:
        coffee_usage = available.get('coffee')
    coffee_cost = choice[user_coffe]['cost']
    amount_remaining = cost - coffee_cost

    remaining_resources = [water_usage, milk_usage, coffee_usage, amount_remaining]
    return remaining_resources


# TODO 1: Prompt user by asking for type of coffe they want


user_coffee = input("What would you like? (espresso/latte/cappuccino): ")

print('Please insert coins.')
quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickles = int(input("How many nickles?: "))
pennies = int(input("How many pennies?: "))

coffee_choice = MENU[user_coffee]["ingredients"]
water_quantity = coffee_choice['water']
milk_quantity = coffee_choice['milk']
coffe_quantity = coffee_choice['coffee']
coffee_costs = MENU[user_coffee]['cost']

payable_amount = coin_processing(quarters, dimes, nickles, pennies)
for_report = usable_check(user_coffee, MENU, resources, payable_amount)

# TODO : Before purchasing report
print('This is what you selected')
print(f"Water : {water_quantity}ml \n Milk : {milk_quantity}ml \n Coffee {coffe_quantity}ml \n Money ${coffee_costs} "
      )
print('--'*20)
# TODO : After purchasing report
if for_report[0] > resources.get('water'):
    print("Sorry there is not enough water.")
elif for_report[1] > resources.get('milk'):
    print("Sorry there is not enough milk.")
elif for_report[2] > resources.get('coffee'):
    print("Sorry there is not enough coffee.")
else:
    print(f"“Here is your {user_coffee}. Enjoy!")
    print(f"Water : {for_report[0]}ml \n Milk : {for_report[1]}ml \n Coffee {for_report[2]}ml \n "
          f"Money ${round(for_report[3], 2)}")




# TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.

to_continue = True
off_machine = input("Do you want to turn off this machine? type 'yes' or 'no'").lower()
if off_machine == 'yes':
    to_continue = False
else:
    to_continue = True
