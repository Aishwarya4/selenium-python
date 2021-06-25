#To import same name functions from two diffrent module
#Approach1
print("Approach1")
import animal_module
import bird_module

animal_module.fly()
animal_module.color()

bird_module.fly()
bird_module.color()

#Approach2
print("Approach2")
#In this approach the last imported module will get executed
from animal_module import *
fly()
color()
from bird_module import *
fly()
color()

