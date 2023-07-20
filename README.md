# DSA
A folder to track my DSA progress.

			Complexity of Python Operations

https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt#:~:text=where%20O%3D%3D(...),an%20%3D%3D%20check%20is%20done.

https://wiki.python.org/moin/TimeComplexity


![complexityGraph](https://user-images.githubusercontent.com/53422351/180032720-344e8686-c70e-4936-980f-a6366dd1acdc.jpeg)

# codeforces template for python inputs
import sys
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

It comprises of 4 functions :-

1) inp — For taking integer inputs.

2) inlt — For taking List inputs.

3) insr — For taking string inputs. Actually it returns a List of Characters, instead of a string, which is easier to use in Python, because in Python, Strings are Immutable.

4) invr — For taking space seperated integer variable inputs.

The input = sys.stdin.readline is actually for Faster Inputs, because line reading through System STDIN (Standard Input) is faster in Python.

https://neetcode.io/courses/lessons/python-for-coding-interviews