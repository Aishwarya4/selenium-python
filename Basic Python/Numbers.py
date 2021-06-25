import math
from filecmp import cmp

n1 = 10
n2 = 20.58

print(type(n1))
print(type(n2))

num = max(34,23,67,78,56,32,90)
print("Max Value",num)

num = min(34,23,67,78,56,32,90)
print("Min Value:",num)

n3 = -45
print("Absolute Value:",abs(n3))#The absolute value of x: the (positive) distance between x and zero.
print("math.fabs(-45.17) : ", math.fabs(-45.17))#This method returns absolute value of x
print("math.fabs(100.12) : ", math.fabs(100.12))
print("math.fabs(100.72) : ", math.fabs(100.72))
print("math.fabs(math.pi) : ", math.fabs(math.pi))

print("ceil value of 20.58:",math.ceil(n2))#The ceiling of x: the smallest integer not less than x

print("floor value of 20.58:",math.floor(n2))#he floor of x: the largest integer not greater than x

print("round value of 20.58:",round(n2))
#x rounded to n digits from the decimal point.
print("round value of 20.58:",round(n2,1))

s = 25
print("Square root of ",s,":", math.sqrt(s))

print("power of ",s,":",pow(s,3))



# use of cmp() method
# when a<b
a = 1
b = 2
print(cmp(a, b))

# when a = b
a = 2
b = 2
print(cmp(a, b))


# when a>b
# a = 30
# b = 28
# print(cmp(a, b))

