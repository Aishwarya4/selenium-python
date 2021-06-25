friends ={'Aishu':'2344','Akshu':'567','Amol':'890','Videhee':'789'}
print(friends)

#Retrieving elements
print(friends['Aishu'])

#Adding element
friends['Jyoti']='906'
print(friends)

#Modifying element
friends['Amol']='7543'
print(friends)

#Deleting element
del friends['Akshu']
print(friends)

#iterating items in dictionary
friends ={'Aishu':'2344','Akshu':'567','Amol':'890','Videhee':'789'}
for i in friends:
    print(i,":",friends[i])

print(friends)
print(len(friends))

#Equality test in dictionary
d1 = {'Aishu':'789','Videhee':'907'}
d2 = {'Videhhe':'765','Aishu':'789'}

print(d1==d2)
print(d1!=d2)

#In Dictionary order of elements not matters
d1 = {'Aishu':'789','Videhee':'765'}
d2 = {'Videhee':'765','Aishu':'789'}
print(d1==d2)

#Return Keys
friends ={'Aishu':'2344','Akshu':'567','Amol':'890','Videhee':'789'}
print(friends.keys())

#Return Values
print(friends.values())

#Return value of key
print(friends.get('Videhee'))
print(friends.get('Akshu'))

#Remove item
print(friends.pop('Aishu'))
print(friends)

#pop item randomly and remove from dicttionary
print(friends.popitem())
print(friends)

#Remove all elements
friends.clear()
print(friends)

