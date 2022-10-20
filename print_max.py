def f(x):
    return ((-5)*(x**5) + 67*(x**2) -47)
a = f(0)
b = f(1)
c = f(2)
d = f(3)
if (a > b) & (a > c) & (a > d):
    print(a)
elif (b > a) & (b > c) & (b > d):
    print(b)
elif (c > a) & (c > b) & (c > d):
    print(c)
else:
    print(d)
