def fibonacci():
    a=1
    b=1
    print(a,b,end=" ")
    for i in range(13):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
fibonacci()