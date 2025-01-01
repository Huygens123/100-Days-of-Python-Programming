from art import logo

# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    '/': divide,
    '*': multiply,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for operator in operations:
        print(operator)
    to_continue = True

    while to_continue:

        operations_symbol = input("Pick an operation from:' +': add,'-': subtract, '/': divide, '*': multiply, ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, "
                                f"or type 'n to start a new calculation.: ")
        if should_continue == "y":
            num1 = answer
        else:
            to_continue = False
            calculator()
calculator()
