#Q 1
def greet(name):
    '''
    This function greets to
    the person passed in as
    a parameter'''
    print("Hello,", name + ". Good morning!")
greet('Paul')
print(greet.__doc__)

def ShowEmployee(name, salary = 9000):
    print("Name:", name, "salary:", salary)
ShowEmployee("Ben", 12000)
ShowEmployee("Jessa")

#Q 1.1
def AbsoluteValue(num):
    if num >= 0:
        return num
    else:
        return -num
print(AbsoluteValue(2))
print(AbsoluteValue(-4))

def Calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
res = Calculation(40, 10)
print(res)

def OuterFunc(a, b):
    square = a ** 2
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5
result = OuterFunc(5, 10)
print (result)

#Q 1.2
def Max(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    elif y > z:
        return y
    else: 
        return z
max = Max(2, 5, 7)
print(max, "is the largest number")

#Q 1.3
list = [8, 2, 3, -1, 7]
def MultiplyList(x):
    sum = 1
    counter = 0
    for i in x:
        sum *= x[counter]
        counter += 1
    return sum
sum = MultiplyList(list)
print(sum)

#Q 1.4
#This is the same question as 1.3

#Q 1.5
list = [1, 2, 3, 3, 3, 3, 4, 5]
def Unique(x):
    newlist = []
  
    for i in x:
        if i in newlist:
            None

        else:
            newlist.append(i)
            print(i)
    return newlist
print(Unique(list))
