x=int(input("Enter First Number"))
y=int(input("Enter Second Number"))
print("sum=",x+y)
print("sub=",x-y)
print("mul=",x*y)
print("div=",x/y)





1.WAP to print the second largest and second smallest element in a list of 10 integers 
without using sort function.
Ans:
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
2.WAP to create two lists first list containing 5 integers and second list containing 5 
strings.print both the lists one element from each list combined at a time.
Ans:
list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C","D","E"] 
s=[]
for i in range(len(list1)): 
s.append(str(list1[i])) 
s.append(list2[i])
print(s)
3.WAP to create an integer list of 20 elements increase the odd valued elements by 5. 
Ans:
s=[]
x=int(input("enter the no of elements:")) 
for i in range(x):
n=int(input("Enter the element:")) 
s.append(n)
for i in range(x): 
if s[i]%2!=0:
s[i]=s[i]+5 
print(s)
4.WAP to create a function that prints the first 15 terms of the fibonacci series without 
using recursion.
Ans:
def fibonacci(n): 
a=1
b = 1 print(a,b,end=" ") 
# print(b)
for i in range(2, n): 
c = a + b 
print(c,end=" ")
a = b
b = c
n = int(input("Enter the number of terms you want to print: ")) 
print("The Fibonacci series of first",n,"terms are:") 
fibonacci(n)
5.WAP to create a function that takes list as argument and returns the even values of 
the list.Print the new list with even values.
Ans:
def even_len(n): 
s=[]
for i in n:
if i%2==0: 
s.append(i)
return s
x=input("enter the list elements:") 
n=[int(i) for i in x.split(",")]S 
s=even_len(n)
print(s)
6.WAP to calculate factorial of a number using recursion. 
Ans:
def factorial(n):
if n==0:
result=1 
else:
result=n*factorial(n-1) 
return result n=int(input("Enter the number:")) 
if(n<0):
print("It is a Negative number:") 
else:
print("Factorial of",n,"is:",factorial(n))
