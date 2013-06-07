#!/usr/bin/env python

multipleThree = [ x for x in range(3, 1000, 3) ]
multipleFive = [ x for x in range(5, 1000, 5) ]
multipleUnique = set(multipleThree + multipleFive)
print sum(multipleUnique)
