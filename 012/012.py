#!/usr/bin/env python


import math


def countDivisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            count += 2
    return count


def getFirstValueMore500Divisors():
    triangle = 0
    i = 1
    while countDivisors(triangle) <= 500:
        triangle += i
        i += 1

    return triangle

print(getFirstValueMore500Divisors())
