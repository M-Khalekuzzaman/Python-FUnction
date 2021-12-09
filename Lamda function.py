#lamda function is a function without name(that means Anonymous Function

'''
def calcution(a,b) :
    result = a*a + 2*a*b + b*b
    return result

'''

result = (lambda a,b : a*a + 2*a*b + b*b)(2,3)    ## lambda function
                                                   ## (lambda parameter : Expresstion)(value)
print(result)
