#private variables only can be accessible within method
class myClass:
    __a=12  #use double uderscrore to declare private method
    b=34  #public variable
    def disp(self):
        print(self.__a)

ob=myClass()
ob.disp()

print(myClass.b) #public variable can be accessible outside class
# print(myClass.__a)#cannot be accessible outside the class

#private method can be access only within method of class
class myclass2:
    def __disp1(self): #private method
        print("This is disp1 method")
    def disp2(self):
        print("This is disp2 method")
        self.__disp1()#to access private method in another method
ob=myclass2()
ob.disp2()

#we can access private variable outside the class indirectly using method

class myClass4:
    __empid=101
    def getempid(self,eid):
       self.__empid=eid

    def dispempid(self):
        print(self.__empid)

ob=myClass4()
ob.getempid(102)
ob.dispempid()

