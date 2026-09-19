def test(x):
    if (x.isupper()):
        return str(x).lower()
    else:
        return str(x).upper()
x=['A','A','B','c','D','e']
res=map(test,x)
print(set(res))