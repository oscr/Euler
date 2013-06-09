#!/usr/bin/env python

from itertools import takewhile


# Solution 1
def fibonacci():
    i = 1
    j = 2
    while True:
        yield i
        i, j = j, i + j

print(sum(filter(lambda x: (x % 2 == 0), takewhile(lambda x: x < 4000000, fibonacci()))))


# Solution 2
def evenFibonacci():
    i = 1
    j = 2
    while True:
        if i % 2 == 0:
            yield i
        i, j = j, i + j


def sumEvenFibonacci(limit):
    fibSum = 0
    fib = evenFibonacci()
    while True:
        v = fib.next()
        if v > limit:
            return fibSum

        fibSum += v

print(sumEvenFibonacci(4000000))


# Solution 3
print(sum(takewhile(lambda x: x < 4000000, evenFibonacci())))
