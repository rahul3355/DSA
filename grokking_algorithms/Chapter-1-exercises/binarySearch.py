def binarySearch(arr, item):
	low = 0
	high = len(arr) - 1
	
	while low <= high:
		mid = (low + high) // 2
		guess = arr[mid]
		if guess == item:
			return mid
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None
	


arr = [1,2,3,4,5,6,7]
item = 6
print(binarySearch(arr, item))