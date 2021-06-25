#using super keyword invoke parent variables, methods and constructor
#Accessing parent class method
# class A:
#     def m1(self):
#         print("This is m1 method from A class")
# class B(A):
#     def m2(self):
#         print("This is m2 method from B class")
#         super().m1() #calling parent class method
# b = B()
# b.m2()

#Accessing parent class variables
# a,b=56,96 #global variables
# class A:
#     a,b=34,21
#
# class B(A):
#     a, b = 84, 26
#     def m(self,a,b):
#         print(a+b) #local var
#         print(self.a+self.b) #class B var
#         print(super().a+super().b) #class A var
#         print(globals()['a']+globals()['b']) #global var
#
# bobj =B()
# bobj.m(56,78)


#to invoke parent class constructor
class A:
    def __init__(self):
        print("This is class A constructor")

class B(A):
    #pass #if child class didn't contain any constructor it will invoke parent class constructor
    def __init__(self):
        print("This is class B constructor")
        super().__init__() #invoke parent class constructor
        A.__init__(self)  #Approach2


bobj = B()
