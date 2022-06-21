#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    height = 1
    if n == 0:
        return height
    elif n == 1:
        height = 2
        return height
    elif n % 2 == 0:
        height = n*2-1
    else:
        for i in range(3,n+1,2):
            eve = (i*2-1)-2
            height = eve * 2
        
    return height
        
    

if __name__ == '__main__':
    

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        print(str(result) + '\n')

