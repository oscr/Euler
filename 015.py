#!/usr/bin/env python

import operator
from functools import reduce


# http://www.wolframalpha.com/input/?i=%282n%29!+%2F+n!^2
def latticePath(r):
    dividend = reduce(operator.mul, [i for i in range(r + 1, r * 2 + 1)])
    divisor = reduce(operator.mul, [i for i in range(1, r + 1)])
    return dividend // divisor

print(latticePath(20))
