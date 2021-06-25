class Myclass:
    def myfunc(self):#self keyword tells that this method belongs to the Myclass
        pass
    def display(self,name):
        print("Name is:",name)
mc = Myclass()
mc.myfunc()
mc.display("Aishwarya")


#Creating instance method and static method
class Myclass2:
    def m1(self):
        print("This is instance method")

    @staticmethod   #use this keyword
    def m2():       #don't need to give self
        print("This is static method")
    @staticmethod
    def m3(self):
        print("static method with self--here self is consider as argument")

    @staticmethod
    def m4(self):
        print(self)
mc = Myclass2()
mc.m1()
#Static method don't need to create object
Myclass2.m2()
Myclass2.m3("none")
Myclass2.m4(2021)

class ArithmaticOperation:
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter second number:"))
    def add(self):
        print("Addition:",self.n1+self.n2)
    def sub(self):
        print("Subtraction:",self.n1-self.n2)
    def mul(self):
        print("Multiplication:",self.n1*self.n2)
    def div(self):
        print("Division:",self.n1/self.n2)
AO = ArithmaticOperation()
AO.add()
AO.sub()
AO.mul()
AO.div()

#Creating Global ,Local and class varibles
a,b = 10,34     #global varibles
class Myclass3:
    n1,n2 = 34,56
    def add(self,x,y):  #local varibles
        print(x+y) #accessing local varible
        print(a+b)  #accessing global varible
        print(self.n1+self.n2) #accessing class varible
mc = Myclass3()
mc.add(123,45)

#Creating same Global ,Local and class varibles
a,b = 10,34     #global varibles
class Myclass4:
    a,b = 34,56
    def add(self,a,b):  #local varibles
        print(a+b) #accessing local varible
        print(globals()['a']+globals()['b'])  #accessing global varible
        print(self.a+self.b) #accessing class varible
mc = Myclass4()
mc.add(123,45)

#creating multiple objects for same class
class Myclass5:
    def myfun(self):
        print("Good Morning")
    def myfun2(self):
        pass
obj1 = Myclass5()
obj1.myfun()

obj2 = Myclass5()#Named object
obj2.myfun()

Myclass5().myfun()#Nameless object

#Check memory location of objects
ob1=Myclass5()
ob2=Myclass5()
ob3=ob1
print(id(ob1))
print(id(ob2))
print(id(ob3))

print(ob1 is ob2)
print(ob1 is ob3)

print(ob1 is not ob2)
print(ob1 is not ob3)