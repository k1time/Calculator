operations = ["+", "-", "*", "/", "^"]

def input_num_1():
    while True:
        try:
            num_1 = float(input("First number: \n"))
            return num_1
        except ValueError:
            print("Please, enter correct number")

def input_num_2():
    while True:
        try:
            num_2 = float(input("Second number: \n"))
            return num_2
        except ValueError:
            print("Please, enter correct number")

def input_operation():
    while True:
        try:
            operation = input("Choose operation: '+', '-', '*', '/', '^' \n")
            if operation not in operations:
                print("Please, enter correct operation")
                continue
            return operation
        except ValueError:
            print("Please, enter correct operation")

def sum(a, b):
    return a + b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Please, enter correct data.")
        return None

def multi(a, b):
    return a * b

def sub(a, b):
    return a - b

def power(a, b):
    return a ** b

def calc(a, b, operation):
    if operation == "+":
        print(f"{a} + {b} = {sum(a, b)}")
    elif operation == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    elif operation == "*":
        print(f"{a} * {b} = {multi(a, b)}")
    elif operation == "/":
        print(f"{a} / {b} = {div(a, b)}")
    elif operation == "^":
        print(f"{a} ^ {b} = {power(a, b)}")

while True:
    number_1 = input_num_1()
    number_2 = input_num_2()
    operation = input_operation()
    calc(number_1, number_2, operation)
    print("==========next==========")