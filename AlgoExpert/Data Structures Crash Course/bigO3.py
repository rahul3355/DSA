import time

def f3(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print("(", arr[i], ",", arr[j],")", end=" | ")
        print()

arr = [x for x in range(4)]
start = time.time()
f3(arr)
end = time.time()
print("start: ",start)
print("end: ", end)
print("time elapsed: ",end - start)