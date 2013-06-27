#!/usr/bin/env python


# Lambda calculates the smallest positive integer that both n and m divide.
from functools import reduce
from fractions import gcd
print(reduce(lambda n, m: (m * n) // gcd(m, n), [i for i in range(1, 21)], 1))
