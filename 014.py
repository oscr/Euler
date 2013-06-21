#!/usr/bin/env python


def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return n * 3 + 1


def getLongestSeq():
    # Will contain already calculated Collatz seq
    collatzDic = {}
    for x in range(1, 1000000):
        terms = 0
        dx = x
        while dx != 1:
            if dx in collatzDic:
                collatzDic[x] = collatzDic[dx] + terms
                break
            dx = collatz(dx)
            terms += 1

        if not x in collatzDic:
            collatzDic[x] = terms

    # Find the key with longest seq
    return max(collatzDic, key=collatzDic.get)

print("Starting number with longest seq: %s." % getLongestSeq())
