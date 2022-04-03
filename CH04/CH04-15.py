a=input("Enter an integer: ")
while not a.isnumeric():
    print("Enter numbers.")
    a=input("Enter an integer: ")
a=int(a)
print(a,type(a))
