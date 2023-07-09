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


n = inp()
arr = []

for i in range(n):
	a1, a2, a3 = invr()
	arr.append([a1, a2, a3])

count = 0

for i in range(n):
	if arr[i][0] + arr[i][1] == 2 or arr[i][1] + arr[i][2] == 2 or arr[i][0] + arr[i][2] == 2:
		count += 1

print(count)