#recursion is a process where a function can call itself
'''
def fact(n) :
    if n == 1:
        return 1
    else :
        return n * fact(n-1)

n = int(input("Enter your input integer number : "))
factorial = fact(n)
print("Total factorial number is = ",factorial)
'''
def fact(n) :
    if n == 1:
        return 1
    else :
        return n * fact(n-1)

n = int(input("Enter your given integer number : "))
factorial = fact(n)
print("Total Factorial number = ",factorial)