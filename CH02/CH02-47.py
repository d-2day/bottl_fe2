numList=[64,74,23,60,87]
print("주어진 수:",numList)
myNumber=int(input("Enter number:"))
for anyNumber in numList:
    if anyNumber>myNumber:
        print(anyNumber,">",myNumber)
    else:
        print(anyNumber,"<=",myNumber)
