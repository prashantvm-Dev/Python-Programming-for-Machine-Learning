from collections import Counter
my_list=[1,3,5,1,3,2,5,4,2,1]
print("Original lis:"+str(my_list))
temp=Counter(my_list)
res=[[key]*val for key,val in temp.items()]
print("Matrix after grouping:"+str(res))