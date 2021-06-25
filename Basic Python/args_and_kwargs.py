#*args=args is not keyword you can give any variable after *
#*args can pass any number of arguments to function

def sum(*args):
    s=0
    for i in args:
        s+=i
    print("Sum is:",s)

sum(10,45)
sum(78,90,53)
sum(54,78,23,12)


def arg_three(a,b,c):
    print(a,b,c)

args = [45,43,78]
arg_three(*args)


#**kwargs used to give key value argument

def kwarg_three(a,b,c):
    print(a,b,c)

a = {'a':"one",'b':"two",'c':"three"}
kwarg_three(**a)

def myfunc(**kargs):
    for i,j in kargs.items():
        print(i,j)
myfunc(name="Aishwarya",age=21,Class="Msc")
