from abc import ABC,abstractmethod

#ABC is predefined abstract class
class myClass(ABC):
    @abstractmethod
    def display(self):
        None

class myClass2(myClass):
    def display(self):
        print("This is abstract display method")

ob = myClass2()
ob.display()

class Animal(ABC):
    @abstractmethod
    def eat(self):
        None
class Tiger(Animal):
    def eat(self):
        print("Eat NON-VEG")
class COW(Animal):
    def eat(self):
        print("Eat VEG")

ob = Tiger()
ob.eat()

ob = COW()
ob.eat()


class X(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
class Y(X):
    def m1(self):
        print("This is m1 method")

class Z(Y):
    def m2(self):
        print("This is m2 method")

z=Z()
z.m1()
z.m2()

class Cal(ABC):
    def __init__(self,value):
        self.value=value
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass

class C(Cal):
    def add(self):
        print(self.value+100)
    def sub(self):
        print(self.value-10)

cobj=C(20)
cobj.add()
cobj.sub()