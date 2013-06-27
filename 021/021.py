#!/usr/bin/env python


from math import sqrt


def getDivisorSum(n):
    sum = 1
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            sum += i
            sum += n // i

    return sum


def getAmicableSumLimit10000():
    divisorSums = {i: getDivisorSum(i) for i in range(1, 10000)}

    # More fun solution
    # return sum([i for (i, j) in divisorSums.items() if i != j and divisorSums.get(j) == i])
    sum = 0
    for (i, j) in divisorSums.items():
        if i != j and divisorSums.get(j) == i:
            sum += i

    return sum


print(getAmicableSumLimit10000())
