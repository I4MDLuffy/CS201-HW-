#Q 1.1
list1 = [1, 2, 3, "a", "b", "c"]
def InList(list):
    if "a" in list:
        print("It is in the list")
        print("a" in list)
    else:
        print("It is not in the list")
InList(list1)

#Q 1.2
name = ["Snowball", "Chewy", "Bubbles", "Gruff"]
animal = ["Cat", "Dog", "Fish", "Goat"]
age = [1, 2, 2, 6]
def MultipleListIt(name, animal, age):
    z = zip(name, animal, age)
    for name, animal, age in z:
        print("%s the %s is %s" % (name, animal, age))
MultipleListIt(name, animal, age)

#Q 1.3
# if either a list or a dictionary can be used then use a dictionary; because it is faster
# a list should be used of the order of the values matters or there are duplicate values that need to be kept
#such as in the case of id records
ids = [23, 1, 7, 9]
# or in the case of needing duplicate values
list1 = [5, 4, 5, 7, 4]
# each key of a dictionary has to be unique, it can also be other data types
dict = {(5, 4): 9, (6, 4, 3): 13}
# dict is well used for counting occurences of something
pets = {"Cats":1, "Dogs": 3, "Fish": 0}

#Q 1.4
# Lists are alterable (mutable)
x = [1]
print(id(x), ":", x)
x.append (5)
x.extend([6, 7])
print(id(x), ":", x)

#Q 1.5
#Different data types can be in the same list
a = [1, "a", 1.0, []]
print (a)

#Q 1.6
# the append function adds a value to the end of a list (if it adds another list is adds the list as a single element)
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])
print(a)
# To append a list to a list as individual values use the extend() function 
b = [1, 2, 3]
b.extend([5, 6])
print(b)

#Q 1.7
print(id(1))
print(id(2))
a = [1, 2, 3]
print(id(a))
print(id(a[0]))
print(id(a[1]))
# the list has separate memory location from the values

#Q 1.8
#the del keyword deletes a value of a list at a certain index
a = ["w", "x", "y", "z"]
print(a)
del a[1]
print(a)

#Q 1.9
# the remove() function removes a value of a list using the value (only removes the first iteration of the value if there are multiple)
a = ["a", "a", "b", "b", "c", "c"]
a.remove("b")
print(a)

#The pop() function removes a value of a list using the index (defaults to the last value in the list)
a = ["a", "a", "b", "b", "c", "c"]
a.pop(4)
print(a)

#Q 1.10
# You can remove duplicates in a list (and order numbers from ascending order) by converting to a set and back to a list
values = [3, 2, 2, 1, 1, 1]
print(list(set(values)))

#Q 1.11
# Use index() function to find the index of a value in a list (if there are multiple of the value only the lowest index one is called)
fruit = ["pear", "orange", "apple", "grapefruit", "apple", "pear"]
print(fruit.index("apple"))
print(fruit.index("pear"))

#Q 1.12
# use clear() function to remove all elements from a list
fruit = ["pear", "orange", "apple"]
print(fruit)
print(id(fruit))
fruit.clear()
#the clear function does not change the memory location at all
print(fruit)
print(id(fruit))
#del can be used by specifying from which points the list should be deleted

#Q 1.13
GroceryList = ["flour", "cheese", "carrots"]
for idx, val in enumerate(GroceryList):
    print("%s: %s" % (idx, val))

#Q 1.14
one = ["a", "b", "c"]
two = [1, 2, 3]
print(one + two)

#Q 1.15
li = [0, 25, 50, 100]
print([i + 1 for i in li])

#Q 1.16
pets = ['dog', 'cat', 'fish', 'fish', 'cat']
print(pets.count('fish'))

#Q 1.17
round1 = ['chuck norris', 'bruce lee', 'sonny chiba']
round2 = round1.copy()
round2.remove('sonny chiba')
print(round1)
print(round2)