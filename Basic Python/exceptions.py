#Exception is abnormal condition in code that distrub normal program flow

try:
    print(10/0)
    # print(10/5)
except TypeError:
    print("TypeError-Exception Handled successfully")
except ZeroDivisionError:
    print("ZeroDivisionError-Exception Handled successfully")
except SyntaxError:
    print("SyntaxError-Exception Handled successfully")
else: #no exception raised else will execute
    print("Entered into else block")
finally: #alway execute
    print("program completed")


def enterage(age):
    if age<0:
        raise ValueError
    if age%2==0:
        print("Age is even")
    else:
        print("Age is odd")
try:
    num=-6
    enterage(num)
except ValueError:
    print("Only positive integers are allowed")
except:
    print("Went something wrong")

try:
    number=one
    print("The number is",number)
except NameError as ne:
    print("Exception:",ne)