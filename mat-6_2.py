m=[[1,2,3],
    [3,1,0],
    [1,3,2]]

for i in range(3):
    r_sum=sum(m[i])
    print(m[i][0],m[i][1],m[i][2],r_sum)

for j in range(3):
    c_sum=0
    for i in range(3):
        c_sum+=m[i][j]
    print(c_sum,end=" ")