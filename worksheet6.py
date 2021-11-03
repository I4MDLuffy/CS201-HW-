#Q1
age = int(input("How old are you? "))
isGraduated = input("Are you graduated? (true or false)")
def moreThan18 (age, isGraduated):
    if age >= 18:
        print("You're 18 or older. Welcome to adulthood!")
        if isGraduated == "true":
            print("Congratulations with your graduation!")
        else:
            print("Unfortunately you did not graduate.")
    else:
        print("You're younger than 18!")
    return 
moreThan18(age, isGraduated)
#Q2
var = int(input("Input a number "))
def Value (var):
    if var < 200:
        print("Value is less than 200")
        if var == 150:
            print("Which is 150")
        elif var == 100:
            print("Which is 100")
        elif var == 50:
            print("Which is 50")
        elif var < 50:
            print("Value is less than 50")
        else:
            print("Could not find true expression")
        print("Good bye!")
    return
Value (var)
#Q3
list1 = ["Physics", "Chemistry", 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
#Q4
list1 = ["Physics", "Chemistry", 1997, 2000]
list2 = [1, 2, 3, 4, 5]
print ("List1 [0]: ", list1 [0])
print ("list2 [1:5]: ", list2 [1:5])
#Q5
list = ["Physics", "Chemistry", 1997, 2000]
print("Value available at index 2: ")
print(list [2])
list[2] = 2001
print("New value available at index 2: ")
print(list[2])
#Q6
list1 = ["Physics", "Chemistry", 1997, 2000]
print (list1)
del list1 [2]
print("After deleting value at index 2: ")
print (list1)
#Q7
i = 1
while i < 6:
    print(i)
    i += 1
#Q8
x = range(6)
for n in x:
    print(n)

