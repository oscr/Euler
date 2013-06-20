#!/usr/bin/env python


def isPythagoreanTriplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def findPythagoreanTripletProduct():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - a - b
            if isPythagoreanTriplet(a, b, c):
                print("product abc: %s" % (a * b * c))
                return

findPythagoreanTripletProduct()
