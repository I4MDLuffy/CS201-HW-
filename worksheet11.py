#Q 1
s = "yes"
def ShutDown(s):
    if s == "yes":
        print("Shutting Down")
    elif s == "no":
        print("Shutdown Aborted")
    else:
        print("Sorry")
ShutDown(s)

#Q 2
import math
def SquareRoot(x):
    y = math.sqrt(x)
    print(y)
SquareRoot(int(input("Input a number: ")))

#Q 3
num = input("Pick a number for its absolute value ")
def DistanceFromZero(x):
    try: 
        if float(x) % 1 == 0:
            x = int(x)
            absolute = abs(int(x))
            return absolute
        elif float(x) % 1 != 0:
            absolute = abs(float(x))
            return absolute
        else:
            return
    except ValueError:
        print("Nope")
        
print("The absolute value of the input is: ", DistanceFromZero(num))

#Q 4.1
nights = int(input("How many nights? "))
def HotelCost(nights):
    cost = 140 * nights
    return cost
print("The cost is", HotelCost(nights))

#Q 4.2
city = input("What city? ")
def PlaneRideCost(city):
    dict = {"Charlotte" : 183, "Tampa" : 220, "Pittsburgh" : 222, "Los Angeles" : 475}
    cost = dict.get(city)
    return cost
print("The cost of the plane ride is", PlaneRideCost(city))

days = int(input("How many days will you have the car? "))
def RentalCarCost(days):
    if days >= 7:
        cost = (days * 40) - 50
    elif days >= 3 and days < 7:
        cost = (days * 40) - 20
    else:
        cost = days * 40
    return cost
RentalCarCost(days)
print("The cost to rent the car is", RentalCarCost(days))

city = input("What city are you going to? ")
days = int(input("How many days are you leaving for? "))
def TripCost(city, days):
    cost1 = RentalCarCost(days)
    cost2 = PlaneRideCost(city)
    cost3 = HotelCost(days)
    sum = cost1 + cost2 + cost3
    return sum

#Q 4.3
spendingMoney = int(input("How much spending money?"))
def TripCost(city, days, spendingMoney):
    cost1 = RentalCarCost(days)
    cost2 = PlaneRideCost(city)
    cost3 = HotelCost(days)
    sum = cost1 + cost2 + cost3 + spendingMoney
    return sum

#Q 5.1 -5.2
number = int(input("Give a number to be cubed"))
def Cube(number):
    cube = number ** 3
    return cube
print("The cube of this number is", Cube(number))

#Q 5.3
def ByThree(number):
    if number % 3 == 0:
        result = Cube(number)
        return result
    else:
        return False
print(ByThree(number))