def oddNumber(start, end, odd=True):
    return [x for x in range(start, end) if x%2!=0] if odd else [x for x in range(start, end) if x%2==0]

sNum = int(input("Input start number: "))
eNum = int(input("Input end number: "))

print(f"Even and odd number from {sNum} to {eNum}: ")
print(f"Even numbers: {oddNumber(sNum, eNum, False)}")
print(f"Odd numbers: {oddNumber(sNum, eNum)}")