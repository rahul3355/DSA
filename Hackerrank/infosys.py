n = int(input("Enter n: "))
x = int(input("Enter x: "))
arr = []
diff = 0
for i in range(n):
    u = int(input("Enter element: "))
    arr.append(u)

sumTotal = sum(arr)

if sumTotal <= x:
    print(0)
else:
    for i in range(n-1):
        if (arr[i] + arr[i+1]) >= x:
            v = ((arr[i] + arr[i+1]) - x)
            arr[i] = arr[i] - v
            diff += v
            

sumDiff = 0           
for element in arr:
    sumDiff += abs(element)

print(sumDiff)