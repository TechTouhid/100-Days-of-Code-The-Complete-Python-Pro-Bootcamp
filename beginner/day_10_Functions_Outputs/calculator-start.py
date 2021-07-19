from art import logo




# Calculator

# Add
def add(x, y):
    return x + y


# Subtract
def sub(x, y):
    return x - y


# Multiply
def mul(x, y):
    return x * y


# Device
def div(x, y):
    return x / y


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculate():
    print(logo)
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pic an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        ask = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation : ")
        if ask == 'y':
            num1 = answer
        else:
            should_continue = False
            calculate()


calculate()
