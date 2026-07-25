x=int(input("Enter number:"))
fact=1 
if x<0:
    print("Not Valid") 
elif x==0:
    print(fact) 
else:
    for i in range(1,x+1):
        fact=fact*i
    print(fact)