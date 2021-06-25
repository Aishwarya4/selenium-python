#packages contains diiffrent modules
from pack1 import module1,module2
from pack1.pack3 import module3
#Approach1
module1.display()
print("Sum :",module1.sum(34,67))
print("Average:",module1.average(23,56))
print("Power :",module1.power(3,3))
module2.show()
module3.show()


from EmpPackage.emp import Employee
e = Employee(101,'Aishwarya',200000)
e.displayemp()

from StudentPackage.stud import Student
s = Student(1,'Damini','A')
s.displaystud()
