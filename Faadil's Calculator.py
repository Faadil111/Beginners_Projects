#addition between two numbers
def add(x, y):
    return x + y

# subtraction between two numbers
def subtract(x, y):
    return x - y

# multiplication between two numbers
def multiply(x, y):
    return x * y

# division between two numbers
def divide(x, y):
    return x / y

while True:
    x = int(input("Pick your first number: "))
    # first number
    operator_choice = input("Pick your operator: ")
    # operator
    y = int(input("Pick your second number: "))
    # second number

    if operator_choice == "+":
        result = add(x, y)
        print(f"{x} + {y} = {result}")

    elif operator_choice == "-":
        result = subtract(x, y)
        print(f"{x} - {y} = {result}")

    elif operator_choice == "*":
        result = multiply(x, y)
        print(f"{x} * {y} = {result}")

    elif operator_choice == "/":
        result = divide(x, y)
        print(f"{x} / {y} = {result}")

    else:
        print("Invalid operator")

#Now to check whether the user wants to continue calculating
    next_calculation = input("Do you want to continue? (yes/no): ").lower()

    if next_calculation == "no":
        print("""Thank You for your time 
Goodbye""")
        break

    elif next_calculation == "yes":
        continue

    else:
        print("Invalid input")






