units = int(input("What is your electricity unit charges? "))
cost = 0
def ElectricityBill (units, cost):
    if units >= 0 and units <= 50:
        cost = units * 0.5
    elif units > 50 and units <=150:
        cost = ((units - 50) * 0.75) + 25
    elif units > 150 and units <= 250:
        cost = ((units - 150) * 1.2) + 100
    elif units > 250:
        cost = ((units - 250) * 1.5) + 220
    else:
        print("Error \nLike What the FUCK bro?!?!")
    cost *= 1.2
    print("Your cost is $", cost)
    return
ElectricityBill(units, cost)







#assigning variable
num = int(input("Give me a number "))
#Creating function for equation
def EvenOdd (num):
    #if statement to check if number is odd, even, or not a number
    if num % 2 == 1:
        print("This number is odd!")
    elif num % 2 == 0:
        print("This number is even!")
    else:
        print("You did not input a number")
    return
#Calling the function
EvenOdd(num)


#discount rate exercise
items = int(input("How many items do you have?"))
def Discount(items):
    if items >= 0 and items <= 10:
        print("You get no discount \nPlease buy more items!")
    elif items > 10 and items <= 24:
        print("Your discount is 10%")
    elif items > 24 and items <= 50:
        print("Your discount rate is 15%")
    elif items > 50:
        print("Your discount is 20%!")
    else:
        print("That is not a valid response \nFuck off")
    return
Discount(items)

#Largest of three number Exercise
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
num3 = int(input("What is the third number? "))
def Largest(num1, num2, num3):
    if num1 > num2 and num1 > num2:
        print("The largest number is ", num1)
    elif num2 > num1 and num2 > num3:
        print("The largest number is ", num2)
    elif num3 > num1 and num3 > num2:
        print("The largest number is ", num3)
    else:
        print("Invalid input")