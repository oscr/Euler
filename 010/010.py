#!/usr/bin/env python


# Sieve of Eratosthenes implementation
def findPrimeSum(limit):
    primes = [True] * limit
    primes[0] = False
    primes[1] = False

    sum = 0
    for (i, isPrime) in enumerate(primes):
        if isPrime:
            sum += i
            for j in range(i * i, limit, i):
                primes[j] = False

    return sum

print(findPrimeSum(2000000))
