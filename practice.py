# num = int(input("Up to what number? "))
# power = int(input("Up to what power? "))
# def ExponentTable(num, power):
#     table = []
#     for x in range(num +1):
#         for y in range(power + 1):
#             table.append(x ** y)
#         table.append("/")
#     return table
# print(ExponentTable(num, power))

#sampleDict = {'Physics':82, 'Math':65, 'history':75}


#print(list(sampleDict.keys())[list(sampleDict.values()).index(min(sampleDict.values()))])
#print(min(sampleDict,key = sampleDict.get))
#print(sampleDict.get)
D = dict()
for i in range(3):
    for j in range(2):
        D[i] = j
print(D)
