#taking input without typecasting
#It will consider the input as a string
'''num1 = input("Enter First Number:")
num2 = input("Enter Second Number:")
print(num1 + num2)


#With typecasting
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
print(num1 + num2)

#TypeCast at the time of printing value
a = input("Enter First Number:")
b = input("Enter Second Number:")
print(int(a) + int(b))

#Input Float Values
num1 = float(input("Enter First Decimal Number"))
num2 = float(input("Enter Second Decimal Number:"))
print(num1 + num2)


#Adding values having two different datatypes
num1 = input("Enter Integer Number:")
num2 = input("Enter Decimal Number:")
print(int(num1) + float(num2))
'''
#integer can be stored as decimal but decimal cann't be stored as integer
num1 = input("Enter Integer Number:")
num2 = input("Enter Decimal Number:")
print(float(num1) + float(num2))