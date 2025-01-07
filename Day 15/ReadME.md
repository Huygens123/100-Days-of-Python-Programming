Resource Management
The usable_check() function serves as the core resource management system. It performs several critical operations:
First, it determines which ingredients are required for the selected beverage by examining the recipe stored in the MENU dictionary. Then, it calculates the remaining resources after a potential beverage preparation by subtracting the required amounts from the available resources. The function handles three main resources: water, milk, and coffee.
The function's implementation shows careful consideration for cases where certain ingredients might not be required for particular beverages. It uses conditional checks to handle these scenarios, making the code more robust and flexible.
User Interface
The program implements a command-line interface that guides users through the coffee-making process. The interaction flow includes:

Beverage selection (espresso/latte/cappuccino)
Coin insertion with denominations breakdown
Order confirmation with ingredient details
Result reporting with either success message or resource shortage notification
Machine power control option
