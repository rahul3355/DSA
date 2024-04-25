def findSmallest(arr):
	smallest = arr[0]
	smallestIndex = 0
	for i in range(len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallestIndex = i
	return smallestIndex


def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr



arr = [23,4,55,6,88,12,54,2]
print(selectionSort(arr))