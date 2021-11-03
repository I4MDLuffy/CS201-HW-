import numpy
from numpy.lib.shape_base import column_stack
# Q1
SampleArray = numpy.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print(SampleArray[:,2])
#print(SampleArray)
#ThirdColumn = []
#for x in SampleArray:
 #   ThirdColumn.append(x[2])
#print("Printing array of items in the third column from all rows\n", ThirdColumn)

# Q2
SampleArray = numpy.array([[3, 6, 9, 12], [15, 18, 21, 24],[27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])
print("Printing input array\n", SampleArray)
print(SampleArray[::2,1::2])

# Q3
arrayOne = numpy.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = numpy.array([[15, 33, 24], [4, 7, 1]])
arrayThree = arrayOne[::,::] + arrayTwo[::,::]
print("Printing Input Array \naddition of two arrays is\n", arrayThree)
for num in numpy.nditer(arrayThree,op_flags = ["readwrite"]):
    num[...]=num*num
print("Result array after calculating the square root of all elements\n", arrayThree)

# Q4
SampleArray = numpy.arange(10,34).reshape((8,3))
print(SampleArray)
SampleArray = numpy.split(SampleArray,4)
print(SampleArray)

# Q5
# A
sampleArray = numpy.array([[34, 43, 73], [82, 22, 12],[53, 94, 66]])
print("output",sampleArray[:,sampleArray[1,:].argsort()])
# uses all arrays and sorts the individual array values in order 
# of ascending order of the specified array within
print("output",sampleArray[:,[2, 1, 0]])
print(sampleArray.argsort(-1))

# B
print("output",sampleArray[sampleArray[:, 1].argsort(), :])
# uses all arrays and sorts all arrays based on values in order 
# of ascending order of the specified array within

# Q6
sampleArray = numpy.array([[34, 43, 73], [82, 22, 12],[53, 94, 66]])
#Takes minimum value of each array within the array
print("Printing amin of Axis 1:",numpy.amin(sampleArray, axis = 1))
#Takes maximum value of each array within the array
print("Printing amax of Axis 0:",numpy.amax(sampleArray, axis = 0))

# Q7
sampleArray = numpy.array([[34, 43, 73], [82, 22, 12],[53, 94, 66]])
newColumn = numpy.array([[10, 10, 10]])
print(numpy.delete(sampleArray,1,1))
#deleting index 1 of sample array value
sampleArray = numpy.delete(sampleArray,1,1)
print(numpy.insert(sampleArray, 1, newColumn, 1))