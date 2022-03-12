def gcd_fun(a, b):
    if b != 0:
        return gcd_fun(b, a % b)
    else:
        return a


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
num = gcd_fun(x, y)
print("GCD of two number is: ")
print(num)
