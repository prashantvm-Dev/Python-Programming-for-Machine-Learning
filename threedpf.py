x=int(input("Enter a 3 digit numbers:"))
c=2
while(x>1):
    if(x%c == 0):
        print(c,end=" ")
        x=x/c
    else:
        c=c+1