#Q1
count = 0
def Count(count):
    while count > 5:
        print(count, " is less than 5")
        count += 1
    else:
        print(count, " is not less than 5")
    return
Count(count)
#Q2
i = 1
def Break(i):
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1
    return
Break(i)
#Q3
i = 0
def Continue(i):
    while i < 6:
        i += 1
        if i == 3:
            continue
        print (i)
    return
Continue(i)
#Q4
num = int(input("Input a number "))
i = 2
tag = False
def Prime(num, i, tag):
    for j in range(i,num):
        if (num % j == 0):
            print (num, " is not prime")
            tag = True
        i += 1
    if(tag == False):
        print(num, " is prime")
    return
Prime(num, i, tag)
#Q5
i = 10
counter = 0
num = int(input("What is an integer number? "))
def Digits(num, i, counter):
    if num > 0:
        while num % i > 0 or num > 0:
            counter += 1
            num = num // 10
        print("The amount of digits are: ", counter)
    else: 
        print("You cannot put in 0")
    return
Digits(num, i, counter)
#Q6
fruits = ["apple", "banana", "cherry"]
def Fruits(fruits):
    for x in fruits:
        print (x)
    return
Fruits(fruits)
#Q7
num = int(input("What is an integer? "))
counter = "1"
def Factorial(num, counter):
    if num == 0:
        print ("Factorial is 1")
    elif num < 0:
        print ("Factorial of a negative number is not defined")
    else:
        for x in range(2, num +1):
            counter += " X "
            counter += str(x)
            #counter.append (x)
            #counter.append(" X ")

    print(counter)
    return
Factorial(num, counter)

