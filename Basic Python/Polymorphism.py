#Override=Same method name doing diffrent task
#Overriding a variable
class Parent:
    name = "Aishwarya"
class Child(Parent):
    #name = "Damini"
    pass
ob = Child()
print(ob.name)

#Overriding a method
class Bank:
    def rateofinterest(self):
        return 0
class SBI(Bank):
    def rateofinterest(self):  #when this method is not available it will call parent method
        # return 23.8
        pass
ob1 =SBI()
print(ob1.rateofinterest())
ob2=Bank()
print(ob2.rateofinterest())

#Overloading=single method or function with with diffrent numbers parameters

class Name:
    def sayHello(self,name=None):
        if name is not None:
            print("Hello "+name)
        else:
            print("Hello")

obj = Name()
obj.sayHello()
obj.sayHello("Aishwarya")

class Birds:
    def fly(self,name=None):
        if name=="parrot":
            print("can fly")
        if name=="peguine":
            print("cannot fly")
        if name is None:
            print("no input")
obj=Birds()
obj.fly("parrot")
obj.fly("peguine")
obj.fly()

