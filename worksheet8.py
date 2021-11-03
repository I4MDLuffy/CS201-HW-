#Q1
numberSets = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
print(numberSets[1])
print(numberSets[0][1])

numberSets =  [[[1, 2, 3, 4], [5, 6, 7, 8,], [9, 10, 11, 12]],
[[13, 14, 15, 16] , [17 , 18 , 19 , 20],
[21, 22, 23, 24]], [[25, 26, 27, 28],
[29, 30, 31, 32], [33, 34, 35, 36]]]
print(numberSets[0][1][2])

listData = [89, 56, 90, 34, 89, 12]
print(listData)
listData.insert(2,23)
print("The list elements are: ", listData)
for i in range(0, len(listData)):
    print(listData[i])

listData = ["Dell", "HP", "Lenovo", "ASUS"]
print(listData)
listData.append ("Toshiba")
print ("The list elements are", listData)
for i in range(0, len(listData)):
    print(listData[i])

list1 = ["html", "CSS", "JavaScript", "JQuery"]
list2 = ["PHP", "Laravel", "CodeIgniter"]
print (list1)
list1.extend(list2)
print ("The list elements are: ", list1)
for i in range(0, len(list1)):
    print(list1[i])

list = ["Cake", "Pizza", "Juice", "Pasta", "Burger"]
print("List before delete\n", list)
list.remove("Juice")
print("List after delete\n", list)

#Q2
fileDirectories = ("/home/user/Pictures", "var/www/siteroot/uploads", "/var/www/siteroot/staticfiles")
randomJunk = ("Bacon", 7, True, 11, "Your mother was a hamster!")
print(randomJunk)
print(type(randomJunk))
print(fileDirectories)

randomJunk = ("Bacon", 7, True, 11, "Your mother was a hamster!")
print(randomJunk[2])
print(randomJunk[:2])
tAdd = (1,2) + randomJunk
print(tAdd)

#Q3 !pip install numpy
import numpy
a = [0, 0, 1, 4, 7, 16, 31, 64, 127]
b = numpy.array(a)
print(b)
print(type(b))

a = numpy.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)
b = numpy.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
print(b[0,0], b[0,1], b[1,0])

#Q4
distroInstallCommand = {"Debian": "Apt-get", "Ubuntu": "Apt-get", "Fedora": "dnf", "CentOS": "yum", "OpenSUSE": "Zypper", "Arch": "pacman", "Gentoo": "emerge"}
print(type(distroInstallCommand))
print(distroInstallCommand)

#Q4.1
testDict = {}
testDict[3] = "Boat"
testDict["Green"] = 42
testDict["a list"] = [2, 4, 6, 8, 10]
otherDict = {"a": 1, "b": 2, "c":3}
testDict["a dict"] = otherDict
print(testDict)
print(testDict["a dict"])
print(testDict["a list"][1])

distroInstallCommand = {"Debian": "Apt-get", "Ubuntu": "Apt-get", "Fedora": "dnf", "CentOS": "yum", "OpenSUSE": "Zypper", "Arch": "pacman", "Gentoo": "emerge"}
del distroInstallCommand["Ubuntu"]
print(distroInstallCommand)