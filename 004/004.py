#!/usr/bin/env python


def isPalindrome(n):
    return str(n) == str(n)[::-1]


def findLargestPalindromeProduct():
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            l = i * j
            if l > largest and isPalindrome(l):
                largest = l
    return largest


print(findLargestPalindromeProduct())
