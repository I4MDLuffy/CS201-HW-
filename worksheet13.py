#Q 1
dec = 334
def Conversion(dec):
    print("The decimal of", dec, "is:")
    print(bin(dec), "in binary.")
    print(oct(dec), "in octal.")
    print(hex(dec), "in hexadecimal.")
Conversion(dec)

num1 = "0b100"
num2 = "0b110"
mysum = int(num1, 2) + int(num2, 2)
print(bin(mysum))

num1 = 0b100
num2 = 0b110
mysum = num1 + num2
print(bin(mysum))

hnum1 = "0x10"
hnum2 = "0x10"
myhsum = int(hnum1, 16) + int(hnum2, 16)
print(hnum1)
print(myhsum)
print(hex(myhsum))

hnum1 = 0x10
hnum2 = 0x10
myhsum = hnum1 + hnum2
print(hnum1)
print(myhsum)
print(hex(myhsum))

onum1 = "0o10"
onum2 = "0o10"
myosum = int(onum1, 8) + int(onum2, 8)
print(onum1)
print(myosum)
print(oct(myosum))

onum1 = 0o10
onum2 = 0o10
myosum = onum1 + onum2
print(onum1)
print(myosum)
print(oct(myosum))

#Q 2
str1 = "Hire the top \n1% freelance developers"
print(str1)
str1 = '''Hire the top
1% freelance developers'''
print(str1)

#Q 3
DataString = "0\t12\t24"
print(DataString)
print("It\'s raining")
print("'\\' is the backslash")
print("\"hello\"")

#Q 4
txt = "Welcome to the jungle"
x = txt.split()
print(x)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#", 1)
print(x)

s = "foobar"
print(list(s))
#OR
print([c for c in "foobar"])

#Q 5
f = open("demofile2.txt", "a")
#"a" adds to the end of the file
f.write("Now the file has more Content!")
f.close()

f = open("demofile2.txt", "r")
#"r" reads exactly what code is in the file (not what the code does)

print(f.read())

f = open("demofile3.txt", "w")
#"w" Overwrites all code within the file
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt", "r")
print(f.read())

#Q 6
f = open("Myfile.txt","x")
f = open("Myfile1.txt","w")

fhandle = open("examp.txt","w")
fhandle.write("This is a write example")
fhandle.write("Text will be sequentially written tuntil a newline control character occurs. \n")
fhandle.write("then a new line will begin with \n")
fhandle.write("and another new line, etc \n")
fhandle.close()

#Q 7
fruits = ["orange", "apple", "pear", "banana", "kiwi","apple", "banana"]
print(fruits.count("apple"))
print(fruits.count("tangerine"))
print(fruits.index("banana"))
print(fruits.index("banana", 4))
print(fruits.reverse())
print(fruits)
fruits.append("grape")
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)