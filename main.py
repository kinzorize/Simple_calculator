from replit import clear
from art import logo


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    logo()
    should_continue = True
    num1 = float(int(input("what's your first number: ")))

    for symbol in operations:
        print(symbol)
    while should_continue:
        symbol_operations = input("Pick a symbol: ")
        num2 = float(int(input("what's your next number: ")))

        calculation_symbol = operations[symbol_operations]
        answer = calculation_symbol(num1, num2)

        print(f"{num1} {symbol_operations} {num2} = {answer}")
        continue_calculating = input(
            f"Type 'y' to continue with {answer} or Type 'n' to exit: ")
        if continue_calculating == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()
