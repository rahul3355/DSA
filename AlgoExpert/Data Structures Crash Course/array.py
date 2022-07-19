arr = [1,2,3,4,5]

print(arr[2]) # O(1) Time

arr[2] = 300 # O(1) Time
print(arr[2])

arr.insert(0,10) # O(n) Time
print(arr)

arr.insert(2, 40) # O(n) Time
print(arr)

arr.append(84) # O(1) Time
print(arr)

arr.pop(0) # O(n) Time
print(arr)

arr.pop(3) # O(n) Time
print(arr)

arr.pop() # O(1) Time
print(arr)

arr2 = arr # O(n) Time
print(arr2)