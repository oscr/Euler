#!/usr/bin/env python


from operator import mul
from functools import reduce

print(sum([int(i) for i in str(reduce(mul, [i for i in range(1, 101)]))]))
