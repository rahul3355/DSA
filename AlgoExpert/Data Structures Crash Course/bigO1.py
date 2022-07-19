import time

def f1(arr):
    print(1 + arr[0])

arr = [1,2,3,4]
start = time.time()
print("start: ",start)
f1(arr)
end = time.time()
print("end: ", end)
print("time elapsed: ",end - start)