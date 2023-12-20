from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)
    first_number = float(input("What is the next number?: "))

    for symbol in operations:
        print(symbol)

    calculating = True

    while calculating:
        operation_symbol = input('Pick an operation: ')
        second_number = float(input("What is the next number?: "))

        result = operations[operation_symbol]
        first_answer = result(first_number, second_number)

        print(f'{first_number} {operation_symbol} {second_number} = {first_answer}')
        want_to_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation, or type 'exit' to leave the program.: ")

        if want_to_continue == 'y':
            first_number = first_answer
        elif want_to_continue == 'n':
            calculating = False
            calculator()
        else:
            calculating = False

calculator()