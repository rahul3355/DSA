# Functions

def myFunc(n, m):
	return n * m

print(myFunc(3, 5))

def double(arr, val):
	def helper():
		for i, n in enumerate(arr):
			arr[i] *= 2

		nonlocal val
		val *= 2

	helper()
	print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)