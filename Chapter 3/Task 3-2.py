print("Simple Calculator")

try:
    n1 = int(input("Enter Number 1: "))
    n2 = int(input("Enter Number 2: "))
    div = n1/n2
except ZeroDivisionError:
    print("Error: Zero Division Error")
except ValueError:
    print("Invalid Data Type Conversion")
else:
    print(f"{n1} + {n2} = {n1+n2}")
    print(f"{n1} - {n2} = {n1-n2}")
    print(f"{n1} * {n2} = {n1*n2}")
    print(f"{n1} / {n2} = {n1/n2}")
