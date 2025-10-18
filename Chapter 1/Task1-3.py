from tabulate import tabulate
def area(a=0, b=0, h=0, TOS=" "):#type of shape; if its s
    TOS = TOS.lower()
    if(TOS == "rectangle" or TOS == "parralleogram"):
        return a*b
    elif(TOS == "square" or TOS == "rhombus"):
        return a*a
    elif(TOS == "triangle"):
        return (a*h)/2
    elif(TOS == "trapezium"):
        return 0.5*(a+b)*h
header = ["Simple 2d Shape Calculator"]
data=[
    ["1. Rectangle/Parralleogram"],
    ["2. Square/Rhombus"],
    ["3. Triangle"],
    ["4. Trapezium"],
    ['5. Exit']
]
choice = 0
while choice!=5:
    print(tabulate(data, headers=header, tablefmt='tsv'))
    choice = int(input("Choose: "))

    if(choice ==1):
        a = int(input("Enter the Base: "))
        b = int(input("Enter the Height: "))
        print(area(a=a, b=b, TOS="rectangle"))
    
    elif(choice ==2):
        a = int(input("Enter the Base: "))
        print(area(a=a, TOS="square"))

    elif(choice ==3):
        a = int(input("Enter the Base: "))
        b = int(input("Enter the Height: "))
        print(area(a=a, h=b, TOS="triangle"))
    elif(choice ==4):
        a = int(input("Enter the length of the bottom Base: "))
        b = int(input("Enter the length of the Upper Base: "))
        h = int(input("Enter the Height: "))
        print(area(a=a, b=b, h=h, TOS="square"))
