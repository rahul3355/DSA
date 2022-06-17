import math
import os
import random
import re
import sys



def birthday(s, d, m):
    # Write your code here
    count, temp = 0,0
    for i in range(len(s)-m+1):
        for j in range(i+1, i+m-1, 1):
            temp += s[j]
            print(temp)
        if (s[i] + temp == d):
            count += 1
            temp = 0
            print(count)
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['K:\DSA\Hackerrank\subarrayDivision.txt'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()