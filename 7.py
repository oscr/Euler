#!/usr/bin/env python


def isPrime(n):
    # We only need to check squareroot of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def findPrime(n):
    i = 1
    while n > 0:
        i += 2

        if isPrime(i):
            n -= 1

    return i

print(findPrime(10000))
