iNum = list(map(int, input("Input numbers: ").split()))
onum, enum = list(filter(lambda x: x%2!=0, iNum)), list(filter(lambda x: x%2==0, iNum))
print(f"Result: {enum+onum}")