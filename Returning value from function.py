'''
def add(a,b) :
    sum = a + b
    return sum

result = add(20,30)
print("Result is : ",result)
'''
def value(a,b,c) :
    if a>b and a>c :
        return a
    elif b>a and b>c :
        return b
    else:
        return c

a = int(input("Enter your first value :"))
b = int(input("Enter your second value :"))
c = int(input("Enter your Third value :"))

High = value(a,b,c)
print("Highest value is : ",High)
