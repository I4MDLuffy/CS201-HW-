# Q-1
# it prints error
def displayPerson(*args):
    for i in args:
        print(i)
#displayPerson(name = "Emma", age="25")

# Q-2
# a function only executes when it is called and we can reuse it in a program

# Q-3
# it prints out "Emma 25"
def fun1(name, age=20):
    print(name, age)
fun1("Emma", 25)

# Q-4
#It prints keys for the newly created dictionary, according to **kwargs, which are "emp" and 'salary'
def display(**kwargs):
    for i in kwargs:
        print(i)
display(emp="Kelly", salary=9000)

# Q-5
# It prints 5
def outerFun(a,b):
    def innerFun(c,d):
        return c+d
    return a
result = outerFun(5,10)
print(result)

# Q-6
def fun1(name,age):
    print(name, age)
#These two work
fun1("Emma", age = 23)
fun1(age = 23, name = "Emma")

# Q-7
def fun1(*data):
    return data
print(fun1(25, 75, 55))
print(fun1(10, 20))

# Q-8
#True

# Q-9
def add (a,b):
    return a+5, b+5
result = add(3,2)
print(result)

# Q-10
#Does nothing because 'num' is a local variable
def fun1(num):
    return num +25
fun1(5)
#print(num)

# Q-11
# A function can take an unlimited number of arguments
#A python function can return multiple values

# Q-12
#Outputs 15
def outerFun(a,b):
    def innerFun(c,d):
        return c+d
    return innerFun(a,b)
res = outerFun(5, 10)
print(res)