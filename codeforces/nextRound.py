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


n = inlt()
arr = inlt()

k = n[1]

arr.sort()
arr.reverse()

least_score = arr[k-1]

count = 0
for num in arr:
	if num >= least_score and least_score > 0:
		count += 1

print(count)