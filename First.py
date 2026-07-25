x=int(input("Enter First Number"))
y=int(input("Enter Second Number"))
print("sum=",x+y)
print("sub=",x-y)
print("mul=",x*y)
print("div=",x/y)


N=int(input("Enter a number:")) 
for i in range(2,N):
d=0
for j in range(1,i+1): 
if i%j==0:
d=d+1 
if d==2:
d=0 
N=i+2
for j in range(1,N+1): 
if N%j==0:
d=d+1 
if d==2:
print("(%d,%d)"%(i,N))


x=int(input("Enter a number:"))
factorial=1 
if x<0:
print("It is a negative number") elif x==0:
print("The factorial of ",x,"is :",factorial) 
else:
for i in range(1,x+1):
factorial=factorial*i
print("The factorial of",x,"is:",factorial)


x=int(input("Enter a year:"))
if(x%4 == 0) and (x%100 != 0) or (x%400==0):
print(x,"is a leap year") 
else:
print(x,"is not a leap year")

x=input("enter a string:")
z=(str(str(x)[::-1])) 
if x == z:
print("it is a palindrome") 
else:
print("it is not a palindrome")

x=input("Enter a String:")
y= ""
for c in x:
if c != " ": 
y=y+c else:
if len(y) % 2 == 0: 
print(y)
y = ""
if len(y) % 2 == 0:
print(y)

x=input("Enter a string:")
result = "" 
for char in x:
if char not in result: 
result=result+char
print(result)



arr=[]
x=int(input("enter the no of elements:")) 
for i in range(x):
m=int(input("Enter the element:")) 
arr.append(m)
for j in range(len(arr)-1):
for k in range(len(arr)-j-1): 
if arr[k] > arr[k+1]:
arr[k],arr[k+1]=arr[k+1],arr[k] 
print("The sorted array is:")
print(arr) second_largest=arr[-2] 
second_smallest=arr[1]
print("Second largest element is:",second_largest)
print("Second smallest element is:",second_smallest)
