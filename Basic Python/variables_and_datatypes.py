
#Redeclare the varibles

a = 23
print(a)

a = 20
print(a)

#Deleting varibles

var_a = 29
print(var_a)

del var_a
#print(var_a) #Will show Nameerror
#To print different varibles having different datatypes

var_int = 10
var_float = 3.6
var_string = "Aishu"
var_string2 = 'Aishwarya'
var_bool = True

print(var_int)
print(var_float)
print(var_string)
print(var_string2)
print(var_bool)


#Assigen multiple values to multiple varibles

a, b, c = 10, 20.8, "Aishu"
print(a, b, c)

#Assign same value to multiple varibles

a = b = c = 104
print(a, b, c)

# Swap to values

x = 10
y = 20
print("Value of x and y:", x, y)

x,y=y,x
print("Value afer swapping",x,y)


#Datatypes

x = 20 #int type
y = 10.9  #float type
s = "Welcome Aishu"
b = False

print(type(x), type(y), type(s), type(b))

#Concatenation
#Concatenation works on varibles having same types otherwise it will show the Typeerror
print(6 + 5)
print(34.8 + 3.9)
print(10 + 20.7)
print("Aishwarya" + "Parab")
print(True + True)
print(True + 6)

