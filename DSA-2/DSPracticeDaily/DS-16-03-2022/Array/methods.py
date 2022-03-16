nums = [12, 5, 77, 44, 2, 1, 42, 77]

print(nums)

nums.append(32)
print(nums)

nums2 = nums.copy()
print(nums2)

nums.extend(nums2)
print(nums)

print(nums.count(77))

print(nums.index(77))

nums.insert(0, 22)
print(nums)

nums.pop() 
print(nums)

nums.remove(77)
print(nums)

nums.reverse()
print(nums)

nums.sort()
print(nums)