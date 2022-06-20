#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    setarr = set(a)
    listarr = list(setarr)
    print(listarr)
    if len(listarr) == 1:
        return a.count(listarr[0])

    maxCount, newCount = 1,1
    for i in range(len(listarr) - 1):
        if listarr[i] == listarr[i+1] or listarr[i] == listarr[i+1] - 1:
            x = a.count(listarr[i])
            y = a.count(listarr[i+1])
            print("x = ", x, " y = ",y)
            z = x + y
            if z > maxCount:
                maxCount = z
    if a.count(listarr[0]) > maxCount:
        maxCount = a.count(listarr[0])
    return maxCount
    
if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)