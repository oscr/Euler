#!/usr/bin/env python


triangle = [[int(i) for i in j.split()] for j in open('triangle.txt', 'r').readlines()]

# for i in range(second last row, row 0, steping -1
for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

print(triangle[0][0])
