# arrays

arr = [1,2,3]
print(arr)

# stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1,7)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)

n = 5
arr = [1] * n
print(arr)


print("arr[-1] = ", arr[-1])

print(arr[-2])

arr = [1,2,3,4]
print(arr[1:3])

print(arr[0:4])

a,b,c = [1,2,3]
print("a = ", a, "b = ",b, "c = ", c)


nums = [1,2,3,45,6,7,88]
for i in range(len(nums)):
	print(nums[i])

for n in nums:
	print(n)

for i, n in enumerate(nums):
	print(i, n)


nums1 = [2,3,5]
nums2 = [6,7,8]

for n1, n2 in zip(nums1, nums2):
	print(n1, n2)

nums = [1,2,3]
nums.reverse()
print(nums)
