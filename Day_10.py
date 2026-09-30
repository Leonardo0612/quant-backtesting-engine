def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = float(input("Choose your first number: "))
should_continue = True

while should_continue:
    
    which_operation = input("+\n-\n*\n/\nChoose an operation:")
    num2 = float(input("Choose your second number: "))

    answer = operations[which_operation](num1, num2)
    print(f"{num1} {which_operation} {num2} = {answer}")

    choice = input(f"Type 'y' to continue with {answer}, type 'n' to start with new values: ").lower()

    if choice == "y":
        num1 = answer
    else:
        print("\n" * 20)
        num1 = float(input("Choose your first number: "))