#Creating Lists
list1 = list()
print(list1)

list2 = list([1,2,3,4,5,6])
print(list2)

list3 = list(["Aishwaray","Amol","Akshu","Videhee"])
print(list3)

list4 = list( "Aishwarya")
print(list4)

#Accessing elements from list
l = ["Aishu","Akshu","Videhee","Amol"]
print(l[1])
print(l[0])

#List operations
l = [1,5,3,7,3]
print(len(l))
print(min(l))
print(max(l))
print(sum(l))
print(3 in l)
print(3 not in l)

#List Slicing
l = [1,5,3,7,3,9,10,23]
print(l[:4])
print(l[2:])
print(l[2:6])


#+ and * operators in list
l1 = [1,5,3,7]
l2 = [3,9,10,23]
print(l1+l2) #+ operator to join the list
print(l1*3)  #* operator to replicate list

#Traversing list
l = [1,5,3,7,3,9,10,23]
for i in l:
    print(i)
#List Methods
l1 = [1,5,3,7,3,9,5,10,23]
l1.append(90)
print(l1)

l2 = [34,12]
l1.extend(l2)
print(l1)

print(l1.count(5))
print(l1.index(7)) #return index value of list item

l1 = [1,5,3,7,3,9,5,10,23]
l1.insert(1,27)
print(l1)

l1 = [1,5,3,7,3,9,5,10,23]
print(l1.pop(3))
print(l1)

l1.remove(23)
print(l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)

#List Comprehension

list1 = [x for x in range(10)]
print(list1)

list1 = [x+1 for x in range(10)]
print(list1)

#even numbers
list1  = [x for x in range(10) if x%2==0]
print(list1)