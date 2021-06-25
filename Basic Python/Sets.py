#set can have diffrent datatypes value
#set cannot have duplicate value

myset = {12,34,65,89,23}
print(myset)
myset2 = {45,67,12,"aishu",45.67}
print(myset2)

myset.add(123)
print(myset)

myset.pop() #remove random value
print(myset)

myset.remove(89) #remove specific value
print(myset)

myset.discard(890) #remove specific value but if value is not present it will print the set as it is
print(myset)

myset3 = {2,45,"Aishu",12,89.9}
print(myset3)
print(len(myset3))
myset4 = myset3.copy()
myset3.clear()
print(myset3)
print(myset4)

set1 = set([12,34,"aishu",12.9]) #list in set
print(set1)

set2 = set((12,45,"asd",87.9)) #tuple in set
print(set2)