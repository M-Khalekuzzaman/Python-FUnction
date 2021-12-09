#How to use map function,map function is a list object
'''
def square (x) :
     return  x*x
num = [1,2,3,4,5]
result = list(map(square,num))
print(result)

'''
'''
def cube(x) :
    cube = x*x*x
    return cube
num = [1,2,3,4,5]
result = list(map(cube,num))
print(result)
'''
#How to use filtar function to the list
num = [1,2,3,4,5]
result = list(filter(lambda x : x%2 == 0,num))
print(result)

