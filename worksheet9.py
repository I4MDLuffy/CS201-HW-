#Q1-1
list1d = []
N = int(input("How long should the list be? \n"))
def List1D(list1d, N):
    for i in range(N):
        list1d.append (0)
    print(list1d)
    return
List1D(list1d, N)

#Q1-2
list2d = []

w = int(input("How long should the first dimension list be? \n"))
l = int(input("How long should the second dimension list be? \n"))
def List2D(list2d, w, l):  
    x=1  
    for i in range(w):
        list1d=[]
        
        for j in range (l):
            list1d.append(1)
        list2d.append(list1d)  
        
    print(list2d)
    return
List2D(list2d, w, l)

#Q1-3
def Change(list1d):
    list1d.pop (0)
    list1d.insert (0,5)
    print(list1d)
    return
Change(list1d)

#Q1-4
def Change2(list1d):
    list2d.pop (0)
    list2d.insert (1,5)
    print(list1d)
    return
Change2(list2d)

#Q1-5
def NewElement(list1d):
    list1d.append(15)
    print(list1d)
    return
NewElement(list1d)

#Q1-6
list2d = [1, 2, 3, 4, 5]
def RemoveElement(list2d):
    list2d.pop()
    print(list2d)
    return
RemoveElement(list2d)

#Q1-7
list1d = [1, 2, 3, 4, 5]
def Insert(list1d):
    list1d.insert(3,9)
    print(list1d)
    return
Insert(list1d)

#Q1-8
list1d = [1, 2, 3, 4, 5]
def PrintList(list1d):
    for i in range(len(list1d)):
        print(list1d[i])
    return
PrintList(list1d)

#Q1-9
list1d = [1, 2, 3, 4, 5]
list2d = [[5, 4, 3, 2, 1],[5, 4, 3, 2, 1]]
combinedList = []
def Combine(list1d, list2d, combinedList):
    combinedList.append(list1d)
    combinedList.append(list2d)
    print(combinedList)
    return
Combine(list1d, list2d, combinedList)

#Q2-1
# A list is created using [] and is capable of being altered after being created
# A tuple is created using () and is NOT capable of being altered after being created
# They can be referenced in the same ways

#Q2-2
aTuple = (10, 20, 30, 40, 50)
bTuple = type(tuple)
def Reverse(aTuple):
    bTuple = aTuple[ : :-1]
    print (bTuple)
    return
Reverse(aTuple)

#Q2-3
aTuple = (10, 20, 30, 40)
def Unpack(aTuple):
    print(*aTuple)
    return
Unpack(aTuple)
# or
aTuple = (10, 20, 30, 40)
def Unpack2(aTuple):
    aTuple1 = aTuple[0]
    aTuple2 = aTuple[1]
    aTuple3 = aTuple[2]
    aTuple4 = aTuple[3]
    print (aTuple1, aTuple2, aTuple3, aTuple4)
    return
Unpack2(aTuple)

#Q2-4
aTuple = (10, 20, 30, 40, 50)
def First2Elements(aTuple):
    for i in range(0,2):
        print(aTuple[i])
    return
First2Elements(aTuple)

#Q2-5
aTuple = (10, 20, 30, 40, 50)
def Add(aTuple):
    aTuple1 = (*aTuple, 50, 60)
    print(aTuple1)
    return
Add(aTuple)
# You Can Not Change the Variables in a Tuple so I had to create a new tuple

#Q2-6
tuple1 = (11, 22)
tuple2 = (99, 88)
def Swap(tuple1, tuple2):
    tuple12 = tuple2
    tuple21 = tuple1
    print(tuple12, tuple21)
    return
Swap(tuple1, tuple2)
# You Can Not Change the Variables in a Tuple so I had to create a new tuple

#Q2-7
tuple1 = (11,[22,33], 44, 55)
def Modify(tuple1):
    temp = list(tuple1)
    temp[1] = [222, 33]
    tuple1 = tuple(temp)
    print ("tuple1 :", tuple1)
    return
Modify(tuple1)

#Q2-8
tuple1 = (50, 10, 60, 70, 50)
counter = 0
occurances = 0
def Count(tuple1, counter, occurances):
    for i in tuple1:
        if tuple1[counter] == 50:
            occurances += 1
        counter +=1
    print ("There are ", occurances, "occurances of 50 in the tuple")
    return
Count(tuple1, counter, occurances)

#Q2-9
tuple1 = (45, 45, 45, 45)
counter = 0
repeats = 0
def Same(tuple1, repeats, counter):
    for i in tuple1:
        
        if tuple1[counter] == 45:
            repeats += 1
        counter +=1
    if repeats == len(tuple1):
        print("All Items in the Tuple are the same")
    else:
        print("The items in the tuple are not all the same")
    return
Same(tuple1, repeats, counter)

#Q3-1
dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
def DictGet(dict1, temp):
    print(temp)
    return
DictGet(dict1, temp)
#the output is "None"

#Q3-2
student = {
    "name":"Emma",
    "class": 9,
    "marks": 75
    }
def DictDel(student):
    del student["marks"]
    print("marks" in student)
    return
DictDel(student)

#Q3-3
sampleDict = dict([
    ("first", 1), 
    ("second", 2), 
    ("third", 3)
    ])
print (sampleDict)

#Q3-4
dict1 = {"key1":1, "key2": 2}
dict2 = {"key1":2, "key2":1}
print (dict1 == dict2)

#Q3-5

student = {
    "name": "Emma",
    "class": 9,
    "marks": 75
}
def DeleteDict(student):
    
    #student.clear()

    #student["name"] = None
    #student["class"] = None
    #student["marks"] = None
    for i in student.keys():
        student[i]=None
    print(student)
    return
DeleteDict(student)

#Q4-1
import numpy
array = [
    [64392, 31655],
    [32579, 0],
    [49248, 462],
    [0, 0]
]
array1=numpy.array(array)
print("Printing Array\n ", array1, "\n Printing NumPy array Attributes\n Array Shape is: ", array1.shape, "\n Array Dimensions are ", array1.ndim, "\n Length of each element of array in Bytes is: ", array1.itemsize)

#Q4-2
array = numpy.arange(100, 200, 10)
Newarray = array.reshape(5, 2)
print(Newarray)