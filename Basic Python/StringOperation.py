name1 = "Aishu"
name2 = 'Parab'
print(name1)
print(name2)

#String are immutable(cann't be modified)
str1 = "Aishwarya"
str2 = "Parab"
print(id(str1),id(str2))  #id-to get memeory address
print(str1+" Welcome")
print(id(str1))
print(id(str2))


#+ and * operation on string
str = "Aishwarya"
print(str+" "+"Parab")
print(str*3)

#Slicing in String

str = "Aishwarya Parab"
print(str[:9])
print(str[10:])
print(str[1:5])
print(str[2:-1])

print(ord("G")) #return ASCII Value of Character
print(chr(90))  #return ASCII character for value

print(len("Aishwarya")) #return length of the string
print(max("Aishu"))   #return the character having maximum ASCII value
print(min("Aishu"))  #return the character having minimum ASCII value

# in and not in opeators to check existance of string in another string
str = "Aishwarya Parab"
print("Parab" in str)
print("Aishu" in str)

print("Aishwarya" not in str)
print("Aishu" not in str)

#String comparision
#python compares string lexicographically. i.e Using ASCII value
print("Aishu" == "Aishu")
print("Aishwarya" != "Aishu")
print("Videhee" >= "Jyoti")
print("Amol" <= "Anmol")
print("free" > "freedom")
print("apple" < "pineapple")
print("Aishu" > "")

#iterating string
str = "Aishwarya"
for i in str:
    print(i)

#Testing String

str = "Welcome to python"
print(str.isalnum())
print(str.islower())
print(str.isupper())
print(" ".isspace())
print("2012".isdigit())
print("first number".isidentifier())

#Searching substring
str = "Welcome to python"
print(str.startswith("Welcome"))
print(str.endswith("thon"))
print(str.find("e"))
print(str.rfind("o"))
print(str.count("e"))

#Converting string
str = "String in python"
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.swapcase())
print(str.replace("python","java"))