#Q 1
# an = a1 + (n-1) * d      
# equation to find the nth term in an arithmetic sequence (sequence where every value has the same difference from the previous value)
# an = the position of the term you are going to
# a1 the starting term in the sequence
# n = term position
# d = common difference  (the difference between each value in the sequence)

def FindTermN(start, n, difference):
    if start % 1 != 0:
        print("Please choose an integer")
    elif n % 1 != 0 and n < 1:
        print("Please choose a positive whole number")
    else: 
        termN = start + (n - 1) * difference
        return termN
print (FindTermN(start = 1, n = 10, difference = 6))

#Q 2
# n = ((an - a1) / d) + 1
# Equation to find the number of terms in the sequence
# an = the end term in the sequence
# a1 the starting term in the sequence
# n =  number of terms
# d = common difference  (the difference between each value in the sequence)
def FindNumTerms_ArithmSeq(start, end, difference):
    if start %1 != 0:
        print("Please choose an integer. ")
    numTerms = 1 + ((end - start) / difference)
    if numTerms > 0:
        return int(numTerms)
    else:
        print("The number of terms cannot be negative.\nTry again.")
print(FindNumTerms_ArithmSeq(1, 10, 1))

#Q 3
# sn = (n / 2) * (a1 + an)
# Equation to find the sum of an arithmetic sequence
# sn = sum of terms
# n = number of terms
# an = the end term in the sequence
# a1 the starting term in the sequence
def FindArithmeticSeriesSum_VerOne(start, end, n):
    if start % 1 == 0 and start > 0:
        if end % 1 == 0 and end > 0 and end > start:
            total = (0.5 * n) * (start + end)
            return total
    else:
        print("Choose a starting number that is a whole positive number, please. ")
print (FindArithmeticSeriesSum_VerOne(start = 1, end = 10, n = FindNumTerms_ArithmSeq(1, 10, 1)))

#Q 4
def FindArithmeticSeriesSum_VerTwo(start, increment, end):
    sum = 0
    if start > 0:
        if end > 0 and end > start:
            for x in range(end):
                sum  = sum + (start + (increment * x))
                
    return sum
print(FindArithmeticSeriesSum_VerTwo(1, 2, 4))