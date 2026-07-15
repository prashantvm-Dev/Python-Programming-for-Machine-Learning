x=int(input("Enter the percentage:"))
if x>=90:
    print("Grade is 'O'")
elif x>=80 and x<90:
    print("Grade is 'E'")
elif x>=70 and x<80:
    print("Grade is 'A'")
elif x>=60 and x<70:
    print("Grade is 'B'")
elif x>=50 and x<60:
    print("Grade is 'C'")
elif x>=40 and x<50:
    print("Grade is 'D'")
else:
    print("Grade is 'F'")