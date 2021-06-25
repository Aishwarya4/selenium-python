class myClass:
    # def values(self,val1,val2):
    #     print(val1)
    #     print(val2)
    #     self.val1=val1#to use local variable in other method make them as class variable
    #     self.val2=val2

    #or

    def __init__(self,val1,val2):
        print(val1)
        print(val2)
        self.val1=val1#to use local variable from constructor in other method make them as class variable
        self.val2=val2
    def add(self):
        print(self.val1+self.val2)

mc = myClass(23,56) #pass constructor values
#mc.values(12,34)
mc.add()


#To call current class method in another method
class myClass2:
    def m1(self):
        print("This is method m1")
        self.m2(34)
    def m2(self,a):
        print("This is method m2:",a)
ob = myClass2()
ob.m1()

#constructor with argument
class myClass3:
    name="Akshaya"
    def __init__(self,name):
        print(name)
        print(self.name)

ob = myClass3("Aishu")

class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print("Empid:{} Ename:{} Salary:{}".format(self.eid,self.ename,self.sal))

ob = Emp(12,"Aishu",3000)
ob.display()
