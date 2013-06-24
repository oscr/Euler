#!/usr/bin/env python


names = [n.strip('"') for n in open('names.txt', 'r').readline().split(',')]

# I trust that timsort is sufficient
list.sort(names)

totalSum = 0
startIndex = ord('A') - 1
for (position, name) in enumerate(names, 1):
    nameSum = 0
    for c in name:
        nameSum += ord(c) - startIndex

    totalSum += nameSum * position

print(totalSum)
