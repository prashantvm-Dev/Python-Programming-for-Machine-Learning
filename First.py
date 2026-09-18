x=int(input("Enter First Number"))
y=int(input("Enter Second Number"))
print("sum=",x+y)
print("sub=",x-y)
print("mul=",x*y)
print("div=",x/y)



1.WAP to triple all numbers in a given list of integers. Use map()
Ans:


x=list(eval(input("Enter a list:")))
def triple(x):
return x*3
y=list(map(triple,x))
print(y)


2.WAP to add three given list using python map and lambda.
Ans:



x=list(eval(input("Enter the 1st list:")))
y=list(eval(input("Enter the 2nd list:")))
z=list(eval(input("Enter the 3rd list:")))
print("Original list:")
print(x)
print(y)
print(z)
l1=list(map(lambda x,y,z:x+y+z,x,y,z))
print("The resulttant list is:",l1)



3.WAP to create a list containing the power of said number in bases raised to the
corresponding number in the index using python map.
Ans:




from math import *
x=list(eval(input("Enter the power list:")))
y=list(eval(input("enter the number list:")))
def power(x,y):
z=int(pow(y,x))
return z
l=list(map(power,x,y))
print("The resultant list:",l)


4.WAP to convert all the characters into uppercase and lowercase and eliminate
duplicate letters from a given sequence. Use map() function.

Ans:


def swap(y):
if (y.isupper()):
return str(y).lower()
else:
return str(y).upper()
y=list(eval(input("Enter the character list:")))
s=map(swap,y)
print(set(s))



5.WAP to convert a given list of integer and a tuple of integer in a list of string using
map().
Ans:


def convert(c):
if c==1:
return "one"
elif c==2:
return "Two"
elif c==3:
return "three"
elif c==4:
return "four"
elif c==5:
return "five"
elif c==6:
return "six"
elif c==7:
return "Seven"
elif c==8:
return "eight"
elif c==9:
return "nine"
else:
return "zero"
l1=list(eval(input("Enter the number list:")))
l2=list(map(convert,l1))
print(l2)
t1=tuple(eval(input("enter the number tuple:")))
t2=list(map(convert,l2))
print(l2)




6.WAP to find the ratio of positive numbers, negative numbers and zeroes in an array
of integers using map().
Ans:



x=list(eval(input("Enter the integer array:")))
print("The original list:",x)
pos=list(filter(lambda y:y>0,x))
zero=list(filter(lambda y:y==0,x))
neg=list(filter(lambda y:y<0,x))
n=len(x)
z1=[]
P_ratio=round(len(pos)/n,2)
N_ratio=round(len(neg)/n,2)
Z_ratio=round(len(zero)/n,2)
z1.append(P_ratio)
z1.append(N_ratio)
z1.append(Z_ratio)
def ratio(z1):
return z1
l1=list(map(ratio,z1))
print("The ratio array:",l1)
