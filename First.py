x=int(input("Enter First Number"))
y=int(input("Enter Second Number"))
print("sum=",x+y)
print("sub=",x-y)
print("mul=",x*y)
print("div=",x/y)



a = []

for i in range(10):
    n = int(input("Enter number: "))
    a.append(n)

for i in range(10):
    for j in range(i + 1, 10):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print("Second smallest:", a[1])
print("Second largest:", a[8])


a = [1, 2, 3, 4, 5]
b = ["A", "B", "C", "D", "E"]

for i in range(5):
    print(a[i], b[i])


a = []

for i in range(20):
    n = int(input("Enter number: "))
    a.append(n)

for i in range(20):
    if a[i] % 2 != 0:
        a[i] = a[i] + 5

print(a)



def fibonacci():
    a = 1
    b = 1

    print(a, b, end=" ")

    for i in range(13):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

fibonacci()



def even(a):
    b = []

    for i in a:
        if i % 2 == 0:
            b.append(i)

    return b

a = [1, 2, 3, 4, 5, 6]

print(even(a))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter number: "))

print("Factorial:", factorial(n))
