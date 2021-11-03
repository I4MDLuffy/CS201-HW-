#Lab 4
def SurfaceArea():
    try:
        x = int(input("What is the length of the room? "))
        y = int(input("What is the width of the room? "))
        z = int(input("What is the height of the room? "))
        xd = int(input("What is the width of the door? "))
        yd = int(input("What is the height of the door? "))
        SA = ((x * z) * 2) + ((y * z) * 2) - (xd * yd) + (x * y)
        return SA
    except:
        return "Input numbers you jackass!"
print(SurfaceArea())

#Lab 5
def QuadraticSolver():
    try:
        a = int(input("What is the term of the highest degree? "))
        b = int(input("What is the term of the middle degree? "))
        c = int(input("What is the term of the last degree? "))
        x1 = ((-1 * b) + (((b ** 2) - (4 * a * c)) ** (1 / 2))) / (2 * a)
        x2 = ((-1 * b) - (((b ** 2) - (4 * a * c)) ** (1 / 2))) / (2 * a)
        return x1, x2
    except:
        return "Input proper numbers you donkey!"
x, y = QuadraticSolver()
print("The first root is", x)
print("The second root is", y)

#Lab 6
def Digits():
    try:
        num = int(input("Which number do you want to know the digits of? "))
        digits = 0
        while num > 0:
            digits += 1
            num = num // 10
        return digits
    except:
        return "Input a number you monkey"
print (Digits())

#Lab 7
def Prime():
    try:
        num = int(input("Input a number "))
        if num  == 2:
            return "The number is prime"
        elif num > 1:
            for x in range(2, num):
                if num % x == 0:
                    return "The number is not prime"
                else:
                    return "The number is prime"
        else:
            return "the number is prime"
    except:
        return "Put in a real number you monkey fucker"
print(Prime())

#Lab 8
def Digits(num):
    digits = 0
    for x in range(len(str(num))):
        digits += 1
    return digits
print(Digits(int(input("What is a number? "))))

#Lab 9
num = int(input("Up to what number? "))
power = int(input("Up to what power? "))
def ExponentTable(num, power):
    table = []
    for x in range(num +1):
        for y in range(power + 1):
            table.append(x ** y)
        table.append("/")
    return table
print(ExponentTable(num, power))

#Lab 10
num = int(input("Pick a number: "))
def Bits(num):
    bits = list(bin(num))
    NBits = -2
    for x in bits:
        NBits += 1
    return NBits
print("The number of bits in", num, "is", Bits(num))
print(bin(num))

#Lab 11
def FibonacciSeq():
    length = int(input("How big should the sequence be? "))
    Fib = []
    newnum = 1
    oldnum = 0
    temp = 0
    for x in range(length):
        Fib.append(newnum)
        temp = newnum
        newnum = oldnum + newnum
        oldnum = temp
    return Fib
print(FibonacciSeq())

#Lab 12
def Occurences():
    string = input("Input the string to search within: ")
    char = input("Input the character to search for within the string: ")
    occurences = 0
    string = list(string)
    for x in string:
        if char in string:
            string.remove(char)
            occurences += 1
    return occurences
print(Occurences())

#Lab 13
def Palindrome():
    word = input("what word should be checked? ")
    word = word.lower()
    backwards = word[::-1]
    palindrome = False
    if word == backwards:
        palindrome = True
        return palindrome
    else:
        palindrome = False
        return palindrome
print(Palindrome())

#Lab 14
def ListReverse():
    listOS = ["swodniw", "xunil", "socam"]
    newlistOS = []
    for x in listOS:
        newlistOS.append(x[::-1])
    return newlistOS
print(ListReverse())

#Lab 15
def CreateList():
    print("Enter any number of strings to add, type '0' to end")
    x = input()
    strings = []
    while x != "0":
        strings.append(x)
        x = input()
    return strings
print(CreateList())

#Lab 16
