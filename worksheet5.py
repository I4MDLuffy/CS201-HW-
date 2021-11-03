#Q1
a = int(input("What is the first number? "))
b = int(input("What is the second number? "))
def Average (a,b):
    average = (a + b) / 2
    print(average)
    return 
Average (a,b)
#Q2
a = int(input("What is the first number? "))
b = int(input("What is the second number? "))
def MinMax (a,b):
    if (a > b):
        minimum = b
        maximum = a
    else: 
        minimum = a
        maximum = b
    print ("The minimum is: ", minimum)
    print ("The Maximum is: ", maximum)
    return 
MinMax (a,b)
#Q3
a = int(input("What is the first number? "))
b = int(input("What is the second number? "))
def PosNeg (a,b):
    if (a > 0):
        num1 = "Positive"
    else: 
        num1 = "Negative"
    if (b > 0):
        num2 = "Positive"
    else:
        num2 = "Negative"
    print("The first number is: ", num1)
    print("The second number is: ", num2)
    return
PosNeg (a,b)
#Q4
a = int(input("What is the first number? "))
b = int(input("What is the second number? "))
def EvenOdd (a,b):
    if (a % 2 == 0):
        num1 = "Even"
    else:
        num1 = "Odd"
    if (b % 2 == 0):
        num2 = "Even"
    else: 
        num2 = "Odd"
    print ("The first number is: ", num1)
    print ("The second number is:", num2)
    return
EvenOdd (a,b)
#Q5
a = str(input("What is your name? "))
def Name (a):
    Length = len(a)
    name = a.upper ()
    print("Your name is: ", name)
    print("The length of your name is: ", Length)
    return
Name (a)
#Q6
base1=10
base2=15
height=20
doorBase1=5
doorBase2=10
surfaceArea = (2 * (base1 * height)) + (2 * (base2 * height)) + (base1 * base2) - (doorBase1 * doorBase2)
print(surfaceArea)
#Q7
a = float(input("What is the digit of the first number? "))
b = float(input("What is the digit of the second number? "))
c = float(input("What is the digit of the third number? "))
def Quadratic (a,b,c):
    if ((b ** 2) - (4 * a * c))<0:
        print("There is no solution")
    else:
        xValue1 =((-1 * b) + (((b ** 2) - (4 * a * c)) ** (1 / 2))) / (2 * a)
        xValue2 = ((-1 * b) - (((b ** 2) - (4 * a * c)) ** (1 / 2))) / (2 * a)
        print(xValue1)
        print(xValue2)
    return
Quadratic (a,b,c)
