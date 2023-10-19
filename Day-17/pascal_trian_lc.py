import math
def fun(rowIndex):
    for i in range(rowIndex+1):
        print(math.factorial(rowIndex)//(math.factorial(rowIndex-i)*math.factorial(i)))        
    #return [math.factorial(rowIndex)//(math.factorial(rowIndex-i)*math.factorial(i)) for i in range(rowIndex+1)]
rowIndex=int(input())
print(fun(rowIndex))