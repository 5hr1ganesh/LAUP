import numpy as np

u = np.array((3, 4, 5))
v = np.array((1, 2, 7))
print("vector u", u)
print("vector v", v)
print("enter the value of a and b")

# typecast input to float then and there
a = float(input())
b = float(input())
d = (a * u) + (b * v)

# Plain input
# a = input()
# b = input()
# then typecast to float
# d = (float(a) * u) + (float(b) * v)

p = np.dot(u, v)
print("vector au+bv", d)
print("dot product of u and v", p)
