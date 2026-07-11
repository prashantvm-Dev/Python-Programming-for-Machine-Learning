import math
x=int(input("Enter a:"))
y=int(input("Enter b:"))
z=int(input("Enter c:"))
d=math.sqrt(y*y)-(4*x*z)
root1=(-y+d)/(2*x)
root2=(-y-d)/(2*x)
print("Root 1:",root1)
print("Root 2:",root2)