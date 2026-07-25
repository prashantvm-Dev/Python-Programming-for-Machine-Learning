x=input("enter a string:")
I=x.split()
I1=[]
i=len(I)-1
while i>=0:
    I1.append(I[i])
    i=i-1
output=' '.join(I1)
print(output)
vowels=0
consonant=0
for i in x:
        if i in "aeiouAEIOU":
            vowels=vowels+1
else:
    consonant=consonant+1
    print("The vowels are:",vowels)
    print("The consonants are:",consonant)
