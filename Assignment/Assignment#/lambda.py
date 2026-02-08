#Reduce 
from functools import reduce
list = [1,2,3,4,5]
def mysum (x,y):
    return x+y
    
sum = reduce(lambda x,y: x+y,list)
print(sum)

#LAMBDA
