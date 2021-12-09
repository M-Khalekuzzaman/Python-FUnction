'''
def add(a,b) :
    sum = a + b
    print(sum)

def addition(x,y,z) :
    addi = x + y + z
    print(addi)


a = int(input("Enter your a value : "))
b = int(input("Enter your b value : "))
x = int(input("Enter your x value : "))
y = int(input("Enter your y value : "))
z = int(input("Enter your z value : "))
add(a,b)
addition(x,y,z)
'''

#Student Information Function:
i = 1
while i<=10 :
    def studentInfo(name,roll,sub1,sub2):
        print("Name : ",name)
        print("Roll : ",roll)
        print("Sub1 : ",sub1)
        print("Sub2 : ",sub2)
        total = sub1 + sub2
        print("Total marks is : ",total)
        print("\n\n")


    name = input("Enter your name : ")
    roll = int(input("Enter your roll : "))
    sub1 = int(input("Enter your sub1 marks : "))
    sub2 = int(input("Enter your sub2 marks : "))
    studentInfo(name,roll,sub1,sub2)
    i = i + 1
