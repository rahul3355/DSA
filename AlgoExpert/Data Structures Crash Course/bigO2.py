from ipaddress import summarize_address_range


import time

def f2(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum)

arr = [1,2,3,4]
start = time.time()
print("start: ",start)
f2(arr)
end = time.time()
print("end: ", end)
print("time elapsed: ",end - start)