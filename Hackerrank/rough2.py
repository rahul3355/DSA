n = int(input("Enter n: "))
arr = []
for i in range(n):
	x = int(input())
	arr.append(x)

print(arr)

minCut = min(arr)
for i in range(n):
	if arr[i] - minCut >= 0:
		arr[i] = arr[i] - minCut
	
print(arr)

     
    # using list comprehension to perform the task
arr = [i for i in arr if i != 0]
 
print(arr)