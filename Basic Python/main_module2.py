#Approach1
import a
import b

obj = a.Animal()
obj.display()
obj2 = b.Bird()
obj2.diplay()


#Approach2

from a import Animal
from b import Bird

ob1 = Animal()
ob1.display()

ob2 = Bird()
ob2.diplay()

import m
# dir to count number classes in module
print(dir(m))


