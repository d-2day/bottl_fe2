def add_multiply(x,y):
        sum=x+y
        mult=x*y
        return sum, mult
a=int(input('Enter a : '))
b=int(input('Enter b : '))
m,n=add_multiply(a,b)
print(m,n)
