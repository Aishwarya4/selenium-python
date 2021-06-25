#Single level inheritance
# class A: #parent class
#     a=23
#     b=56
#     def m1(self):
#         print(self.a+self.b)
#         print("This is m1 method from A class")
#
# class B(A): #child class inherited parent class
#     c=23
#     d=34
#     def m2(self):
#         print(self.c + self.d)
#         print("This is m2 method from B class")
# aobj1 = A()
# aobj1.m1()
#
# bobj1 =B()
# bobj1.m1()
# bobj1.m2()

#Single level inheritance
# class A: #parent class
#     a=23
#     b=56
#     def m1(self):
#         print(self.a+self.b)
#         print("This is m1 method from A class")
#
# class B(A): #child class inherited parent class
#     c=23
#     d=34
#     def m2(self):
#         print(self.c + self.d)
#         print("This is m2 method from B class")
#
# class C(B):  # child class inherited parent class
#     x = 25
#     y = 30
#
#     def m3(self):
#         print(self.x + self.y)
#         print("This is m3 method from C class")
#
# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

#Hierarchical level inheritance
# class A: #parent class
#     a=23
#     b=56
#     def m1(self):
#         print(self.a+self.b)
#         print("This is m1 method from A class")
#
# class B(A): #child class inherited parent class
#     c=23
#     d=34
#     def m2(self):
#         print(self.c + self.d)
#         print("This is m2 method from B class")
#
# class C(A):  # child class inherited parent class
#     x = 25
#     y = 30
#
#     def m3(self):
#         print(self.x + self.y)
#         print("This is m3 method from C class")
#
# bobj = B()
# bobj.m1()
# bobj.m2()
#
# cobj = C()
# cobj.m1()
# cobj.m3()

#Multiple level inheritance
class A: #parent class
    a=23
    b=56
    def m1(self):
        print(self.a+self.b)
        print("This is m1 method from A class")

class B: #child class inherited parent class
    c=23
    d=34
    def m2(self):
        print(self.c + self.d)
        print("This is m2 method from B class")

class C(A,B):  # child class inherited parent class
    x = 25
    y = 30

    def m3(self):
        print(self.x + self.y)
        print("This is m3 method from C class")

cobj = C()
cobj.m1()
cobj.m2()
cobj.m3()
