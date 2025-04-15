import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+" :add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    first_num = float(input("What's the first number?: "))

    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))

        result = operations[operation](first_num, second_num)

        print(f"{first_num} {operation} {second_num} = {result}")

        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if cont == "y":
            first_num = result
        else:
            print("\n" * 20)
            should_accumulate = False
            calculator()

calculator()