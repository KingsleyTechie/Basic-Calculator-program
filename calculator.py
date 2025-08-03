
def clean(n):
    return int(n) if n.is_integer() else n

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
op = input("Choose an operation (+, -, *, /): ")

if op == "+":
    result = first + second
    print(f"{clean(first)} + {clean(second)} = {clean(result)}")
elif op == "-":
    result = first - second
    print(f"{clean(first)} - {clean(second)} = {clean(result)}")
elif op == "*":
    result = first * second
    print(f"{clean(first)} * {clean(second)} = {clean(result)}")
elif op == "/":
    if second != 0:
        result = first / second
        print(f"{clean(first)} / {clean(second)} = {clean(result)}")
    else:
        print("Oops! You can’t divide by zero.")
else:
    print("That’s not a valid operation. Please use +, -, *, or /.")