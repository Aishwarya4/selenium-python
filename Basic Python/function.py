def sum(start,end):
    result = 0
    for i in range(start,end+1):
        result=result+i
    print(result)
sum(2,8)


def sum2(start,end):
    if start>end:
        print("start should be less than end")
        return
    result = 0
    for i in range(start,end+1):
        result=result+i
    print(result)
sum2(2,7)

#Global and local variable
global_var = 23
def var():
    local_var = 78
    print(local_var)
    print(global_var)

var()

#same global and local var using global kw
g = 1
def func():
    global g
    g = 12
    print(g)
func()

#passing arguments with default values/(positional)
def func(i,j=90):
    print(i,j)

func(10)
func(10,89)

#keyword argument
def named_args(name,greeting):
    print(greeting +" "+name)
named_args("Aishu","Hello") #positional arg
named_args(name="Aishu",greeting="Good Morning")#keyword arg
named_args(greeting="Good Morning",name="Aishu")


def abc(a,b,c):
    print(a,b,c)
abc(12,34,56) #positional
abc(12,b=34,c=56) #positional and kw arg
abc(12,c=56,b=34)
#abc(12,b=34,56) incorrect all positional arg must be st the starting