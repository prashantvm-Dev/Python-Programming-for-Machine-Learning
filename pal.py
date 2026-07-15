x=int(input("enter a number:"))
temp=x
rev=0
while x>0:
    y=x%10
    rev=rev*10+y
    x=x//10
if temp==rev:
    print("It is a Palindrome number")
else:
    print("It is not a Palindrome number")