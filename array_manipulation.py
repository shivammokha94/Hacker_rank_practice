#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:13:24 2019

@author: smokha
"""



# My Method O(n*m)
def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        for j in range(i[0]-1, i[1]):
            arr[j] = arr[j] + i[2]
            print(arr)
    res = max(arr)
    return res



# O(n + m)
def arrayManipulation2(n, queries):
    arr = [0]*(n+1)
    for i, j ,k in queries:
        arr[i -1] = arr[i -1] + k
        arr[j] = arr[j] - k
        print(arr)
    result = acc = 0
    for x in arr:
        acc+=x
        result = max(result, acc)
    return result



n = 5
q = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]


#result = arrayManipulation(n, q)
result = arrayManipulation2(n, q)
print(result)