a=[]
for i in range(20):
    n=int(input("Enter number:"))
    a.append(n)
for i in range(20):
    if(a[i]%2!=0):
        a[i]=a[i]+5
print(a)