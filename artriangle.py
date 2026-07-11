import math
x=int(input("Enter First side="))
y=int(input("Enter Second Side="))
z=int(input("Enter Third Side="))
s=float((x+y+z)/2)
a=math.sqrt(s*(s-x)*(s-y)*(s-z))
print("Area of Triangle:",a)