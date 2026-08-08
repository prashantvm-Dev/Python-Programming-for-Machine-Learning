a=[1,2,3,4,5]
b=["A","B","C","D","E"]
c=[]
for i in range(len(a)):
    c.append(str(a[i]))
    c.append(b[i])
print(c)