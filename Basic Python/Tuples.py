t1 = ()
t2 = (1,2,3,4,5)
t3 = ([6,4,2,7,8])
t4 = tuple("Aishwarya")
print(t1)
print(t2)
print(t3)
print(t4)

print(len(t2))
print(max(t2))
print(min(t2))
print(sum(t2))

#iterate tuple
t2 = (1,2,3,4,5)
for i in t2:
    print(i,end=" ")
print("\n")
#Slicing in tuple
t = (1,2,3,4,5,6,7,8,9)
print(t[:5])
print(t[1:])
print(t[4:7])

#in and not in operator
print(21 in t)
print(2 in t)
print(3 not in t)

