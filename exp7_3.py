from math import *
x=[2,4,6,8]
y=[2,3,4,5]
def power(x,y):
    z=int(pow(y,x))
    return z
res=list(map(power,x,y))
print("Resultant:",res)