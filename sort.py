a=[]
for i in range(10):
    n=int(input("Enter numbers:"))
    a.append(n)
for i in range(10):
    for j in range(i+1,10):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("Second smallest:",a[1])
print("Second largest:",a[-2])