#!/usr/bin/env python
# If n is 1 these won't work :)


# Solution 1
def factorize(n):
    factor = 2

    while n > factor:
        if n % factor == 0:
            n //= factor
            continue

        factor += 1

    return factor

print(factorize(600851475143))


# Solution 2
def factorRec(n, factor):
    if n <= factor:
        print(factor)
    else:
        while n % factor != 0:
            factor += 1
        factorRec(n // factor, factor)

factorRec(600851475143, 2)
