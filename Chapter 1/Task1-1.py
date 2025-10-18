def max_of_three(a, b, c):
    if(a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c

number1 = int(input("Number 1: "))
number2 = int(input("Number2: "))
number3 = int(input("Number 3: "))
print(f"The greatest number is {max_of_three(number1, number2, number3)}")
