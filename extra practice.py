# PrimeAmount = []
# num = 1
# prime = True
# while len(PrimeAmount) < 100:
#     prime = True
#     for x in range(2, num + 1):
#         if num % x == 0 and num != x:
#             prime = False
#             break
#         else:
#             continue
#     if prime == True:
#         PrimeAmount.append(num)
#     num = num + 1
# print (PrimeAmount)

def Syllogism():
    Major = input("What is the major premise? ")
    Minor = input("What is the minor premise? ")
    Universal = type(bool)
    Affirmative = type(bool)
    Conclusion = []
    ValidTerms = []
    Valid = type(bool)
    Middle = type(str)
    if (Major[0] == "A" or Major[0] == "E") and (Minor[0] == "A" or Minor[0] == "E"):
        Universal = True
        ValidTerms.append(Major[1])
        ValidTerms.append(Minor[1])
    else:
        Universal = False
    if (Major[0] == "A" or Major[0] == "I") and (Minor[0] == "A" or Minor[0] == "I"):
        Affirmative = True
    else:
        Affirmative = False
        ValidTerms.append(Major[2])
        ValidTerms.append(Minor[2])
    if Universal == True and Affirmative == True:
        Conclusion.append("A")
    elif Universal == True and Affirmative == False:
        Conclusion.append("E")
    elif Universal == False and Affirmative == True:
        Conclusion.append("I")
    else:
        Conclusion.append("O")
    if Minor[1] in Major:
        Middle = Minor[1]
        Conclusion.append(Minor[2])
    else:
        Middle = Minor[2]
        Conclusion.append(Minor[1])
    if Major[1] in Minor:
        Conclusion.append(Major[2])
    else:
        Conclusion.append(Major[1])
    Conclusion = str(Conclusion)
    if Major[0] == ("A" or "E"):
        ValidTerms.append(Major[1])
    if Minor[0] == ("A" or "E"):
        ValidTerms.append(Minor[1])
    if Major[0] == ("E" or "O"):
        ValidTerms.append(Major[2])
    if Minor[0] == ("E" or "O"):
        ValidTerms.append(Minor[2])
    if Conclusion[0] == "A":
        if Middle in ValidTerms and Conclusion[1] in ValidTerms:
            Valid = True
        else:
            Valid = False
    elif Conclusion[0] == "E":
        if Middle in ValidTerms and Conclusion[1] in ValidTerms and Conclusion[2] in ValidTerms:
            Valid = True
        else:
            Valid = False
    elif Conclusion[0] == "O":
        if Middle in ValidTerms and Conclusion[2] in ValidTerms:
            Valid = True
        else:
            Valid = False
    else:
        if Middle in ValidTerms:
            Valid = True
        else:
            Valid = False
    return Conclusion, Valid
print("The Conclusion is %s and its validity is %s" % Syllogism())