try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Not a number")
finally:
    print(f"The number you entered is {number}")