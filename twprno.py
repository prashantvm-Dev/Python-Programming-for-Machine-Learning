Num=int(input("Enter Value:"))
for i in range(2,Num):
    x=0
    for j in range(1,i+1): 
        if i%j==0:
            x=x+1 
    if x==2:
        x=0
        Num=i+2
        for j in range(1,Num+1):
            if Num%j==0:
                x=x+1 
        if x==2:
            print(i,Num)